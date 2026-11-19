# Voltage themes

The theme store of Voltage, the YouTube Music desktop client for Windows: every folder in `themes/` is a theme package
(how to make one: [THEMING.md](https://github.com/CastilloA27/Voltage-Plugins/blob/main/THEMING.md) in Voltage-Plugins), and
`catalog.json` is what Voltage's **Settings > Theme store** reads. Themes contain no code; Voltage checks every file again when it installs one.

## How it works

- `catalog.json` lists each theme: name, version, author, licence, tags, size, every file with its **sha256**, and preview
  pictures. Downloads point at the **commit** that holds those exact files.
- `catalog.json.sig` is an **Ed25519 signature** made with the maintainer's offline key. Voltage has the public half built in
  and refuses a store catalog that isn't signed, or that is older than one it has already seen.
- Install = download each file over HTTPS, check its sha256, then the same checks as installing a theme folder (file types,
  sizes, names, SVG content, CSS limits). Updates are shown when the catalog has a newer version; they never install by
  themselves.
- The nine bundled themes ship inside Voltage's installer too, and get fixes from here without an app update.

## The themes

| Theme | Idea | Layout |
|---|---|---|
| Terminal, CRT green, Pastel goth, Sidebar, Frosted light, Jackpot, Paper, Tactical, Sumi Ink | the nine that ship with Voltage | each its own |
| Voltage (starter) | Voltage's own look with every value written out: the template to copy | Voltage's |
| Spreadsheet | stealth mode: a plain-looking sheet (formula bar with the song, numbered rows, a status bar) | toolbar / formula bar / sheet |
| Blueprint | blue grid paper, the cover as a drawing with a dimension line, a title block | parts list / drawing / title block |
| E-ink | grey on paper, nothing moves, no blur: the cheapest theme to draw (2.4% of a core playing vs 17.6% for Voltage's, measured) | page header / list |
| Retro Desktop | late-90s windows (generic, no OS logos): bevels, a title bar on every panel, a taskbar along the bottom | windows + taskbar |
| Comic | ink-bordered panels, halftone dots, the lyrics as speech bubbles, POW! on a like | cover + bubbles + list |
| Big & Clear | accessibility: big legible text, big buttons, contrast above 7:1 (measured 9.85), nothing moves | player first, list below |
| Deep Space | a slow starfield, the cover as a planet with an orbit ring and a moon | planet + docked list |
| Aquarium | teal water, rising bubbles, light ripples over the round cover | list + tank, controls on the sand |
| Vinyl Lounge | walnut and brass: the cover as a spinning record, a tonearm that swings in on play | turntable + record crate |
| Cassette | an 80s tape deck: the cover as the cassette label with turning reels, the queue as a hand-written J-card, piano keys | tape + J-card |
| Handheld | a 4-green pocket console look (no console branding), pixel font, the mini player as the device | screen + buttons |
| Night City | rain over neon, the title as a buzzing sign, a glitch on every track change | sign over cover + list |
| Studio | a mixing desk: two VU meters (needles move with the music with the **VU meter** plugin), rack-mounted player | channel list + meters |
| Halloween, Winter | tiny seasonal themes (a palette and an overlay on Voltage): how small a theme can be | Voltage's |
| **Theme FX wave 1** (need Voltage 1.7.2; most need their plugin from Settings > Plugins) | | |
| Aurora | northern lights in the album's colours over a black sky, a different sky per song (WebGL, **Aurora sky** plugin) | the sky gets the window, the player floats |
| Neon Sign | the title as a neon sign on a brick wall: letters buzz on, the glow swells with the beat, a tube flickers (off with Reduce flashing) | the sign over everything, the queue as the bar menu |
| Departures | a station board: the title on split-flap tiles, the queue as departures with clock times (**Departures board** plugin) | board + platform poster |
| Messenger | the song as a chat with the artist: lyrics arrive as bubbles, typing… before the next song | chat list / header / chat |
| Cinema | a screen between black bars, lyrics as subtitles, a title card and THE END, pages fade through black | screen / subtitles / program |
| JRPG | a turn-based battle: the song is the enemy, HP is the time left, FIGHT / ITEM / RUN / MAGIC; seeking hits for damage and you level up (**JRPG battle** plugin) | party / enemy / text box / menu |
| Word Rain | every sung word falls behind the player and piles up (**Word rain** plugin) | a quiet stage |
| Jackpot 3 | Jackpot with a lever that skips, coins on a winning line, bulbs on the beat, 5 or 3 reels (the **Reels** plugin) | the cabinet |
| **Effect packs** (`"kind": "effect"`: they stack on whatever theme is on, up to 6 at once) | | |
| Snow, Film grain, Beat pulse | snowfall over the window, a film-grain overlay, the window edge glowing with the beat (softer with Reduce flashing) | none of their own |

Theme sources that aren't copies of Voltage-Plugins' examples are made by `tools/make-store.py`.

## Adding a theme

1. A pull request adds `themes/<id>/` (the folder name is the theme's `id`) and `previews/<id>-1.png` (+ `-2.png`), 1280 x 800,
   made with Voltage's demo library (start Voltage with `--demo`: made-up songs and covers): never a picture of a real library.
2. It must pass `node sdk/theme-check.mjs themes/<id> --strict` (the checker is one file in
   [Voltage-Plugins](https://github.com/CastilloA27/Voltage-Plugins): `sdk/theme-check.mjs`; Node 18+).
3. Licences: fonts under the SIL OFL (with their `OFL.txt` in the package), art and sounds CC0, CC BY (credited) or made for the
   theme, all listed in the theme's `CREDITS.md`.
4. **No characters, logos or brands of other companies**, and nothing that imitates gambling with money (a slot-machine *look*
   is fine; credits, betting or odds are not).
5. The maintainer reviews it, rebuilds and signs the catalog (`node build-catalog.mjs`). Only he can sign, so nothing
   reaches the store without his review.

## Licences

Each theme's licence is in its folder (`CREDITS.md`, `OFL.txt`). The catalog tooling (`build-catalog.mjs`) is MIT.
