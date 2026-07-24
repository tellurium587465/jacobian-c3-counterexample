# Literature sweep: rigidity theory of rational cuspidal plane curves vs. a
# rational curve with 4(s) cusps of type <2,5>/<4,5> PLUS a node

Date of sweep: 2026-07-24. Method: WebSearch + WebFetch (arXiv abstracts, ar5iv HTML mirrors,
r.jina.ai mirrors of raw PDFs — plain WebFetch could not decode most of the source PDFs, listed
below where this happened). No primary source was paywalled-blocked outright, but several were
only accessible through AI-mediated re-renderings rather than direct text; every such case is
flagged **(mirror-read)** and treated as slightly less certain than a direct quote.

**Target configuration (as given):** Ē ⊂ P² irreducible, rational (normalization P¹), degree d,
with (A) at least 4 (or 4s, s≥1) unibranch cusps each of type <2,5> (δ=2, mult 2) OR type <4,5>
(δ=6, mult 4); (B) at least one multibranch point (e.g. a node); (C) one place at infinity.
Existing degree bounds: d≥6 for the <2,5> case, d≥9 for the <4,5> case.

Rating key: **DIRECT KILL** (excludes the configuration outright), **STRONG BOUND** (real
theorem, numerically checked, not violated but constrains), **SUPPORTING** (relevant background,
no sharp numeric bite), **NOT-APPLICABLE** (real theorem, but hypotheses fail for our curve —
stated explicitly why), **TODO** (could not verify to the precision required; flagged rather than
guessed).

---

## 0. Single most decisive finding

**Every sharp/rigidity theorem found in this sweep — Tono's 8-cusp bound, Palka's 6-cusp bound,
and the final Koras–Palka sharp 4-cusp theorem — is a theorem about curves that are *purely
cuspidal*, i.e. whose only singular points are unibranch (in the precise technical sense: "a
complex planar curve homeomorphic to the [projective] line").** A node is a multibranch point;
a curve with a node is topologically **not** homeomorphic to P¹ (removing the node disconnects a
punctured neighborhood into more local branches than a smooth/cuspidal point would), so it falls
**outside the hypothesis** of every one of these theorems, including the sharpest one:

> **Koras–Palka (2019/2020):** "We show that a complex planar curve homeomorphic to the
> projective line has at most four singular points. If it has exactly four then it has degree
> five and is unique up to a projective equivalence." — M. Koras, K. Palka, *Complex planar
> curves homeomorphic to a line have at most four singular points*, arXiv:1905.11376
> (J. Math. Pures Appl., 2019/2020). <https://arxiv.org/abs/1905.11376>

If our curve had **no** node (purely cuspidal with ≥4 cusps of type <2,5> or <4,5>), this theorem
would be a **DIRECT KILL** for every case with 4s cusps, s≥2 (already >4 singular points), and for
the s=1 case it would force d=5 with the *specific known* cusp types (one <2,7> + three <2,3>,
see §5) — **not** <2,5> or <4,5> and **not** d=6 or d=9. So the purely-cuspidal analogue of our
configuration is flatly excluded by an unconditional, published theorem.

**Because our curve has a node, this kill does not transfer automatically.** I found **no
published theorem** that bounds the number of cusps on a rational plane curve that also carries a
node/multibranch point with anything like this sharpness (§2). The entire "semigroup
distribution property / gap function" machinery (§3) is likewise explicitly restricted by its
authors to "all singular points cuspidal" (Borodzik–Livingston, verbatim quote in §3) and so also
does **not** apply as stated. The one general-purpose tool that *does* survive the presence of a
node — the coarse degree/multiplicity inequalities (Matsuoka–Sakai, Orevkov) via the logarithmic
BMY inequality — turn out, on numerical evaluation (§4), to **not be violated** by either the
d=6/<2,5>×4 or the d=9/<4,5>×4 configuration; they are not tight enough to bite once a node is
added to the delta-invariant budget.

**Bottom line: rigidity theory for rational cuspidal curves kills the purely-cuspidal version of
this configuration outright (Koras–Palka), but the presence of the node moves our curve into a
genuinely under-studied class for which I could not find a published sharp bound. The honest
verdict is "not excluded by any theorem found," not "excluded."** This is a real gap in the
literature as far as I could determine, not a case of the bound simply not having been checked
against our numbers — see §2's TODO for exactly where a new argument would be needed.

---

## 1. Maximal number of cusps (purely cuspidal case)

Three results, in chronological/logical order, all requiring **purely cuspidal** curves (every
singular point unibranch):

**(a) Tono (2005) — first uniform bound, any genus.**
> K. Tono, *On the number of the cusps of cuspidal plane curves*, Math. Nachr. 278 (2005),
> 216–221. "A cuspidal plane curve of genus g has no more than (21g+17)/2 cusps." Consequence:
> **a rational (g=0) cuspidal plane curve has at most 8 cusps.**

Proof method: dual graph of the minimal embedded resolution + the log-BMY inequality, computing
κ̄ and e_top(P²\C). Requires the curve to be **cuspidal** by definition of the object studied
(all singularities unibranch) — Tono's own definition of "cuspidal plane curve" already excludes
nodes. There is a follow-up erratum/refinement:
> S. Yu. Orevkov, *Remark on Tono's theorem about cuspidal curves*, Math. Nachr. 290 (2017),
> 2992–2994, PDF at <https://www.math.univ-toulouse.fr/~orevkov/tono.pdf> — corrects a gap in
> Tono's argument; the 8-cusp bound for g=0 survives.

Rating: **STRONG BOUND** for the purely-cuspidal analogue; **NOT-APPLICABLE** to our curve (has a
node).

**(b) Palka (2016/2019) — sharpened to 6.**
> K. Palka, *Cuspidal curves, minimal models and Zaidenberg's finiteness conjecture*, J. Reine
> Angew. Math. (Crelle) 2019(747), 147–174; arXiv:1405.5346. Verbatim abstract: "Let E ⊆ P²
> be a complex rational cuspidal curve and let (X,D) → (P²,E) be the minimal log resolution of
> singularities. We prove that Ē has at most six cusps and we establish an effective version of
> the Zaidenberg Finiteness Conjecture (1994) concerning Eisenbud–Neumann diagrams of E."
> <https://arxiv.org/abs/1405.5346>

Method: almost-minimal model program (MMP) for the pair (X, ½D); Palka's own program, predecessor
to the Koras–Palka classification series. "Rational cuspidal curve" here again means purely
unibranch singularities (this is the standing definition throughout the Koras–Palka research
program). Rating: **STRONG BOUND**, superseded by (c); **NOT-APPLICABLE** to our curve.

**(c) Koras–Palka (2019/2020) — the sharp, final theorem.**
> M. Koras, K. Palka, *Complex planar curves homeomorphic to a line have at most four singular
> points*, arXiv:1905.11376 (submitted 2019, revised 2020; J. Math. Pures Appl.). Verbatim
> abstract: "We show that a complex planar curve homeomorphic to the projective line has at most
> four singular points. If it has exactly four then it has degree five and is unique up to a
> projective equivalence." <https://arxiv.org/abs/1905.11376>

This is the theorem I would flag as the single most important one in this whole sweep: it is
**unconditional** (not "conjectural, verified to degree 20" like the earlier Flenner–Zaidenberg/
Piontkowski picture — see below), it is **sharp** (achieved, uniquely), and it is stated in terms
of "singular points," not "cusps," which is precisely how it makes the no-nodes hypothesis
explicit: a curve *with* a node is not homeomorphic to a line, so is simply outside the theorem's
universe of discourse — the theorem says nothing about it either way.

Method: builds on the Coolidge–Nagata conjecture proof (Koras–Palka, Duke Math. J. 2017,
<https://arxiv.org/abs/1502.07149>, and the "more than four cusps ⇒ rectifiable" partial result,
K. Palka, *The Coolidge–Nagata conjecture holds for curves with more than four cusps*,
arXiv:1202.3491 — verbatim abstract: "Let E be a plane rational curve defined over complex
numbers which has only locally irreducible singularities. ... We show that if it is not
rectifiable then the tree of the exceptional divisor for its minimal embedded resolution of
singularities has at most nine maximal twigs. This settles the conjecture in case E has more than
four singular points." <https://arxiv.org/abs/1202.3491> — again explicit "only locally
irreducible singularities," i.e. no nodes) via the almost-minimal MMP.

Rating: **DIRECT KILL for the purely-cuspidal analogue of our configuration** (any curve with 4s
cusps, s≥2, is already excluded by ">4 singular points"; the s=1, 4-cusp case is excluded because
the unique example has the wrong degree (5, not 6 or 9) and wrong cusp types, see §5).
**NOT-APPLICABLE to our actual curve as stated, because of the node.**

**Purely computational/conjectural picture predating (c), for context:**
> J. Piontkowski, *On the Number of Cusps of Rational Cuspidal Plane Curves*, Experiment. Math.
> 16 (2007), no. 2; PDF <https://www.math.uni-duesseldorf.de/~piontkow/Rat.pdf>. Verbatim (via
> mirror-read): "**Conjecture 2:** A rational cuspidal plane curve has at most three cusps — with
> the exception of a rational plane quintic with four cusps," verified computationally up to
> degree 20 **conditional on** the Flenner–Zaidenberg rigidity conjecture (that Q-acyclic affine
> surfaces of log Kodaira dimension 2 are rigid/unobstructed — this conjecture is what makes
> "count equisingular strata = count curves" valid). Koras–Palka's theorem (c) above proves this
> conjecture unconditionally (indeed proves the sharper/cleaner "≤4 singular points, =4 forces
> the quintic" form). Rating: **SUPERSEDED**, kept for the cusp-type table in §5.

---

## 2. Rational curves with cusps AND nodes — is there an analogous bound?

This is where the sweep comes up short of a clean citation, and I want to be precise about what I
did and didn't find, rather than paper over the gap.

**What I found on the general log-Kodaira-dimension classification (which in principle does not
presuppose purely-cuspidal curves):**

> I. Wakabayashi, *On the logarithmic Kodaira dimension of the complement of a curve in P²*,
> Proc. Japan Acad. Ser. A Math. Sci. 54 (1978), no. 6, 157–162.
> <https://projecteuclid.org/journals/proceedings-of-the-japan-academy-series-a-mathematical-sciences/volume-54/issue-6/On-the-logarithmic-Kodaira-dimension-of-the-complement-of-a/10.3792/pjaa.54.157.full>

Quoted **(mirror-read, via ar5iv rendering of the Fernandez de Bobadilla–Luengo–Melle-Hernández–
Némethi survey math/0604421, NOT the primary Wakabayashi paper itself — flagged accordingly)**:
"If g(C)≥1 and d≥4 then κ̄(P²∖C)=2" and "If g(C)=0 and C has at least 3 cuspidal points then
κ̄(P²∖C)=2." The phrasing "C has at least 3 cuspidal points" (rather than "C is cuspidal") is
suggestive that this specific statement is about a rational curve C that merely *possesses* ≥3
unibranch singular points, without asserting these are its *only* singularities — which would
mean it is not automatically voided by an extra node. **I could not verify this reading against
Wakabayashi's original 1978 paper itself (only 2 pages, in Japanese-academy Proceedings, not
freely retrieved in this sweep) — TODO: confirm directly.** If this reading is right, it would
tell us κ̄(P²\Ē)=2 (log general type) for our curve (which has ≥4 cuspidal points regardless of
the node), which is a **necessary precondition** for the whole log-BMY machinery in §4 to be
non-vacuous, but by itself it does not bound the *number* of cusps — it is a classification
trichotomy (κ̄ ∈ {-∞, 0, 1, 2}), not a counting bound.

> Sh. Tsunoda, *The complements of projective plane curves*, RIMS Kôkyûroku 446 (1981), 48–56.
> Excludes the κ̄=0 case for rational cuspidal curves (via secondary citation only — **TODO**,
> primary text not retrieved).

> M. Miyanishi, T. Sugie, *On a projective plane curve whose complement has logarithmic Kodaira
> dimension −∞*, Osaka J. Math. 18 (1981), 1–11. Classifies the κ̄=−∞ case; per the survey, "all
> these curves are classified... and contain only one singularity" — **this classification is
> for the (at most) 1-singular-point case, essentially irrelevant to our ≥5-singular-point curve
> (4+ cusps plus a node) since κ̄=−∞ would already require ν≤1.**

**What I explicitly did NOT find:** any paper that states "a rational plane curve with r nodes
and c cusps satisfies c ≤ f(r)" or similar, for any function f — i.e. no analogue of Koras–Palka
extending to the mixed nodal-cuspidal case. I searched specifically for this (queries on "rational
cuspidal curve node bound," "curves with nodes and cusps classification," "Koras Palka node") and
turned up nothing beyond the purely-cuspidal literature above. The Koras–Palka MMP program (their
series "Classification of planar rational cuspidal curves I/II," arXiv:1609.03992 and
arXiv:1810.08180) is explicitly restricted to curves homeomorphic to a line throughout — I
fetched the abstract of part I and it discusses only "bicuspidal curves" (2-cusp, still purely
cuspidal) as the frontier of what remains unclassified within the no-nodes universe; there is no
stated intention to extend to nodal curves.

**Why I believe this is a genuine gap and not just my search missing it:** the topological
invariant that organizes this whole research program (κ̄(P²\C), computed via a minimal log
resolution) changes character qualitatively once you add a node — a node is already SNC
(simple-normal-crossing) locally, so it needs **no** blow-up to resolve (unlike a cusp, which
needs a weighted sequence of blow-ups whose exceptional divisors carry all the "rigidity" data
that Koras–Palka's MMP analyzes), but it **does** change π₁(P²\C) and the topological Euler
characteristic e_top(P²\C) (a node identifies two points of the normalization P¹ to one, dropping
e_top(C) by 1 per node, hence changing e_top(P²\C) = 3 − e_top(C)). The entire machinery would
need to be redone (not merely re-cited) to track this, and as far as I found, nobody has published
that redo for the specific case "cusps + one node." Rating for point 2 as a whole: **TODO / open
gap** — no theorem found, honestly reported rather than invented.

---

## 3. Semigroup distribution property and multi-cusp lattice/spectrum constraints

**Primary source:** J. Fernandez de Bobadilla, I. Luengo, A. Melle-Hernández, A. Némethi, *On
rational cuspidal projective plane curves*, Proc. London Math. Soc. (3) 92 (2006), 99–138;
arXiv:math/0410611 <https://arxiv.org/abs/math/0410611>, and the companion survey *On rational
cuspidal curves, open surfaces and local singularities*, arXiv:math/0604421
<https://arxiv.org/abs/math/0604421>.

**Precise statement of the Semigroup Distribution Property** (quoted via ar5iv mirror-read of
math/0410611, §Introduction/§3.2): for a **unicuspidal** (ν=1) rational plane curve of degree d
with cusp semigroup Γ = Γ(C,p), define the intervals

> I_l := ((l−1)d, ld]  for l > 0.

The conjecture (property "(DP)"/"(CP)"; the survey also calls it Conjecture B) states:

> "there are exactly min{l+1, d} elements of the semigroup Γ in I_l for any l > 0."

This connects the local numerical semigroup of the cusp to the global degree d in a way finer than
the delta-invariant/genus formula alone — it is a distributional constraint, not just a counting
one. It is proved to be equivalent (their Theorem 2.6, per mirror-read) to a generating-function
identity D(t) ≡ 0. **Explicitly restricted to ν=1 (a single cusp)** in this original formulation.

**Multi-singular-point generalization exists, but is explicitly still cusps-only.**
> M. Borodzik, C. Livingston, *Heegaard Floer homology and rational cuspidal curves*, Forum Math.
> Sigma; arXiv:1304.1062 <https://arxiv.org/abs/1304.1062>.

Verbatim abstract (direct fetch, not mirror): "We apply the methods of Heegaard Floer homology to
identify topological properties of complex curves in the complex projective plane. As one
application, we resolve an open conjecture that constrains the Alexander polynomial of the link
of the singular point of the curve in the case that there is exactly one singular point, having
connected link, and the curve is of genus 0. **Generalizations apply in the case of multiple
singular points.**"

Quoted (mirror-read) theorem statements:
- **Theorem 1.1** (unicuspidal case): for C a rational cuspidal curve of degree d with one
  singular point, a cone on knot K, Alexander polynomial Δ_K(t) expanded at t=1 as
  Δ_K(t) = 1 + [(d−1)(d−2)/2](t−1) + (t−1)² Σ k_l t^l, then for all j, 0 ≤ j ≤ d−3:
  k_{d(d−j−3)} = (j−1)(j−2)/2. [I flag the exact subscript/exponent placement as **mirror-read,
  possibly garbled in re-transcription** — TODO: verify against the primary PDF before using this
  formula for a real computation.]
- **Theorem 5.4** (multiple singular points): "Let C be a rational cuspidal curve of degree d.
  Let I₁,…,Iₙ be the gap functions associated to each singular point on C. Then for any
  j ∈ {−1,0,…,d−2} we have I₁⋄I₂⋄⋯⋄Iₙ(jd+1) = (j−d+1)(j−d+2)/2," where ⋄ is a "star product"
  combining per-cusp gap functions (defined earlier in the paper; not independently verified here
  — **TODO**).

**Critical caveat, quoted directly from the paper's introduction (mirror-read):** *"Unless
specified otherwise, all singular points are assumed to be cuspidal."* The multi-singular-point
generalization (Theorem 5.4) is stated for multiple **cusps**, not for a mix of cusps and nodes.
Rating: **NOT-APPLICABLE** to our curve as literally stated — the entire semigroup-distribution /
gap-function / d-invariant apparatus (this section) has, as far as this sweep found, never been
extended to curves carrying a node. This mirrors the finding in §2: the obstruction-theoretic tool
kit for rational cuspidal curves is thoroughly developed for the no-nodes case and, to my
knowledge from this sweep, simply hasn't been built out for the nodal-plus-cuspidal case.

**Related semicontinuity-of-spectrum work** (context, not independently re-derived here):
M. Borodzik, A. Némethi, *Spectrum of plane curves via knot theory*, J. London Math. Soc. (2) 86
(2012), 87–110; arXiv:1101.5471 <https://arxiv.org/abs/1101.5471>. Uses Seifert forms/
Tristram–Levine signatures of links to reprove (weaker form of) Steenbrink–Varchenko semicontinuity
of the spectrum at infinity. I did not find in this sweep an explicit "multi-cusp + node" version
of this either; rating **SUPPORTING** background only, **TODO** for anything sharper.

---

## 4. The Orevkov inequality (and Matsuoka–Sakai, and the underlying log-BMY)

**Primary source, obtained via r.jina.ai mirror of the author's own PDF** (direct WebFetch could
not decode the PDF stream; the mirror-read is internally consistent with all secondary citations
found independently, so I have reasonable confidence in it, but flag it as mirror-read):

> S. Yu. Orevkov, *On rational cuspidal curves. I. Sharp estimate for degree via multiplicities*,
> Math. Ann. 324 (2002), 657–673. PDF: <https://www.math.univ-toulouse.fr/~orevkov/cusp.pdf>.

Verbatim abstract opening (mirror-read): "Let C ⊂ P² be a rational curve of degree d which has
only one analytic branch at each point [i.e. **purely cuspidal, no nodes** — explicit hypothesis].
Denote by m the maximal multiplicity of singularities of C."

**Theorem A** (general form, requires only κ̄(P²∖C) ≥ 0):
> d < α(m+1) + 1/√5 = αm + 3.0652…, where α = (3+√5)/2 = 2.6180… ("the square of the golden
> section," satisfying α² + 1 = 3α... [equivalently α = φ² where φ=(1+√5)/2 is the golden ratio]).

**Theorem B**, refined trichotomy:
- (a) if κ̄(P²∖C) = −∞: d < αm.
- (b) if κ̄(P²∖C) = 2 (log general type — the relevant case for us per §2): **d < α(m+1) − 1/√5
  = αm + 2.1708…** (sharper than Theorem A).
- (c) κ̄(P²∖C) ≠ 0 (Tsunoda's exclusion, re-derived/cited here too).

**Theorem C** (sharpness/examples): for j > 0, j ≢ 2 (mod 4), there is a rational cuspidal curve
C_j of degree d_j = φ^{j+2} with a single cusp of multiplicity m_j = φ^j (φ = golden ratio) — these
Orevkov curves show the αm asymptotics cannot be improved.

**Underlying log-BMY inequality** (Section 2, mirror-read):
- Theorem 2.1(a): if κ̄(X∖D) ≥ 0 then (K+D)² ≤ 3ē(X∖D).
- Theorem 2.1(b): if κ̄(X∖D) = 2, a refined form H² ≤ 3ē(X∖D) [H the appropriate nef push-forward].
- **Corollary 2.2** (the genuinely *sum-over-cusps* form the task asked about): for a rational
  cuspidal curve with singular points p₁,…,p_s and associated "M-numbers" M₁,…,M_s (a finer
  per-cusp invariant than raw multiplicity, defined via the continued-fraction/Puiseux data of
  each cusp in the paper's §3, Prop. 3.3): **M₁ + ⋯ + M_s ≤ 3d − 4** (stated for κ̄(P²−C) ≥ 0,
  sharpened form again for κ̄ = 2).

I was **not able to pin down, within this sweep, the closed-form expression of the M-number for a
single-Puiseux-pair cusp (p,q)** (needed to evaluate Corollary 2.2 numerically for our <2,5> and
<4,5> cusps) — Prop. 3.3's formulas (μ = 1 − d₁ + Σqᵢ(dᵢ−1), M = d₁ − 2 + Σ(qᵢ − ⌈qᵢ/dᵢ⌉)) are
given in terms of a continued-fraction encoding (dᵢ,qᵢ) of the Puiseux data whose translation from
(p,q) I did not verify carefully enough to trust a from-scratch computation here. **Marked TODO**
rather than guessed. I did, however, evaluate the coarser (but citable and unambiguous) Theorem
A/B(b) and the earlier Matsuoka–Sakai bound, both keyed only on the maximal multiplicity m:

> **Matsuoka–Sakai** (earlier, weaker, superseded result): T. Matsuoka, F. Sakai, *The degree of
> rational cuspidal curves*, Math. Ann. 285 (1989), 233–247;
> <https://link.springer.com/article/10.1007/BF01443516>. Result (per multiple independent
> secondary citations, consistent wording): for a rational cuspidal curve of degree d with maximal
> singularity multiplicity m, **d < 3m**.

### Numerical evaluation

All of Matsuoka–Sakai / Orevkov require **purely cuspidal** curves (locally irreducible at every
point) — so strictly speaking **NOT-APPLICABLE** to our curve because of the node. I evaluate them
anyway as the honest "what if the node weren't there" sanity check the task asked for, and to see
whether the coarse degree-vs-multiplicity route would even bite in the purely-cuspidal limit:

**Case d=6, four <2,5> cusps (δ=2, mult m=2 each ⇒ max multiplicity m=2):**
- Matsuoka–Sakai: need d < 3m = 6. Actual d = 6. **6 < 6 is FALSE** — d=6 sits exactly on this
  (weaker, superseded) bound, technically violating its strict inequality if it applied.
- Orevkov Theorem A: need d < αm + 3.0652 = 2.618×2 + 3.0652 = 8.301. **6 < 8.301: holds**,
  comfortably.
- Orevkov Theorem B(b) (κ̄=2 case, sharper): need d < αm + 2.1708 = 5.236 + 2.171 = 7.407.
  **6 < 7.407: holds.**
- **Verdict: not excluded by the sharp (Orevkov) coarse bound; sits right at the edge of the older
  Matsuoka–Sakai bound (which Orevkov's paper explicitly supersedes as non-sharp), so this is not
  by itself a red flag.**

**Case d=9, four <4,5> cusps (δ=6, mult m=4 each ⇒ max multiplicity m=4):**
- Matsuoka–Sakai: need d < 3m = 12. **9 < 12: holds**, with room to spare.
- Orevkov Theorem A: need d < αm + 3.0652 = 2.618×4 + 3.0652 = 13.537. **9 < 13.537: holds.**
- Orevkov Theorem B(b): need d < αm + 2.1708 = 10.472 + 2.171 = 12.643. **9 < 12.643: holds.**
- **Verdict: comfortably satisfied, not excluded.**

**Reading of this result:** the coarse degree/max-multiplicity inequalities are simply not tight
enough, at these small multiplicities (m=2 or m=4), to exclude either configuration — they are
asymptotic bounds that bite hard for *large* m (single high-multiplicity cusps), not for several
small-multiplicity cusps. This is consistent with why the *sharp* exclusion of the purely-cuspidal
analogue in §1 comes from Koras–Palka's finer classification (which cusp *types* are achievable in
a 4-cusp curve, not merely how large a single multiplicity can be), not from Orevkov's degree
inequality. **Rating: STRONG BOUND but not a kill, and NOT-APPLICABLE to our actual curve (node)
in any case.**

---

## 5. Do <2,5> or <4,5> cusps appear in known/classified multi-cuspidal rational curves?

**The unique 4-cusp curve (Koras–Palka's exceptional case, degree 5).** Per Piontkowski's census
(mirror-read of <https://www.math.uni-duesseldorf.de/~piontkow/Rat.pdf>), the degree-5 four-cusp
curve has cusp-type list "[(2³), (2), (2), (2)]" in multiplicity-sequence notation, i.e. **one
cusp with multiplicity sequence (2,2,2)** — by the standard correspondence for two-generator
semigroups <2, 2k+1> (k successive multiplicity-2 infinitely-near points ⇒ δ=k), this is a
**<2,7> cusp (δ=3)** — **plus three ordinary cusps with multiplicity sequence (2)**, i.e. **<2,3>
cusps (δ=1 each)**. Total δ = 3+1+1+1 = 6 = (5−1)(5−2)/2, matching the genus-0 formula exactly (an
internal consistency check I ran myself, not quoted from a source). **Neither <2,5> nor <4,5>
appears.** This translation (multiplicity-sequence ↔ Puiseux pair) is standard but I performed it
myself rather than finding it spelled out verbatim in a source — flagged as a **derived, not
directly quoted**, fact, though I'm confident in it.

**Known 3-cusp series on P² (Piontkowski, mirror-read), general degree d, none matching <2,5> or
<4,5>:**
- degree d=2k+3 (k≥1): cusp types [(d−3, 2ᵏ)], [(3ᵏ)], [(2)].
- degree d=3k+4 (k≥1): cusp types [(d−4, 3ᵏ)], [(4ᵏ, 2²)], [(2)].
- degree d≥4 general family: [(d−2)], [(2ⁿ)], [(2ᵐ)], n+m=d−2.

**4-cusp curves on Hirzebruch surfaces F_e** (a different ambient surface, not P² — included for
context only): T. Fenske / follow-up work, *Rational cuspidal curves with four cusps on Hirzebruch
surfaces*, arXiv:1303.4178 <https://arxiv.org/abs/1303.4178>. Mirror-read classification table:
all listed cusp multiplicity-sequences use only entries in {2,3,4} with δ up to 3 (e.g. [2³]);
**again no <2,5> (δ=2, but as a *two-term* semigroup, not the (2,2,2)-sequence <2,7>) or <4,5>
(δ=6) cusp type appears.** Because this is on F_e rather than P², it is only **SUPPORTING**
context, not a direct statement about our P² curve — flagged as such.

**Direct search for "4 cusps of type <2,5> or <4,5>" anywhere in the literature:** none found.
Given that (i) the unique purely-cuspidal 4-cusp curve is completely classified and doesn't have
these cusp types, and (ii) I found no papers constructing or excluding a nodal curve with these
cusp types, this specific configuration (with a node) appears to be **outside the scope of any
published classification** — neither confirmed to exist nor excluded by name. Rating: **TODO /
open**, reported honestly rather than inferred either way.

**One more internal-consistency note (not from a citation, just genus-formula arithmetic):** a
purely-cuspidal curve with exactly a single <2,5> cusp cannot exist at all on genus grounds: δ=2
would require (d−1)(d−2)/2 = 2, i.e. (d−1)(d−2)=4, which has no integer solution — confirming why
<2,5> cusps only ever occur as *part of* a multi-singular-point configuration, consistent with
(and unsurprising given) our curve's need for extra singularities (multiple cusps + node) to
satisfy the degree-genus formula exactly.

---

## Summary table

| # | Question | Sharpest citable result | Requires no-node? | Numerically violated by our data? | Rating |
|---|---|---|---|---|---|
| 1 | Max cusps, purely cuspidal | Koras–Palka: ≤4, =4 ⇒ d=5 unique curve (arXiv:1905.11376) | Yes (theorem's actual hypothesis) | Would be violated for s≥2 (>4 cusps); s=1 case has wrong d/cusp-types | **DIRECT KILL of purely-cuspidal analogue; NOT-APPLICABLE to our curve (has node)** |
| 2 | Cusps+nodes bound | Wakabayashi/Tsunoda/Miyanishi-Sugie classify κ̄; no cusp-counting analogue of (1) found | — | n/a — no bound exists to check | **TODO / open gap** |
| 3 | Semigroup distribution property | FdBLMN 2006 (ν=1); Borodzik–Livingston Thm 5.4 (multi-cusp, still no nodes) | Yes, explicit | n/a — not applicable | **NOT-APPLICABLE** (node) |
| 4 | Orevkov inequality | d < αm+3.0652 (Thm A); d< αm+2.1708 (Thm B(b), κ̄=2) | Yes, explicit | No — both cases (d=6,m=2) and (d=9,m=4) satisfy it comfortably (borderline only vs. the older, superseded Matsuoka–Sakai d<3m at d=6) | **STRONG BOUND, not a kill; NOT-APPLICABLE strictly (node)** |
| 5 | <2,5>/<4,5> in known 4-cusp curves | Unique quintic has <2,7>+3×<2,3>; no <2,5>/<4,5> found anywhere in the census | — | — | **Absent from all known examples; TODO whether excluded or merely unexplored** |

---

## Bibliography (all URLs checked live in this sweep)

- K. Tono, *On the number of the cusps of cuspidal plane curves*, Math. Nachr. 278 (2005), 216–221.
- S. Yu. Orevkov, *Remark on Tono's theorem about cuspidal curves*, Math. Nachr. 290 (2017), 2992–2994. <https://www.math.univ-toulouse.fr/~orevkov/tono.pdf>
- K. Palka, *Cuspidal curves, minimal models and Zaidenberg's finiteness conjecture*, J. Reine Angew. Math. 2019(747), 147–174; arXiv:1405.5346. <https://arxiv.org/abs/1405.5346>
- M. Koras, K. Palka, *Complex planar curves homeomorphic to a line have at most four singular points*, arXiv:1905.11376. <https://arxiv.org/abs/1905.11376>
- M. Koras, K. Palka, *The Coolidge–Nagata conjecture*, Duke Math. J. (2017); arXiv:1502.07149. <https://arxiv.org/abs/1502.07149>
- K. Palka, *The Coolidge-Nagata conjecture holds for curves with more than four cusps*, arXiv:1202.3491. <https://arxiv.org/abs/1202.3491>
- K. Palka, M. Koras, *Classification of planar rational cuspidal curves. I. C**-fibrations*, arXiv:1609.03992. <https://arxiv.org/abs/1609.03992>
- K. Koras, K. Palka, *Classification of planar rational cuspidal curves. II. Log del Pezzo models*, arXiv:1810.08180. <https://arxiv.org/abs/1810.08180>
- J. Piontkowski, *On the Number of Cusps of Rational Cuspidal Plane Curves*, Experiment. Math. 16 (2007), no. 2. <https://www.math.uni-duesseldorf.de/~piontkow/Rat.pdf>
- I. Wakabayashi, *On the logarithmic Kodaira dimension of the complement of a curve in P²*, Proc. Japan Acad. Ser. A 54 (1978), 157–162. <https://projecteuclid.org/journals/proceedings-of-the-japan-academy-series-a-mathematical-sciences/volume-54/issue-6/On-the-logarithmic-Kodaira-dimension-of-the-complement-of-a/10.3792/pjaa.54.157.full>
- Sh. Tsunoda, *The complements of projective plane curves*, RIMS Kôkyûroku 446 (1981), 48–56. (primary text not retrieved — TODO)
- M. Miyanishi, T. Sugie, *On a projective plane curve whose complement has logarithmic Kodaira dimension −∞*, Osaka J. Math. 18 (1981), 1–11.
- J. Fernandez de Bobadilla, I. Luengo, A. Melle-Hernández, A. Némethi, *On rational cuspidal projective plane curves*, Proc. London Math. Soc. (3) 92 (2006), 99–138; arXiv:math/0410611. <https://arxiv.org/abs/math/0410611>
- Same authors, survey: *On rational cuspidal curves, open surfaces and local singularities*, arXiv:math/0604421. <https://arxiv.org/abs/math/0604421>
- M. Borodzik, C. Livingston, *Heegaard Floer homology and rational cuspidal curves*, arXiv:1304.1062 (Forum Math. Sigma). <https://arxiv.org/abs/1304.1062>
- M. Borodzik, A. Némethi, *Spectrum of plane curves via knot theory*, J. London Math. Soc. (2) 86 (2012), 87–110; arXiv:1101.5471. <https://arxiv.org/abs/1101.5471>
- P. Bodnár, J. Celoria, M. Golla, *Cuspidal curves and Heegaard Floer homology*, arXiv:1409.3282. <https://arxiv.org/abs/1409.3282>
- S. Yu. Orevkov, *On rational cuspidal curves. I. Sharp estimate for degree via multiplicities*, Math. Ann. 324 (2002), 657–673. <https://www.math.univ-toulouse.fr/~orevkov/cusp.pdf>
- T. Matsuoka, F. Sakai, *The degree of rational cuspidal curves*, Math. Ann. 285 (1989), 233–247. <https://link.springer.com/article/10.1007/BF01443516>
- T. Fenske et al., *Rational cuspidal curves with four cusps on Hirzebruch surfaces*, arXiv:1303.4178. <https://arxiv.org/abs/1303.4178>
- T. K. Moe, *Rational Cuspidal Curves* (PhD thesis, survey), arXiv:1511.02691. <https://arxiv.org/abs/1511.02691> (fetched but content did not render usably in this sweep — background only)
