# The math of lesion network mapping, as a video course

This is a set of narrated math animations about lesion network mapping (LNM): the
2025-26 critique by van den Heuvel and colleagues, the replies from Siddiqi and
Petersen, and the linear algebra and statistics that actually settle the argument.
I built it with [Manim](https://www.manim.community/) for the visuals and
[Piper](https://github.com/rhasspy/piper) for a local text-to-speech narration.

The point I keep coming back to: there is one matrix, the normative connectome `C`,
and two very different things you can do with it. If you average lesion maps across
patients, you mostly get back the connectome's hub structure, and the critique is
right that this average looks the same no matter where the lesions are. But the
symptom contrast is a different calculation, and the hub part drops out of it
algebraically, so a real lesion-symptom relationship can still show up. A null model
that finds nothing is often just the wrong question, not proof that the method fails.

Every equation in the videos gets taken apart symbol by symbol. The numbers come
from the written source analysis, not from anywhere I made up.

## What's in here

| Path | What it is |
|------|-----------|
| `videos/` | The finished mp4s (stored with Git LFS). `part0_overview.mp4` is the ~6.5 minute summary; `_ryan.mp4` is the same thing in a male voice. |
| `overview/` | Part 0, the whole argument across 7 scenes. `scenes.py` plus `narration.py`. |
| `chapters/` | The longer series, one folder per short video. |
| `lnm_engine.py` | The base class every scene uses. It pins each visual step to one line of narration. |
| `build_video.py` | Runs the text-to-speech, lays audio over each scene, and joins them. |
| `render.sh` | Sets up the render environment (PATH, a native-disk media folder, an ffmpeg fix). |
| `docs/SERIES_PLAN.md` | The plan for every video and what it covers. |
| `AUTHORING.md` | How to write a chapter, and the rules an automated author has to follow. |
| `docs/adr/` | Short notes on why the toolchain ended up the way it did. |
| `tests/test_sync.py` | Checks that the narration lines and the visual steps line up, without rendering anything. |

## Running it

On macOS with Apple Silicon, you need Homebrew, [uv](https://docs.astral.sh/uv/),
and a TeX install (TinyTeX or MacTeX). Then:

```bash
make setup     # installs the toolchain; see scripts/bootstrap.sh for the steps
make test      # the narration/visual sync check
make part0     # renders and narrates the overview into videos/part0_overview.mp4
```

You can change the quality and the voice:

```bash
make part0 QUAL=qh VOICE=en_US-ryan-high     # 1080p, male narrator
```

## How a video gets built

`narration.py` holds the spoken lines. `scenes.py` holds the Manim code, and it
imports the base class from `lnm_engine.py`. Manim renders each scene and turns the
LaTeX into SVG through dvisvgm. Separately, the neural voice (Kokoro by default,
Piper as a fallback) reads each scene's narration into a wav file. Then
`build_video.py` puts the audio over the video, pads whichever one is shorter so the
full narration always plays, and concatenates the scenes.

The sync matters more than it sounds. Each `play_beat()` call shows one line of
narration as a subtitle and holds the screen for as long as that line takes to say.
The rule is that the number of beats has to equal the number of narration lines. I
enforce it in code and check it in `tests/test_sync.py`, because getting it wrong
silently pushes the voice out of sync with the picture.

## The parts of the setup that fought back

These took real time to figure out. They live in `scripts/bootstrap.sh` and the ADRs
so nobody has to rediscover them.

Building pycairo needs `pkg-config` plus Homebrew's `cairo` and `pango`, with
`PKG_CONFIG_PATH` pointing at them. MathTex needs both `dvisvgm` and `babel-english`,
and they have to be installed through `tlmgr` so they line up with TinyTeX's path
config. Homebrew's own `dvisvgm` can't find the TeX files and fails, so keep
`/usr/local/bin` ahead of Homebrew on your PATH.

Render to a folder on your internal disk (`$HOME/lnm_media`). On an external or
non-APFS volume, macOS scatters `._` sidecar files around, and Manim's LaTeX cleanup
trips over them and crashes before you see the real error.

One more: Homebrew's ffmpeg 7.1.1 is linked against `libx265.215` from x265 4.1, and
if your x265 is 4.2 the loader can't find it. `render.sh` and `build_video.py` point
`DYLD_FALLBACK_LIBRARY_PATH` at the 4.1 library that's still on disk. A
`brew reinstall ffmpeg` also fixes it.

## Voices

The series narrator is Kokoro's `am_michael`, a local neural voice that sounds
clearly more human than the older Piper voices. You'll hear it in
`videos/part0_overview.mp4`. Other male Kokoro voices worth trying are `am_fenrir`
and `am_puck` (`--kokoro-voice`). Piper (`en_US-ryan-high`, `en_US-lessac-high`) is
still supported with `--tts piper`. Everything runs locally, so there's no API key
and nothing leaves the machine.

## How the chapters are written

Two rules drive every chapter. First, explain every symbol before moving on: what `C`
is, what the lesion vector `ℓ` is, what `(Cℓ)_a` picks out, what the sum runs over.
If you can't decode the formula from the video alone, the video isn't done. Second,
treat the critique and the replies as a live argument. The critique holds for the
group-average map under uniform, non-overlapping sampling, and that's a narrow claim.
Real lesions overlap and aren't placed at random, so they touch only certain rows of
`C`, and the contrast keeps signal the average throws away. The numbers that back
this up (same-symptom maps correlating at 0.44 against 0.09 for different symptoms and
0.16 for the degree map, zero false positives in a thousand runs at t over 10) are in
`AUTHORING.md`.

## Sources

The math and figures come from a written analysis of the critique and the replies
(van den Heuvel et al.; Zalesky and Cash; Pini, Salvalaggio and Corbetta; Siddiqi et
al.; Petersen et al.). Where the source marks a claim as not yet checked against the
primary paper, the video keeps that caveat.

## License

MIT, in `LICENSE`. The Piper voice models have their own licenses; see the Piper
voices repository.
