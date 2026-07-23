# Toward geometric degree 4: an obstruction, a corrective discovery, and the sharp open question

This note records one full loop of discovery → obstruction → pivot →
**correction** (the round-6 adversarial review overturned our initial framing
of §4, and the corrected version is *more* informative). Every computational
claim is machine-checked in [`src/verify_degree4.py`](../src/verify_degree4.py).

## 1. The question

Which geometric degrees are realizable by Keller counterexamples?

* `d = 1` — impossible (birational Keller theorem).
* `d = 2` — impossible **in every dimension**: a degree-2 field extension is
  Galois (char 0), and the Galois case of the Jacobian Conjecture is a theorem
  (Campbell; Razar; Wright).
* `d = 3` — realized by Alpoge's map on `C³` (and `3^k` by compositions).
* `d = 4` — **open**. A natural attack: extend the marked-cubic mechanism to a
  *marked quartic* on `C⁴`.

## 2. The naive quartic tower — and why it dies

Alpoge's map *is* the marked-cubic model: over a target `(a,b,c)` the fiber
variable `t = y + 1/x` satisfies `P(T) = cT³ − 2T² + bT − 2a` with the marking
`P'(t) = 2/x`, and `P` is weighted-homogeneous of weight 2 with `T` of weight 1
(coefficient weights `(−1, 0, 1, 2)`, the constant `−2` sitting at the weight-0
slot).

The naive `d = 4` analogue is `P(T) = eT⁴ + cT³ − 2T² + bT − 2a` on `C⁴`,
target weights `(2, 1, −1, −2)`, source weights `(−1, 1, 2, 3)`, with
`c = x·C(s₁,s₂,s₃)`, `e = x²·E(s₁,s₂,s₃)` (`s₁ = xy, s₂ = x²z, s₃ = x³w`), and
`a, b` *defined* by `P(t) = 0`, `P'(t) = 2/x`.

**Step 1 succeeds**: polynomiality of `(a, b)` imposes only three linear
conditions (`C(0) = 2`, a linear relation between the `s₁`-coefficients, and
`E(0) = 0`), leaving a **21-parameter family** of polynomial candidate maps
containing the cubic model.

**Step 2 kills all of it.**

> **Obstruction Lemma (graded weight bound).** Let `C*` act on `C^n` with
> exactly one negative weight, say `wt(x) = −1`. Then every semi-invariant of
> weight `−m ≤ −2` lies in the ideal `(x²)` — each monomial `x^i·(positive
> part)` of weight `−m` has `i = m + (positive contributions) ≥ m ≥ 2`. Hence
> if an equivariant polynomial map has a component of weight `≤ −2`, that
> component's differential vanishes identically on `{x = 0}`, so `det DF ≡ 0`
> there: **`F` cannot be Keller.**

The naive quartic model has the weight-`(−2)` component `e`, so *none* of the
21 parameters give a Keller map (verified: `det DF|_{x=0} ≡ 0` identically in
all 21 parameters).

## 3. What survives the weight arithmetic

For a marked degree-`d` model with `T`-weight 1 and `P`-weight `ω`, the
coefficient of `T^k` has weight `ω − k`. The Lemma forces every *varying*
coefficient to have weight `≥ −1`, so `ω ≥ d − 1`; the constant slot sits at
`k = ω`. For `d = 4` the *only* viable pattern is `ω = 3`:

```
coefficient weights  (3, 2, 1, 0, −1)  —  constant at the T³ slot,
P(T) = e T⁴ − 2 T³ + b₂T² + b₁T + b₀ ,   target weights (−1, 1, 2, 3).
```

But then the marking `r = P'(t)` has weight `ω − 1 = 2`, while the cubic's
reconstruction identity `r = 2/x` is weight-1: **the cubic's marking cannot
transfer**. A degree-4 tower therefore needs either a genuinely different
marking identity or at least two negative-weight source variables. That is the
precisely-located open door — not a dead end, but a fork whose both branches
leave the cubic template.

Two caveats from the round-6 adversarial review, adopted: (i) the
classification is complete *for this model shape* (one fixed nonzero
coefficient, four varying slots, a unique primitive negative source weight) —
it is an arithmetic screen, not a universal no-go; for `T`-weight `τ = −q < 0`
there are two mirror patterns (`k₀ = 0`, any `q`; and `k₀ = 1, q = 1`). (ii)
The *monic* variant (`k₀ = 4`, constant leading coefficient) is **not**
excluded by this argument: "monic fiber polynomial ⟹ proper" is unproven
(`t = y + 1/x` lives only in a localization, so its monic equation does not
establish finiteness of the coordinate ring extension). What survives is only
the conditional: a *proper* Keller map would be a finite étale cover of a
simply connected space, hence degree 1.

## 4. First-order rigidity is universal — a corrective discovery

We initially computed "enlarged-box rigidity" for Alpoge's map
(`ker L = gauge`: 7 = 7 in F's own 25-parameter box, 13 = 13 in the
39-parameter box) as *uniqueness evidence*. The round-6 adversarial review
found the true explanation, which we then verified symbolically — and it
deflates that framing:

> **Proposition (universal first-order triviality).** Let `F` be *any* Keller
> map. Since `det DF` is a unit, `(DF)⁻¹ = adj(DF)/det` is a polynomial
> matrix, so **every** polynomial perturbation `δF` factors as `δF = DF·X`
> with `X := (DF)⁻¹·δF` a polynomial vector field — i.e. every first-order
> deformation is an infinitesimal *source reparametrization* — and
> `δ(det DF) = det DF · div X`. Hence
> `ker L = DF·{vector fields with constant divergence}` automatically, for
> every Keller map and every compatibly chosen box.

(Verified exactly for Alpoge's `F` with generic vector fields in
`src/verify_degree4.py` §4.) So the box computations are correct but are
*implementation checks of a universal identity*, *not* evidence that Alpoge's
map is special: the first-order deformation theory of every Keller map is
trivial. The honest moral is sharper than the one we started with:

* meaningful uniqueness lives **globally**, not infinitesimally: the right
  computation is a full classification of solutions of the bracket equation
  `−2Pf{Pg,Ph} + Pg{Pf,Ph} + Ph{Pf,Pg} = const` in bounded graded boxes,
  gauge-sliced, with per-component tests for geometric degree and
  non-properness — feasible for the minimal box with serious computer algebra
  (modular Gröbner / numerical homotopy), likely beyond naive sympy for
  larger boxes;
* and the conjecture should be stated globally:

> **Primitive graded cubic uniqueness conjecture** (formulation refined by
> the round-6 review). Up to equivariant polynomial automorphisms of source
> and target, scalar normalization of the Jacobian, and inversion of the
> `C*`-action, Alpoge's map is the unique non-proper Keller map of `C³` of
> geometric degree 3 whose effective source and target weight multisets are
> `{−1, 1, 2}`.

## 5a. The second door also resists (round 7 of the loop)

We then attacked the surviving pattern head-on with a **new marking identity**:
`r := κ·t/x` has weight 2 (as the pattern requires), and inverts rationally —
`x = κt/r`. Setting `P(T) = eT⁴ − λT³ + b₂T² + b₁T + b₀` with `b₁, b₀` defined
by `P(t) = 0`, `P'(t) = r`:

* **Polynomiality forces `κ = λ`** — the marking constant must equal the fixed
  coefficient, exactly as in the cubic (`r = 2/x` against the fixed `−2`); one
  branch, `e₀ = λ, e₁ = −3λ/2, c_y = λ/2, e₁₁ = 2λ − c_y2/3`, all scalable to
  `λ = 2` (verified exactly, `verify_degree4.py` §5). So the `κ = λ = 2`
  search below is fully general.
* This leaves a genuine **12-parameter family of polynomial maps** on `C⁴`
  containing quartic fiber structure — the obstruction of §2 is avoided
  (`e = x·E` with `E(0) = 2 ≠ 0`).
* Numerically, the Keller condition then showed a residual floor `≈ 1` in 12-
  and 24-parameter ansätze (only degenerate `det ≡ 0` solutions; reproducible
  via [`src/quartic_search.py`](../src/quartic_search.py)) — and the round-7
  review turned that numerical floor into an **exact theorem**:

> **Tower no-go theorem** (GPT-5.6 round 7; identity verified exactly in
> `verify_degree4.py` §6). For the derivative-marked degree-`d` tower
> (marking `P'(t) = λ·t^{d−3}/x`, with `κ = λ` forced), the invariant-chain
> factorization gives the *universal factor*
> ```
> det ∂(T₁,…,T_{d−1})/∂(u, E, A_{d−2},…,A₂)  =  λ²·(1+u)^{2(d−3)}·E^{N_d}
> ```
> (verified for `d = 3, 4, 5` with `N = 2, 5, 9`). Hence for **every**
> polynomial choice of the free data:
> * `d ≥ 4`: `det DF = λ²(1+xy)^{2(d−3)}·(a polynomial bracket)` — it
>   **vanishes on the hypersurface `xy = −1`** and can never be a nonzero
>   constant. *No Keller map exists in the derivative-marked tower for any
>   degree `d ≥ 4`.*
> * `d = 3`: the factor is trivial, `det DF = −λ²·E_{s₂}` (constant iff `E`
>   is linear in `s₂`), and Alpoge's `E = 2 − 3s₁ − s₂` recovers `det = −2`
>   exactly. Moreover every solution (`E = f(s₁) + c·s₂`) is carried to
>   Alpoge's by the graded gauge `z ↦ z + y²g(xy)` — within the tower,
>   **degree 3 contains exactly the Alpoge orbit**.

**Why 3 is special, in one sentence:** the marking `P'(t) = λt^{d−3}/x`
vanishes at `t = 0` for every `d ≥ 4` — the marked root becomes critical on
the hypersurface `{t = 0} = {xy = −1}` — while for `d = 3` the marking
`λ/x` is nowhere-critical. The counterexample lives in degree 3 not by
accident but by necessity of its own mechanism.

Also from round 7, the **principal-part lemma**: for every degree `d`, the
two leading pole cancellations force `E(0) = λ` and `κ = λ` — the marking
constant, the fixed coefficient, and the leading value of `E` all coincide
(in the cubic: the "2" of `r = 2/x`, of `−2T²`, and of `Ph(0) = 2` are the
same 2).

Status of the degree-4 question after this loop:

* naive marking (`r = 2/x`): **dead** (§2, weight obstruction);
* derivative marking (`r = λt^{d−3}/x`): **dead for all `d ≥ 4`** (tower
  no-go theorem), and for `d = 3` it contains exactly the Alpoge orbit;
* still open: non-derivative weight-`(d−2)` markings, reconstructions not
  eliminating `(b₁, b₀)` from `P(t) = 0, P'(t) = r`, sparse/multi-fixed
  coefficient models, `≥ 2` negative source weights
  (`(−1, 1, −m, m+5)`-type), the monic pattern (pending a properness proof),
  and non-graded constructions.

## 5b. The Ψ breakthrough: the no-go's boundary, and a near-Keller structure

Round 8 of the loop found the *precise* boundary of the tower no-go — and
stepped over it.

**The exact mathematics (new).** The fiber identity `b₀ + t·b₁ = R` pins down
the pair `(b₁, b₀)` only up to the shift

```
(b₁, b₀)  ⟼  (b₁ + x·ψ,  b₀ − t·x·ψ),      ψ any weight-3 polynomial,
```

which in invariant form reads `P₁ ↦ P₁ + Ψ`, `P₀ ↦ P₀ − HΨ` with `Ψ` **not**
divisible by `H = 1 + s₁`. The no-go theorem's forced factor `H^{2(d−3)}`
came exactly from `H | P₁`, `H² | P₀` — which the shift destroys. The general
determinant (free functions `E, A, Ψ`) provably contains `H`-free terms
(e.g. `2Ψ²·{A,E}`): **the no-go theorem is sharp — it characterizes the
`Ψ = 0` stratum, and the full fiber-tower escapes it.** A second exact fact:
with the mixed marking `m = c·t² + d·t/x`, polynomiality now leaves `c` free
(`d = λ − c` locked) — a genuine extra modulus.

**The numerical event** (`src/quartic_psi_search.py`; three independent runs,
different seeds, sample sets and ansätze): the least-squares floor that was
stuck at `≈ 1.0` through every `Ψ = 0` search **collapses to `7.5×10⁻⁴`**,
with

```
det DF ≈ 0.0859–0.0860   (stable across runs; μ = 11.62–11.64)
λ drifting (1.78 → 1.93 → 2.13):  a solution curve, not an isolated point,
```

and the determinant constant to 4–5 digits across 50–90 random sample points.
Honest interpretation — *numeric evidence only, no theorem claimed*: either a
genuine polynomial Keller map of geometric degree 4 lives at higher ansatz
degree (the significant coefficients climb the `s₁`-tail, suggesting the
truncation is what blocks exactness), or a formal, non-polynomial solution
shadows the family — which would itself set up a sharp
"formal-yes/polynomial-no" no-go. The decisive experiment is the exact
degree-by-degree (graded Newton) solve of `det = const` in the `Ψ`-extended
family; it is the single highest-value computation left on this branch.

Either resolution is a major result: a **new counterexample of geometric
degree 4** (answering our own public question), or the **complete closure of
the graded quartic tower** with the exact formal/polynomial dichotomy.

## 5c. The formal solution exists (round 9; 40-digit staged Gauss-Newton)

The decisive computation ran (`src/quartic_gn_solver.py`; numerics, clearly
labeled). Reduce the whole tower to: find `E, A, P₁` and `δ ≠ 0` with the
support conditions and `det ∂(AE, P₁E², P₀E³)/∂S = δ·E⁵`,
`P₀ = λH³ − EH⁴ − AH² − P₁H`, `λ = 2`. Then, at 40-digit precision:

* staged Gauss-Newton solves **every** tested window (all coefficient
  equations through weighted degree 6) to residuals `10⁻³⁵–10⁻³⁷` —
  exact solvability at working precision, reproducibly from random seeds;
* the same holds with **`δ` frozen at `11/128`** — the solution is
  **non-degenerate** (the `det ≡ 0` trap is excluded; `δ` is
  gauge-normalizable by `S₂,S₃`-scalings);
* the stage structure is underdetermined at every degree
  (`3p(m+3) > p(m)` unknowns vs equations), and every tested stage had
  full-rank solvable systems — consistent with continuation to all orders.

**Round-10 corrections (adopted).** Two downgrades to the above, from the
adversarial review: (i) *semantics* — if the formal series solution exists,
the induced `F` is a **formal automorphism** of `Spf C[[x,y,z,w]]` (formal
inverse function theorem; `det DF = δ ≠ 0`), *not* a "formal 4:1 cover"; the
quartic identity supplies only an auxiliary algebraic relation of degree ≤ 4
for the Laurent element `t = y + 1/x` over a rationally generated subfield.
"Four sheets" is meaningful only for genuine polynomial/global solutions.
(ii) *strength* — what the computation establishes is high-precision
**order-6 jets**, and the factorization identity below suggests jet-lifting
may be structurally easy (the problem is one scalar equation for three
series in a coordinate system `(B,C,T)`); formal existence to all orders is
plausible but unproven. The nonvacuous content of the whole question is
**polynomiality** — exactly where the numerics say no.

What is *not* yet settled: **polynomiality**. The degree-≤6 truncated
solution satisfies its windows exactly but its full residual profile shows
`O(10²)` violations at degrees 7–30 — the truncation does not extend as-is.

**Endgame round (first sweep, `src/quartic_truncation_search.py`).** The
overdetermined truncation search ran for four asymmetric patterns
`(dE, dA, dP)` — degree caps for `(E, A, P₁)` — with 8 random starts each:

| pattern | unknowns | equations | best residual |
|---|---|---|---|
| (2,4,5) | 24 | 314 | 4.1×10⁻¹ |
| (3,4,6) | 34 | 458 | 1.6×10⁰ |
| (3,5,6) | 39 | 458 | 2.4×10⁰ |
| (2,5,7) | 44 | 640 | 1.6×10⁰ |

**All floor at `O(1)`** — no polynomial solution in any tested pattern.
(A 39× faster vectorized evaluator independently reproduces the `(3,5,6)`
floor: 2.41 vs 2.36 — the floors are real, not optimizer artifacts.)

**Second sweep (vectorized), eight larger patterns — same verdict:**

| pattern | unknowns | equations | best residual |
|---|---|---|---|
| (4,6,8) | 68 | 865 | 2.6 |
| (6,6,6) | 62 | 458 | 1.3 |
| (4,5,7) | 51 | 640 | 1.4 |
| (5,7,9) | 93 | 1041 | 2.7 |
| (4,6,9) | 80 | 1041 | 2.2 |
| (5,6,8) | 73 | 865 | 1.7 |
| (6,8,10) | 124 | 1041 | 2.4 |
| (3,6,8) | 64 | 865 | 2.4 |

Twelve patterns total, all `O(1)` floors — and §5d's divisibility obstruction
`Φ | E³` is the exact reason why.

## 5d. The factorization identity (round 10) — the sharpest tool yet

The round-10 review produced, and we verified exactly (sympy, generic
functions), a factorization of the entire Keller equation. With
`B = AE`, `C = P₁E²`, `T = HE` and

```
Φ := 3λH² − 4EH³ − 2AH − P₁ ,
```

one has the **exact identity**

```
J(AE, P₁E², P₀E³) = E²·Φ·J(B, C, T),      so   Keller ⟺ Φ·J(B,C,T) = δ·E³.
```

Consequences:

* **Polynomial obstruction.** For polynomial solutions the UFD gives
  **`Φ | E³`** — every irreducible factor of `Φ` divides `E`. Since
  `Φ(0) = −λ ≠ 0` and `E(0) = λ ≠ 0`, the cases are rigid:
  `Φ = c·E^j` (`j = 0..3`, constants fixed by `λ`) when `E` is irreducible.
* **Sharp explanation of the numeric floors.** In the balanced pattern
  `k = d_E = 2`, the top form of `Φ` generically has degree 5, but every
  divisor of `e³` (`e` irreducible of degree 2) has degree 2, 4 or 6 — the
  divisibility is *impossible* without extra cancellation. The `O(1)` floors
  are the numerical shadow of this exact obstruction.
* **The `j = 3` case reduces dimensions — and also floors.**
  `Φ = −E³/λ²` forces `J(B, C, T) = const`: the triple `(B, C, T)` is then a
  **Keller triple of `C³`** with `C` *determined* by `(E, A)` and support
  locks `A₁ = −5λ, E₁ = 4λ`. A first small-ansatz exact solve yields only
  degenerate branches, and the dedicated numeric sweep
  (`src/quartic_rigid_j3_search.py`) floors at `O(1)` through `(dE, dA)`
  up to `(6, 8)` — 60 unknowns against 3571 equations:

  | (dE,dA) | (2,4) | (3,5) | (4,6) | (4,8) | (5,7) | (5,9) | (6,8) |
  |---|---|---|---|---|---|---|---|
  | residual | 3.2 | 2.9 | 3.1 | 3.0 | 2.9 | 3.0 | 5.6 |

  The last structured door within computational reach is closed.

> **Conjecture (polynomial non-realizability of the graded quartic tower).**
> There are no polynomials `E, A, P₁ ∈ C[S₁,S₂,S₃]` satisfying the support
> conditions and `Φ·J(AE, P₁E², HE) = δE³` with `δ ≠ 0`. Equivalently,
> geometric degree 4 is not realizable by the `(−1,1,2,3)`-graded
> marked-quartic mechanism. (Supported by: 12 general truncation patterns +
> 7 rigid-case sizes all flooring at `O(1)`; the exact divisibility
> obstruction `Φ | E³`; and order-6 formal jets showing the *formal* problem
> is unobstructed — the failure is genuinely about polynomiality.)
* For formal series `Φ` is a *unit* (`Φ(0) ≠ 0`), so no divisibility
  constrains the formal branch — precisely the formal/polynomial asymmetry
  the numerics detected.

Honest status: numerics on both sides plus one exact identity; the endgame
is now a structured case analysis (`Φ = cE^j`) rather than a blind search.

## 5. Realizable geometric degrees: the sharp open question

With attributions checked in round 6:

* `d = 1`: realized only by automorphisms — impossible for a non-invertible
  Keller map (birational Keller theorem).
* `d = 2`: impossible in **every** dimension — a separable quadratic extension
  is Galois, and the Galois case is a theorem (Campbell 1973 over `C`; Razar
  1979 and independently Wright 1981 in char 0; *geometric* degree 2, distinct
  from Wang's coordinate-degree-2 theorem).
* `d = 3`: realized (Alpoge). Products `F × G` multiply geometric degrees
  (block-diagonal Jacobians; generic fibers multiply), so the realizable set
  is a multiplicative monoid: all `3^k` occur.
* Everything else is unknown. The two sharp public questions:

> **Does there exist a Keller map of geometric degree 4?**
> More generally: **is there a Keller map whose geometric degree has a prime
> divisor other than 3?**
