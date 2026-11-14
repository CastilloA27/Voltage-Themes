"""Writes the theme store's own themes (Voltage review round 14 > B2) into themes/<id>/: python tools/make-store.py
Each has a layout of its own; art made here is CC0, fonts SIL OFL (google/fonts, with OFL.txt); no other company's brands."""
import importlib.util, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_store_base import write, ofl, credits, light, FLAT, FONTS  # noqa: E402

# ── Spreadsheet: stealth mode. Looks like a plain sheet: a toolbar, a formula bar with the song, numbered rows, a status bar ──
write('spreadsheet', {
    'id': 'spreadsheet', 'name': 'Spreadsheet', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'light',
    'description': 'Stealth mode: a plain-looking sheet. The controls in a toolbar, the song in the formula bar, numbered rows, a status bar.',
    'tokens': light('#ffffff', '#1f1f1f', '#5c5c5c', '#ffffff', '#d4d4d4', '#1e7145', '#ffffff', {'font.body': '"Segoe UI", Calibri, Arial, sans-serif'}),
    'accent': {'mode': 'fixed', 'color': '#1e7145'},
    'parts': {'tracklist': {'variant': 'table'}, 'art': {'variant': 'none'}, 'progress': {'variant': 'line'}, 'player': {'variant': 'compact'}, 'nav': {'variant': 'text'}},
    'supports': {'background': ['black']},
    'strings': {'brand': 'Book1', 'tab.search': 'Query', 'tab.library': 'Data', 'tab.queue': 'Sheet1', 'search.placeholder': 'Find (Ctrl+F)',
                'nowplaying.idle': 'Ready', 'empty.queue': 'Sheet1 is empty', 'nav.settings': 'Options', 'nav.explore': 'Insert', 'nav.stats': 'Review', 'nav.mini': 'View'},
    'layout': {'home': {
        'areas': ['ctl find', 'fx fx', 'list list', 'prog prog'], 'columns': 'minmax(0, 1fr) minmax(220px, 340px)', 'rows': '46px 32px minmax(0, 1fr) 32px',
        'place': {'ctl': 'player', 'find': 'search', 'fx': 'info', 'list': 'tracklist', 'prog': 'progress'},
        'below': {'700px': {'areas': ['ctl', 'fx', 'list', 'prog'], 'columns': '1fr', 'rows': '46px 32px minmax(0, 1fr) 32px',
                            'place': {'ctl': 'player', 'fx': 'info', 'list': 'tracklist', 'prog': 'progress'}}}}},
}, css=r"""
""" + FLAT + r"""
.lay-area { background-color: #ffffff !important; border: 0 !important; border-bottom: 1px solid #d4d4d4 !important; border-radius: 0 !important; }
[data-part="titlebar"] { background-color: #1e7145; color: #ffffff; }
[data-part="titlebar.brand"] { color: #ffffff; font-weight: 600; }
[data-part="titlebar"] button { color: #ffffff !important; }
/* the toolbar */
.lay-player { background-color: #f3f3f3 !important; justify-content: flex-start !important; }
/* the formula bar: fx | =PLAY("song") */
.lay-info { display: flex; align-items: center; padding: 0 0 0 46px !important; position: relative; text-align: left; }
.lay-info::before { content: "fx"; position: absolute; left: 0; top: 0; bottom: 0; width: 38px; display: grid; place-items: center; font: italic 13px Georgia, serif; color: #5c5c5c; border-right: 1px solid #d4d4d4; }
.lay-info [data-part="info.title"] { font: 13px Consolas, "Cascadia Mono", monospace; color: #1f1f1f; }
.lay-info [data-part="info.title"]::before { content: '=PLAY("'; color: #1e7145; }
.lay-info [data-part="info.title"]::after { content: '")'; color: #1e7145; }
.lay-info { overflow: hidden; }
.lay-info .info-part { display: flex !important; flex-direction: row !important; align-items: center; gap: 14px; width: 100%; white-space: nowrap; }
.lay-info .info-part > :not([data-part="info.title"]) { font-size: 12px; color: #4a4a4a; }
.lay-info [data-part="info.title"] { margin: 0; overflow: hidden; text-overflow: ellipsis; }
.lay-info .btn { width: 22px !important; height: 22px !important; }
[data-part="tracklist.row.artist"], [data-part="tracklist.row.time"] { color: #4a4a4a !important; opacity: 1; }
/* the sheet: column letters, row numbers, cell borders, a selected-cell box on the playing row */
.lay-tracklist { padding: 0 !important; }
.lay-tracklist [data-part="tracklist"] { counter-reset: row; background-image: linear-gradient(#f3f3f3, #f3f3f3); background-size: 40px 100%; background-repeat: no-repeat; }
.lay-tracklist [data-part="tracklist"]::before { content: "          A                                      B                         C                D"; display: block; white-space: pre; height: 22px; line-height: 22px;
  font: 12px "Segoe UI", sans-serif; color: #5c5c5c; background-color: #f3f3f3; border-bottom: 1px solid #d4d4d4; position: sticky; top: 0; z-index: 1; }
[data-part="tracklist.row"] { counter-increment: row; border-radius: 0 !important; border-bottom: 1px solid #e3e3e3; padding: 4px 8px 4px 48px !important; position: relative; }
[data-part="tracklist.row"]::before { content: counter(row); position: absolute; left: 0; top: 0; bottom: 0; width: 40px; display: grid; place-items: center; font-size: 11.5px; color: #5c5c5c; border-right: 1px solid #d4d4d4; }
[data-part="tracklist.row"]:hover { background-color: #f3f9f5 !important; }
[data-part="tracklist.row"][data-state~="active"] { background-color: #ffffff !important; box-shadow: inset 0 0 0 2px #1e7145 !important; }
[data-part="tracklist.row.title"] { font-weight: 400 !important; }
/* the status bar */
.lay-progress { background-color: #f3f3f3 !important; font-size: 12px; }
""")

# ── Blueprint: a drafting sheet. The cover is the drawing, a title block in the corner, the list as the parts list ──
GRID = ('linear-gradient(rgb(255 255 255 / .12) 1px, transparent 1px), linear-gradient(90deg, rgb(255 255 255 / .12) 1px, transparent 1px), '
        'linear-gradient(rgb(255 255 255 / .05) 1px, transparent 1px), linear-gradient(90deg, rgb(255 255 255 / .05) 1px, transparent 1px)')
write('blueprint', {
    'id': 'blueprint', 'name': 'Blueprint', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark',
    'description': 'A drafting sheet: blue grid paper, white lines, the cover as the drawing with a dimension line, a title block in the corner.',
    'fonts': [{'family': 'Architects Daughter', 'src': 'assets/architects/ArchitectsDaughter-Regular.ttf'},
              {'family': 'IBM Plex Mono', 'src': 'assets/plexmono/IBMPlexMono-Regular.ttf'}],
    'tokens': {'color.bg': '#0b3c8c', 'color.text': '#f2f6ff', 'color.text-dim': '#c4d4f4', 'color.text-strong': '#ffffff', 'color.text-soft': '#e6eeff',
               'color.text-muted': '#c4d4f4', 'color.surface': 'rgba(11, 60, 140, .55)', 'color.border': 'rgba(255, 255, 255, .7)', 'color.brand': '#ffffff',
               'color.on-accent': '#0b3c8c', 'color.knob': '#ffffff', 'color.select-bg': '#1a4fa8', 'surface.menu': '#0d438f', 'surface.pop': '#0d438f',
               'surface.tip': '#0d438f', 'effect.blur': '0px', 'effect.glow-size': '0px', 'effect.glow-alpha': '0%', 'accent.album-mix': '0',
               'shape.radius': '0px', 'shape.roundness': '0', 'font.mono': '"IBM Plex Mono", Consolas, monospace'},
    'accent': {'mode': 'fixed', 'color': '#ffffff'},
    'parts': {'progress': {'variant': 'line'}, 'tracklist': {'variant': 'dense'}},
    'supports': {'background': ['gradient']},
    'strings': {'tab.search': 'Search', 'tab.library': 'Drawings', 'tab.queue': 'Parts list', 'nowplaying.idle': 'No drawing loaded', 'empty.queue': 'Parts list empty'},
    'layout': {'home': {
        'areas': ['list draw draw', 'list draw draw', 'list prog block', 'list bar block'], 'columns': 'minmax(240px, 320px) minmax(0, 1fr) minmax(220px, 300px)',
        'rows': 'minmax(0, 1fr) minmax(0, 1fr) 48px 76px', 'place': {'list': 'sidebar', 'draw': 'art', 'block': 'info', 'prog': 'progress', 'bar': 'player'},
        'resizable': ['list'],
        'below': {'900px': {'areas': ['draw block', 'prog prog', 'bar bar', 'list list'], 'columns': '1fr 1fr', 'rows': 'minmax(0, 1fr) 48px 76px minmax(0, 1fr)',
                            'place': {'draw': 'art', 'block': 'info', 'prog': 'progress', 'bar': 'player', 'list': 'sidebar'}}}}},
}, css=r"""
[data-part="background"] { background-color: #0b3c8c !important; opacity: 1 !important; background-image: """ + GRID + r""" !important;
  background-size: 48px 48px, 48px 48px, 12px 12px, 12px 12px !important; }
""" + FLAT + r"""
.lay-area { background-color: transparent !important; border: 1.5px solid rgb(255 255 255 / .85) !important; border-radius: 0 !important; position: relative; }
[data-part="titlebar.brand"], [data-part="info.title"], .lay-area::before { font-family: "Architects Daughter", "Segoe Print", cursive; }
[data-part="titlebar.brand"] { letter-spacing: .12em; text-transform: uppercase; }
.lay-area::before { position: absolute; top: -11px; left: 12px; padding: 0 6px; background-color: #0b3c8c; font-size: 12px; letter-spacing: .14em; color: #ffffff; text-transform: uppercase; }
.lay-sidebar::before { content: "Parts list"; }
.lay-art::before { content: "Detail A: cover"; }
.lay-info::before { content: "Title block"; }
.lay-player::before { content: "Controls"; }
/* the drawing: the cover in white lines, a dimension line under it */
.lay-art { display: grid; place-items: center; min-height: 0; padding: 28px 24px 44px; overflow: hidden; }
.lay-art .art-part { display: grid; grid-template: minmax(0, 1fr) / minmax(0, 1fr); place-items: center; width: 100%; height: 100%; min-height: 0; }
.lay-art img { width: auto !important; height: auto !important; max-width: 100% !important; max-height: 100% !important; aspect-ratio: 1; object-fit: cover;
  border-radius: 0 !important; filter: grayscale(1) contrast(1.4) brightness(1.15); mix-blend-mode: screen; outline: 1.5px solid #ffffff; outline-offset: 6px; }
.lay-art::after { content: "|<-------------------  1 : 1  ------------------->|"; position: absolute; left: 0; right: 0; bottom: 12px; text-align: center;
  font: 11px "IBM Plex Mono", monospace; color: rgb(255 255 255 / .8); letter-spacing: .05em; white-space: pre; overflow: hidden; }
/* the title block: ruled boxes */
.lay-info { text-align: left; padding: 14px 12px 8px !important; background-image: linear-gradient(rgb(255 255 255 / .55) 1px, transparent 1px); background-size: 100% 26px; background-position: 0 40px; }
.lay-info [data-part="info.title"] { font-size: 22px; text-transform: uppercase; letter-spacing: .04em; }
.lay-info, .lay-progress, [data-part="tracklist.row.artist"], [data-part="tracklist.row.time"] { font-family: "IBM Plex Mono", Consolas, monospace; color: #e6eeff !important; opacity: 1; }
[data-part="tracklist.row"][data-state~="active"] { background-color: rgb(255 255 255 / .12) !important; box-shadow: inset 0 0 0 1.5px #ffffff !important; }
[data-part="tracklist.row"] img { filter: grayscale(1) contrast(1.3); }
[data-part="player.button.play"] { background-color: transparent !important; border: 1.5px solid #ffffff !important; color: #ffffff !important; box-shadow: none !important; }
""", files={**ofl('architects', 'ArchitectsDaughter-Regular.ttf'), **ofl('plexmono', 'IBMPlexMono-Regular.ttf'),
            'CREDITS.md': credits(['Fonts: Architects Daughter by Kimberly Geswein, and IBM Plex Mono by IBM; both SIL Open Font License 1.1 (assets/*/OFL.txt).',
                                   'Everything else: made for Voltage, CC0.'])})

# ── E-ink: grey on paper, no animation at all, no blur: calm, and the cheapest theme to draw ──
write('e-ink', {
    'id': 'e-ink', 'name': 'E-ink', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'light',
    'description': 'Grey on paper like an e-reader: a page header with a small cover, the list as the page. No animation, no blur, no glow.',
    'tokens': light('#e9e7e1', '#202020', '#4a4a4a', '#e9e7e1', '#b9b6ae', '#202020', '#e9e7e1', {'font.body': 'Georgia, "Times New Roman", serif'}),
    'accent': {'mode': 'fixed', 'color': '#202020'},
    'parts': {'progress': {'variant': 'line'}, 'tracklist': {'variant': 'dense'}, 'player': {'variant': 'compact'}},
    'supports': {'background': ['black'], 'miniSkin': ['classic']},
    'holidays': False,
    'strings': {'nowplaying.idle': 'Nothing open', 'empty.queue': 'This page is blank', 'tab.queue': 'Contents', 'tab.library': 'Shelf', 'tab.search': 'Find'},
    'layout': {'home': {
        'areas': ['cover head', 'prog prog', 'bar bar', 'list list'], 'columns': '132px minmax(0, 1fr)', 'rows': '132px 40px 60px minmax(0, 1fr)',
        'place': {'cover': 'art', 'head': 'info', 'prog': 'progress', 'bar': 'player', 'list': 'sidebar'}}},
}, css=r"""
/* nothing moves: e-ink can't, and it costs nothing to draw */
*, *::before, *::after { animation: none !important; transition: none !important; }
""" + FLAT + r"""
.lay-area { background-color: transparent !important; border: 0 !important; border-radius: 0 !important; }
.lay-art { padding: 12px !important; display: grid; place-items: center; min-height: 0; overflow: hidden; }
.lay-art .art-part { display: grid; grid-template: minmax(0, 1fr) / minmax(0, 1fr); place-items: center; width: 100%; height: 100%; min-height: 0; }
.lay-art img { width: auto !important; height: auto !important; max-width: 100% !important; max-height: 100% !important; aspect-ratio: 1; object-fit: cover;
  border-radius: 0 !important; filter: grayscale(1) contrast(1.1); box-shadow: none !important; }
.lay-info { text-align: left; align-self: center; border-bottom: 1px solid #202020 !important; padding-bottom: 10px !important; }
.lay-info [data-part="info.title"] { font: 400 30px Georgia, serif; letter-spacing: .01em; }
img { filter: grayscale(1); }
[data-part="tracklist.row"][data-state~="active"] { background-color: transparent !important; box-shadow: none !important; text-decoration: underline; text-underline-offset: 4px; }
[data-part="tracklist.row"] { border-bottom: 1px solid #cfccc4; border-radius: 0 !important; }
[data-part="player.button.play"] { background-color: #202020 !important; color: #e9e7e1 !important; box-shadow: none !important; }
[data-part="titlebar.brand"] { color: #202020 !important; text-shadow: none !important; }
[data-part="tracklist.row.artist"], [data-part="tracklist.row.time"] { color: #3a3a3a !important; opacity: 1; }
""")

# ── Retro Desktop: late-90s windows (generic, no OS logos): bevels, title bars, a taskbar along the bottom ──
BEVEL_OUT = 'box-shadow: inset -1px -1px 0 #0a0a0a, inset 1px 1px 0 #ffffff, inset -2px -2px 0 #808080, inset 2px 2px 0 #dfdfdf !important;'
BEVEL_IN = 'box-shadow: inset 1px 1px 0 #0a0a0a, inset -1px -1px 0 #ffffff, inset 2px 2px 0 #808080, inset -2px -2px 0 #dfdfdf !important;'
write('retro-desktop', {
    'id': 'retro-desktop', 'name': 'Retro Desktop', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'light',
    'description': 'Late-90s desktop windows: grey bevels, blue title bars on every panel, a teal desktop, the title bar as a taskbar along the bottom.',
    'tokens': light('#008080', '#000000', '#3a3a3a', '#c0c0c0', '#808080', '#000080', '#ffffff',
                    {'font.body': 'Tahoma, "MS Sans Serif", Verdana, sans-serif', 'color.text-strong': '#000000', 'color.knob': '#c0c0c0'}),
    'accent': {'mode': 'fixed', 'color': '#000080'},
    'parts': {'progress': {'variant': 'blocks'}, 'tracklist': {'variant': 'dense'}, 'player': {'variant': 'compact'}},
    'supports': {'background': ['black']},
    'strings': {'nowplaying.idle': 'Media Player: no file open', 'empty.queue': 'Playlist is empty', 'tab.queue': 'Playlist', 'tab.library': 'My Music', 'tab.search': 'Find'},
    'layout': {'home': {
        'areas': ['list art info', 'list art info', 'list prog prog', 'list bar bar', 'task task task'], 'columns': 'minmax(240px, 330px) minmax(0, 1fr) minmax(220px, 300px)',
        'rows': 'minmax(0, 1fr) minmax(0, 1fr) 54px 72px 36px', 'place': {'list': 'sidebar', 'art': 'art', 'info': 'info', 'bar': 'player', 'prog': 'progress', 'task': 'titlebar'},
        'resizable': ['list']}},
}, css=r"""
[data-part="background"] { background-color: #008080 !important; background-image: none !important; opacity: 1 !important; }
""" + FLAT.replace('box-shadow: none !important; ', '') + r"""
.lay-area { background-color: #c0c0c0 !important; border: 0 !important; border-radius: 0 !important; """ + BEVEL_OUT + r""" padding: 26px 6px 6px !important; position: relative; }
/* every panel is a window with a title bar */
.lay-area::before { position: absolute; top: 3px; left: 3px; right: 3px; height: 18px; padding: 0 6px; line-height: 18px; font: bold 12px Tahoma, sans-serif; color: #ffffff;
  background-image: linear-gradient(90deg, #000080, #1084d0); }
.lay-sidebar::before { content: "Playlist"; } .lay-art::before { content: "Album Art"; } .lay-info::before { content: "Now Playing"; }
.lay-player::before { content: "Controls"; } .lay-progress::before { content: "Progress"; }
/* the taskbar (the title bar, placed at the bottom) */
.lay-titlebar { padding: 0 !important; }
.lay-titlebar::before { display: none; }
.lay-titlebar [data-part="titlebar"] { background-color: #c0c0c0; border-top: 2px solid #ffffff; }
.lay-titlebar [data-part="titlebar.brand"] { margin: 3px 6px; padding: 0 10px; font: bold 12px Tahoma, sans-serif; color: #000000; line-height: 26px; """ + BEVEL_OUT + r""" }
.lay-titlebar button { color: #000000 !important; }
/* sunken fields, raised buttons */
[data-part="search"] input, .field, input[type="text"] { background-color: #ffffff !important; border-radius: 0 !important; border: 0 !important; """ + BEVEL_IN + r""" }
.btn, .chip, .pill, [data-part^="player.button"] { border-radius: 0 !important; background-color: #c0c0c0 !important; color: #000000 !important; border: 0 !important; """ + BEVEL_OUT + r""" }
.btn:active, [data-part^="player.button"]:active { """ + BEVEL_IN + r""" }
[data-part="tracklist"] { background-color: #ffffff; """ + BEVEL_IN + r""" }
[data-part="tracklist.row"] { border-radius: 0 !important; }
[data-part="tracklist.row"][data-state~="active"], [data-part="tracklist.row"]:hover { background-color: #000080 !important; box-shadow: none !important; }
[data-part="tracklist.row"][data-state~="active"] *, [data-part="tracklist.row"]:hover * { color: #ffffff !important; }
.lay-art { display: grid; place-items: center; min-height: 0; overflow: hidden; }
.lay-art .art-part { display: grid; grid-template: minmax(0, 1fr) / minmax(0, 1fr); place-items: center; width: 100%; height: 100%; min-height: 0; }
.lay-art img { width: auto !important; height: auto !important; max-width: 100% !important; max-height: 100% !important; aspect-ratio: 1; object-fit: cover; border-radius: 0 !important; image-rendering: pixelated; }
.lay-info { text-align: left; }
.lay-info [data-part="info.title"] { font: bold 18px Tahoma, sans-serif; }
[data-part="tracklist.row.artist"], [data-part="tracklist.row.time"] { color: #333333 !important; opacity: 1; }
.lay-titlebar [data-part="titlebar.brand"] { color: #000000 !important; text-shadow: none !important; }
""")

# the second batch
spec = importlib.util.spec_from_file_location('make_store_2', Path(__file__).resolve().parent / 'make-store-2.py')
spec.loader.exec_module(importlib.util.module_from_spec(spec))
spec = importlib.util.spec_from_file_location('make_store_3', Path(__file__).resolve().parent / 'make-store-3.py')
spec.loader.exec_module(importlib.util.module_from_spec(spec))
spec = importlib.util.spec_from_file_location('make_store_4', Path(__file__).resolve().parent / 'make-store-4.py')
spec.loader.exec_module(importlib.util.module_from_spec(spec))
