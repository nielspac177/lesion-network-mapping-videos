export const meta = {
  name: 'author-lnm-chapters',
  description: 'Author + adversarially fidelity-check a batch of LNM math-video chapters',
  phases: [
    { title: 'Author', detail: 'write narration.py + scenes.py per chapter' },
    { title: 'Verify', detail: 'math-fidelity + manim-API adversary fixes each chapter in place' },
  ],
}

// args = { repo: "/abs/path", chapters: [ {id, title, sources:[...], scenes:[{key,title,brief}]} ] }
const A = typeof args === 'string' ? JSON.parse(args) : args
const REPO = A.repo
const CHAPTERS = A.chapters

const RECORD = {
  type: 'object',
  properties: {
    id: { type: 'string' },
    wrote_narration: { type: 'boolean' },
    wrote_scenes: { type: 'boolean' },
    scene_keys: { type: 'array', items: { type: 'string' } },
    beats_per_scene: { type: 'array', items: { type: 'integer' } },
    notes: { type: 'string' },
  },
  required: ['id', 'wrote_narration', 'wrote_scenes', 'scene_keys', 'beats_per_scene', 'notes'],
}

const VERDICT = {
  type: 'object',
  properties: {
    id: { type: 'string' },
    beat_counts_match: { type: 'boolean' },
    fabricated_numbers_found: { type: 'array', items: { type: 'string' } },
    symbol_gaps_found: { type: 'array', items: { type: 'string' } },
    manim_risks_found: { type: 'array', items: { type: 'string' } },
    fixes_applied: { type: 'array', items: { type: 'string' } },
    final_status: { type: 'string', enum: ['clean', 'fixed', 'needs_human'] },
  },
  required: ['id', 'beat_counts_match', 'fabricated_numbers_found', 'symbol_gaps_found',
             'manim_risks_found', 'fixes_applied', 'final_status'],
}

const CONTRACT = `
You are authoring ONE chapter of a narrated Manim math-video course on the
mathematics of Lesion Network Mapping (LNM). Working directory is the repo root:
${REPO}

BEFORE writing anything, READ these files in full to internalise the standard:
  - AUTHORING.md                         (the non-negotiable contract)
  - lnm_engine.py                        (the NarratedScene base class + palette)
  - chapters/c0103_charge_formalized/scenes.py     (GOLD-STANDARD exemplar scenes)
  - chapters/c0103_charge_formalized/narration.py  (GOLD-STANDARD exemplar narration)
Then READ the source .md file(s) listed for THIS chapter and pull every equation,
number, and claim from them. Do not invent constants. Keep any "[verify against
primary source]" caveat the source carries.

HARD RULES (from AUTHORING.md):
1. Explain EVERY symbol on screen with Brace/labels before moving on. Never show a
   formula the viewer cannot fully decode from the video alone.
2. Do NOT pre-concede the critique. It is correct ONLY about the GROUP-AVERAGE map
   under UNIFORM, NON-OVERLAPPING sampling. Give the rebuttal full standing: real
   symptom lesions OVERLAP and are NON-RANDOM, sampling specific rows of C; the
   CONTRAST (not the average) carries signal. Numbers: same-symptom r=0.44 vs
   different-symptom r=0.09 vs degree r=0.16; 0 false positives / 1000 at t>10.
3. THE BEAT-COUNT CONTRACT: in each scene's construct(), the number of
   play_beat()+wait_beat() calls MUST EQUAL len(SCENES[scene_key]). Count them.
   Over-consumption raises IndexError at render; under-consumption warns. This is
   the #1 bug. Put a "# beat N" comment on each play_beat/wait_beat line.
4. Long-form proofs: pre-proof strategy -> proof with words between every step ->
   post-proof moral. Type every variable.

MANIM PITFALLS (already hit & fixed — obey):
  - MathTex("a","=","b")[i] indexes ARGUMENTS; an argument rendering to zero glyphs
    (a lone r"\\,") is dropped and shifts indices. Keep each indexed arg non-empty.
  - Helper methods that build mobjects must return a VGroup (not a list) if the
    caller does .shift(...). Iterate grp.submobjects.
  - No \\emph or exotic packages. Only amsmath/amssymb: \\text \\top \\perp
    \\underbrace \\frac \\sum \\mathrm \\mathbb \\langle \\rangle \\geq \\leq.
  - Keep <= ~6 dense mobjects on screen; FadeOut a group before the next block.
  - Colours from lnm_engine: VAR EIG BACK RES BAD DIM BG. import them.

NARRATION STYLE (narration.py):
  SCENES = { "S1_Key": [ ("spoken line decoding the math", 7.0), ... ], ... }
  6-9 beats per scene, each 5-11 s, ~2.5 words/sec, conversational, decodes symbols.
  Write numbers as words for TTS ("zero point four four", "lambda one", "u sub one").
  Add an  if __name__ == "__main__":  block printing per-scene beat counts.

scenes.py MUST start with:
  from manim import *
  from lnm_engine import NarratedScene, VAR, EIG, BACK, RES, BAD, DIM, BG
  from narration import SCENES
  NarratedScene.narration = SCENES
and define one class per scene with  scene_key = "<key>"  matching SCENES.
`

phase('Author')
const authored = await pipeline(
  CHAPTERS,
  (ch) => {
    const scenes = ch.scenes.map((s, i) =>
      `  Scene ${i + 1}  key="${s.key}"  on-screen title: "${s.title}"\n     content: ${s.brief}`
    ).join('\n')
    const prompt = `${CONTRACT}

================  THIS CHAPTER  ================
id: ${ch.id}
title: ${ch.title}
source file(s) to read and quote from (relative to repo root):
${ch.sources.map(s => '  - ' + s).join('\n')}

Write EXACTLY these ${ch.scenes.length} scenes, in order. Each scene 6-9 beats:
${scenes}

DELIVERABLES — write both files to disk with the Write tool:
  chapters/${ch.id}/narration.py
  chapters/${ch.id}/scenes.py
Make absolutely sure: for every scene, the count of play_beat()+wait_beat() calls
in scenes.py equals the number of entries in SCENES["<key>"] in narration.py.
After writing, re-open both files and re-count beats vs narration entries; fix any
mismatch before you finish. Return the structured record.`
    return agent(prompt, { label: `author:${ch.id}`, phase: 'Author', schema: RECORD })
  },
  // Verify/fix stage runs per-chapter as soon as its author finishes
  (rec, ch) => {
    if (!rec) return null
    const prompt = `${CONTRACT}

================  ADVERSARIAL REVIEW of chapter ${ch.id}  ================
The author just wrote chapters/${ch.id}/narration.py and chapters/${ch.id}/scenes.py.
READ both files AND the source(s):
${ch.sources.map(s => '  - ' + s).join('\n')}

Your job, as a hostile reviewer, is to BREAK then FIX this chapter:
1. BEAT COUNT: for each scene, count play_beat()+wait_beat() calls in scenes.py and
   compare to len(SCENES[key]) in narration.py. They MUST be equal. If not, fix the
   scene (add/remove a beat or merge anims into one play_beat) so they match. This is
   the most important check — a mismatch crashes the render or desyncs audio.
2. FABRICATED NUMBERS: every numeric constant on screen or in narration must appear
   in the source .md. Flag any that do not; replace with the correct source value or
   remove. Keep "[verify against primary source]" caveats.
3. SYMBOL GAPS: every symbol in every equation must be explained on screen (Brace/
   label) and in narration. Add the missing annotation+beat if absent (and update the
   matching narration entry so counts still match).
4. MANIM RISKS: scan for the known pitfalls (MathTex index drift from empty args,
   helpers returning lists not VGroups, \\emph/exotic LaTeX, >6 dense mobjects).
   Fix them in place.
5. FRAMING: ensure the critique is NOT pre-conceded — scope it to the group-average
   under uniform non-overlapping sampling, and give the contrast/rebuttal standing.
Apply all fixes by editing the files directly. Return the structured verdict.`
    return agent(prompt, { label: `verify:${ch.id}`, phase: 'Verify', schema: VERDICT, agentType: 'general-purpose' })
  }
)

const verdicts = authored.filter(Boolean)
log(`authored+verified ${verdicts.length}/${CHAPTERS.length} chapters`)
return { verdicts }
