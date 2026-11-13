"""Second batch of store themes (Comic, Big & Clear, Deep Space, Aquarium). Run make-store.py, which imports this."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_store_base import write, ofl, credits, light, FLAT, FONTS

# ── Comic: a comic page. Panels with thick ink borders and halftone dots, the lyrics as speech bubbles, POW on a like ──
write('comic', {
    'id': 'comic', 'name': 'Comic', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'light',
    'description': 'A comic page: ink-bordered panels, halftone dots, the lyrics as speech bubbles, a lettered title and a POW! on every like.',
    'fonts': [{'family': 'Bangers', 'src': 'assets/bangers/Bangers-Regular.ttf'}],
    'tokens': light('#fff6d8', '#111111', '#3a3a3a', '#ffffff', '#111111', '#e5221a', '#ffffff', {'font.body': '"Segoe UI", sans-serif'}),
    'accent': {'mode': 'fixed', 'color': '#e5221a'},
    'parts': {'progress': {'variant': 'line'}, 'tracklist': {'variant': 'dense'}},
    'supports': {'background': ['black']},
    'overlay': True,
    'strings': {'note.liked': 'POW!', 'nowplaying.idle': 'Meanwhile... nothing is playing', 'empty.queue': 'To be continued (queue a song)'},
    'layout': {'home': {
        'areas': ['art lyr list', 'info lyr list', 'prog prog prog', 'bar bar bar'], 'columns': 'minmax(220px, 1fr) minmax(0, 1.2fr) minmax(260px, 330px)',
        'rows': 'minmax(0, 1fr) auto 44px 72px',
        'place': {'art': 'art', 'info': 'info', 'lyr': 'lyrics', 'prog': 'progress', 'bar': 'player', 'list': 'sidebar'},
        'resizable': ['list']}},
}, css=r"""
[data-part="background"] { background-color: #fff6d8 !important; opacity: 1 !important; background-image: radial-gradient(circle, rgb(229 34 26 / .16) 1.2px, transparent 1.6px) !important; background-size: 8px 8px !important; }
""" + FLAT + r"""
.lay-area { background-color: #ffffff !important; border: 3px solid #111111 !important; border-radius: 2px !important; box-shadow: 5px 5px 0 #111111 !important; }
[data-part="titlebar.brand"], [data-part="info.title"], .for-you-title { font-family: "Bangers", "Impact", sans-serif; letter-spacing: .06em; }
[data-part="titlebar.brand"] { font-size: 22px; color: #c0150e; text-shadow: 1px 1px 0 #111111; }
.lay-info [data-part="info.title"] { font-size: 34px; color: #111111; background-color: #ffe14a; padding: 2px 12px; display: inline-block; transform: rotate(-1.5deg); border: 2.5px solid #111111; }
.lay-info { text-align: left; }
.lay-art { display: grid; place-items: center; min-height: 0; overflow: hidden; padding: 10px !important;
  background-image: radial-gradient(circle, rgb(17 17 17 / .18) 1.4px, transparent 1.8px) !important; background-size: 6px 6px !important; }
.lay-art .art-part { display: grid; grid-template: minmax(0, 1fr) / minmax(0, 1fr); place-items: center; width: 100%; height: 100%; min-height: 0; }
.lay-art img { width: auto !important; height: auto !important; max-width: 100% !important; max-height: 100% !important; aspect-ratio: 1; object-fit: cover;
  border: 3px solid #111111; border-radius: 0 !important; filter: contrast(1.25) saturate(1.3); }
/* the lyrics as speech bubbles */
.lay-lyrics .lyrics { width: 100% !important; height: 100% !important; padding: 20% 18px !important; text-align: left; }
.lay-lyrics [data-part="lyrics.line"] { display: table; position: relative; margin: 14px 0; padding: 8px 14px; max-width: 85%; font-size: 16px; font-weight: 600;
  color: #111111; background-color: #ffffff; border: 2.5px solid #111111; border-radius: 18px; opacity: .6; }
.lay-lyrics [data-part="lyrics.line"]:nth-child(even) { margin-left: auto; }
.lay-lyrics [data-part="lyrics.line"]::after { content: ""; position: absolute; left: 22px; bottom: -9px; width: 12px; height: 12px; background-color: inherit;
  border-right: 2.5px solid #111111; border-bottom: 2.5px solid #111111; transform: rotate(45deg); }
.lay-lyrics [data-part="lyrics.line"][data-state~="active"] { opacity: 1; background-color: #ffe14a; }
[data-part="tracklist.row"][data-state~="active"] { background-color: #ffe14a !important; box-shadow: inset 0 0 0 2px #111111 !important; }
[data-part="tracklist.row.artist"], [data-part="tracklist.row.time"] { color: #333333 !important; opacity: 1; }
[data-part="player.button.play"] { background-color: #e5221a !important; color: #ffffff !important; border: 2.5px solid #111111 !important; box-shadow: 3px 3px 0 #111111 !important; }
/* POW! on a like */
[data-part="overlay"]::after { content: "POW!"; position: absolute; left: 50%; top: 45%; transform: translate(-50%, -50%) scale(0); padding: 30px 46px;
  font: 400 min(12vw, 110px) "Bangers", sans-serif; color: #ffe14a; -webkit-text-stroke: 3px #111111; background-color: #e5221a; opacity: 0;
  clip-path: polygon(50% 0, 61% 30%, 98% 20%, 72% 48%, 100% 72%, 64% 70%, 56% 100%, 44% 72%, 6% 86%, 30% 56%, 0 30%, 38% 32%); }
:root[data-event="like"] [data-part="overlay"]::after { animation: pow 1s cubic-bezier(.2, 1.4, .4, 1); }
@keyframes pow { 0% { opacity: 0; transform: translate(-50%, -50%) scale(0) rotate(-12deg); } 25% { opacity: 1; transform: translate(-50%, -50%) scale(1.1) rotate(4deg); } 70% { opacity: 1; transform: translate(-50%, -50%) scale(1) rotate(0); } 100% { opacity: 0; transform: translate(-50%, -50%) scale(1.2); } }
""", files={**ofl('bangers', 'Bangers-Regular.ttf'),
            'CREDITS.md': credits(['Font: Bangers by the Bangers Project Authors (Vernon Adams), SIL Open Font License 1.1 (assets/bangers/OFL.txt).',
                                   'Everything else: made for Voltage, CC0. No characters from any comic.'])})

# ── Big & Clear: an accessibility theme. Large text, big buttons, contrast above 7:1, nothing moving ──
write('big-and-clear', {
    'id': 'big-and-clear', 'name': 'Big & Clear', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark',
    'description': 'Large, clear and calm: big text in a font made for legibility, big buttons, contrast above 7:1, no blur and no motion. The player first, the list below.',
    'fonts': [{'family': 'Atkinson Hyperlegible', 'src': 'assets/atkinson/AtkinsonHyperlegible-Regular.ttf', 'weight': '400'},
              {'family': 'Atkinson Hyperlegible', 'src': 'assets/atkinson/AtkinsonHyperlegible-Bold.ttf', 'weight': '700'}],
    'tokens': {'color.bg': '#000000', 'color.text': '#ffffff', 'color.text-dim': '#e0e0e0', 'color.text-strong': '#ffffff', 'color.text-soft': '#ffffff',
               'color.text-muted': '#e0e0e0', 'color.surface': '#111111', 'color.border': '#ffffff', 'color.brand': '#ffd400', 'color.on-accent': '#000000',
               'color.knob': '#ffffff', 'color.focus': '#ffd400', 'color.select-bg': '#333300', 'surface.menu': '#111111', 'surface.pop': '#111111',
               'surface.tip': '#111111', 'effect.blur': '0px', 'effect.glow-size': '0px', 'effect.glow-alpha': '0%', 'accent.album-mix': '0',
               'shape.radius': '10px', 'font.body': '"Atkinson Hyperlegible", "Segoe UI", sans-serif'},
    'accent': {'mode': 'fixed', 'color': '#ffd400'},
    'parts': {'progress': {'variant': 'line'}},
    'supports': {'background': ['black']},
    'layout': {'home': {
        'areas': ['art info', 'prog prog', 'bar vol', 'list list'], 'columns': 'minmax(160px, 240px) minmax(0, 1fr)', 'rows': 'minmax(150px, 240px) 60px 96px minmax(0, 1fr)',
        'place': {'art': 'art', 'info': 'info', 'prog': 'progress', 'bar': 'player', 'vol': 'volume', 'list': 'sidebar'}}},
}, css=r"""
*, *::before, *::after { animation: none !important; transition: none !important; }
""" + FLAT + r"""
.app { font-size: 17px; }
.lay-area { background-color: #111111 !important; border: 2px solid #ffffff !important; }
.lay-art { display: grid; place-items: center; min-height: 0; overflow: hidden; }
.lay-art .art-part { display: grid; grid-template: minmax(0, 1fr) / minmax(0, 1fr); place-items: center; width: 100%; height: 100%; min-height: 0; }
.lay-art img { width: auto !important; height: auto !important; max-width: 100% !important; max-height: 100% !important; aspect-ratio: 1; object-fit: cover; }
.lay-info { text-align: left; align-self: center; padding: 0 18px !important; }
.lay-info [data-part="info.title"] { font-size: 36px; font-weight: 700; line-height: 1.15; }
.lay-info .info-part > :not([data-part="info.title"]) { font-size: 20px; }
[data-part="tracklist.row"] { padding: 12px 10px !important; font-size: 18px; border-bottom: 1px solid #555555; }
[data-part="tracklist.row"] img { width: 56px !important; height: 56px !important; }
[data-part="tracklist.row.artist"], [data-part="tracklist.row.time"] { font-size: 16px !important; color: #e0e0e0 !important; opacity: 1; }
[data-part="tracklist.row"][data-state~="active"] { background-color: #333300 !important; box-shadow: inset 0 0 0 3px #ffd400 !important; }
.lay-player .btn, .lay-volume .btn { min-width: 52px !important; min-height: 52px !important; }
[data-part="player.button.play"] { min-width: 76px !important; min-height: 76px !important; background-color: #ffd400 !important; color: #000000 !important; }
:focus-visible { outline: 4px solid #ffd400 !important; outline-offset: 3px !important; }
[data-part="progress.time"] { font-size: 16px; color: #ffffff; }
""", files={**ofl('atkinson', 'AtkinsonHyperlegible-Regular.ttf'), 'assets/atkinson/AtkinsonHyperlegible-Bold.ttf': (FONTS / 'atkinson' / 'AtkinsonHyperlegible-Bold.ttf').read_bytes(),
            'CREDITS.md': credits(['Font: Atkinson Hyperlegible by the Braille Institute of America, SIL Open Font License 1.1 (assets/atkinson/OFL.txt).'])})

# ── Deep Space: a slow starfield, the cover as a planet in an orbit ring with a moon, HUD lettering ──
STARS = ', '.join(f'radial-gradient({r}px {r}px at {x}% {y}%, rgb(255 255 255 / {a}), transparent)' for x, y, r, a in
                  [(7, 12, 1.2, .9), (19, 66, 1, .7), (31, 28, 1.5, .8), (44, 81, 1, .6), (52, 9, 1.2, .8), (63, 47, 1, .7), (71, 73, 1.6, .9),
                   (83, 22, 1, .7), (91, 59, 1.3, .8), (12, 44, 1, .6), (37, 57, 1.1, .7), (77, 91, 1, .6), (96, 6, 1.2, .8), (4, 87, 1, .6)])
write('deep-space', {
    'id': 'deep-space', 'name': 'Deep Space', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark',
    'description': 'A slow starfield, the cover as a planet inside an orbit ring with a moon, HUD lettering; the list docked on the right.',
    'fonts': [{'family': 'IBM Plex Mono', 'src': 'assets/plexmono/IBMPlexMono-Regular.ttf'}],
    'tokens': {'color.bg': '#02030a', 'color.text': '#dfe8ff', 'color.text-dim': '#9fb0d8', 'color.text-strong': '#ffffff', 'color.text-soft': '#cfdcff',
               'color.text-muted': '#aebde3', 'color.surface': 'rgba(10, 16, 40, .55)', 'color.border': 'rgba(120, 170, 255, .22)', 'color.brand': '#7fb2ff',
               'color.on-accent': '#02030a', 'color.knob': '#dfe8ff', 'color.select-bg': '#14224a', 'surface.menu': '#0a1028', 'surface.pop': '#0a1028',
               'surface.tip': '#0a1028', 'effect.blur': '10px', 'effect.glow-size': '14px', 'effect.glow-alpha': '35%', 'accent.album-mix': '0.25',
               'shape.radius': '14px', 'font.mono': '"IBM Plex Mono", Consolas, monospace'},
    'accent': {'mode': 'fixed', 'color': '#7fb2ff'},
    'parts': {'progress': {'variant': 'line'}, 'tracklist': {'variant': 'dense'}},
    'supports': {'background': ['gradient']},
    'overlay': True,
    'strings': {'nowplaying.idle': 'Signal lost in deep space', 'tab.queue': 'Flight plan', 'empty.queue': 'Flight plan empty'},
    'layout': {'home': {
        'areas': ['orbit list', 'info list', 'prog list', 'bar list'], 'columns': 'minmax(0, 1fr) minmax(260px, 340px)', 'rows': 'minmax(0, 1fr) auto 44px 72px',
        'place': {'orbit': 'art', 'info': 'info', 'prog': 'progress', 'bar': 'player', 'list': 'sidebar'}, 'resizable': ['list']}},
}, css=r"""
[data-part="background"] { background-color: #02030a !important; opacity: 1 !important;
  background-image: radial-gradient(70% 60% at 30% 40%, rgb(40 60 140 / .35), transparent 70%), radial-gradient(50% 40% at 80% 80%, rgb(120 40 140 / .25), transparent 70%) !important; }
[data-part="overlay"] { background-image: """ + STARS + r"""; background-size: 100% 100%; opacity: .9; animation: drift 120s linear infinite alternate; }
@keyframes drift { to { transform: translate(-2%, 1.5%) scale(1.04); } }
.lay-art, .lay-info, .lay-progress, .lay-player { background-color: transparent !important; border-color: transparent !important; box-shadow: none !important; backdrop-filter: none !important; }
.lay-art { display: grid; place-items: center; min-height: 0; overflow: hidden; position: relative; }
.lay-art .art-part { display: grid; grid-template: minmax(0, 1fr) / minmax(0, 1fr); place-items: center; width: 100%; height: 100%; min-height: 0; }
.lay-art img { width: auto !important; height: auto !important; max-width: 60% !important; max-height: 60% !important; aspect-ratio: 1; object-fit: cover; border-radius: 50% !important;
  box-shadow: inset -18px -12px 40px rgb(0 0 0 / .7), 0 0 60px rgb(127 178 255 / .35) !important; }
/* the orbit ring (a flat ellipse) and a moon going round it */
.lay-art::before { content: ""; position: absolute; left: 50%; top: 50%; width: 88%; height: 26%; transform: translate(-50%, -50%) rotate(-12deg);
  border: 1.5px solid rgb(127 178 255 / .45); border-radius: 50%; pointer-events: none; }
.lay-art::after { content: ""; position: absolute; left: 50%; top: 50%; width: 12px; height: 12px; margin: -6px; border-radius: 50%; background-color: #dfe8ff;
  box-shadow: 0 0 10px #7fb2ff; animation: orbit 24s linear infinite; pointer-events: none; }
@keyframes orbit { 0% { transform: rotate(-12deg) translate(-44cqw, 0) rotate(12deg); } 25% { transform: rotate(-12deg) translate(0, 13cqh) rotate(12deg); }
  50% { transform: rotate(-12deg) translate(44cqw, 0) rotate(12deg); } 75% { transform: rotate(-12deg) translate(0, -13cqh) rotate(12deg); } 100% { transform: rotate(-12deg) translate(-44cqw, 0) rotate(12deg); } }
.lay-art { container-type: size; }
[data-part="app"]:not([data-state~="playing"]) .lay-art::after, [data-part="app"]:not([data-state~="playing"]) [data-part="overlay"] { animation-play-state: paused; }
.lay-info [data-part="info.title"] { font-family: "IBM Plex Mono", Consolas, monospace; letter-spacing: .18em; text-transform: uppercase; font-size: 22px; font-weight: 400; }
.lay-info, [data-part="progress.time"], [data-part="tracklist.row.time"] { font-family: "IBM Plex Mono", Consolas, monospace; }
[data-part="tracklist.row"][data-state~="active"] { background-color: rgb(127 178 255 / .12) !important; box-shadow: inset 2px 0 0 #7fb2ff !important; }
@media (prefers-reduced-motion: reduce) { [data-part="overlay"], .lay-art::after { animation: none; } }
""", files={**ofl('plexmono', 'IBMPlexMono-Regular.ttf'),
            'CREDITS.md': credits(['Font: IBM Plex Mono by IBM, SIL Open Font License 1.1 (assets/plexmono/OFL.txt).', 'Everything else: made for Voltage, CC0.'])})

# ── Aquarium: deep teal water, bubbles rising, light ripples over the cover ──
BUBBLE = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 400 800"><g fill="none" stroke="#bff6ff" stroke-opacity=".5">'
          + ''.join(f'<circle cx="{x}" cy="{y}" r="{r}" stroke-width="{1 if r < 6 else 1.5}"/>' for x, y, r in
                    [(40, 700, 6), (60, 520, 4), (120, 640, 9), (170, 300, 5), (210, 760, 7), (260, 420, 3), (300, 600, 10), (330, 180, 5), (370, 520, 6), (90, 90, 4), (240, 60, 8)])
          + '</g></svg>\n')
write('aquarium', {
    'id': 'aquarium', 'name': 'Aquarium', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark',
    'description': 'Deep teal water: bubbles rising, light ripples playing over the round cover, the controls on the sand at the bottom.',
    'tokens': {'color.bg': '#021a1f', 'color.text': '#e2fbff', 'color.text-dim': '#9fd0d8', 'color.text-strong': '#ffffff', 'color.text-soft': '#d0f4fa',
               'color.text-muted': '#acdbe2', 'color.surface': 'rgba(4, 52, 62, .5)', 'color.border': 'rgba(150, 240, 255, .2)', 'color.brand': '#4fe3e8',
               'color.on-accent': '#022126', 'color.knob': '#e2fbff', 'color.select-bg': '#0a4a55', 'surface.menu': '#04323b', 'surface.pop': '#04323b',
               'surface.tip': '#04323b', 'effect.blur': '14px', 'effect.glow-size': '12px', 'effect.glow-alpha': '35%', 'accent.album-mix': '0.2', 'shape.radius': '22px'},
    'accent': {'mode': 'fixed', 'color': '#4fe3e8'},
    'parts': {'progress': {'variant': 'line'}},
    'supports': {'background': ['gradient']},
    'overlay': True,
    'strings': {'nowplaying.idle': 'Just bubbles', 'tab.queue': 'Current', 'empty.queue': 'The tank is empty'},
    'layout': {'home': {
        'areas': ['list tank', 'list name', 'sand sand', 'bar bar'], 'columns': 'minmax(260px, 340px) minmax(0, 1fr)', 'rows': 'minmax(0, 1fr) auto 44px 76px',
        'place': {'list': 'sidebar', 'tank': 'art', 'name': 'info', 'sand': 'progress', 'bar': 'player'}, 'resizable': ['list']}},
}, css=r"""
[data-part="background"] { background-color: #021a1f !important; opacity: 1 !important;
  background-image: linear-gradient(180deg, rgb(20 120 130 / .55), transparent 55%), linear-gradient(0deg, rgb(160 130 80 / .35), transparent 16%) !important; }
[data-part="overlay"] { background-image: url("assets/bubbles.svg"), url("assets/bubbles.svg"); background-size: 400px 800px, 260px 520px; background-repeat: repeat;
  animation: rise 28s linear infinite; opacity: .8; }
@keyframes rise { to { background-position: 0 -800px, 130px -520px; } }
[data-part="app"]:not([data-state~="playing"]) [data-part="overlay"] { animation-play-state: paused; }
.lay-art, .lay-info, .lay-progress { background-color: transparent !important; border-color: transparent !important; box-shadow: none !important; backdrop-filter: none !important; }
.lay-art { display: grid; place-items: center; min-height: 0; overflow: hidden; position: relative; }
.lay-art .art-part { display: grid; grid-template: minmax(0, 1fr) / minmax(0, 1fr); place-items: center; width: 100%; height: 100%; min-height: 0; position: relative; }
.lay-art img { width: auto !important; height: auto !important; max-width: 78% !important; max-height: 78% !important; aspect-ratio: 1; object-fit: cover; border-radius: 50% !important;
  box-shadow: 0 0 0 6px rgb(79 227 232 / .25), 0 20px 60px rgb(0 0 0 / .5) !important; }
/* caustics: light ripples over the cover */
.lay-art .art-part::after { content: ""; position: absolute; left: 50%; top: 50%; width: min(78%, 78vh); aspect-ratio: 1; transform: translate(-50%, -50%); border-radius: 50%; pointer-events: none;
  background-image: radial-gradient(40% 18% at 30% 30%, rgb(220 255 255 / .28), transparent 70%), radial-gradient(30% 14% at 65% 55%, rgb(220 255 255 / .22), transparent 70%),
    radial-gradient(35% 16% at 45% 78%, rgb(220 255 255 / .18), transparent 70%);
  mix-blend-mode: screen; animation: caustic 7s ease-in-out infinite alternate; }
@keyframes caustic { to { background-position: 20px 12px, -16px 8px, 10px -14px; } }
[data-part="app"]:not([data-state~="playing"]) .lay-art .art-part::after { animation-play-state: paused; }
.lay-info [data-part="info.title"] { font-size: 30px; }
.lay-progress { border-top: 2px solid rgb(200 170 110 / .35) !important; }
[data-part="tracklist.row"][data-state~="active"] { background-color: rgb(79 227 232 / .14) !important; }
@media (prefers-reduced-motion: reduce) { [data-part="overlay"], .lay-art .art-part::after { animation: none; } }
""", files={'assets/bubbles.svg': BUBBLE, 'CREDITS.md': credits(['Bubbles and everything else: made for Voltage, CC0.'])})
