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
