#!/usr/bin/env python3
"""
Add narrated voiceover to rendered manim scenes and stitch them together.

For each scene it:
  1. joins that scene's narration beats (from a narration module),
  2. synthesizes speech with macOS `say`,
  3. mux audio onto the scene video, padding whichever stream is shorter so the
     full narration is always heard and the video always covers it,
  4. concatenates all scenes into one final mp4.

Usage:
  build_video.py --script script --narration narration --quality 480p15 \
      --out final.mp4 --voice Samantha Scene1_TheMap Scene2_Backbone ...

If no scenes are passed, every scene in the narration module is used (in order).
"""
import argparse
import importlib
import subprocess
import sys
import os

ROOT = os.path.dirname(os.path.abspath(__file__))

# Homebrew ffmpeg 7.1.1 links libx265.215 (x265 4.1); the current keg is 4.2.
# Point dyld at the still-present 4.1 lib so ffmpeg loads. Harmless if unused.
os.environ["DYLD_FALLBACK_LIBRARY_PATH"] = ":".join(filter(None, [
    "/opt/homebrew/Cellar/x265/4.1/lib", "/opt/homebrew/lib",
    os.environ.get("DYLD_FALLBACK_LIBRARY_PATH", ""),
]))
os.environ["PATH"] = "/opt/homebrew/bin:/usr/bin:/usr/local/bin:" + os.environ.get("PATH", "")


def run(cmd, **kw):
    return subprocess.run(cmd, check=True, capture_output=True, text=True, **kw)


def probe_dur(path):
    out = run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
               "-of", "default=nk=1:nw=1", path]).stdout.strip()
    return float(out)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--script", default="script", help="manim script module name (no .py)")
    ap.add_argument("--narration", default="narration", help="narration module name")
    ap.add_argument("--quality", default="480p15", help="manim quality dir, e.g. 480p15 or 1080p60")
    ap.add_argument("--media", default="media", help="manim media dir")
    ap.add_argument("--out", default="final.mp4")
    ap.add_argument("--tts", default="piper", choices=["piper", "say"],
                    help="voiceover backend (piper = natural neural TTS)")
    ap.add_argument("--voice", default="Samantha", help="macOS `say` voice (tts=say)")
    ap.add_argument("--rate", default="172", help="say words-per-minute (tts=say)")
    ap.add_argument("--piper-voice", default="en_US-ryan-high",
                    help="piper voice name (tts=piper)")
    ap.add_argument("--piper-dir", default=os.path.join(ROOT, "piper_voices"),
                    help="dir holding downloaded piper .onnx voices")
    ap.add_argument("scenes", nargs="*")
    args = ap.parse_args()
    piper_py = os.path.join(ROOT, ".venv", "bin", "python")

    sys.path.insert(0, ROOT)
    narr = importlib.import_module(args.narration)
    scenes = args.scenes or list(narr.SCENES.keys())

    workdir = os.path.join(ROOT, "audio_build")
    os.makedirs(workdir, exist_ok=True)
    vdir = os.path.join(ROOT, args.media, "videos", args.script, args.quality)

    av_parts = []
    for sc in scenes:
        vpath = os.path.join(vdir, f"{sc}.mp4")
        if not os.path.exists(vpath):
            print(f"!! missing video {vpath}", file=sys.stderr)
            sys.exit(2)
        text = "  ".join(t for t, _ in narr.SCENES[sc])
        txt_f = os.path.join(workdir, f"{sc}.txt")
        with open(txt_f, "w") as f:
            f.write(text)
        wav = os.path.join(workdir, f"{sc}.wav")
        raw = os.path.join(workdir, f"{sc}.raw.wav")
        if args.tts == "piper":
            run([piper_py, "-m", "piper", "-m", args.piper_voice,
                 "--data-dir", args.piper_dir, "-f", raw], input=text)
        else:
            aiff = os.path.join(workdir, f"{sc}.aiff")
            run(["say", "-v", args.voice, "-r", args.rate, "-o", aiff, "-f", txt_f])
            raw = aiff
        run(["ffmpeg", "-y", "-i", raw, "-ar", "44100", "-ac", "2", wav])

        dv, da = probe_dur(vpath), probe_dur(wav)
        target = max(dv, da) + 0.4  # small tail
        out_av = os.path.join(workdir, f"{sc}_av.mp4")
        # pad video (freeze last frame) and audio (silence) to target, then mux
        run([
            "ffmpeg", "-y", "-i", vpath, "-i", wav,
            "-filter_complex",
            f"[0:v]tpad=stop_mode=clone:stop_duration={target}[v];"
            f"[1:a]apad[a]",
            "-map", "[v]", "-map", "[a]",
            "-t", f"{target}",
            "-c:v", "libx264", "-pix_fmt", "yuv420p", "-r", "30",
            "-c:a", "aac", "-b:a", "192k",
            out_av,
        ])
        av_parts.append(out_av)
        print(f"  ✓ {sc}: video {dv:.1f}s + audio {da:.1f}s -> {target:.1f}s")

    concat_f = os.path.join(workdir, "concat_av.txt")
    with open(concat_f, "w") as f:
        for p in av_parts:
            f.write(f"file '{p}'\n")
    out_path = os.path.join(ROOT, args.out)
    run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", concat_f,
         "-c:v", "libx264", "-pix_fmt", "yuv420p", "-c:a", "aac", out_path])
    print(f"\nDONE -> {out_path}  ({probe_dur(out_path):.1f}s)")


if __name__ == "__main__":
    main()
