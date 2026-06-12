"""
Shared engine for the LNM video series.

Every chapter's script.py imports from here so all mini-videos share one
validated foundation: the color palette and the NarratedScene base class that
ties each visual "beat" to one narration line (for subtitle + voiceover sync).

CONTRACT (enforced):
  The number of play_beat()/wait_beat() calls in a scene's construct() MUST
  equal len(SCENES[scene_key]). Over-consumption raises immediately;
  under-consumption prints a loud warning at tear-down. Either way the audio
  would desync, so keep them equal.
"""

from manim import *

# ---- palette (math-visualizer standard + project additions) ----
VAR  = "#58C4DD"   # variables: lesion, map, x
EIG  = "#FFFF00"   # eigenvalues / constants: lambda
BACK = "#83C167"   # backbone / key term: u_1
RES  = "#FFD700"   # results / theorems
BAD  = "#FC6255"   # the villain: false positives, what cancels
DIM  = "#9AA0A6"   # secondary text
BG   = "#101018"

config.background_color = BG


class NarratedScene(Scene):
    """Base class: pulls timed narration beats and keeps visuals in sync.

    Subclass and set `scene_key` to a key in the chapter's narration SCENES dict,
    then pass that dict via the class attribute `narration` (a dict) OR override
    `_load_beats`.
    """
    scene_key = ""
    narration = None  # dict {scene_key: [(text, seconds), ...]}, set per chapter

    def setup(self):
        super().setup()
        self.camera.background_color = BG
        if self.narration is None:
            raise RuntimeError(f"{type(self).__name__}: set class attr `narration`")
        self._beats = list(self.narration[self.scene_key])
        self._bi = 0

    def _next(self):
        if self._bi >= len(self._beats):
            raise IndexError(
                f"{self.scene_key}: visual consumed beat #{self._bi + 1} but only "
                f"{len(self._beats)} narration beats are defined. The number of "
                f"play_beat()/wait_beat() calls MUST equal len(narration[scene_key]) "
                f"so the voiceover stays in sync.")
        text, dur = self._beats[self._bi]
        self._bi += 1
        self.add_subcaption(text, duration=dur)
        return dur

    def play_beat(self, *anims, run_time=None, lag_ratio=0.0):
        """Register the next narration beat and play anims within its duration."""
        dur = self._next()
        if anims:
            rt = run_time if run_time is not None else min(dur, max(0.6, dur * 0.55))
            self.play(AnimationGroup(*anims, lag_ratio=lag_ratio), run_time=rt)
            rem = dur - rt
            if rem > 0.05:
                self.wait(rem)
        else:
            self.wait(dur)

    def wait_beat(self):
        self.wait(self._next())

    def header(self, label):
        t = Text(label, font_size=26, color=DIM).to_edge(UP, buff=0.3)
        self.add(t)
        return t

    def tear_down(self, *args, **kwargs):
        if self._bi != len(self._beats):
            import sys
            print(f"\n[narration-sync WARNING] {self.scene_key}: used "
                  f"{self._bi}/{len(self._beats)} beats.\n", file=sys.stderr)
        return super().tear_down(*args, **kwargs)
