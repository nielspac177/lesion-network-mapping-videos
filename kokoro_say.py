#!/usr/bin/env python3
"""Synthesize speech with Kokoro (neural TTS). Reads text on stdin, writes a wav.

Run with the project venv python (it has kokoro_onnx + soundfile):
    echo "hello" | .venv/bin/python kokoro_say.py --voice am_michael --out out.wav
"""
import argparse
import os
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
os.environ.setdefault(
    "PHONEMIZER_ESPEAK_LIBRARY",
    "/opt/homebrew/opt/espeak-ng/lib/libespeak-ng.dylib",
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--voice", default="am_michael")
    ap.add_argument("--out", required=True)
    ap.add_argument("--speed", type=float, default=1.0)
    ap.add_argument("--model", default=os.path.join(ROOT, "kokoro_models", "kokoro-v1.0.onnx"))
    ap.add_argument("--voices", default=os.path.join(ROOT, "kokoro_models", "voices-v1.0.bin"))
    args = ap.parse_args()

    import soundfile as sf
    from kokoro_onnx import Kokoro

    text = sys.stdin.read().strip()
    k = Kokoro(args.model, args.voices)
    samples, sr = k.create(text, voice=args.voice, speed=args.speed, lang="en-us")
    sf.write(args.out, samples, sr)


if __name__ == "__main__":
    main()
