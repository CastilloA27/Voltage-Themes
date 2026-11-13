# Voltage themes

The theme store of [Voltage](https://github.com/CastilloA27/Voltage-Releases): every folder in `themes/` is a theme package
(see THEMING.md in Voltage-Plugins for how to make one), and `catalog.json` is what Voltage's **Settings > Appearance > Theme
store** reads. Themes contain no code; Voltage checks every file again when it installs one.

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

Theme sources that aren't copies of Voltage-Plugins' examples are made by `tools/make-store.py`.

## Adding a theme

1. A pull request adds `themes/<id>/` (the folder name is the theme's `id`) and `previews/<id>-1.png` (+ `-2.png`), 1280 x 800,
   made with Voltage's demo library (`voltage --demo`, `tools/theme-previews.mjs`): never a picture of a real library.
2. It must pass `node tools/theme-check.mjs themes/<id> --strict` (in the Voltage repo).
3. Licences: fonts under the SIL OFL (with their `OFL.txt` in the package), art and sounds CC0, CC BY (credited) or made for the
   theme, all listed in the theme's `CREDITS.md`.
4. **No characters, logos or brands of other companies**, and nothing that imitates gambling with money (a slot-machine *look*
   is fine; credits, betting or odds are not).
5. The maintainer reviews it, rebuilds and signs the catalog (`node build-catalog.mjs`). Only he can sign, so nothing
   reaches the store without his review.

## Licences

Each theme's licence is in its folder (`CREDITS.md`, `OFL.txt`). The catalog tooling (`build-catalog.mjs`) is MIT.
