# The n = 2 program: what we tried, proved, and could not do

The plane Jacobian Conjecture (`n = 2`) remains **open**. This document records an
honest AI attack on it (Claude Opus 4.8 + GPT-5.6 as adversarial strategist,
2026-07-21/22), with every mathematical claim machine-checked in
[`src/n2/verify_n2.py`](../src/n2/verify_n2.py). Nothing here settles `n = 2`;
what it does is (a) extract everything the new `n = 3` counterexample teaches
about the plane case, (b) prove a small rigidity theorem delimiting where a plane
counterexample cannot live, and (c) document the strategies that *fail*, with
precise reasons — which is genuine information for anyone attacking `n = 2`.

## 1. The shadow: how close the n=3 mechanism comes to the plane

Alpoge's map `F` is equivariant for the hyperbolic `C*` action with source
weights `(-1,1,2)` and target weights `(2,1,-1)`. Its invariant rings are
polynomial rings in two variables (`s = xy, w = x²z` and `B = bc, C = ac²`), so
`F` induces a **polynomial plane map** — the *shadow*:

```
phi(s,w) = (Pg·Ph, Pf·Ph²)
Pf = (s+1)(3s³+s²w+4s²+2sw+w),  Pg = 9s³+3s²w+12s²+6sw+s+3w,  Ph = 2-3s-w
```

Verified properties:

* **Shadow principle** (generic, symbolic): writing `f = x⁻²Pf, g = x⁻¹Pg,
  h = xPh`, one has `det DF = D(s,w)` with the bracket formula
  `D = -2·Pf{Pg,Ph} + Pg{Pf,Ph} + Ph{Pf,Pg}` (`{A,B} = A_s B_w - A_w B_s`), and
  ```
  det J_phi = - Ph² · D .
  ```
  The entire 3-dimensional Keller condition compresses to a *two-variable*
  bracket identity: for Alpoge's data, `D ≡ -2`.
* The shadow has `det J_phi = 2(3s+w-2)²` — **a perfect square, not a
  constant**: `phi` is étale exactly off the line `L: 3s+w = 2`, and `phi`
  **contracts L to the origin**.
* `phi` is generically **3-to-1** and inherits rational triple collisions, e.g.
  `(-4/3,3), (-2,9), (1/3,-1/2) ↦ (-1,-1)`.
* **Normal form** (found by GPT-5.6, verified here): `phi` factors through the
  "universal marked cubic": `psi(s,w) = (τ,ρ) = (Ph·(s+1), 2Ph)` — the invariant
  avatars of `(c·t, c·P'(t))` — followed by
  `chi(τ,ρ) = (ρ+4τ-3τ², τ²-τ³+ρτ/2)`, with
  `τ³-2τ²+Bτ-2C = 0`, `ρ = 3τ²-4τ+B`, `det Dpsi = -2Ph`, `det Dchi = -ρ/2`.
* The target discriminant curve is `Δ(B,C) = 27C²-18BC+16C+B³-B²`
  (`Disc = -4Δ`; this is `A·c²` in invariant coordinates); its pullback under
  `phi` is `-Ph²·(an explicit quartic)`, and fibers over `Δ = 0` degenerate
  (e.g. a single point over `(B,C) = (1,0)`; the entire critical line over
  `(0,0)`).

**Moral.** The degree-3 mechanism *does* descend to the plane — but the price is
exactly the factor `Ph²` in the Jacobian, concentrated on one contracted line.
A plane Keller map would need that factor to be absent, i.e. `Ph` constant; the
corollary below shows this can only happen if the input already contained a
plane counterexample. The weight-2 variable `z` is the "room" dimension 3 has
and dimension 2 lacks.

**No free lunch corollary.** The shadow of a hyperbolic `C³` Keller map is
itself Keller iff `Ph ≡ c₀ ∈ C*`; then `h = c₀x` and `(f,g)` restricts on every
slice `x = const` to a plane Keller family. The quotient construction can never
*create* a plane counterexample from honest 3-dimensional data.

## 2. Plane hyperbolic rigidity (the small theorem)

> **Theorem** (char 0; the field need not be algebraically closed). Let `G_m`
> act on `A²` with two nonzero weights of opposite signs:
> `t·(x,y) = (t⁻ᵖx, tᵠy)`, `p,q ≥ 1` (gcd not needed — divide by it). Every
> polynomial self-map with semi-invariant components and constant nonzero
> Jacobian is **a monomial linear map**: `(αx, βy)` or `(αy, βx)`. In
> particular it is an automorphism — **no hyperbolically equivariant plane
> Keller counterexample exists.**

Proof (elementary; every identity machine-checked in `verify_n2.py` §7–8):

1. A semi-invariant is `xᵃyᵇA(v)`, `v = x^q y^p`, `A(0) ≠ 0` (the exponent
   lattice of a fixed weight is one arithmetic progression — no second minimal
   monomial exists).
2. **All-degrees identity** (GPT-5.6's repair of our finite-degree check;
   verified with symbolic `a,b,c,d,p,q` and *generic functions* `A,B`):
   ```
   det DΦ = x^{a+c-1} y^{b+d-1} · E(v),
   E(v) = (ad-bc)·AB + v·[(ap-bq)·AB' + (qd-pc)·A'B]
   ```
   (the candidate `v²A'B'` terms cancel identically).
3. `det = δ ≠ 0` as a Laurent-polynomial identity forces a single surviving
   monomial with exponent `(0,0)`: either `(a+c, b+d) = (1,1)`, or the boundary
   case `p = q = 1, a=b=c=d=0` — where both components are functions of `xy`
   and `det ≡ 0`. 
4. Four sign patterns remain. Diagonal `(xA, yB)`: `E = AB + v(pAB' + qA'B)`,
   and the top-degree coefficient `α_A α_B (1 + p·degB + q·degA)` cannot vanish
   in characteristic 0 — so `A, B` are constants. Antidiagonal `(yA, xB)`:
   symmetric. Crossed `(xyA, B)`: `det = (p−q)vAB'` is divisible by `v` — never
   a nonzero constant. ∎

**Corollaries** (from the round-3 review, all elementary): for *elliptic*
weights (both positive) the classification relaxes only to resonant triangular
shears `(x, y + γx^{s/r})` — still automorphisms; strict equivariance (same
action on both sides) or equivariance up to a character `t^r` forces `r = 0`
and the diagonal form.

**The dimension gap, stated correctly.** Alpoge's counterexample *is*
hyperbolically equivariant (weights `(-1,1,2)`). Within the
hyperbolically-symmetric class:

* dimension 2: étale + semi-invariant coordinates ⟹ linear, geometric degree 1
  (rigidity — proven above);
* dimension 3: geometric degree 3 occurs (Alpoge);
* and the two are linked by the shadow principle: the 3D map **does** descend
  to the plane — what fails is *preservation of étaleness*, and the failure is
  measured exactly by `det J_φ = −Ph²·det DF`: supported on `{Ph = 0}`, with
  multiplicity two.

*Honesty note*: this rigidity lemma is presumably standard to experts in
weighted methods for the plane Jacobian problem (the negative-weight tradition
goes back to Abhyankar); we found no exact statement to cite and claim only the
formulation + machine-checked proof + the `n = 3` contrast, not priority.

## 3. Strategies that fail, with reasons (GPT-5.6 adversarial triage)

* **S₃ / quadratic-resolvent descent** ("degree-3 counterexample ⟹ degree-2
  Keller map ⟹ contradiction with the known Galois case"): **dies**. The
  quadratic resolvent field `E = K(√Disc)` is *not* an intermediate field of the
  cubic extension `L/K` (fixed fields of an order-2 subgroup vs `A₃` — neither
  contains the other). Moreover the resolvent double cover must *ramify*
  (`A²` has no nontrivial connected finite étale covers), so it is never
  "another plane Keller map". Only the weak unconditional statement survives:
  any degree-3 plane counterexample has non-square discriminant, `S₃` normal
  closure, and a resolvent normalization ramified over a nonempty divisor.
* **Monic cubic models**: if a plane counterexample's fiber cubic were monic
  (a finite covering), it would give a connected finite étale degree-3 cover of
  `A²` — impossible (`A²` is simply connected). So any cubic model must have a
  *rational* primitive element and boundary corrections outside the cubic
  chart — exactly as in the `n = 3` example, where `t = y + 1/x`.
* **Linear-coefficient cubic ansatz as a finite search**: not finite-dimensional
  without arbitrary degree bounds (source tame automorphisms are unbounded);
  with bounds it becomes a Gröbner problem but encodes little.
* **Known constraints** (for context): geometric degree `d = 1` impossible
  (birational Keller theorem); `d = 2` impossible (quadratic ⟹ Galois ⟹ known);
  so `d ≥ 3`. Moh: no plane counterexample of degree ≤ 100.
  `gcd(deg P, deg Q) ≥ 16`. A 2024 preprint (Moskowicz, arXiv:2407.13795)
  claims no prime `d` — unvetted, not used anywhere here.

## 4. Status

**The plane Jacobian Conjecture remains open.** This program's yield: the shadow
principle + normal form (a complete, exact description of the plane projection
of the `n = 3` mechanism), the rigidity theorem (hyperbolic symmetry cannot
carry a plane counterexample), and precise kill-reasons for the resolvent and
finite-étale routes. The essential open difficulty isolated by all three:
**boundary completion** — whether the missing sheets of a degree-≥3 cubic-type
mechanism can be compactified into an honest `A²` — which is where any future
attack (or disproof) has to live.
