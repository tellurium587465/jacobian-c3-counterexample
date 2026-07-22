# The exact image, and infinitesimal rigidity

Two further structural results about Alpoge's map `F`, each machine-checked:
[`src/verify_image.py`](../src/verify_image.py) and
[`src/verify_rigidity3d.py`](../src/verify_rigidity3d.py).

## 1. The exact image: `F(C³) = C³ ∖ Z`

Let `A = 27a²c² − 18abc + 16a + b³c − b²` (so `Disc_T P = −4A` for the fiber
cubic `P = cT³ − 2T² + bT − 2a`), and

```
Z := V( 3bc − 4 ,  27ac² − 4 )   ⊂   C³      (a closed curve).
```

> **Theorem (complete fiber census).** For every `v ∈ C³`:
> ```
> |F⁻¹(v)| = 3   if A(v) ≠ 0,
> |F⁻¹(v)| = 1   if A(v) = 0 and v ∉ Z,
> |F⁻¹(v)| = 0   iff v ∈ Z.
> ```
> In particular the image of `F` is exactly `C³ ∖ Z`: the counterexample misses
> precisely one explicit closed rational curve, parametrized by
> `c ↦ (4/(27c²), 4/(3c), c)` and isomorphic to `C*`.

**Proof ingredients** (each verified exactly):

* For `c ≠ 0` the finite preimages correspond to the *simple* roots of the
  fiber cubic (`P'(t) = 2/x` kills multiple roots). A cubic over `C` has a
  simple root unless it is a perfect cube `c(T−t₀)³`; matching coefficients,
  the perfect-cube case is exactly `t₀ = 2/(3c)`, `b = 4/(3c)`, `a = 4/(27c²)`
  — i.e. exactly `Z`. Off `Z`: three simple roots if `A ≠ 0`; a double + a
  simple root (hence **one** preimage) if `A = 0`.
* For `c = 0` the `x = 0` sheet gives the explicit section
  `F(0, b, a − 4b²) = (a, b, 0)` — fibers there are never empty (and `Z` misses
  the plane `c = 0`, since `3bc = 4` forces `c ≠ 0`; this also shows `Z` is
  genuinely closed).
* Sample fibers on every stratum agree between the t-model and brute-force
  solving, with exact (or 60-digit certified) map-back checks.

**Structure of the missing curve.** `Z` is a *single orbit* of the hyperbolic
`C*` action on the target (weights `(2,1,−1)`) — the orbit through
`(4/27, 4/3, 1)`. It lies inside the branch surface `{A = 0}`, and under the
shadow invariants `(B, C) = (bc, ac²)` it collapses to the single point
`(4/3, 4/27)` on the shadow discriminant `Δ = 0`.

**A conceptual corollary.** `Z` is a smooth complex subvariety of codimension
2, so `π₁(C³ ∖ Z) ≅ π₁(C³) = 0`. If `F : C³ → C³ ∖ Z` were proper then, being
étale and quasi-finite, it would be finite étale — a finite topological
covering; a connected covering of a simply connected space has degree 1,
contradicting generic degree 3. (Even more elementarily: a proper map into
`C³` has closed image, and `C³ ∖ Z` is not closed.) So the non-properness of
`F` is topologically forced. Note this argument forces non-properness only —
identifying the non-proper *locus* as `{A = 0}` still needs the fiber/escape
analysis above.

*Novelty note*: the cubic model, discriminant, and generic degree 3 are
public; the `jacobianfun.org` explainer explicitly leaves the complete
non-proper-value set open, and we found no earlier public statement of the
exact image or of the 3/1/0 census — "apparently not previously recorded in
the currently public analyses" is the accurate framing (GPT-5.6 round 5).

## 2. Infinitesimal rigidity: the counterexample cannot be deformed (in its class)

The natural next question — *is the counterexample isolated, or one of a
continuous family?* — has a clean first-order answer.

Setup: consider deformations `F + ε·δF` where `δF = (δf, δg, δh)` is graded
like `F` and supported in the same weighted monomial boxes as `F` itself
(13 + 9 + 3 = 25 coefficients; `F` lies in this box). By Jacobi's formula, the
Keller condition `det = const` holds to first order iff the nonconstant part of
`tr(adj(DF)·D(δF))` vanishes — a linear condition `L` on the 25 coefficients
(26 coefficient equations, coefficient-matrix rank 18, kernel dimension 7).

First-order *reparametrizations* (dual-number gauge) are `δF = V(F) + DF·W`
with `V, W` graded polynomial vector fields (target weights `(2,1,−1)`, source
weights `(−1,1,2)`) whose divergences are **separately constant**:
`div V = const` and `div W = const` — the necessary first-order condition
along genuine automorphism families `Φ_ε ∘ F ∘ Ψ_ε` (each polynomial
automorphism has spatially constant Jacobian). Such gauge directions always
lie in `ker L`, since `δ(det DF) = det DF·(div V∘F + div W)`.

> **Result (machine-checked).** `dim ker L = 7`, and there are 7 independent
> gauge directions inside the box — *even under the separate
> divergence-constancy constraints*. Hence `ker L` **equals** the gauge space:
> **Alpoge's map is first-order gauge-rigid inside its weighted monomial box**
> — every box-supported Keller tangent vector is induced by a dual-number
> source/target reparametrization.

Note the logic is one-sided and therefore robust: gauge ⊆ `ker L` holds
unconditionally, so *exhibiting* 7 spanning gauge directions closes the
argument — no completeness claim about the candidate list is needed. (The
seven basis directions are reconstructed deterministically by the script.)

**Honest scope** (per the round-5 adversarial review). This does **not**
establish: rigidity for higher weighted degrees or unrestricted supports;
rigidity under non-graded deformations; that the seven directions integrate to
genuine automorphism *families* (constant divergence alone does not guarantee
polynomial integrability); formal rigidity beyond first order; or local
isolation on the full Keller variety.

**Post-script (round-6 review — important).** The result above is *correct
but universal*: for **any** Keller map, `(DF)⁻¹ = adj(DF)/det` is polynomial,
so every polynomial perturbation factors as `δF = DF·X` with
`X = (DF)⁻¹·δF`, and `δ(det) = det·div X`. Hence `ker L` equals the source
reparametrizations *automatically*, for every Keller map and every compatible
box — the computation is an implementation check of this identity (verified
symbolically in `src/verify_degree4.py` §4), **not** a special property of
Alpoge's map. The first-order deformation theory of every Keller map is
trivial; genuine uniqueness questions live globally. See
[`degree4-obstruction.md`](degree4-obstruction.md) §4–5.
