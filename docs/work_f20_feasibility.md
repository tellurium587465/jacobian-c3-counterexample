# P4 feasibility test: can F20 (or D5) pack 4 cusps + 1 node into a one-place-at-infinity rational curve?

**Status: numerical necessary-condition sieve, run for `d = deg E` in `5..16`.**
Machine parts: [`src/n2/f20_feasibility.py`](../src/n2/f20_feasibility.py).
This adjudicates prediction **P4** from
[`docs/n2-campaign.md`](n2-campaign.md), Session 6 table (confidence 0.40):
*"the `F₂₀` case dies on δ-budget + Bézout + Abhyankar–Moh semigroup
arithmetic alone at all degrees ≤ 16."*

## 0. The question

`cusp_capability()` in
[`src/n2/degree5_ledger.py`](../src/n2/degree5_ledger.py) established that a
degree-5 plane Keller counterexample with solvable monodromy `G ∈ {D₅, F₂₀}`
and irreducible exceptional curve `E` must channel its escape through cusps
capable of hosting the group's local monodromy, with **minimal `F₂₀` cusp =
`(4,5)` (δ = 6)** and **minimal `D₅` cusp = `(2,5)` (δ = 2)** — and that the
surviving configuration needs **4 such cusps + ≥ 1 multibranch point** on a
**rational** curve `E` with **one place at infinity** (forced by the
irreducibility + solvable-monodromy chain in Sessions 4–5). This script asks,
for each candidate `d = deg E` from 5 to 16, whether that combinatorial
package is even numerically consistent — independent of whether it can
actually be realized as the exceptional curve of a genuine Keller map.

**This is deliberately a weaker question than the campaign's real target.**
Passing every test below is *necessary but not sufficient* for the
configuration to exist as an abstract plane curve, and abstract existence is
itself *necessary but not sufficient* for it to arise as the `E` of an actual
counterexample (which carries extra structure — the dicritical data flagged
in Session 5, item (4) of the ranked plan — not modeled here). Failing any
test below, however, is a **rigorous, unconditional exclusion** of that
degree.

## 1. The three tools

### (1) Genus / δ-budget (rigorous)

For a rational (geometric genus 0) plane curve of degree `d`, the arithmetic
genus formula gives

```
sum over ALL singular points P of the projective closure of delta_P  =  (d-1)(d-2)/2,
```

the sum running over affine points **and** the point(s) at infinity. Since
`one place at infinity` means that point is unibranch, write
`delta_infinity` for its contribution. The affine part must then satisfy

```
(d-1)(d-2)/2 - delta_infinity  >=  4 * delta_cusp + delta_extra,     delta_extra >= 1.
```

Two facts make this a *clean* necessary condition:

* **`delta_infinity = 0` is always achievable** (Section 2) — so the sharpest
  version of this bound is with `delta_infinity = 0`:
  `(d-1)(d-2)/2 >= 4*delta_cusp + 1`.
* **the "+1" (or any larger amount) is always realizable without raising any
  point's multiplicity above 2** — two smooth branches meeting with
  intersection multiplicity `I` form a point of multiplicity exactly 2 (sum
  of branch multiplicities) and delta exactly `I`, for *any* `I >= 1`
  (`delta_budget_is_flexible()` in the script). So the extra-point budget can
  absorb arbitrarily large slack `(d-1)(d-2)/2 - 4*delta_cusp - 1` at *no*
  extra Bézout cost, however large `d` gets.

`delta_cusp = 6` for `(4,5)` and `2` for `(2,5)` (both verified against a
brute-force gap-count of the numerical semigroup, not just the closed-form
`(p-1)(q-1)/2`, in `self_check_semigroups()`).

### (2) Bézout / multiplicity (rigorous)

Any auxiliary plane curve `F` of degree `k`, not sharing a component with
`E`, satisfies `(F.E)_P >= mult_P(F) * mult_P(E)` at every point, and Bézout
gives `sum_P (F.E)_P <= k*d`. Forcing `F` to pass through a point with
multiplicity `>= r` is exactly `r(r+1)/2` **linear** conditions on the
`(k+1)(k+2)/2` coefficients of a degree-`k` curve; a homogeneous linear
system with more unknowns than equations always has a nonzero solution, so
existence of a suitable `F` is *guaranteed by dimension count alone* — no
general-position assumption on the 5 special points (4 cusps + node) is
needed anywhere in this argument.

`bezout_search()` brute-forces degree `k = 1..10` and multiplicity
assignments `r_i = 0..8` at the 5 special points (multiplicities on `E`:
`4,4,4,4,2` for F20, `2,2,2,2,2` for D5), keeping only assignments that pass
the dimension-count existence check, and reports the largest forced lower
bound on `d`. The search is robust to widening (checked up to `k<=10`,
`r<=8`; the optimum never moves): the winner in both cases is the **conic
through all 5 points** (`k=2`, `r=(1,1,1,1,1)`, unique generically but
guaranteed to exist regardless, possibly degenerating to a line pair):

* **F20**: `2d >= 4*4 + 1*2 = 18` &nbsp;⟹&nbsp; `d >= 9`.
* **D5**: `2d >= 4*2 + 1*2 = 10` &nbsp;⟹&nbsp; `d >= 5`.

(A line through any 2 of the 4 cusps gives the weaker `d >= 8` resp. `d >=
4`; higher-degree curves with higher forced multiplicities were all checked
and never beat the plain conic.)

### (3) The point at infinity — partial Abhyankar–Moh / Suzuki theory

A rational curve with one place at infinity is exactly a polynomial
parametrization `t -> (f(t), g(t))`. The branch at infinity carries a
numerical semigroup (the Abhyankar–Moh "δ-sequence"; re-proved
algebro-geometrically by **Suzuki**, *Affine plane curves with one place at
infinity*, Ann. Inst. Fourier **49** (1999) 375–404; effectivized by
**Assi–García-Sánchez**, *On curves with one place at infinity*,
[arXiv:1407.0490](https://arxiv.org/abs/1407.0490)) whose first generator is
`deg(f)` and whose genus (`= delta_infinity`) is a Frobenius-number formula
over a whole chain of "approximate roots" — the same combinatorics as an
affine branch's semigroup, but generally with *more than 2* generators, so
the simple `(p-1)(q-1)/2` shortcut used in (1) does not apply to it directly.

**Full enumeration of that semigroup theory for every `d <= 16` was NOT
attempted (this is the honest gap the task asked to flag).** What *is*
proved, elementarily, with no semigroup machinery needed:

> **Lemma (verified in `smooth_infinity_lemma()`).** Choosing `deg f = d`,
> `deg g = d-1` (any lower-order coefficients, only the two leading
> coefficients need be nonzero) makes the local coordinate at infinity have
> order **exactly 1** — the point at infinity is *smooth*, `delta_infinity =
> 0` — for every `d`, unconditionally (no genericity assumption at all).

Proof sketch: in the chart normalizing the dominant projective coordinate to
1, the other affine coordinate is `u(s) = s * G(s)/F(s)` where `s = 1/t`,
`F(s) = s^d f(1/s)`, `G(s) = s^{d-1} g(1/s)` are power series with `F(0) =
G(0) = 1` (leading coefficients). So `u(s)` is `s` times a unit power series
— order exactly 1, regardless of any other coefficient. Checked by direct
`sympy` power-series computation for `d = 5..16` with arbitrary (non-generic,
deterministically chosen) lower coefficients each time; all 12 cases pass.

Since `delta_infinity = 0` is the *best possible* case for the budget in (1)
(any `delta_infinity > 0` only shrinks the affine allowance), this lemma
shows bound (1) is already the sharpest available from the "genus at
infinity" angle for the *abstract existence* question — the deeper
approximate-root machinery would be needed only to (a) try to rule out
`delta_infinity = 0` for some structural reason specific to the Keller
context (it cannot be ruled out in the abstract — this is a constructive
existence proof of a one-place-at-infinity curve with that property), or (b)
attempt to actually *realize* the 4 prescribed affine cusps by an honest
`(f,g)` pair, which is a different and much harder question (Section 3).

## 2. Results

Combined minimal degree = `max(genus-budget minimal d, Bézout minimal d)`.
Degrees below it are **rigorously impossible**; degrees at or above it are
**not excluded by these tools** (existence remains open).

### F20 (4 × cusp `(4,5)`, δ=6, mult 4, + 1 node/tangential point)

min affine δ needed = `4*6+1 = 25`.

| d | genus budget `(d-1)(d-2)/2` | genus OK | Bézout min d | Bézout OK | **survives sieve** | binding constraint if excluded |
|---|---|---|---|---|---|---|
| 5 | 6 | no | 9 | no | **no** | both |
| 6 | 10 | no | 9 | no | **no** | both |
| 7 | 15 | no | 9 | no | **no** | both |
| 8 | 21 | no | 9 | no | **no** | both |
| 9 | 28 | yes | 9 | yes | **yes** | — |
| 10 | 36 | yes | 9 | yes | **yes** | — |
| 11 | 45 | yes | 9 | yes | **yes** | — |
| 12 | 55 | yes | 9 | yes | **yes** | — |
| 13 | 66 | yes | 9 | yes | **yes** | — |
| 14 | 78 | yes | 9 | yes | **yes** | — |
| 15 | 91 | yes | 9 | yes | **yes** | — |
| 16 | 105 | yes | 9 | yes | **yes** | — |

**Minimal surviving degree: `d = 9`.** `d = 5,6,7,8` are rigorously excluded
(both tests fail simultaneously — a coincidence of this particular cusp
package, not a general phenomenon, see D5 below where the two bounds differ).
`d = 9..16` all survive with room to spare (e.g. at `d=9` the leftover affine
δ-budget is exactly `28-24 = 4`, comfortably absorbed by a single tangential
2-branch point of intersection multiplicity 4).

### D5 (4 × cusp `(2,5)`, δ=2, mult 2, + 1 node/tangential point) — the contrast case

min affine δ needed = `4*2+1 = 9`.

| d | genus budget | genus OK | Bézout min d | Bézout OK | **survives sieve** | binding constraint if excluded |
|---|---|---|---|---|---|---|
| 5 | 6 | no | 5 | yes | **no** | genus/delta budget |
| 6 | 10 | yes | 5 | yes | **yes** | — |
| 7–16 | 15..105 | yes | 5 | yes | **yes** | — |

**Minimal surviving degree: `d = 6`.** Here the two tools disagree and the
**genus/δ-budget is the strictly binding constraint** (Bézout alone would
already allow `d=5`, since mult-2 cusps only need `2d >= 10`; it is the
"not enough room for 4 cusps + a node inside genus `(d-1)(d-2)/2`" bound that
pushes the true minimum up to 6). This matches the "much looser" contrast
anticipated in the task: multiplicity-2 cusps barely constrain Bézout, so
the genus formula (a property of the *whole* configuration, not just pairs
or 5-point subsets) becomes the binding tool.

### F20 vs D5, side by side

| | cusp mult | cusp δ | min affine δ | genus-min `d` | Bézout-min `d` | **combined min `d`** | binding |
|---|---|---|---|---|---|---|---|
| F20 | 4 | 6 | 25 | 9 | 9 | **9** | tie |
| D5  | 2 | 2 | 9  | 6 | 5 | **6** | genus budget |

The F20 tie (genus-min = Bézout-min = 9) is an observed numerical
coincidence of this specific cusp package (`4*mult+2 = 18`, and `2*mult+1 =
9` happens to match `ceil(18/2)`), not a theorem; it is not reproduced for
D5, where the two bounds differ by one degree.

## 3. Honest TODOs / what this does NOT settle

1. **No realizability construction attempted.** Passing the sieve at `d=9`
   (F20) or `d=6` (D5) does **not** prove a curve with exactly this singular
   content exists. Constructing (or obstructing) an actual polynomial pair
   `(f,g)` with 4 branches analytically equivalent to `<4,5>` plus a node is
   the genuine open problem — comparable in difficulty to the general
   classification questions around rational cuspidal plane curves (Orevkov,
   Fenske, Flenner–Zaidenberg, Koras–Palka, Borodzik–Żołądek-type results);
   none of that literature was consulted or applied here.
2. **Full Abhyankar–Moh semigroup-at-infinity enumeration not done.** Only
   the single constructive fact `delta_infinity = 0` via `deg g = deg f - 1`
   was established (Section 1.3). The general theory (arbitrary `(deg f, deg
   g)` pairs, multi-generator semigroups, the Assi–García-Sánchez
   δ-sequence machinery) was looked up (Suzuki 1999; arXiv:1407.0490,
   1407.0514) but not implemented/enumerated. It is not needed for the
   *upper-bound* direction (δ_∞=0 is already optimal for budget purposes),
   but it **would** be needed to check whether some *other* structural
   requirement (e.g. Keller-map dicritical data, see next point) forces
   `delta_infinity > 0` for reasons outside the abstract curve theory,
   in which case bound (1) would tighten.
3. **This sieve ignores the Keller-map embedding entirely.** Session 5's
   ranked plan, item (4), flags that the *dicritical* structure of the
   actual exceptional curve (pole orders along the unique dicritical divisor
   of a genuine counterexample) may determine the semigroup at infinity
   directly, and may be **more rigid** than "some one-place rational curve
   exists abstractly." That map-theoretic constraint is not modeled by
   anything in this script.
4. **No refined Plücker / log-BMY-type inequality attempted.** A sharper
   classical tool (accounting for the *full* infinitely-near multiplicity
   sequence of each `(4,5)` cusp — multiplicity 4 at the first blow-up, then
   multiplicity 1, i.e. resolved in one further non-transverse blow-up — via
   the class formula or a log-Bogomolov–Miyaoka–Yau-type bound for rational
   cuspidal curves) was considered but not carried through; it was checked
   by hand that the *naive* multiplicity-4 Bézout bound used here is not
   obviously improvable by low-degree auxiliary curves (search up to degree
   10 confirms), but a genuinely sharper inequality of this type is not
   ruled out and is flagged as the natural next step if P4 is to be
   revisited.
5. **δ-budget "extra point" flexibility used a tangential 2-branch model.**
   This is a valid realization of *some* multibranch point with the required
   δ, but the campaign's actual escape mechanism may demand the extra
   point be specifically a *node* (δ=1 exactly, per the D5/F20 class-field
   5-coloring arguments in Session 5) rather than a high-tangency point.
   If so, the genus-budget slack at `d=9` (F20) would need to be absorbed
   by *additional* affine singular points instead of one flexible point —
   plausible (any 2-nodal / 2-cuspidal split works) but not checked here.

## 4. Verdict on P4

**P4 (confidence 0.40: "F20 dies on δ-budget + Bézout + AM-semigroup
arithmetic alone at all degrees ≤ 16") is FALSIFIED as stated**, to the
extent the three named tools were implemented here: `d = 9` through `d = 16`
all survive the genus-budget and Bézout sieves simultaneously, and the one
constructive fact available about the point at infinity (`delta_infinity =
0` achievable via `deg g = deg f - 1`) does not add a further obstruction —
if anything it confirms bound (1) is already tight. `d = 5..8` are
rigorously excluded (both tools agree), so the honest updated statement is:

> *the F20 configuration cannot occur below degree 9; from degree 9 up
> through 16, none of {genus budget, Bézout, the smooth-infinity
> construction} obstructs it, and the question of whether it is actually
> realizable (or excluded by deeper tools per Section 3) remains open.*

For D5, the parallel minimal degree is 6, with the genus/δ-budget (not
Bézout) as the binding constraint — confirming the "much looser" contrast
anticipated for the weaker `(2,5)` cusp.

## Files

* [`src/n2/f20_feasibility.py`](../src/n2/f20_feasibility.py) — all
  computations above (semigroup self-check, δ-budget flexibility argument,
  smoothness-at-infinity lemma verification, Bézout search, combined
  feasibility tables for F20 and D5, `d = 5..16`). Run with
  `python src/n2/f20_feasibility.py`.
* [`src/n2/degree5_ledger.py`](../src/n2/degree5_ledger.py) — upstream
  `cusp_capability()` establishing the `(4,5)` / `(2,5)` minimal cusps this
  test takes as input.
* [`docs/n2-campaign.md`](n2-campaign.md) — Session 5 (δ-budget bounds,
  ranked plan), Session 6 (P4 registration).
