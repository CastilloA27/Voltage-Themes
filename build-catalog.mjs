// Builds catalog.json (+ catalog.json.sig) for Voltage's theme store (Voltage review round 14 > C) from themes/<id>/:
// per theme id, name, version, author, licence, tags, minVoltage, size, every file with its sha256, and preview pictures.
// Downloads point at the commit that holds these exact files, so commit the theme folders first. Signed with the same
// offline Ed25519 key as the plugin catalog (Voltage has the public half built in and refuses an unsigned store).
//   node build-catalog.mjs                 the real catalog (signed, pinned to HEAD on GitHub)
//   node build-catalog.mjs --local <url>   a test catalog for a debug build (unsigned, files served from <url>)
import fs from 'node:fs';
import path from 'node:path';
import crypto from 'node:crypto';
import os from 'node:os';
import { fileURLToPath } from 'node:url';
import { spawnSync } from 'node:child_process';

const RAW = 'https://raw.githubusercontent.com/CastilloA27/Voltage-Themes';
const EXPIRES_DAYS = 365;
const root = path.dirname(fileURLToPath(import.meta.url));
const local = process.argv.includes('--local') ? process.argv[process.argv.indexOf('--local') + 1] : null;

// the same DPAPI-sealed key as Voltage-Plugins/build-catalog.mjs (one key signs both catalogs)
function signingKey() {
  const sealed = path.join(os.homedir(), '.voltage-signing', 'catalog-ed25519.pem.dpapi');
  if (!fs.existsSync(sealed)) throw new Error('no signing key (run Voltage-Plugins/build-catalog.mjs once to seal it)');
  const r = spawnSync('powershell', ['-NoProfile', '-NonInteractive', '-Command',
    "Add-Type -AssemblyName System.Security; $e=[Text.Encoding]::UTF8.GetBytes('voltage-catalog-key'); [Text.Encoding]::UTF8.GetString([Security.Cryptography.ProtectedData]::Unprotect([Convert]::FromBase64String([Console]::In.ReadToEnd()),$e,'CurrentUser'))"],
  { input: fs.readFileSync(sealed, 'utf8'), encoding: 'utf8' });
  if (r.status !== 0) throw new Error(`DPAPI: ${r.stderr.trim()}`);
  return r.stdout.trim();
}
const git = (...a) => {
  const r = spawnSync('git', a, { cwd: root, encoding: 'utf8' });
  if (r.status !== 0) throw new Error(`git ${a.join(' ')}: ${r.stderr.trim()}`);
  return r.stdout.trim();
};
const sha = (b) => crypto.createHash('sha256').update(b).digest('hex');
const walk = (dir, rel = '') => fs.readdirSync(dir, { withFileTypes: true }).flatMap((e) => (e.isDirectory()
  ? walk(path.join(dir, e.name), `${rel}${e.name}/`) : [`${rel}${e.name}`]));

let base;
if (local) base = local.replace(/\/$/, '');
else {
  const dirty = git('status', '--porcelain', '--', 'themes', 'previews').split('\n').filter(Boolean);
  if (dirty.length) throw new Error(`commit the theme folders first (the catalog points at a commit):\n${dirty.join('\n')}`);
  base = `${RAW}/${git('rev-parse', 'HEAD')}`;
}
let prevSeq = 0;
try { prevSeq = JSON.parse(fs.readFileSync(path.join(root, 'catalog.json'), 'utf8')).seq ?? 0; } catch { /* first build */ }

const themes = [];
for (const id of fs.readdirSync(path.join(root, 'themes')).sort()) {
  const dir = path.join(root, 'themes', id);
  const mf = path.join(dir, 'theme.json');
  if (!fs.existsSync(mf)) continue;
  const m = JSON.parse(fs.readFileSync(mf, 'utf8'));
  if (m.id !== id) throw new Error(`themes/${id}: theme.json id is "${m.id}"`);
  const files = walk(dir).sort().map((f) => { const b = fs.readFileSync(path.join(dir, f)); return { path: f, sha256: sha(b), size: b.length }; });
  const css = m.css && fs.existsSync(path.join(dir, m.css)) ? fs.readFileSync(path.join(dir, m.css), 'utf8') : '';
  const animated = /@keyframes/.test(css);
  const tags = [m.appearance === 'light' ? 'light' : m.appearance === 'system' ? 'light' : 'dark', ...(m.appearance === 'system' ? ['dark'] : []),
    m.layout && 'layout', m.sounds && 'sounds', m.fonts?.length && 'fonts', m.overlay && 'overlay', animated ? 'animated' : 'low-cpu'].filter(Boolean);
  const licence = fs.existsSync(path.join(dir, 'CREDITS.md')) ? 'see CREDITS.md' : 'CC0 / see files';
  const previews = fs.readdirSync(path.join(root, 'previews')).filter((f) => f.startsWith(`${id}-`) && f.endsWith('.png')).sort()
    .map((f) => `${base}/previews/${f}`);
  if (m.kind === 'effect') tags.unshift('effect');
  themes.push({ id, ...(m.kind === 'effect' ? { kind: 'effect' } : {}), name: m.name, version: m.version, author: m.author ?? '', description: m.description ?? '', licence, tags,
    ...(m.minVoltage ? { minVoltage: m.minVoltage } : {}), ...(m.plugin ? { plugin: m.plugin } : {}),
    size: files.reduce((a, f) => a + f.size, 0), base: `${base}/themes/${id}`, files: files.map(({ path: p, sha256 }) => ({ path: p, sha256 })), previews });
}
const expires = Math.floor(Date.now() / 1000) + EXPIRES_DAYS * 86400;
const body = `${JSON.stringify({ version: 1, kind: 'themes', seq: prevSeq + 1, expires, themes }, null, 2)}\n`;
fs.writeFileSync(path.join(root, 'catalog.json'), body);
if (local) {
  fs.rmSync(path.join(root, 'catalog.json.sig'), { force: true });
  console.log(`catalog.json (LOCAL TEST, unsigned) seq ${prevSeq + 1}: ${themes.length} themes from ${base}. Don't commit it.`);
} else {
  const sig = crypto.sign(null, Buffer.from(body), crypto.createPrivateKey(signingKey()));
  fs.writeFileSync(path.join(root, 'catalog.json.sig'), `${sig.toString('base64')}\n`);
  console.log(`catalog.json seq ${prevSeq + 1}: ${themes.map((t) => `${t.id} ${t.version}`).join(', ')}`);
  console.log('Next: commit catalog.json + catalog.json.sig and push (the commit above must be pushed too).');
}
