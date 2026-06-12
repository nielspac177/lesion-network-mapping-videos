"""
Narration-sync invariants for the whole series — no manim/render required.

For every chapter (overview/ and chapters/*/), for every NarratedScene subclass,
the number of play_beat()/wait_beat() calls in the class MUST equal the number of
narration beats for that scene_key. This is the #1 source of audio desync, so we
assert it statically (AST) plus validate narration structure.

Run:  python3 -m pytest -q tests   (or)   python3 tests/test_sync.py
"""
import ast
import importlib.util
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _load_scenes_dict(narration_path):
    spec = importlib.util.spec_from_file_location("chap_narr", narration_path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.SCENES


def _find_chapters():
    """Yield (scenes_py, narration_py) pairs."""
    for d in [os.path.join(ROOT, "overview")] + [
        os.path.join(ROOT, "chapters", c) for c in
        sorted(os.listdir(os.path.join(ROOT, "chapters")))
        if os.path.isdir(os.path.join(ROOT, "chapters", c))
    ] if os.path.isdir(os.path.join(ROOT, "chapters")) else [os.path.join(ROOT, "overview")]:
        s = os.path.join(d, "scenes.py")
        n = os.path.join(d, "narration.py")
        if os.path.exists(s) and os.path.exists(n):
            yield s, n


def _count_beats_per_class(scenes_py):
    """AST: {scene_key: number_of_play_beat/wait_beat_calls} for each subclass."""
    tree = ast.parse(open(scenes_py).read())
    out = {}
    for node in tree.body:
        if not isinstance(node, ast.ClassDef):
            continue
        scene_key = None
        for stmt in node.body:
            if (isinstance(stmt, ast.Assign) and len(stmt.targets) == 1
                    and isinstance(stmt.targets[0], ast.Name)
                    and stmt.targets[0].id == "scene_key"
                    and isinstance(stmt.value, ast.Constant)):
                scene_key = stmt.value.value
        if scene_key is None:
            continue
        count = 0
        for sub in ast.walk(node):
            if (isinstance(sub, ast.Call) and isinstance(sub.func, ast.Attribute)
                    and sub.func.attr in ("play_beat", "wait_beat")):
                count += 1
        out[scene_key] = count
    return out


def _check_chapter(scenes_py, narration_py):
    scenes_dict = _load_scenes_dict(narration_py)
    counts = _count_beats_per_class(scenes_py)
    problems = []
    # structure of narration
    for key, beats in scenes_dict.items():
        for i, beat in enumerate(beats):
            assert isinstance(beat, tuple) and len(beat) == 2, f"{key}[{i}] not (text, sec)"
            text, sec = beat
            assert isinstance(text, str) and text.strip(), f"{key}[{i}] empty text"
            assert isinstance(sec, (int, float)) and sec > 0, f"{key}[{i}] bad seconds"
    # beat counts match
    for key, n_calls in counts.items():
        assert key in scenes_dict, f"{scenes_py}: scene_key '{key}' missing in narration"
        n_beats = len(scenes_dict[key])
        if n_calls != n_beats:
            problems.append(f"{key}: {n_calls} play/wait_beat calls vs {n_beats} narration beats")
    assert not problems, f"{scenes_py} sync mismatch:\n  " + "\n  ".join(problems)
    return counts


def test_all_chapters_in_sync():
    any_checked = False
    for scenes_py, narration_py in _find_chapters():
        any_checked = True
        _check_chapter(scenes_py, narration_py)
    assert any_checked, "no chapters found"


if __name__ == "__main__":
    ok = True
    for s, n in _find_chapters():
        try:
            counts = _check_chapter(s, n)
            print(f"OK  {os.path.relpath(s, ROOT)}  ({sum(counts.values())} beats across "
                  f"{len(counts)} scenes)")
        except AssertionError as e:
            ok = False
            print(f"FAIL {os.path.relpath(s, ROOT)}\n  {e}")
    sys.exit(0 if ok else 1)
