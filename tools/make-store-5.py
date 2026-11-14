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
