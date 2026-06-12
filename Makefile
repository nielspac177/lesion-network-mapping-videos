# Reproducible build for the LNM math-video series.
# Renders go to a native-filesystem media dir (avoids macOS AppleDouble TeX bugs).

MEDIA ?= $(HOME)/lnm_media
QUAL  ?= qm
QDIR  ?= 720p30
TTS   ?= kokoro
VOICE ?= am_michael          # kokoro voice; for piper use e.g. en_US-ryan-high
PY    := ./.venv/bin/python

OVERVIEW_SCENES := Scene1_TheMap Scene2_Backbone Scene3_Critique \
                   Scene4_Specificity Scene5_Cancellation \
                   Scene6_ConvergenceMaps Scene7_Resolution

.PHONY: help setup voices part0 part0-render part0-voice clean test

help:
	@echo "make setup     - install full toolchain (scripts/bootstrap.sh)"
	@echo "make voices    - download Piper neural voices"
	@echo "make part0     - render + voice the overview -> videos/part0_overview.mp4"
	@echo "make test      - narration-sync + sanity checks"
	@echo "Vars: QUAL=ql|qm|qh  VOICE=en_US-lessac-high|en_US-ryan-high"

setup:
	bash scripts/bootstrap.sh

voices:
	mkdir -p kokoro_models
	curl -sL -o kokoro_models/kokoro-v1.0.onnx https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/kokoro-v1.0.onnx
	curl -sL -o kokoro_models/voices-v1.0.bin   https://github.com/thewh1teagle/kokoro-onnx/releases/download/model-files-v1.0/voices-v1.0.bin
	$(PY) -m piper.download_voices en_US-ryan-high en_US-lessac-high --download-dir piper_voices

part0: part0-render part0-voice

part0-render:
	./render.sh overview/scenes.py -q $(QUAL) $(OVERVIEW_SCENES)

part0-voice:
	python3 build_video.py --media $(MEDIA) --quality $(QDIR) --script scenes \
	  --narration overview.narration --tts $(TTS) --kokoro-voice $(VOICE) \
	  --out videos/part0_overview.mp4

test:
	python3 -m pytest -q tests || python3 tests/test_sync.py

clean:
	rm -rf audio_build $(MEDIA)/videos/scenes __pycache__ */__pycache__
