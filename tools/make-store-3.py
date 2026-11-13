"""Third batch of store themes: Vinyl Lounge, Cassette, Handheld, Night City, Studio, Seasonal (Halloween, Winter)."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from make_store_base import write, ofl, credits, light, FLAT, FONTS  # noqa: E402

FIT = r"""
.lay-art { display: grid; place-items: center; min-height: 0; overflow: hidden; position: relative; }
.lay-art .art-part { display: grid; grid-template: minmax(0, 1fr) / minmax(0, 1fr); place-items: center; width: 100%; height: 100%; min-height: 0; position: relative; }
"""
PAUSED = '[data-part="app"]:not([data-state~="playing"])'

# ── Vinyl Lounge: walnut and brass; the cover is a record that spins while playing, a tonearm swings in on play ──
write('vinyl-lounge', {
    'id': 'vinyl-lounge', 'name': 'Vinyl Lounge', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark',
    'description': 'Walnut and brass: the cover as a spinning record on a turntable, a tonearm that swings in on play and out on pause, the queue as a record crate.',
    'fonts': [{'family': 'DM Serif Display', 'src': 'assets/dmserif/DMSerifDisplay-Regular.ttf'}],
    'tokens': {'color.bg': '#1a0f08', 'color.text': '#f4e6d0', 'color.text-dim': '#cdb79a', 'color.text-strong': '#fff6e6', 'color.text-soft': '#ead8bc',
               'color.text-muted': '#d6c0a2', 'color.surface': 'rgba(52, 30, 16, .7)', 'color.border': 'rgba(212, 170, 100, .3)', 'color.brand': '#d4aa64',
               'color.on-accent': '#1a0f08', 'color.knob': '#e8cc90', 'color.select-bg': '#4a2c14', 'surface.menu': '#2a180c', 'surface.pop': '#2a180c',
               'surface.tip': '#2a180c', 'effect.blur': '0px', 'effect.glow-size': '8px', 'effect.glow-alpha': '25%', 'accent.album-mix': '0.15', 'shape.radius': '10px'},
    'accent': {'mode': 'fixed', 'color': '#d4aa64'},
    'parts': {'progress': {'variant': 'line'}, 'tracklist': {'variant': 'dense'}},
    'supports': {'background': ['gradient']},
    'strings': {'tab.queue': 'Crate', 'nowplaying.idle': 'Put a record on', 'empty.queue': 'The crate is empty'},
    'layout': {'home': {
        'areas': ['deck crate', 'info crate', 'prog crate', 'bar crate'], 'columns': 'minmax(0, 1fr) minmax(260px, 340px)', 'rows': 'minmax(0, 1fr) auto 44px 76px',
        'place': {'deck': 'art', 'info': 'info', 'prog': 'progress', 'bar': 'player', 'crate': 'sidebar'}, 'resizable': ['crate']}},
}, css=r"""
[data-part="background"] { background-color: #1a0f08 !important; opacity: 1 !important;
  background-image: repeating-linear-gradient(92deg, rgb(255 220 170 / .025) 0 3px, transparent 3px 11px), radial-gradient(80% 60% at 40% 30%, rgb(120 70 30 / .45), transparent 70%) !important; }
""" + FLAT + FIT + r"""
.lay-art, .lay-info, .lay-progress, .lay-player { background-color: transparent !important; border-color: transparent !important; }
/* the plinth */
.lay-art { margin: 10px; border-radius: 16px; background-image: linear-gradient(160deg, #5a3418, #3a200e) !important; box-shadow: inset 0 0 0 2px #d4aa64, 0 20px 40px rgb(0 0 0 / .5) !important; }
/* the record: a black disc with grooves, the cover as its label */
.lay-art { container-type: size; } /* on the cell: on .art-part it collapses to 0 wide (size containment) */
.lay-art .art-part::before { content: ""; position: absolute; width: min(82cqw, 82cqh); aspect-ratio: 1; border-radius: 50%;
  background-image: repeating-radial-gradient(circle, #111 0 2px, #1c1c1c 2px 3px), radial-gradient(circle, transparent 30%, rgb(255 255 255 / .06) 31%, transparent 60%);
  box-shadow: 0 6px 18px rgb(0 0 0 / .7); }
.lay-art img { width: min(32cqw, 32cqh) !important; height: auto !important; aspect-ratio: 1; object-fit: cover; border-radius: 50% !important; position: relative; z-index: 1;
  animation: spin 1.8s linear infinite; }
""" + PAUSED + r""" .lay-art img { animation-play-state: paused; }
@keyframes spin { to { transform: rotate(360deg); } }
/* the tonearm: swings onto the record while playing */
.lay-art::after { content: ""; position: absolute; right: 9%; top: 10%; width: 12px; height: 46%; border-radius: 6px; z-index: 2; transform-origin: 50% 6px;
  background-image: linear-gradient(90deg, #b48a46, #f2d48c, #b48a46); box-shadow: 0 0 0 3px rgb(0 0 0 / .25); transform: rotate(-4deg); transition: transform .9s cubic-bezier(.3, .6, .3, 1); }
[data-part="app"][data-state~="playing"] .lay-art::after { transform: rotate(24deg); }
.lay-info [data-part="info.title"] { font-family: "DM Serif Display", Georgia, serif; font-size: 32px; font-weight: 400; color: #fff6e6; }
[data-part="tracklist.row"][data-state~="active"] { background-color: rgb(212 170 100 / .16) !important; box-shadow: inset 3px 0 0 #d4aa64 !important; }
[data-part="player.button.play"] { background-image: radial-gradient(circle at 40% 30%, #f2d48c, #b48a46) !important; color: #1a0f08 !important; }
@media (prefers-reduced-motion: reduce) { .lay-art img { animation: none; } .lay-art::after { transition: none; } }
""", files={**ofl('dmserif', 'DMSerifDisplay-Regular.ttf'),
            'CREDITS.md': credits(['Font: DM Serif Display by Colophon Foundry / Google, SIL Open Font License 1.1 (assets/dmserif/OFL.txt).', 'Everything else: made for Voltage, CC0.'])})

# ── Cassette: an 80s tape deck. Two reels turning in the window, the queue as a hand-written J-card, chunky piano keys ──
write('cassette', {
    'id': 'cassette', 'name': 'Cassette', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark',
    'description': 'An 80s tape deck: the cover on the cassette label with two reels turning in its window, the queue as a hand-written J-card, chunky piano-key buttons.',
    'fonts': [{'family': 'Caveat', 'src': 'assets/caveat/Caveat.ttf', 'weight': '400 700'}],
    'tokens': {'color.bg': '#16161a', 'color.text': '#efe9dd', 'color.text-dim': '#bdb6a8', 'color.text-strong': '#ffffff', 'color.text-soft': '#e6dfd2',
               'color.text-muted': '#c8c1b3', 'color.surface': 'rgba(36, 36, 42, .9)', 'color.border': 'rgba(255, 255, 255, .12)', 'color.brand': '#ff6a3d',
               'color.on-accent': '#16161a', 'color.knob': '#efe9dd', 'color.select-bg': '#3a2a24', 'surface.menu': '#222228', 'surface.pop': '#222228',
               'surface.tip': '#222228', 'effect.blur': '0px', 'effect.glow-size': '0px', 'effect.glow-alpha': '0%', 'accent.album-mix': '0.2', 'shape.radius': '6px'},
    'accent': {'mode': 'fixed', 'color': '#ff6a3d'},
    'parts': {'progress': {'variant': 'line'}, 'tracklist': {'variant': 'text'}},
    'supports': {'background': ['black']},
    'strings': {'tab.queue': 'Side A', 'tab.library': 'Tapes', 'nowplaying.idle': 'Insert a tape', 'empty.queue': 'Side A is blank', 'player.prev': 'REW', 'player.next': 'FF'},
    'layout': {'home': {
        'areas': ['tape card', 'info card', 'prog card', 'keys card'], 'columns': 'minmax(0, 1fr) minmax(260px, 340px)', 'rows': 'minmax(0, 1fr) auto 40px 84px',
        'place': {'tape': 'art', 'info': 'info', 'prog': 'progress', 'keys': 'player', 'card': 'sidebar'}, 'resizable': ['card']}},
}, css=r"""
[data-part="background"] { background-color: #16161a !important; background-image: none !important; opacity: 1 !important; }
""" + FLAT + FIT + r"""
.lay-art, .lay-info, .lay-progress { background-color: transparent !important; border-color: transparent !important; }
/* the cassette shell, the label (the cover), the window with two reels */
.lay-art { container-type: size; } /* on the cell: on .art-part it collapses to 0 wide (size containment) */
.lay-art .art-part::before { content: ""; position: absolute; width: min(92cqw, 150cqh); aspect-ratio: 1.6; border-radius: 14px;
  background-image: linear-gradient(#2a2a30, #1d1d22); box-shadow: inset 0 0 0 3px #3a3a42, 0 18px 40px rgb(0 0 0 / .6); }
.lay-art img { width: min(80cqw, 130cqh) !important; height: auto !important; aspect-ratio: 2.4; object-fit: cover; border-radius: 6px !important; position: relative; z-index: 1;
  -webkit-mask-image: radial-gradient(ellipse 25% 30% at 50% 52%, transparent 98%, #000 100%); mask-image: radial-gradient(ellipse 25% 30% at 50% 52%, transparent 98%, #000 100%); }
.lay-art .art-part::after { content: ""; position: absolute; z-index: 2; width: min(26cqw, 42cqh); aspect-ratio: 2.2;
  background-image: radial-gradient(circle at 28% 50%, #efe9dd 0 8%, #3a2a20 9% 26%, transparent 27%), radial-gradient(circle at 72% 50%, #efe9dd 0 8%, #3a2a20 9% 18%, transparent 19%);
  animation: reels 1.2s steps(6) infinite; }
@keyframes reels { 50% { filter: brightness(1.15); } }
""" + PAUSED + r""" .lay-art .art-part::after { animation-play-state: paused; }
/* the J-card: hand-written on lined card */
[data-part="tracklist"] { background-color: #f6efe0 !important; background-image: linear-gradient(rgb(60 90 160 / .18) 1px, transparent 1px) !important; background-size: 100% 28px !important; }
[data-part="tracklist"] * { color: #1e2a4a !important; }
[data-part="tracklist.row"] { font: 600 19px "Caveat", "Segoe Print", cursive !important; padding-top: 1px !important; padding-bottom: 1px !important; }
[data-part="tracklist.row"][data-state~="active"] { background-color: rgb(255 106 61 / .18) !important; box-shadow: none !important; }
.lay-info [data-part="info.title"] { font: 700 34px "Caveat", cursive; color: #efe9dd; }
/* piano keys */
.lay-player .btn, [data-part^="player.button"] { border-radius: 4px !important; background-image: linear-gradient(#f2f2f2, #c8c8c8) !important; color: #222 !important; border: 0 !important;
  box-shadow: inset 0 -5px 0 #8a8a8a, 0 3px 0 #111 !important; min-width: 54px !important; min-height: 44px !important; }
.lay-player .controls { gap: 8px !important; }
[data-part="player.button.play"] { background-image: linear-gradient(#ff8a63, #e0502a) !important; color: #fff !important; box-shadow: inset 0 -5px 0 #a33a1c, 0 3px 0 #111 !important; }
@media (prefers-reduced-motion: reduce) { .lay-art .art-part::after { animation: none; } }
""", files={**ofl('caveat', 'Caveat.ttf'),
            'CREDITS.md': credits(['Font: Caveat by the Caveat Project Authors (Impallari Type), SIL Open Font License 1.1 (assets/caveat/OFL.txt).', 'Everything else: made for Voltage, CC0.'])})

# ── Handheld: a 4-shade green pocket console look (original, no console branding): a dot-matrix screen, d-pad buttons ──
G = ['#0f380f', '#306230', '#8bac0f', '#9bbc0f']
write('handheld', {
    'id': 'handheld', 'name': 'Handheld', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'light',
    'description': 'A pocket console look in four greens: everything on a dot-matrix screen in a pixel font, round A / B buttons, the mini player as the whole device. No console branding.',
    'fonts': [{'family': 'Press Start 2P', 'src': 'assets/pressstart/PressStart2P-Regular.ttf'}],
    'tokens': light(G[3], G[0], '#1f4a1f', G[3], G[1], G[0], G[3], {'font.body': '"Press Start 2P", monospace', 'color.text-strong': G[0], 'color.select-bg': G[2]}),
    'accent': {'mode': 'fixed', 'color': G[0]},
    'parts': {'progress': {'variant': 'blocks'}, 'tracklist': {'variant': 'text'}, 'player': {'variant': 'text'}, 'nav': {'variant': 'text'}},
    'supports': {'background': ['black']},
    'strings': {'brand': 'POCKET', 'player.play': 'A', 'player.next': '>', 'player.prev': '<', 'nowplaying.idle': 'PRESS START', 'tab.queue': 'LIST', 'tab.library': 'SAVES',
                'tab.search': 'FIND', 'empty.queue': 'NO DATA', 'nav.settings': 'OPT', 'nav.explore': 'MAP', 'nav.stats': 'HI', 'nav.mini': 'MINI'},
    'layout': {'home': {
        'areas': ['screen screen', 'prog prog', 'pad ab'], 'columns': 'minmax(0, 1fr) minmax(0, 1fr)', 'rows': 'minmax(0, 1fr) 40px 96px',
        'place': {'screen': 'sidebar', 'prog': 'progress', 'pad': 'player', 'ab': 'info'}},
               'mini': {'areas': ['art meta', 'ctl ctl'], 'columns': '64px 1fr', 'rows': '64px auto', 'place': {'art': 'art', 'meta': 'info', 'ctl': 'player'}}},
}, css=r"""
[data-part="background"] { background-color: #c4cfa1 !important; background-image: linear-gradient(170deg, #d6dcc0, #a7b48a) !important; opacity: 1 !important; }
*, *::before, *::after { text-shadow: none !important; }
""" + FLAT + r"""
.lay-area { border-radius: 10px !important; border: 0 !important; }
/* the screen: a dark bezel around a green dot-matrix */
.lay-sidebar { background-color: #3a3a46 !important; padding: 14px 18px !important; border-radius: 12px 12px 36px 12px !important; }
.lay-sidebar > * { background-color: """ + G[3] + r"""; background-image: radial-gradient(circle, rgb(15 56 15 / .08) 1px, transparent 1.4px); background-size: 3px 3px; border-radius: 4px; }
[data-part="tracklist"] * , .lay-sidebar * { font-family: "Press Start 2P", monospace !important; font-size: 11px !important; line-height: 1.8 !important; color: """ + G[0] + r""" !important; }
[data-part="tracklist.row"][data-state~="active"] { background-color: """ + G[2] + r""" !important; box-shadow: none !important; }
[data-part="tracklist.row"][data-state~="active"] [data-part="tracklist.row.title"]::before { content: "> "; }
.lay-sidebar img { filter: grayscale(1) sepia(1) hue-rotate(40deg) saturate(2.5) contrast(1.3) brightness(.75); image-rendering: pixelated; }
.lay-progress, .lay-player, .lay-info { background-color: transparent !important; }
/* the buttons: A / B on the right, the d-pad on the left */
.lay-player .btn { border-radius: 50% !important; background-color: #8a1e4a !important; color: #ffffff !important; border: 0 !important; box-shadow: 0 4px 0 #4a0e26 !important;
  font: 12px "Press Start 2P", monospace !important; min-width: 44px !important; min-height: 44px !important; }
.lay-info { display: flex; align-items: center; justify-content: center; font-family: "Press Start 2P", monospace; }
.lay-info [data-part="info.title"] { font: 12px "Press Start 2P", monospace; color: """ + G[0] + r"""; line-height: 1.6; }
.lay-info .info-part > :not([data-part="info.title"]) { font-size: 10px; color: """ + G[1] + r"""; }
[data-part="titlebar.brand"] { font: 12px "Press Start 2P", monospace; color: #3a3a46; }
/* the mini player as the whole device */
.lay-view-mini { background-color: #c4cfa1; border-radius: 14px; }
.lay-view-mini [data-cell="art"] img { image-rendering: pixelated; filter: grayscale(1) sepia(1) hue-rotate(40deg) saturate(2.5) contrast(1.3) brightness(.75); }
""", files={**ofl('pressstart', 'PressStart2P-Regular.ttf'),
            'CREDITS.md': credits(['Font: Press Start 2P by CodeMan38, SIL Open Font License 1.1 (assets/pressstart/OFL.txt).',
                                   'Everything else: made for Voltage, CC0. An original pocket-console look: no console names, logos or button labels of any company.'])})

# ── Night City: rain over neon signage, magenta / cyan; a glitch on every track change ──
RAIN = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 300 600"><g stroke="#9fe8ff" stroke-opacity=".35" stroke-width="1.2" stroke-linecap="round">'
        + ''.join(f'<line x1="{x}" y1="{y}" x2="{x - 6}" y2="{y + 34}"/>' for x, y in
                  [(12, 20), (40, 300), (66, 120), (90, 450), (118, 60), (140, 380), (170, 210), (196, 520), (222, 90), (250, 330), (276, 170), (30, 520), (154, 10), (288, 470), (204, 260)])
        + '</g></svg>\n')
write('night-city', {
    'id': 'night-city', 'name': 'Night City', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark',
    'description': 'Rain over neon: a magenta / cyan sign with the song title, rain streaks across the window, a glitch on every track change. The list as a lit shopfront.',
    'fonts': [{'family': 'Monoton', 'src': 'assets/monoton/Monoton-Regular.ttf'}],
    'tokens': {'color.bg': '#07040f', 'color.text': '#f0e6ff', 'color.text-dim': '#b8a8d8', 'color.text-strong': '#ffffff', 'color.text-soft': '#e0d4ff',
               'color.text-muted': '#c4b6e4', 'color.surface': 'rgba(20, 8, 36, .62)', 'color.border': 'rgba(255, 60, 200, .3)', 'color.brand': '#ff3cc8',
               'color.on-accent': '#07040f', 'color.knob': '#00f0ff', 'color.select-bg': '#3a0c40', 'surface.menu': '#140824', 'surface.pop': '#140824',
               'surface.tip': '#140824', 'effect.blur': '12px', 'effect.glow-size': '18px', 'effect.glow-alpha': '55%', 'accent.album-mix': '0.15', 'shape.radius': '6px'},
    'accent': {'mode': 'fixed', 'color': '#ff3cc8'},
    'parts': {'progress': {'variant': 'line'}, 'tracklist': {'variant': 'dense'}},
    'supports': {'background': ['gradient']},
    'overlay': True,
    'strings': {'nowplaying.idle': 'The city is quiet tonight', 'tab.queue': 'Tonight'},
    'layout': {'home': {
        'areas': ['sign sign', 'art list', 'prog list', 'bar list'], 'columns': 'minmax(0, 1fr) minmax(260px, 340px)', 'rows': '120px minmax(0, 1fr) 44px 76px',
        'place': {'sign': 'info', 'art': 'art', 'list': 'sidebar', 'prog': 'progress', 'bar': 'player'}, 'resizable': ['list']}},
}, css=r"""
[data-part="background"] { background-color: #07040f !important; opacity: 1 !important;
  background-image: linear-gradient(0deg, rgb(255 60 200 / .25), transparent 30%), linear-gradient(0deg, rgb(0 240 255 / .12), transparent 55%),
    repeating-linear-gradient(90deg, transparent 0 60px, rgb(255 255 255 / .02) 60px 62px) !important; }
[data-part="overlay"] { background-image: url("assets/rain.svg"), url("assets/rain.svg"); background-size: 300px 600px, 200px 400px; animation: rain .9s linear infinite; opacity: .7; }
@keyframes rain { to { background-position: -40px 600px, -30px 400px; } }
""" + PAUSED + r""" [data-part="overlay"] { animation-duration: 6s; }
""" + FIT + r"""
.lay-info, .lay-art { background-color: transparent !important; border-color: transparent !important; box-shadow: none !important; backdrop-filter: none !important; }
/* the neon sign */
.lay-info { display: grid; place-items: center; }
.lay-info [data-part="info.title"] { font: 400 clamp(24px, 4vw, 46px) "Monoton", sans-serif; color: #ffd6f6; letter-spacing: .06em;
  text-shadow: 0 0 6px #ff3cc8, 0 0 18px #ff3cc8, 0 0 40px #ff3cc8; animation: buzz 6s steps(1) infinite; }
.lay-info .info-part > :not([data-part="info.title"]) { color: #b8fbff; text-shadow: 0 0 8px #00f0ff; }
@keyframes buzz { 0%, 100% { opacity: 1; } 91% { opacity: 1; } 92% { opacity: .35; } 93% { opacity: 1; } 95% { opacity: .6; } 96% { opacity: 1; } }
.lay-art img { width: auto !important; height: auto !important; max-width: 92% !important; max-height: 92% !important; aspect-ratio: 1; object-fit: cover;
  box-shadow: 0 0 0 2px #00f0ff, 0 0 30px rgb(0 240 255 / .45) !important; }
/* the glitch on a track change */
:root[data-event="track-change"] .lay-art img, :root[data-event="skip"] .lay-art img { animation: glitch .55s steps(2); }
:root[data-event="track-change"] .lay-info [data-part="info.title"], :root[data-event="skip"] .lay-info [data-part="info.title"] { animation: glitch .55s steps(2); }
@keyframes glitch { 0% { transform: translate(0); filter: none; } 20% { transform: translate(-6px, 2px); filter: hue-rotate(90deg) saturate(2); clip-path: inset(10% 0 55% 0); }
  40% { transform: translate(5px, -2px); clip-path: inset(50% 0 12% 0); } 60% { transform: translate(-3px, 0); filter: hue-rotate(-60deg); clip-path: none; } 100% { transform: none; filter: none; } }
[data-part="tracklist.row"][data-state~="active"] { background-color: rgb(255 60 200 / .14) !important; box-shadow: inset 0 0 0 1px #ff3cc8, 0 0 14px rgb(255 60 200 / .35) !important; }
@media (prefers-reduced-motion: reduce) { [data-part="overlay"], .lay-info [data-part="info.title"] { animation: none !important; } }
""", files={**ofl('monoton', 'Monoton-Regular.ttf'), 'assets/rain.svg': RAIN,
            'CREDITS.md': credits(['Font: Monoton by Vernon Adams, SIL Open Font License 1.1 (assets/monoton/OFL.txt).', 'Rain and everything else: made for Voltage, CC0.'])})

# ── Studio: a mixing desk. A channel-strip list, two VU meters that move with the music (helper plugin "vu-meter"), a rack player ──
write('studio', {
    'id': 'studio', 'name': 'Studio', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark',
    'description': 'A mixing desk: two VU meters whose needles move with the music (with the VU meter plugin), a rack-mounted player, the queue as a channel list.',
    'fonts': [{'family': 'IBM Plex Mono', 'src': 'assets/plexmono/IBMPlexMono-Regular.ttf'}],
    'plugin': 'vu-meter',
    'tokens': {'color.bg': '#121314', 'color.text': '#e8e8e2', 'color.text-dim': '#aaaaa2', 'color.text-strong': '#ffffff', 'color.text-soft': '#dcdcd4',
               'color.text-muted': '#b8b8b0', 'color.surface': '#1c1d1f', 'color.border': 'rgba(255, 255, 255, .1)', 'color.brand': '#ffb02e',
               'color.on-accent': '#121314', 'color.knob': '#e8e8e2', 'color.select-bg': '#3a2e18', 'surface.menu': '#1c1d1f', 'surface.pop': '#1c1d1f',
               'surface.tip': '#1c1d1f', 'effect.blur': '0px', 'effect.glow-size': '6px', 'effect.glow-alpha': '30%', 'accent.album-mix': '0', 'shape.radius': '4px',
               'font.mono': '"IBM Plex Mono", Consolas, monospace'},
    'accent': {'mode': 'fixed', 'color': '#ffb02e'},
    'parts': {'progress': {'variant': 'line'}, 'tracklist': {'variant': 'dense'}},
    'supports': {'background': ['black']},
    'strings': {'tab.queue': 'Channels', 'nowplaying.idle': 'Desk idle', 'empty.queue': 'No channels armed'},
    'layout': {'home': {
        'areas': ['strip vu', 'strip info', 'strip prog', 'strip bar'], 'columns': 'minmax(260px, 330px) minmax(0, 1fr)', 'rows': 'minmax(160px, 1fr) auto 44px 80px',
        'place': {'strip': 'sidebar', 'vu': 'art', 'info': 'info', 'prog': 'progress', 'bar': 'player'}, 'resizable': ['strip']}},
}, css=r"""
[data-part="background"] { background-color: #121314 !important; opacity: 1 !important; background-image: repeating-linear-gradient(0deg, rgb(255 255 255 / .015) 0 2px, transparent 2px 6px) !important; }
""" + FLAT + FIT + r"""
.lay-area { background-color: #1c1d1f !important; border: 1px solid #2c2d30 !important; box-shadow: inset 0 1px 0 rgb(255 255 255 / .05) !important; }
/* rack ears with screws on the player and the progress */
.lay-player, .lay-progress { border-left: 18px solid #2a2b2e !important; border-right: 18px solid #2a2b2e !important;
  background-image: radial-gradient(circle at 9px 50%, #777 0 3px, transparent 3.5px) !important; }
/* the VU meters: two cream faces with an arc scale and a needle each; the needle follows --fx-vu (0-1, from the vu-meter helper) */
.lay-art { background-color: #0d0d0e !important; container-type: size; }
.lay-art img { display: none !important; }
.lay-art .art-part { display: flex !important; flex-direction: row; justify-content: center; align-items: center; gap: 4%; }
.lay-art .art-part::before, .lay-art .art-part::after { content: ""; width: min(44cqw, 120cqh); aspect-ratio: 1.6; border-radius: 6px;
  background-color: #f1e6c8; box-shadow: inset 0 0 0 3px #3a3a3a, inset 0 0 30px rgb(160 120 40 / .35);
  background-image:
    conic-gradient(from calc(-50.65deg + var(--fx-vu, 0) * 100deg) at 50% 100%, #1a1a1a 0 1.3deg, transparent 1.3deg),
    radial-gradient(circle at 50% 100%, transparent 0 58%, #1a1a1a 58.5% 59.5%, transparent 60%),
    radial-gradient(circle at 50% 100%, transparent 0 58%, transparent 60%, rgb(200 40 30 / .7) 60% 62%, transparent 62.5%),
    linear-gradient(transparent 80%, #1a1a1a 80% 81%, transparent 81%);
  background-size: 100% 100%; background-repeat: no-repeat;
  transition: background-image .1s; }
.lay-art .art-part::after { background-image:
    conic-gradient(from calc(-50.65deg + var(--fx-vu-r, var(--fx-vu, 0)) * 100deg) at 50% 100%, #1a1a1a 0 1.3deg, transparent 1.3deg),
    radial-gradient(circle at 50% 100%, transparent 0 58%, #1a1a1a 58.5% 59.5%, transparent 60%),
    radial-gradient(circle at 50% 100%, transparent 0 58%, transparent 60%, rgb(200 40 30 / .7) 60% 62%, transparent 62.5%),
    linear-gradient(transparent 80%, #1a1a1a 80% 81%, transparent 81%); }
.lay-info [data-part="info.title"] { font: 500 22px "IBM Plex Mono", monospace; letter-spacing: .06em; text-transform: uppercase; }
.lay-info, [data-part="progress.time"], [data-part="tracklist"] { font-family: "IBM Plex Mono", Consolas, monospace; }
/* the channel strips */
[data-part="tracklist.row"] { border-left: 4px solid #2c2d30; border-radius: 0 !important; }
[data-part="tracklist.row"][data-state~="active"] { border-left-color: #ffb02e; background-color: rgb(255 176 46 / .1) !important; box-shadow: none !important; }
[data-part="player.button.play"] { background-color: #ffb02e !important; color: #121314 !important; border-radius: 4px !important; }
""", files={**ofl('plexmono', 'IBMPlexMono-Regular.ttf'),
            'CREDITS.md': credits(['Font: IBM Plex Mono by IBM, SIL Open Font License 1.1 (assets/plexmono/OFL.txt).',
                                   'Everything else: made for Voltage, CC0. The meters move with the music through the "VU meter" plugin (Settings > Plugins); without it they rest at zero.'])})

# ── Seasonal: two tiny themes, the smallest a theme can be (extends Voltage: a palette and an overlay) ──
write('season-halloween', {
    'id': 'season-halloween', 'name': 'Halloween', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark',
    'description': 'A small seasonal theme: pumpkin orange on black, a little moon and drifting fog. Voltage underneath (the example of how small a theme can be).',
    'tokens': {'color.bg': '#0b0806', 'color.brand': '#ff7a1a', 'color.border': 'rgba(255, 122, 26, .25)', 'accent.album-mix': '0.2'},
    'accent': {'mode': 'fixed', 'color': '#ff7a1a'},
    'overlay': True,
}, css=r"""
[data-part="overlay"] { background-image: radial-gradient(circle at 92% 8%, #ffe6b0 0 22px, rgb(255 200 120 / .25) 24px, transparent 60px),
  radial-gradient(60% 20% at 30% 100%, rgb(255 255 255 / .06), transparent 70%), radial-gradient(50% 18% at 75% 100%, rgb(255 255 255 / .05), transparent 70%);
  animation: fog 30s ease-in-out infinite alternate; }
@keyframes fog { to { background-position: 0 0, 60px 0, -60px 0; } }
[data-part="app"]:not([data-state~="playing"]) [data-part="overlay"] { animation-play-state: paused; }
""")
write('season-winter', {
    'id': 'season-winter', 'name': 'Winter', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark',
    'description': 'A small seasonal theme: icy blue on deep navy and slow snowfall. Voltage underneath (the example of how small a theme can be).',
    'tokens': {'color.bg': '#060b16', 'color.brand': '#9fd8ff', 'color.border': 'rgba(159, 216, 255, .25)', 'accent.album-mix': '0.25'},
    'accent': {'mode': 'fixed', 'color': '#9fd8ff'},
    'overlay': True,
}, css=r"""
[data-part="overlay"] { background-image: radial-gradient(circle, rgb(255 255 255 / .8) 0 1.5px, transparent 2px), radial-gradient(circle, rgb(255 255 255 / .5) 0 1px, transparent 1.5px);
  background-size: 120px 120px, 70px 70px; background-position: 0 0, 35px 20px; animation: snow 14s linear infinite; }
@keyframes snow { to { background-position: 30px 240px, 70px 140px; } }
[data-part="app"]:not([data-state~="playing"]) [data-part="overlay"] { animation-play-state: paused; }
@media (prefers-reduced-motion: reduce) { [data-part="overlay"] { animation: none; } }
""")
