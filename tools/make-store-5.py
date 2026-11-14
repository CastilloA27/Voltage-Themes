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

# ── Departures: F13 (the title as split-flap tiles that flip in on every new song), F1 (each upcoming song's departure time
#    as a clock time, from the "Departures board" helper, printed with CSS counters), F14 (labels in the board's words).
#    A station board: amber on black, the queue as the departures list. ──
def dep_rows():
    out = []
    for k in range(1, 9):
        sel = '.lay-sidebar [data-part="tracklist.row"][data-state~="active"]' + ' + [data-part="tracklist.row"]' * k
        out.append(f':root[style*="--fx-dep-{k}-h"] {sel}::before {{ counter-reset: h var(--fx-dep-{k}-h) m var(--fx-dep-{k}-m); content: counter(h, decimal-leading-zero) ":" counter(m, decimal-leading-zero); color: #ffc93c; }}')
    return '\n'.join(out)

write('departures', {
    'id': 'departures', 'name': 'Departures', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark', 'minVoltage': '1.7.2',
    'description': 'A station departures board: the title flips in on split-flap tiles, the queue is the list of departures with the clock time '
                   'each song leaves (with the "Departures board" plugin), the playing one is boarding, played ones have departed.',
    'fonts': [{'family': 'IBM Plex Mono', 'src': 'assets/plexmono/IBMPlexMono-Regular.ttf'}],
    'plugin': 'departures',
    'split': ['info.title'],
    'tokens': {'color.bg': '#050505', 'color.text': '#f2f2f2', 'color.text-dim': '#9a9a9a', 'color.text-strong': '#ffffff', 'color.surface': '#0c0c0c',
               'color.border': '#262626', 'color.brand': '#ffc93c', 'color.on-accent': '#111111', 'color.select-bg': '#3a2e0c',
               'surface.menu': '#121212', 'surface.pop': '#121212', 'surface.tip': '#121212', 'effect.blur': '0px', 'effect.glow-size': '0px',
               'effect.glow-alpha': '0%', 'accent.album-mix': '0', 'shape.radius': '3px', 'font.mono': '"IBM Plex Mono", Consolas, monospace'},
    'accent': {'mode': 'fixed', 'color': '#ffc93c'},
    'supports': {'background': ['black']},
    'parts': {'progress': {'variant': 'line'}, 'tracklist': {'variant': 'dense'}},
    'strings': {'tab.queue': 'Departures', 'tab.search': 'Timetable', 'nowplaying.idle': 'No departures', 'empty.queue': 'No further departures today',
                'player.next': 'Next departure', 'player.prev': 'Previous departure', 'nowplaying.cover': 'Platform {index} of {count}'},
    'layout': {'home': {
        'areas': ['info info', 'board art', 'prog prog', 'bar bar'],
        'columns': 'minmax(0, 1fr) minmax(200px, 30%)', 'rows': 'minmax(110px, auto) minmax(0, 1fr) 40px 76px',
        'place': {'info': 'info', 'board': 'sidebar', 'art': 'art', 'prog': 'progress', 'bar': 'player'}, 'resizable': ['board']}},
}, css=r"""
[data-part="background"] { background: #050505 !important; opacity: 1 !important; }
.lay-area { background-color: #0b0b0b !important; border: 1px solid #1f1f1f !important; box-shadow: none !important; }
body, .lay-area, [data-part="tracklist"] { font-family: "IBM Plex Mono", Consolas, monospace; }
/* the boarding line: "NOW BOARDING" over the title's split-flap tiles */
.lay-info { display: grid; align-content: center; justify-items: start; padding: 10px 18px !important; }
.lay-info::before { content: "NOW BOARDING"; font: 600 12px "IBM Plex Mono", monospace; letter-spacing: .3em; color: #ffc93c; margin-bottom: 6px; }
.lay-info [data-part="info.title"] { font: 500 clamp(20px, 3.4vw, 34px)/1.25 "IBM Plex Mono", monospace; text-transform: uppercase; color: #ffc93c; }
.lay-info .split .ch { display: inline-block; min-width: .78em; text-align: center; margin: 0 1px; padding: 0 .06em;
  background: linear-gradient(#1b1b1b 0 49%, #000 49% 51%, #151515 51%); border-radius: 3px; box-shadow: inset 0 0 0 1px #2a2a2a;
  transform-origin: 50% 50%; animation: flap .5s cubic-bezier(.3, 1.4, .5, 1) both; animation-delay: calc(var(--i) * 45ms); }
@keyframes flap { 0% { transform: rotateX(90deg); filter: brightness(2); } 60% { transform: rotateX(-12deg); } 100% { transform: none; filter: none; } }
.reduce-motion .lay-info .split .ch { animation: none !important; }
.lay-info .song-sub, .lay-info [data-part="info.sub"] { text-transform: uppercase; letter-spacing: .08em; color: #c9c9c9; }
/* the board: a time column before every row; boarding, departed, and the clock times from the helper */
.lay-sidebar [data-part="tracklist.row"] { border-radius: 0 !important; border-bottom: 1px solid #191919; }
.lay-sidebar [data-part="tracklist.row"]::before { content: "--:--"; order: -1; flex: 0 0 auto; width: 6.2ch; font: 500 13px "IBM Plex Mono", monospace; color: #6e6e6e; }
.lay-sidebar [data-part="tracklist.row"][data-state~="active"]::before { content: "BOARD"; color: #111; background: #ffc93c; text-align: center; border-radius: 2px; animation: board-blink 1.6s steps(1) infinite; }
@keyframes board-blink { 50% { background: #8a6d1c; } }
:root[data-reduce-flash] .lay-sidebar [data-part="tracklist.row"][data-state~="active"]::before { animation: none; }
.lay-sidebar [data-part="tracklist.row"]:has(~ [data-state~="active"])::before { content: "GONE"; color: #4a4a4a; }
.lay-sidebar [data-part="tracklist.row"]:has(~ [data-state~="active"]) { opacity: .5; }
.lay-sidebar [data-part="tracklist.row.title"] { text-transform: uppercase; letter-spacing: .02em; }
.lay-sidebar [data-part="tracklist.row"][data-state~="active"] { background: #17130a !important; box-shadow: inset 3px 0 0 #ffc93c !important; }
""" + dep_rows() + r"""
/* the cover: the platform poster */
.lay-art { display: grid; place-items: center; min-height: 0; overflow: hidden; container-type: size; }
.lay-art .art-part { display: grid; place-items: center; width: 100%; height: 100%; min-height: 0; }
.lay-art img { width: min(86cqw, 86cqh) !important; height: min(86cqw, 86cqh) !important; object-fit: cover; border-radius: 2px !important; box-shadow: 0 0 0 6px #111, 0 0 0 7px #2a2a2a !important; }
[data-part="player.button.play"] { background: #ffc93c !important; color: #111 !important; border-radius: 3px !important; }
""", files={**ofl('plexmono', 'IBMPlexMono-Regular.ttf'),
            'CREDITS.md': credits(['Font: IBM Plex Mono by IBM, SIL Open Font License 1.1 (assets/plexmono/OFL.txt).',
                                   'Everything else: made for Voltage, CC0. The departure times come from the "Departures board" plugin (Settings > Plugins); without it the board shows --:--.'])})

# ── Messenger: the song as a chat with the artist. Lyrics arrive as message bubbles as they're sung (future lines aren't
#    "sent" yet), click one to jump there (built in), F3 phases ("typing…" in the last seconds: the next song is coming),
#    F14 labels ("{artist} is typing…", "{artist} sent a voice message"). The queue is the chat list. Original look: no
#    other app's colours, logo or layout copied. ──
write('messenger', {
    'id': 'messenger', 'name': 'Messenger', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark', 'minVoltage': '1.7.2',
    'description': 'The song as a chat with the artist: lyrics arrive as message bubbles while they are sung (click one to jump there), '
                   '"typing…" before the next song, the queue as your chat list and the player as the message box.',
    'tokens': {'color.bg': '#0f1115', 'color.text': '#eef1f6', 'color.text-dim': '#9aa3b2', 'color.surface': '#171a21', 'color.border': '#252a34',
               'effect.blur': '0px', 'effect.glow-size': '0px', 'effect.glow-alpha': '0%', 'accent.album-mix': '0.6', 'shape.radius': '16px'},
    'supports': {'background': ['black']},
    'strings': {'tab.queue': 'Chats', 'tab.search': 'Find', 'tab.library': 'Saved', 'nowplaying.idle': 'No new messages',
                'lyrics.loading': '{artist} is typing…', 'lyrics.none': '{artist} sent a song without words',
                'lyrics.instrumental': '{artist} sent a voice message', 'player.next': 'Next chat', 'player.prev': 'Previous chat',
                'empty.queue': 'No chats yet'},
    'layout': {'home': {
        'areas': ['side ava head', 'side chat chat', 'side prog prog', 'side bar bar'],
        'columns': 'minmax(240px, 300px) 64px minmax(0, 1fr)', 'rows': '64px minmax(0, 1fr) 34px 74px',
        'place': {'side': 'sidebar', 'ava': 'art', 'head': 'info', 'chat': 'lyrics', 'prog': 'progress', 'bar': 'player'}, 'resizable': ['side']}},
}, css=r"""
[data-part="background"] { background: #0f1115 !important; opacity: 1 !important; }
.lay-area { background-color: #14171d !important; border-color: #20242d !important; box-shadow: none !important; }
/* the header: the artist's avatar (the cover, round), the song as the contact's name, online while playing */
.lay-art, .lay-info { border-radius: 0 !important; border-left: none !important; border-right: none !important; }
.lay-art { display: grid; place-items: center; padding: 0 !important; }
.lay-art img { width: 44px !important; height: 44px !important; min-width: 44px; flex: none; aspect-ratio: 1; border-radius: 50% !important; object-fit: cover; box-shadow: none !important; }
.lay-art .art-part { display: grid; place-items: center; position: relative; }
.lay-art .art-part::after { content: ""; position: absolute; right: calc(50% - 24px); bottom: calc(50% - 24px); width: 12px; height: 12px; border-radius: 50%;
  background: #3ddc84; box-shadow: 0 0 0 3px #14171d; }
[data-part="app"]:not([data-state~="playing"]) .lay-art .art-part::after { background: #6b7280; }
.lay-info { display: flex; flex-direction: column; justify-content: center; align-items: flex-start !important; text-align: left !important; padding: 0 12px !important; }
.lay-info .info-part { align-items: flex-start !important; text-align: left !important; padding: 0 !important; margin: 0 !important; gap: 0 !important; }
.lay-info [data-part="info.title"] { font-size: 16px !important; font-weight: 650; margin: 0 !important; }
.lay-info .song-actions, .lay-info [data-part="info.actions"] { display: none !important; }
.lay-info::after { content: "online"; font-size: 12px; color: #3ddc84; }
[data-part="app"]:not([data-state~="playing"]) .lay-info::after { content: "last seen just now"; color: var(--text-dim); }
:root[data-phase="outro"] .lay-info::after { content: "typing…"; color: var(--accent); }
/* the chat: every sung line is a bubble from the artist; lines not sung yet haven't been sent */
.lay-lyrics { background: #0f1115 !important; }
.lay-lyrics .lyrics { display: flex; flex-direction: column; align-items: flex-start; gap: 6px; padding: 18px 22px 40px !important; text-align: left !important; mask-image: none !important; -webkit-mask-image: none !important; }
.lay-lyrics [data-part="lyrics.line"] { max-width: min(78%, 560px); margin: 0 !important; padding: 8px 13px !important; border-radius: 18px 18px 18px 5px;
  background: #222733; color: #e9edf3 !important; font-size: 15px !important; line-height: 1.35; transform: none !important; filter: none !important; opacity: 1 !important; cursor: pointer; }
.lay-lyrics [data-part="lyrics.line"]:not([data-state]) { display: none; }
.lyrics:not(.synced) [data-part="lyrics.line"] { display: block !important; }
.lay-lyrics [data-part="lyrics.line"][data-state~="active"] { background: var(--accent); color: var(--on-accent) !important; animation: msg-in .28s cubic-bezier(.2, 1.4, .4, 1) both; }
@keyframes msg-in { from { transform: translateY(10px) scale(.92) !important; opacity: 0; } }
.reduce-motion .lay-lyrics [data-part="lyrics.line"] { animation: none !important; }
.lay-lyrics [data-part="lyrics.line"] .rom, .lay-lyrics [data-part="lyrics.line"] .tr { display: block; font-size: 12px; opacity: .75; margin-top: 2px; }
/* "typing…" dots at the bottom of the chat in the last seconds of the song */
:root[data-phase="outro"] .lay-lyrics .lyrics::after { content: "• • •"; padding: 6px 14px; border-radius: 18px; background: #222733; color: #9aa3b2; letter-spacing: .1em; animation: typing 1.2s ease-in-out infinite; }
@keyframes typing { 50% { opacity: .4; } }
.lay-lyrics .lyrics-src { align-self: center; font-size: 11px; opacity: .6; order: 2; }
.lay-lyrics .lyrics.center, .lay-lyrics .center.dim { align-self: flex-start; margin: 18px 22px; padding: 8px 13px; border-radius: 18px 18px 18px 5px; background: #222733; font-style: italic; }
/* the chat list: round avatars, the artist as the last message */
.lay-sidebar [data-part="tracklist.row"] img, .lay-sidebar [data-part="tracklist.row"] .art { border-radius: 50% !important; }
.lay-sidebar [data-part="tracklist.row"][data-state~="active"] { background: color-mix(in srgb, var(--accent) 16%, transparent) !important; box-shadow: none !important; }
/* the player as the message box */
.lay-player { border-radius: 0 !important; border-left: none !important; border-right: none !important; border-bottom: none !important; }
.lay-progress { border-radius: 0 !important; border-left: none !important; border-right: none !important; }
[data-part="player.button.play"] { border-radius: 50% !important; }
""", files={'CREDITS.md': credits(['Made for Voltage, CC0. An original chat look: no other app\'s colours, logo or layout.'])})

# ── Cinema: F3 phases (a title card for the first seconds, THE END in the last ones), the music video behind the screen when a
#    song has one, lyrics as subtitles, F9 (page changes fade through black with the View Transitions API). ──
write('cinema', {
    'id': 'cinema', 'name': 'Cinema', 'version': '1.0.0', 'author': 'Voltage', 'extends': 'voltage', 'appearance': 'dark', 'minVoltage': '1.7.2',
    'description': 'A cinema: the cover (or the music video) on a big screen between black bars, the lyrics as subtitles, a title card '
                   'when a song starts and THE END when it finishes; pages fade through black.',
    'fonts': [{'family': 'DM Serif Display', 'src': 'assets/dmserif/DMSerifDisplay-Regular.ttf'}],
    'transitions': 'view',
    'tokens': {'color.bg': '#000000', 'color.text': '#f3efe6', 'color.text-dim': '#a8a296', 'color.surface': 'rgba(12, 11, 10, .86)', 'color.border': '#1d1b18',
               'color.brand': '#d9b26a', 'color.on-accent': '#120f08', 'effect.blur': '0px', 'effect.glow-size': '0px', 'effect.glow-alpha': '0%',
               'accent.album-mix': '0', 'shape.radius': '2px'},
    'accent': {'mode': 'fixed', 'color': '#d9b26a'},
    'supports': {'background': ['video', 'cover', 'black']},
    'strings': {'tab.queue': 'Program', 'tab.search': 'Box office', 'nowplaying.idle': 'Intermission', 'player.next': 'Next feature',
                'player.prev': 'Previous feature', 'lyrics.none': 'No subtitles', 'lyrics.instrumental': '[ instrumental ]', 'lyrics.loading': '…'},
    'layout': {'home': {
        'areas': ['info side', 'screen side', 'subs side', 'prog prog', 'bar bar'],
        'columns': 'minmax(0, 1fr) minmax(220px, 290px)', 'rows': 'auto minmax(0, 1fr) 76px 36px 72px',
        'place': {'info': 'info', 'screen': 'art', 'subs': 'lyrics', 'side': 'sidebar', 'prog': 'progress', 'bar': 'player'}, 'resizable': ['side']}},
}, css=r"""
.lay-area { background-color: rgb(0 0 0 / .78) !important; border-color: #15130f !important; box-shadow: none !important; }
/* the room: dark, lit only a little by the screen (the cover or the music video behind, dimmed) */
.bg-cover, .bg-video { filter: blur(50px) brightness(.22) saturate(1.3) !important; }
.bg-cover-shade { background: rgb(0 0 0 / .45) !important; }
/* the marquee line over the screen; a title card for the first seconds of a song (F3 phase "intro") */
.lay-info { background: #000 !important; border: none !important; text-align: center; display: grid; justify-items: center; padding: 8px 12px !important; }
.lay-info .info-part { align-items: center !important; }
.lay-info::before { content: "NOW SHOWING"; font-size: 10px; letter-spacing: .5em; color: var(--accent); margin-bottom: 2px; }
.lay-info [data-part="info.title"] { font: 400 22px/1.2 "DM Serif Display", Georgia, serif; letter-spacing: .02em; transition: font-size .8s ease, letter-spacing .8s ease; }
:root[data-phase="intro"] .lay-info [data-part="info.title"] { font-size: clamp(28px, 4.4vw, 46px); letter-spacing: .08em; animation: card-in 1.6s ease both; }
@keyframes card-in { from { opacity: 0; letter-spacing: .3em; } }
.lay-info .song-actions, .lay-info [data-part="info.actions"] { display: none !important; }
/* the screen: black bars above and below, the cover (or the video) in the middle */
.lay-art { background: #000 !important; border: none !important; border-radius: 0 !important; display: grid; place-items: center; overflow: hidden; container-type: size; position: relative;
  box-shadow: inset 0 18px 0 #000, inset 0 -18px 0 #000 !important; }
.lay-art .art-part { display: grid; place-items: center; width: 100%; height: 100%; min-height: 0; }
.lay-art img, .lay-art video { width: min(100cqw, calc(100cqh * 16 / 9)) !important; height: min(100cqh, calc(100cqw * 9 / 16)) !important; object-fit: cover; border-radius: 0 !important; box-shadow: none !important; }
/* THE END for the last seconds (F3 phase "outro") */
.lay-art::after { content: "THE END"; position: absolute; inset: 0; display: grid; place-items: center; font: 400 clamp(26px, 5vw, 54px) "DM Serif Display", Georgia, serif;
  letter-spacing: .12em; color: #f3efe6; background: rgb(0 0 0 / .72); opacity: 0; transition: opacity 1.4s ease; pointer-events: none; }
:root[data-phase="outro"] .lay-art::after { opacity: 1; }
/* subtitles: only the line being sung, white with a black edge */
.lay-lyrics { background: #000 !important; border: none !important; border-radius: 0 !important; }
.lay-lyrics .lyrics { display: grid; place-items: center; height: 100%; padding: 0 16px !important; mask-image: none !important; -webkit-mask-image: none !important; overflow: hidden !important; }
.lay-lyrics [data-part="lyrics.line"] { display: none; }
.lay-lyrics [data-part="lyrics.line"][data-state~="active"] { display: block; margin: 0 !important; font: 500 19px/1.3 system-ui, sans-serif !important; color: #fff !important; text-align: center;
  text-shadow: 0 0 3px #000, 0 2px 2px #000; transform: none !important; filter: none !important; opacity: 1 !important; }
.lay-lyrics .lyrics:not(.synced) [data-part="lyrics.line"] { display: none !important; }
.lay-lyrics .lyrics-src, .lay-lyrics .ly-offset { display: none !important; }
.lay-lyrics .center.dim { font-style: italic; color: #8a8478; }
/* F9: page changes fade through black */
::view-transition-old(root) { animation: vt-out .25s ease both; }
::view-transition-new(root) { animation: vt-in .35s ease .2s both; }
@keyframes vt-out { to { opacity: 0; } }
@keyframes vt-in { from { opacity: 0; } }
[data-part="player.button.play"] { background: var(--accent) !important; color: #120f08 !important; }
""", files={**ofl('dmserif', 'DMSerifDisplay-Regular.ttf'),
            'CREDITS.md': credits(['Font: DM Serif Display by Colophon Foundry, SIL Open Font License 1.1 (assets/dmserif/OFL.txt).', 'Everything else: made for Voltage, CC0.'])})
