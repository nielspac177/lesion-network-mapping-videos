# The Mathematics of Lesion Network Mapping, Critique, Specificity, and Convergence

## Overview
- **Topic**: The math behind Lesion Network Mapping (LNM), the 2025–26 critique (van den Heuvel et al.), and the rebuttal, told through sensitivity, specificity, and convergence.
- **Hook**: How can lesions in completely *different* places all implicate the *same* brain network, and does that convergence mean the method works, or that it's measuring nothing?
- **Target audience**: Quantitatively literate viewers (linear algebra, basic stats). No neuro background assumed.
- **Estimated length**: ~8–9 minutes, 7 scenes.
- **Key insight**: One matrix $C$, two operations. The *average* map (description) converges to the connectome backbone and is nonspecific, the critique is right. The *contrast* under a symptom-label null (inference) algebraically cancels that backbone, so signal survives. A failed null is a failed *question*, not a failed method.
- **Resolution**: 480p15 for iteration, 1080p60 for final.
- **Aspect Ratio**: 16:9.

## Narrative Arc
We build the LNM map operator $m_\ell = C\ell$, expose the spectral "backbone" that makes every lesion's map point the same way (convergence), then watch the critique weaponize that convergence to show the average map is just the hub/degree map. We reframe with sensitivity & specificity: the location null has catastrophic specificity (random lesions = false positives), while the symptom-label null is exactly valid and the backbone *cancels*. We quantify the convergence "triviality bound," and close on description-vs-inference with residualization.

---

## Scene 1: TheMap, What LNM actually computes
**Duration**: ~70s
**Purpose**: Define the map operator and seed the central mystery.
### Content
- Brain → graph of $V$ voxels; normative connectome $C \in \mathbb{R}^{V\times V}$ (symmetric, normalized).
- Lesion indicator $\ell \in \{0,1\}^V$.
- The map: $m_\ell = C\ell$, with $(C\ell)_a = \sum_b C_{ab}\ell_b$ = total connectivity of voxel $a$ to the lesion.
- Mystery: different $\ell$'s seem to give similar $m_\ell$. Why?
### Voiceover
- "Lesion network mapping starts with one linear operation..." (see narration.py)

## Scene 2: Backbone, Spectral decomposition & convergence
**Duration**: ~85s
**Purpose**: Show WHY maps converge, the spectral funnel.
### Content
- $C = \sum_j \lambda_j u_j u_j^\top$, $\lambda_1 \ge \lambda_2 \ge \dots \ge 0$.
- $m_\ell = \sum_j \lambda_j (u_j^\top \ell) u_j$; backbone term $m_\ell^{bb} = \lambda_1 (u_1^\top\ell)u_1$.
- **Theorem R1 (alignment bound)**: $\tan\theta_\ell \le \frac{\lambda_2}{\lambda_1}\cdot\frac{\|\ell_\perp\|}{|u_1^\top\ell|}$.
- 3-voxel example: $\lambda=(4.0,0.3,0.1)$, ratio $0.075$; three different lesions land within ~$7^\circ$ of $u_1$.
### Visual
- Vectors fanning in, funneled toward fixed direction $u_1$.

## Scene 3: Critique, The convergence trap
**Duration**: ~80s
**Purpose**: The critique's mathematical core.
### Content
- $\text{LNM} = \sum(M\times C)$; as coverage $M \to$ uniform, output $\to \deg(C)$ (row sums).
- Symptom-weighted $\text{sLNM} \to \text{PC1}(C)$, overlaps degree at $r=0.82$.
- Empirics: 78/102 maps carry significant degree trace; random/shuffled lesions reproduce published networks at $r=0.73$–$0.95$; basic connectome properties explain **93%** of map variance.
- The trap: the *average* map is the hub map, nonspecific by construction.

## Scene 4: Specificity, Sensitivity, specificity & the wrong null
**Duration**: ~85s
**Purpose**: Frame the problem as a specificity failure of the *location* null.
### Content
- Confusion matrix; $\text{Sensitivity}=\frac{TP}{TP+FN}$, $\text{Specificity}=\frac{TN}{TN+FP}$.
- Location null $H_0^{loc}$: "is this location special?" Under R1, random lesions reproduce the map → false positives pile up → specificity collapses. 70/78 maps fail.
- Punchline: failing this null isn't "LNM is fake"; the null asked the wrong question.

## Scene 5: Cancellation, The right null & backbone cancellation
**Duration**: ~95s
**Purpose**: The rebuttal's load-bearing algebra.
### Content
- Symptom-label null $H_0^{sym}$: labels exchangeable given fixed maps.
- Permutation exactness: $p=\frac{1}{|G|}\sum_\pi \mathbf{1}[T(y_\pi)\ge T(y_{id})]$, $\Pr(p\le\alpha)\le\alpha$.
- Decompose $x_i = b_i + r_i$ ($b_i=\lambda_1(u_1^\top\ell_i)u_1$, label-free).
- Contrast: $t_v \propto (\bar b^{(1)}-\bar b^{(0)})u_{1,v} + (\bar r^{(1)}-\bar r^{(0)})$; backbone term has same law under every permutation → cancels.
- 4-patient worked table → $T_{obs}=4$, $p=1/6$. Backbone offset 10 (or 10,000) vanishes.
- Specificity restored: zero false positives in 1000 iterations at $t>10$.

## Scene 6: ConvergenceMaps, The triviality bound
**Duration**: ~80s
**Purpose**: Quantify why "convergence across patients" is nearly automatic.
### Content
- Sign-agreement operator $A(v)$.
- Independent baseline: $\Pr[\text{all }K\text{ agree}] = 2^{1-K}$ (K=2:50%, 4:12.5%, 8:0.8%).
- Shared-backbone: $\Pr[\text{all }K\text{ agree}] = p^K + (1-p)^K \to 1$ as $p\to1$, independent of $K$.
- Critique's own curve: Dice $0.08\to10\%$, $0.16\to64\%$, $0.25\to97\%$ "significant."

## Scene 7: Resolution, Camera vs Court
**Duration**: ~80s
**Purpose**: Synthesize. Description vs inference + residualization.
### Content
- Camera (description): average $\bar m$, nonspecific. Critique correct.
- Court (inference): contrast $\Delta=\bar m^+ - \bar m^-$ under label null, backbone cancels, signal survives.
- Residualization: $\tilde m_\ell = \Pi_B^\perp m_\ell = \sum_{j>r}\lambda_j(u_j^\top\ell)u_j$; $\text{SNR}(\tilde m)\ge\text{SNR}(m)$.
- Rebuttal numbers: same-symptom $r=0.44$ vs different-symptom $r=0.09$ vs degree $r=0.16$.
- Closing moral: same $C$, two operations, opposite verdicts.

---

## Color Palette
- Variables ($\ell, x, m$): BLUE (#58C4DD)
- Eigenvalues/constants ($\lambda$): YELLOW (#FFFF00)
- Backbone / key terms ($u_1$, "backbone"): GREEN (#83C167)
- Results / theorems: GOLD (#FFD700)
- The "villain" / false positives / what cancels: RED (#FC6255)
- Background: near-black (#101018)

## Shared Elements
- $u_1$ backbone direction recurs (scenes 2,5,7), always GREEN.
- Spectral gap $\lambda_2/\lambda_1$ motif (scenes 2,6).
- Confusion-matrix / null contrast (scenes 4,5).

## Audio
- Narration authored once in `narration.py` (single source of truth).
- `script.py` uses it for `add_subcaption` subtitles.
- `make_audio.sh` synthesizes per-scene voiceover with macOS `say`, then muxes audio onto each rendered scene (padding the shorter stream) and concatenates to `final.mp4`.
