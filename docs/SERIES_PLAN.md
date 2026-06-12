# Series Plan, *The Mathematics of Lesion Network Mapping*

A sectioned video course mirroring the depth of the LNM-critique PDFs. Each **mini-video** is 3–8 min and self-contained; **Parts** group them. Every equation is taken verbatim from `responses/lnm_critique/` and adversarially fidelity-checked before render.

**Conventions** (shared across all videos)
- Colors: variables `BLUE`, eigenvalues/constants `YELLOW`, backbone/key-term `GREEN`, results/theorems `GOLD`, villain/false-positives/what-cancels `RED`, secondary `GREY`.
- Recurring motifs: backbone direction `u₁` (always green); spectral gap `λ₂/λ₁`; the camera-vs-court split.
- Each mini-video = one manim file + one narration block + synthesized voiceover + subtitles.
- Source map: P1 = van den Heuvel et al. (critique); P2 = Zalesky & Cash; P3 = Pini/Salvalaggio/Corbetta; REBUTTAL = Siddiqi et al.

Target total runtime: **~3.5–5 hours** across ~40 mini-videos.

---

## Part 0, Overview (the whole argument in one sitting) ✅ built
**0.1 The Overview** (~7 min, 7 scenes; `script.py`). The map operator, the backbone, the critique, sensitivity/specificity, the right null & cancellation, the triviality bound, camera-vs-court. Serves as trailer + executive summary.

---

## Part 1, The Setup: What LNM Is  *(source: 00_abstract_intro, 01_the_charge_formalized)*
- **1.1 The map operator.** `mℓ = Cℓ`; what `C` (normative connectome) and `ℓ` (lesion indicator) are; `(Cℓ)_a = Σ_b C_ab ℓ_b` as "total wiring into the wound." Symmetry, normalization.
- **1.2 From voxels to a real LNM pipeline.** Seed → normative functional connectivity → per-subject map → group t-map. Where the linear-operator abstraction is exact and where it idealizes.
- **1.3 The charge, formalized.** State the critique's thesis precisely: "published LNM maps are largely reconstructions of fixed connectome geometry, not disease-specific signal." What must be true for the charge to hold; what would refute it. (Argument map: premises → conclusion.)
- **1.4 Description vs inference, the thesis of the whole series.** Camera (one-sample average map) vs court (label-contrast under a null). Preview of why they have opposite fates.

## Part 2, The Backbone (spectral core)  *(source: 02_what_is_entailed, R1)*
- **2.1 Spectral decomposition.** `C = Σⱼ λⱼ uⱼ uⱼᵀ`, `λ₁ ≥ λ₂ ≥ … ≥ 0`; eigenvectors as orthonormal "connectome patterns," eigenvalues as how much of `C` each carries.
- **2.2 The map in the spectral basis.** `mℓ = Σⱼ λⱼ (uⱼᵀℓ) uⱼ`; the backbone term `mℓ^bb = λ₁(u₁ᵀℓ)u₁`; the spectral gap.
- **2.3 Theorem R1, the alignment bound (full proof).** `tan θℓ ≤ (λ₂/λ₁)·(‖ℓ⊥‖/|u₁ᵀℓ|)`. Pre-proof strategy (work backward from the angle), the proof, post-proof moral. *long-form-math treatment.*
- **2.4 The 3-voxel worked example.** `C` given; `λ=(4.0,0.3,0.1)`, ratio 0.075; three single-voxel lesions land at 2.9°, 5.5°, 7.6° from `u₁` (computed). Convergence as geometry.
- **2.5 Why "convergence" is not validation.** The funnel: every seed points the same way, so a shared endpoint certifies the funnel, not the lesion. Sets up Part 3.

## Part 3, The Critique  *(source: P1; 05 intro framing)*
- **3.1 LNM → degree(C).** `LNM = Σ(M×C)`; as coverage `M →` uniform, output → row-sums = node degree (the hub map). Derivation.
- **3.2 sLNM → PC1(C).** Symptom-weighted variant converges to first principal component; `r(PC1, degree) = 0.82`.
- **3.3 The empirical demolition.** 102 maps / 72 studies; 78/102 carry significant degree trace (P_spin<0.05); random/shuffled lesions reproduce published networks at `r = 0.73–0.95`; basic connectome properties explain **93%** of variance (79% for sLNM).
- **3.4 The convergence trap, stated.** The average map is the hub map; nonspecific by construction. Concede the camera is broken.

## Part 4, Sensitivity & Specificity  *(source: 03_the_right_null, first half)*
- **4.1 The diagnostic vocabulary.** Confusion matrix; `Sensitivity = TP/(TP+FN)`, `Specificity = TN/(TN+FP)`; ROC intuition; what a "null" is (a question).
- **4.2 The location null `H₀^loc`.** "Is this location special vs ensemble 𝓡?" Test statistic = backbone-shape; the construction.
- **4.3 Why specificity collapses.** Under R1 every random seed is backbone-shaped, so fakes reproduce the map → false positives. The chain: R1 ⇒ T^(b) ≈ T_obs ⇒ nothing rejects. P1's own 70/78 (synthetic-lesion) and 71/78 (modular-prevalence) failures.
- **4.4 Steelman + the second reason.** The location null is the *right* tool if the claim is about location; and (REBUTTAL) random-non-overlapping ensembles are the wrong reference for overlapping non-random real lesions. Two reasons, same direction.

## Part 5, The Right Null & Backbone Cancellation  *(source: 03_the_right_null, second half; R4)*
- **5.1 The symptom-label null `H₀^sym`.** Fix lesions & connectome; shuffle labels (impaired/spared); recompute the contrast.
- **5.2 Permutation exactness (full proof).** `p = (1/|G|) Σ_π 𝟙[T(y_π) ≥ T(y_id)]`; `Pr(p ≤ α) ≤ α`. Orbit/exchangeability argument; finite-sample, distribution-free. *long-form-math.*
- **5.3 Backbone cancellation (the algebra).** `x_i = b_i + r_i`, `b_i = λ₁(u₁ᵀℓ_i)u₁` label-independent; `t_v ∝ (b̄¹−b̄⁰)u₁,v + (r̄¹−r̄⁰)`; same law under every permutation ⇒ drops out. The load-bearing step.
- **5.4 The 4-patient worked example.** Backbone 10 + residual ±2; `T_obs = 4`; all 6 relabelings; `p = 1/6`; swap 10→10,000 invariance.
- **5.5 Freedman–Lane & the size nuisance.** Why permute covariate-adjusted residuals; lesion volume as label-correlated nuisance; how cancellation survives in residual space.
- **5.6 Same data, opposite verdicts.** Run both nulls on the same 4 patients: location null finds nothing, symptom null finds `T=4`. The difference is the question. REBUTTAL: 0 false positives / 1000 at `t>10`.

## Part 6, Removing the Backbone  *(source: 04_removing_the_backbone, R5)*
- **6.1 The backbone subspace & projector.** `B = span{u₁,…,u_r}`, `Π_B = Σ_{j≤r} uⱼuⱼᵀ`.
- **6.2 Residualization.** `m̃ℓ = Π_B^⊥ mℓ = Σ_{j>r} λⱼ(uⱼᵀℓ)uⱼ` = zeroing leading spectral coefficients; the backbone fraction `ρ_B(ℓ)`.
- **6.3 Theorem R5, residualization improves SNR (proof).** Under backbone-sharing, signal lives in `δ̃`; `SNR(m̃) ≥ SNR(m)`, strict when backbone carries within-group variance. *long-form-math.*
- **6.4 Empirical agreement.** P1: 93% from connectome properties; P3: 5–7 PCs > 90% of variance, both say the backbone is what to strip.

## Part 7, Convergence Maps & the Triviality Bound  *(source: 05_the_convergence_trap)*
- **7.1 Sign-agreement maps.** `A(v) = [⋀ₖ 𝟙(sign rₖ(v)=sign r₁(v))]·sign r₁(v)`.
- **7.2 The independent baseline.** `Pr[all K agree] = 2^{1−K}` (K=2:50%, 4:12.5%, 8:0.8%). Why agreement *looks* impressive.
- **7.3 Shared-backbone inflation.** `rₖ = μ + εₖ`; `Pr[all K agree] = pᴷ + (1−p)ᴷ → 1` as `p→1`, independent of K.
- **7.4 P1's own curve.** Between-lesion Dice → fraction "significant": 0.08→10%, 0.16→64%, 0.25→97%. Agreement is the default under backbone-sharing.

## Part 8, Single-Target (FUS-VIM)  *(source: 06_single_target)*
- **8.1 The variance decomposition.** `ℓ_i = ℓ₀ + δ_i`; `m_i = Cℓ₀ + Cδ_i`; `Var_i(m_i) = Var_i(Cδ_i)`. The "scattered locations" mechanism vanishes.
- **8.2 Move 1, outcome-label permutation, size-protected.** Freedman–Lane holds `Cℓ₀` and the size effect fixed; tests the outcome–map link only.
- **8.3 Move 2, strip the backbone.** `m̃_i = m_i − Π_B m_i`; VIM fingerprint concentrates in the backbone subspace.
- **8.4 Move 3, beat a degree baseline.** `ŷ_i^deg = a + b(u₁ᵀℓ_i) + c s_i`; out-of-sample prediction must beat it.

## Part 9, Biological Limits  *(source: 07_biological_limits, P3)*
- **9.1 First-order disconnection only.** A static linear `C` models only direct disconnection; no dynamics, no higher-order interactions.
- **9.2 The prediction ceiling.** Anatomical refinement didn't help; stroke `R² = 0.01–0.18` (n=132). What that bounds.
- **9.3 A different critique than P1.** P3 is about model class, not the group-average prior, orthogonal limitation. How it composes with R1–R5.

## Part 10, The Recipe & Synthesis  *(source: 08_recipe, 09_references_caveats)*
- **10.1 The full recommended pipeline.** Contrast under `H₀^sym` + Freedman–Lane + backbone residualization + degree-baseline comparison + FWE max-statistic. One diagram.
- **10.2 Camera vs court, settled.** The synthesis: same `C`, two operations, opposite verdicts; "a failed null is a failed question."
- **10.3 The rebuttal data.** Same-symptom `r=0.44` vs different-symptom `r=0.09` vs degree `r=0.16`; Petersen 2,950-patient label-permutation recovers distinct networks.
- **10.4 Honesty caveats.** What is verified vs `[verify against primary source]`; Freedman–Lane-vs-raw-shuffle open question; unpublished FUS-VIM numbers flagged.

---

## Build order & method
1. **Validate pipeline on Part 0** (render + voiceover + stitch), in progress.
2. For each subsequent mini-video, an **adversarial agent team**:
   - *Author*, writes `narration.py` + `script.py` for the mini-video, equations quoted from source.
   - *Math-fidelity adversary*, checks every symbol against the source `.md`; flags any drift, fabricated number, or sign error. Must pass before render.
   - *Manim-render adversary*, checks the code against known-good API patterns (from the validated Part 0) for render errors; predicts failures.
   - Render → voiceover → stitch → spot-check.
3. Produce per-mini-video mp4s + per-Part concatenations + a master playlist.

## Open scope decisions (confirm before mass execution)
- Final resolution: 480p15 (fast, ~seconds/scene) vs 1080p60 (publication, minutes/scene).
- Voice: macOS `Samantha` (only clear voice installed) vs install enhanced/Premium voices.
- Depth ceiling: stop at Part 10 (~40 videos) or also fold in companion Volumes 1–6 (e-values, conformal, the Three Maps).
