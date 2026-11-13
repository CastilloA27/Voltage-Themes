"""Helpers for make-store.py. Writes the theme store's own themes (Voltage review round 14 > B2) into themes/<id>/: python tools/make-store.py
Each has a layout of its own (the user: "each of the themes' layout to be different"). Art made here is CC0; fonts are SIL OFL
from github.com/google/fonts (each with its OFL.txt in the package); no other company's characters, logos or brands."""
import json, shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = HERE.parent / 'themes'
FONTS = HERE / 'fonts'
SCHEMA = 'https://raw.githubusercontent.com/CastilloA27/Voltage-Plugins/main/themes/theme.schema.json'


def write(pkg, manifest, css, files=None):
    d = OUT / pkg
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)
    manifest['css'] = 'theme.css'
    (d / 'theme.css').write_text(css.strip() + '\n', encoding='utf-8')
    for rel, data in (files or {}).items():
        p = d / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_bytes(data) if isinstance(data, bytes) else p.write_text(data, encoding='utf-8')
    (d / 'theme.json').write_text(json.dumps({'$schema': SCHEMA, **manifest}, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')
    print('wrote', pkg)


def ofl(name, f):
    return {f'assets/{name}/{f}': (FONTS / name / f).read_bytes(), f'assets/{name}/OFL.txt': (FONTS / name / 'OFL.txt').read_bytes()}


def credits(lines):
    return '# Credits\n\n' + ''.join(f'- {l}\n' for l in lines)


# tokens every light theme sets (the core's light-mode slots)
def light(bg, ink, dim, surface, border, accent, on_accent, extra=None):
    t = {'color.bg': bg, 'color.text': ink, 'color.text-dim': dim, 'color.text-strong': ink, 'color.text-soft': ink, 'color.text-muted': dim,
         'color.surface': surface, 'color.border': border, 'color.ink': ink, 'color.shade': dim, 'color.knob': bg, 'color.focus': ink,
         'color.placeholder': border, 'color.select-bg': border, 'color.mini-solid': bg, 'color.media-bg': surface, 'surface.menu': surface,
         'surface.pop': surface, 'surface.drag': surface, 'surface.game': bg, 'surface.tip': surface, 'color.brand': accent,
         'color.on-accent': on_accent, 'effect.blur': '0px', 'effect.glow-size': '0px', 'effect.glow-alpha': '0%', 'accent.album-mix': '0',
         'shape.radius': '0px', 'shape.roundness': '0'}
    t.update(extra or {})
    return t


FLAT = '.lay-area { backdrop-filter: none !important; box-shadow: none !important; }'
