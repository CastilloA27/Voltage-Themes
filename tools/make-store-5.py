"""Wave 1 of the Theme FX themes (Voltage review round 15 > Wave 1, ship gate G4c): each one proves blocks.
python tools/make-store-5.py   (writes themes/<id>/; the helpers live in Voltage-Plugins)"""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_store_base import write, credits  # noqa: E402

PAUSED = '[data-part="app"]:not([data-state~="playing"])'

# ── Aurora: F7 (a WebGL sky in the background layer, from the "Aurora sky" helper) + F3 (the per-song seed: each song its
#    own sky). Black + the album's colours: the most on-brand. Without the helper: plain black (nothing breaks). ──
write('aurora', {
    'id': 'aurora', 'name': 'Aurora', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark', 'minVoltage': '1.7.2',
    'description': "Northern lights in the album's colours over a black sky, a different sky for every song, swaying with the music. "
                   'The player floats at the bottom so the sky has the window. Needs the "Aurora sky" plugin for the lights (graphics card, 30 fps while playing).',
    'plugin': 'aurora-sky',
    'uses': ['level'],
    'tokens': {'color.bg': '#000000', 'color.surface': 'rgba(0, 0, 0, .28)', 'color.border': 'rgba(255, 255, 255, .08)',
               'effect.blur': '14px', 'effect.glow-size': '18px', 'effect.glow-alpha': '35%', 'accent.album-mix': '1', 'shape.radius': '18px'},
    'supports': {'background': ['black']},
    'strings': {'nowplaying.idle': 'Clear skies', 'tab.queue': 'Up next'},
    'layout': {'home': {
        'areas': ['art info side', 'sky sky side', 'prog prog side', 'bar bar bar'],
        'columns': '88px minmax(0, 1fr) minmax(240px, 320px)', 'rows': '88px minmax(0, 1fr) 40px 76px',
        'place': {'art': 'art', 'info': 'info', 'side': 'sidebar', 'prog': 'progress', 'bar': 'player'}, 'resizable': ['side']}},
}, css=r"""
[data-part="background"] { background: #000 !important; opacity: 1 !important; }
/* the sky is the point: panels are thin glass, the empty middle is left to it */
.lay-area { background-color: rgb(0 0 0 / .22) !important; border-color: rgb(255 255 255 / .06) !important; box-shadow: none !important; }
.lay-art { background: none !important; border: none !important; }
.lay-art img { border-radius: 50% !important; box-shadow: 0 0 24px color-mix(in srgb, var(--accent) 45%, transparent) !important; }
.lay-info { background: none !important; border: none !important; align-self: center; }
.lay-info [data-part="info.title"] { font-weight: 300; font-size: 26px; letter-spacing: .02em; text-shadow: 0 0 18px color-mix(in srgb, var(--accent) 50%, transparent); }
.lay-player { border-radius: 38px !important; margin: 0 8% 10px; }
.lay-progress { background: none !important; border: none !important; }
""" + PAUSED + r""" .lay-info [data-part="info.title"] { opacity: .75; }
""", files={'CREDITS.md': credits(['Made for Voltage, CC0. The sky is drawn by the "Aurora sky" plugin (Settings > Plugins); without it the sky stays black.'])})

# ── Neon Sign: F13 (the title's letters buzz on one by one on every new song), F3 (the beat swells the glow), F4 (a tube that
#    flickers now and then, off with Reduce flashing). A sign on a dark brick wall; the Voltage brand showcase. ──
from make_store_base import ofl  # noqa: E402
write('neon-sign', {
    'id': 'neon-sign', 'name': 'Neon Sign', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark', 'minVoltage': '1.7.2',
    'description': "The song's title as a neon sign on a brick wall: its letters buzz on one by one with every new song, the glow swells "
                   'with the beat and one tube flickers now and then (never with Reduce flashing). The queue is the bar menu.',
    'fonts': [{'family': 'Monoton', 'src': 'assets/monoton/Monoton-Regular.ttf'}],
    'uses': ['beat'],
    'split': ['info.title', 'titlebar.brand'],
    'tokens': {'color.bg': '#0d0709', 'color.text': '#ffeef8', 'color.text-dim': '#d9b3c9', 'color.surface': 'rgba(18, 8, 14, .78)',
               'color.border': 'rgba(255, 60, 200, .28)', 'effect.blur': '6px', 'effect.glow-size': '22px', 'effect.glow-alpha': '70%',
               'accent.album-mix': '0.35', 'shape.radius': '10px'},
    'accent': {'mode': 'fixed', 'color': '#ff3cc8'},
    'supports': {'background': ['gradient']},
    'strings': {'nowplaying.idle': 'CLOSED', 'tab.queue': 'Menu', 'empty.queue': 'Nothing on tonight'},
    'layout': {'home': {
        'areas': ['sign sign', 'menu art', 'menu prog', 'bar bar'],
        'columns': 'minmax(240px, 310px) minmax(0, 1fr)', 'rows': 'minmax(120px, auto) minmax(0, 1fr) 40px 78px',
        'place': {'sign': 'info', 'menu': 'sidebar', 'art': 'art', 'prog': 'progress', 'bar': 'player'}, 'resizable': ['menu']}},
}, css=r"""
/* the wall: dark bricks, lit from the sign above */
[data-part="background"] { opacity: 1 !important; background-color: #140a0e !important;
  background-image: radial-gradient(ellipse 70% 45% at 50% 0%, color-mix(in srgb, var(--accent) 22%, transparent), transparent 70%),
    url("assets/bricks.svg") !important;
  background-size: 100% 100%, 96px 48px !important; background-position: 0 0, 0 0 !important; }
.lay-area { background-color: rgb(10 4 8 / .72) !important; box-shadow: none !important; }
.lay-info { background: none !important; border: none !important; display: grid; place-items: center; text-align: center; }
/* the sign: tubes in the accent colour, a glow that swells with the beat (--fx-beat 0-1) */
.lay-info [data-part="info.title"] { font: 400 clamp(26px, 5.2vw, 60px)/1.15 "Monoton", sans-serif; letter-spacing: .04em; color: #fff4fb;
  --glow: calc(8px + var(--fx-beat, 0) * 14px);
  text-shadow: 0 0 4px #fff, 0 0 var(--glow) var(--accent), 0 0 calc(var(--glow) * 2.2) var(--accent), 0 0 calc(var(--glow) * 4) color-mix(in srgb, var(--accent) 60%, transparent); }
.lay-info .split .ch { display: inline-block; animation: tube-on .9s steps(1, end) both; animation-delay: calc(var(--i) * 70ms); }
@keyframes tube-on { 0% { opacity: .08; text-shadow: none; } 30% { opacity: 1; } 38% { opacity: .15; text-shadow: none; } 52% { opacity: 1; } 60% { opacity: .3; } 70%, 100% { opacity: 1; } }
/* one tube in every seven flickers briefly, every few seconds (2 dips in 10 s: well under 3 a second) */
.lay-info .split .ch:nth-child(7n+4) { animation: tube-on .9s steps(1, end) both, tube-flicker 10s steps(1, end) 2s infinite; animation-delay: calc(var(--i) * 70ms), calc(2s + var(--i) * 300ms); }
@keyframes tube-flicker { 0%, 91% { opacity: 1; } 92% { opacity: .2; } 93% { opacity: 1; } 95% { opacity: .35; } 96%, 100% { opacity: 1; } }
:root[data-reduce-flash] .lay-info .split .ch, .reduce-motion .lay-info .split .ch { animation: none !important; opacity: 1; }
[data-part="app"]:not([data-state~="playing"]) .lay-info [data-part="info.title"] { --glow: 4px; opacity: .55; }
.lay-info [data-part="info.sub"], .lay-info .song-sub { color: #ffd6ee; text-shadow: 0 0 8px color-mix(in srgb, var(--accent) 60%, transparent); }
/* the brand in the title bar: a small sign too */
[data-part="titlebar.brand"] { font-family: "Monoton", sans-serif !important; color: #fff4fb !important; text-shadow: 0 0 6px var(--accent), 0 0 14px var(--accent); }
/* the cover: a lit poster in a frame, fitted to its cell */
.lay-art { display: grid; place-items: center; min-height: 0; overflow: hidden; container-type: size; }
.lay-art .art-part { display: grid; place-items: center; width: 100%; height: 100%; min-height: 0; }
.lay-art img { width: min(88cqw, 88cqh) !important; height: min(88cqw, 88cqh) !important; object-fit: cover; border: 3px solid #2a1420 !important; box-shadow: 0 0 0 1px var(--accent), 0 0 30px color-mix(in srgb, var(--accent) 40%, transparent) !important; border-radius: 4px !important; }
/* the menu: chalk-white rows, the playing one lit */
[data-part="tracklist.row"][data-state~="active"] { box-shadow: inset 3px 0 0 var(--accent), 0 0 18px color-mix(in srgb, var(--accent) 30%, transparent) !important; }
""", files={**ofl('monoton', 'Monoton-Regular.ttf'), 'assets/bricks.svg': '<svg xmlns="http://www.w3.org/2000/svg" width="96" height="48" viewBox="0 0 96 48"><rect width="96" height="48" fill="#0a0507"/><rect x="1" y="1" width="46" height="22" fill="#1c0e13"/><rect x="49" y="1" width="46" height="22" fill="#190c11"/><rect x="-23" y="25" width="46" height="22" fill="#1a0d12"/><rect x="25" y="25" width="46" height="22" fill="#1e0f15"/><rect x="73" y="25" width="46" height="22" fill="#1a0d12"/></svg>',
            'CREDITS.md': credits(['Font: Monoton by Vernon Adams, SIL Open Font License 1.1 (assets/monoton/OFL.txt).', 'Everything else: made for Voltage, CC0.'])})
