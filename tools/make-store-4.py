"""Effect packs (Voltage review round 15 F16): small extras stacked on any theme. "kind": "effect": tokens, layout, strings
and hotspots are ignored; CSS, overlay, sprites and options apply on top of the active theme."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_store_base import write, credits  # noqa: E402

PAUSE = '[data-part="app"]:not([data-state~="playing"]) [data-part="overlay"] { animation-play-state: paused; }'
RM = '@media (prefers-reduced-motion: reduce) { [data-part="overlay"] { animation: none; } }'

write('fx-snow', {
    'id': 'fx-snow', 'name': 'Snow', 'version': '1.0.0', 'author': 'Voltage', 'kind': 'effect',
    'description': 'Slow snowfall over any theme. Pauses with the music.', 'overlay': True,
}, css=r"""
[data-part="overlay"] { background-image: radial-gradient(circle, rgb(255 255 255 / .85) 0 1.5px, transparent 2px), radial-gradient(circle, rgb(255 255 255 / .5) 0 1px, transparent 1.5px);
  background-size: 140px 140px, 80px 80px; background-position: 0 0, 40px 25px; animation: snow 16s linear infinite; }
@keyframes snow { to { background-position: 35px 280px, 80px 160px; } }
""" + PAUSE + RM, files={'CREDITS.md': credits(['Made for Voltage, CC0.'])})

write('fx-grain', {
    'id': 'fx-grain', 'name': 'Film grain', 'version': '1.0.0', 'author': 'Voltage', 'kind': 'effect',
    'description': 'A soft film grain and vignette over any theme. Still (no animation): costs almost nothing.', 'overlay': True,
}, css=r"""
[data-part="overlay"] { opacity: .5; mix-blend-mode: overlay;
  background-image: radial-gradient(ellipse at center, transparent 55%, rgb(0 0 0 / .45) 100%),
    repeating-radial-gradient(circle at 17% 32%, rgb(255 255 255 / .06) 0 1px, transparent 1px 3px),
    repeating-radial-gradient(circle at 73% 61%, rgb(0 0 0 / .07) 0 1px, transparent 1px 2.5px); }
""", files={'CREDITS.md': credits(['Made for Voltage, CC0.'])})

write('fx-beat-pulse', {
    'id': 'fx-beat-pulse', 'name': 'Beat pulse', 'version': '1.0.0', 'author': 'Voltage', 'kind': 'effect',
    'description': "The window's edge glows with the beat (at most 3 pulses a second, softer with Reduce flashing).", 'overlay': True, 'uses': ['beat'],
}, css=r"""
[data-part="overlay"] { box-shadow: inset 0 0 calc(10px + var(--fx-beat, 0) * 50px) calc(var(--fx-beat, 0) * 6px) var(--accent, #a020f0); opacity: calc(.15 + var(--fx-beat, 0) * .85); }
""", files={'CREDITS.md': credits(['Made for Voltage, CC0.'])})
