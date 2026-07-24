# The n = 2 campaign — a long-war plan for the plane Jacobian Conjecture

**Started 2026-07-24.** The plane Jacobian Conjecture is the last standing
wall of this landscape: `n ≥ 3` fell in July 2026, every degree `3..100` is
realized in dimension 3, Dixmier fell for `n ≥ 3` — and `n = 2` (equivalently
`DC_2`, stably) has survived everything, including our own rounds 2–3
(shadow principle; plane hyperbolic rigidity; the resolvent dead end).

This document is the standing war plan. It will be updated every campaign
session. **No victory is promised; every claim will be machine-verified or
clearly labeled; every failure will be recorded.**

## 0. The map of known constraints (to be re-verified and sharpened)

A hypothetical plane counterexample `(P, Q)`, `{P,Q} = 1`, must satisfy:

* geometric degree `d ≥ 3` (`d=1`: birational Keller; `d=2`: Galois case);
* `deg > 100` (Moh) and `gcd(deg P, deg Q) ≥ 16` (Appelgate–Onishi/Nagata);
* Newton-polygon constraints (Abhyankar school; to be catalogued precisely);
* **not** hyperbolically graded (our rigidity theorem);
* if the Moskowicz preprint (arXiv:2407.13795, unvetted) holds: `d` cannot
  be prime — with `d=2,3` impossible the minimal case becomes `d = 4`,
  composite. **Vetting this preprint is Phase 1** — it is the single
  unvetted claim that most reshapes the battlefield.

## 1. Our arsenal (what did not exist a week ago)

* **Valuation lemmas** — the technique that cracked the C⁴ tower (forced
  `Φ ≡ const`, squarefreeness) by counting `q`-adic orders of Jacobian rows.
  Does it bite on plane pairs, e.g. through forced factorization structures
  on partial derivatives / on `P_u, P_v`?
* **Collapse phenomenon** — the entire graded quartic tower collapsed to one
  bracket equation in fewer variables. Question: is there a general
  "graded tower ⟹ dimension-collapse" principle, and can hypothetical plane
  structures be shown to collapse to 1D (`f' = const` ⟹ linear ⟹ dead)?
* **Imprimitivity invariants** — monodromy block structure as a live
  invariant of counterexamples; what block structures are possible for a
  degree-`d` plane counterexample's `S_d`-action?
* **The shadow machinery** — hyperbolic C*-equivariant reductions with exact
  Jacobian bookkeeping (`det J_φ = −Ph²·det DF`).

## 2. Phases

* **Phase 1 (active): vet Moskowicz** — read the preprint, formalize its core
  argument, machine-check what is checkable, adversarial GPT review. Outcome
  either "vetted: `d` composite, minimal case `d=4`" (landscape shift) or a
  documented gap (also valuable).
* **Phase 2: the `d = 4` plane case** — assuming Phase 1 or independently:
  a degree-4 plane counterexample has monodromy in `S_4`; `S_4` has a normal
  `V_4` — imprimitivity analysis may force a quadratic subfield, and
  quadratic ⟹ Galois ⟹ dead. If that argument closes, `d = 4` is impossible
  and (with Moskowicz) the minimal case jumps to `d = 6`. **This is our
  sharpest original idea entering the campaign.**
* **Phase 3: valuation attack on plane pairs** — port the row-valuation
  technique to `{P,Q} = 1` directly; hunt for forced factorizations.
* **Phase 4: collapse-theoretic reformulations** — classify which towers
  collapse; seek a reformulation of the plane problem as a collapse
  obstruction.
* **Phase ∞: iterate.** Every phase ends with an adversarial review round
  and a commit, win or lose.

## Round-12 intelligence (2026-07-24, GPT strategy triage)

* **Phase 1 CLOSED — Moskowicz rejected.** The preprint's hinge ("rare
  property ⟹ degree 2") cites a MathOverflow answer that constructs one
  example, not a classification: the main theorem is unproven. Salvage: the
  `xy ∈ K` case is repairable, and the monomial lemma survives conditionally.
  **However the minimal open plane degree is 4 anyway**, on solid published
  ground: degree 2 is Galois (dead) and **Orevkov proved degree-3 plane
  Keller maps impossible**. So: `d = 4` is the true minimal battlefield.
* **Phase 2 verdict:** the fixed-point-free-involution argument is CORRECT
  for genuine finite étale quadratic factors (linearization of finite-order
  plane automorphisms). The intermediate field only gives a rational map a
  priori; the sharp reformulated target is a **boundary-completion problem**:
  *can a smooth surface with a free involution contain an open `A²` meeting
  every orbit?* Log-surface / dual-graph methods apply. Highest EV.
* **Phase 4 upgrade:** a July-23 preprint (arXiv:2607.20210) proves a
  hyperbolic quotient-collapse formula (matching our shadow principle) and
  claims all graded plane Keller maps are automorphisms (matching our
  round-3 rigidity theorem). To vet; then the strategic question: *can every
  hypothetical plane counterexample be degenerated to a graded pair without
  losing the missing-sheet data?* If yes, the plane case closes.
* **The synthesis program (new master plan):**
  1. extract the 3D counterexample's boundary configuration (missing
     divisors, inertia, dual graph);
  2. prove 2D non-realizability of that configuration (curves at infinity
     have Riemann–Hurwitz constraints unavailable in 3D);
  3. classify degree-4 boundary monodromy configurations
     (`V₄, D₄, C₄, A₄, S₄`) — finite, machine-enumerable;
  4. valuation row-counting on inertia matrices (our technique, aimed at
     the boundary rather than the affine plane).

## Session 2 intelligence (2026-07-24)

* **Minimal-degree correction (literature).** The Vitushkin–Orevkov exotic-
  covering program: Orevkov excluded 3-sheeted plane Keller maps;
  Domrina–Orevkov (1998, irreducible ramification curve) + Domrina (1999,
  general case) are reported to treat the 4-sheeted case — *to be confirmed
  by direct reading*. Five-sheeted exotic coverings EXIST (Vitushkin;
  Orevkov's analytic realization; Egorov's extension), so the topological
  obstruction method saturates at 5 sheets. Working assumption pending
  verification: **minimal open plane degree = 5**. Since 5 is prime, the
  extension has NO intermediate fields — the imprimitivity/free-involution
  attack (Phase 2) is void at d = 5. New sharp Phase-2': the monodromy is a
  transitive subgroup of S₅ (C₅, D₅, F₂₀, A₅, S₅); C₅ ⟹ Galois ⟹ dead;
  **can solvable monodromy (D₅, F₂₀) be excluded** via the Galois closure?
  Then only A₅/S₅ remain.
* **Synthesis step 1 DONE — the 3D boundary data card**
  (`src/monodromy3d.py`, machine-measured by numeric continuation):
  - branch divisor `{A=0}`: local monodromy = **transposition** (all four
    crossings of a generic line measured);
  - different crossings give different transpositions; together they
    generate the **full S₃** (non-Galois, as theory requires);
  - the colliding pair escapes to `x = ∞` with the **square-root law**
    `|x| ~ ε^{-1/2}` (measured exponent −0.496);
  - over the triple-root curve `Z`: all three sheets escape (empty fibers).
  This is the configuration whose 2D non-realizability is synthesis step 2:
  the boundary of any completion of `A²` is a *tree* of rational curves, and
  the question is whether transposition-wrapping escape can live there.

## Session 3: the degree-5 monodromy reduction (2026-07-24)

**New literature anchor.** Nguyen Van Chau (Acta Math. Vietnamica 24, 1999):
a plane Keller map whose *exceptional value set* is homeomorphic to `C` must
be bijective (engine: the Lins–Zaidenberg theorem on simply-connected plane
curves). So the minimal Vitushkin-type boundary configuration is impossible
polynomially — the exceptional curve of any counterexample must be
topologically nontrivial. This is the direct 2D counterpart of our 3D
boundary data card.

**The monodromy fork at degree 5.** If the minimal open degree is 5 (pending
Domrina–Orevkov scope confirmation), the Galois closure `N` of `L/K` has
group `G` a transitive subgroup of `S₅` — exactly one of:

| `G` | order | status |
|---|---|---|
| `C₅` | 5 | **dead**: `L = N` Galois ⟹ automorphism (Galois-case theorem) |
| `D₅` | 10 | target: `E = N^{C₅}`, `E/K` quadratic Galois; `N/E` **cyclic** ⟹ Kummer `N = E(u^{1/5})`; note `D₅ ⊂ A₅` ⟹ discriminant is a square |
| `F₂₀` | 20 | target: `E/K` cyclic quartic; `N/E` cyclic ⟹ Kummer |
| `A₅` | 60 | unsolvable remainder |
| `S₅` | 120 | unsolvable remainder |

**The Kummer attack (Phase 2'').** In the solvable cases the geometry is a
tower `A² ← Y_E ← X_N` with `Y_E` an abelian cover branched only over the
exceptional curve and `X_N → Y_E` a *cyclic quintic* cover (`z⁵ = s`) — far
more rigid than a general quintic. Program: étaleness off `E_f` +
Riemann–Hurwitz + Chau/Lins–Zaidenberg topology of `E_f` against the
`z⁵ = s` structure. If `D₅` and `F₂₀` fall, the plane conjecture at degree 5
reduces to **unsolvable monodromy only** (`A₅`/`S₅`).

## Session 3 outcome: the audit, and a new counterexample family (2026-07-24)

* **Minimal open degree = 5, now peer-reviewed-solid.** Round-13 scope check:
  Orevkov excludes degrees 2–3; Domrina–Orevkov 1998 (one-dicritical case) +
  **Domrina, Izvestiya Math. 64 (2000), 1–33 (the full general proof)**
  exclude degree 4 unconditionally. The 1999 Math Notes item was the
  announcement.
* **Moskowicz audit COMPLETE — the prime-degree theorem is unproven.** The
  hinge ("Answer 2.21") is Laurent Moret-Bailly's MO answer, which we read
  directly: it *constructs an index-2 example* of a rare-property subfield;
  it does **not** prove "rare property ⟹ index ≤ 2". Degree 5 is alive.
* **Our new contribution — the classification is false as field theory.**
  The family `R = C((2x−y)^p, y−x)` has the rare property with index `p` for
  **every prime `p`** (proof: σ: s ↦ ζ_p s moves every monomial
  `(s+v)^i(s+2v)^j` — irreducible-factor multiset comparison in the UFD;
  machine-checked for `p = 3, 5`, all `i, j ≤ 6`). So no pure-field-theory
  rescue of the prime-degree exclusion is possible. **But**: our examples
  have `u = w^p`, violating **root closure** — which Keller subrings enjoy
  (Jędrzejewicz–Zieliński). The crisp open lemma that would kill degree 5
  (and all primes):

  > **Root-closed rare-property lemma (open).** If `R = k(u,v) ⊂ k(x,y)`
  > has the rare property and `k[u,v]` is root-closed (+ square-factorially
  > closed) in `k[x,y]`, must `[k(x,y):R] ≤ 2`?

* **Kummer geometry corrected (round 13):** escape exponents along a
  boundary divisor are `p/e` (valuation over transverse inertia) — our 3D
  square-root law is the case `e = 2, p = 1`; "5-sheeted dicritical" does
  not by itself force fifth-root behavior (horizontal degree ≠ transverse
  inertia; `D₅` allows double-transposition inertia, `F₂₀` order-4 inertia).
  The Kummer attack's sticking point: control of `div(s)` in
  `Cl(Y_E)/5Cl(Y_E)` plus the valuations of `x, y` along boundary divisors —
  exactly where our valuation row-counting should be aimed.
* **arXiv:2607.20210 (Shaska) vetted: sound on first read.** Its
  positive-weight theorem (all dimensions) complements our plane rigidity
  theorem (all weights, char 0); its quotient formula is our shadow identity
  up to sign conventions. Corroboration, not contradiction.

## Session 4: the degree-5 escape ledger and the omitted-points theorem (2026-07-24)

All group theory and bookkeeping machine-verified in
[`src/n2/degree5_ledger.py`](../src/n2/degree5_ledger.py). Setup: `f` a
hypothetical degree-5 plane Keller counterexample, `E` its exceptional
(Jelonek) curve, `Ẽ = f⁻¹(E)`, monodromy `G ⊆ S₅` transitive.

* **Lemma A (nonempty affine preimage).** `f` is a genuine degree-`d`
  covering off `E`, so `χ(Ẽ) = dχ(E) − (d−1)`. Empty `Ẽ` would force
  `χ(E) = (d−1)/d ∉ ℤ`. Hence **`f⁻¹(E) ≠ ∅` always** (any `d ≥ 2`).
* **Lemma B (sheet-fix bound).** An affine sheet crossing a component `C`
  of `E` extends `f⁻¹` to a single-valued branch near `C` (étaleness), so
  it is fixed by the meridian monodromy `σ_C`: **`d_C ≤ Fix(σ_C)`**
  (`d_C` = generic affine fiber count over `C`). Calibrated on the 3D map:
  transposition ⟹ exactly 1 affine sheet over `{A=0}` ✓ (measured).
* **Theorem C (section principle).** Meridians generate plane-curve-
  complement `π₁`, so the meridian classes must normally generate `G`.
  Verified class data for the five transitive subgroups gives the ledger:

  | `G` | classes (cycle type, Fix, normally generates) | max `d_C` |
  |---|---|---|
  | `D₅` | (2,2) Fix 1 **gen**; (5) Fix 0 | **1** |
  | `F₂₀` | (4) Fix 1 **gen**; (2,2) Fix 1; (5) Fix 0 | **1** |
  | `A₅` | (3) Fix 2; (2,2) Fix 1; (5) Fix 0 — all gen | 2 |
  | `S₅` | (2) Fix 3 **gen**; (4) Fix 1 **gen**; (2,3) Fix 0 **gen**; … | 3 |

  So in the solvable cases every nontrivial-meridian component of `E`
  keeps **at most one affine sheet** (a section or nothing); `D₅` forces a
  reflection-meridian component, `F₂₀` a 4-cycle one; 5-cycle components
  are generically **outside the image** (the 2D analogue of the missing
  curve `Z` in dimension 3).
* **Theorem D (omitted-points theorem — the session's main new result).**
  If `E` is **irreducible** and `G ∈ {D₅, F₂₀}`: the single meridian class
  must normally generate, so `Fix = 1` is forced; with Lemma A and
  quasi-finiteness, `d_E = 1` exactly and `Ẽ` is irreducible, an open
  immersion on normalizations (`Ẽ^ν = C ∖ B`). Euler bookkeeping with
  `χ(E) = 1 − s` (`s ≥ 1` by Chau's singularity theorem) and
  `χ(Ẽ) = 1 − β′ − s̃` (`s̃ ≤ s`) closes exactly:

  > **`β′ = 5s − s̃`, so `4s ≤ β′ ≤ 5s`: the image of `f` must omit at
  > least FOUR isolated points on `E`** — over each, even the surviving
  > section sheet escapes to infinity.

  **Round-14 audit upgrades (GPT-5.6-sol, confirmed):** the
  *branch-packet lemma* — a point of `Ẽ` over `y ∈ E` reproduces ALL
  `r_y` local branches via the ambient biholomorphism, and the open
  immersion allows at most one such point, so over each `y` the
  normalization points are all punctures or all retained. The bookkeeping
  then closes exactly: **`|E ∖ f(C²)| = 4s`** omitted points.
  Attributions fixed: Chau = "A Remark on
  Vitushkin's Covering" (irreducible case suffices for `s ≥ 1`);
  `E^ν ≅ A¹` via Jelonek's parametric-curve theorem + ZMT; Peretz
  (Israel J. Math. 109, 1999): plane Keller images are cofinite, so
  isolated omissions are exactly the permitted type.

* **The Hartogs section lemma (round-15 audited SOUND — the session's
  main new weapon).** If `q` is a *smooth* point of `E` and the affine
  preimage contains a section over a punctured `E`-neighborhood of `q`,
  then the section's sheet is monodromy-fixed, so it lies in a
  *degree-one* component `V₁` of the covering over `B_ε ∖ E` (a
  connected covering whose monodromy has a fixed point has degree 1);
  `U₁ = V₁ ∪ section` maps bijectively-étale, hence biholomorphically,
  onto `B_ε ∖ {q}`; the inverse extends across `q` by Hartogs/Riemann
  extension (dimension 2, no boundedness needed), forcing
  `f(g̃(q)) = q`. **Sections cannot escape at smooth points of `E`**;
  corollary: the affine fiber count is locally constant on the smooth
  locus of `E`. (Literature: not located as a published statement; a
  close claim — smooth Jelonek set ⟹ surjectivity — appears only in a
  *withdrawn* Jelonek preprint, arXiv:2011.03472, with recorded errors.)
  **Sharpness, machine-verified:** for Alpoge's 3D map,
  `Sing({A=0}) = Z` *exactly* (elimination gives `(3bc−4)² = 0`) — the
  3D omitted curve escapes precisely through the singular locus of the
  exceptional divisor, just outside the lemma's hypothesis.

* **Theorem E (CONDITIONAL — the round-15 cusp gap).** The intended
  contradiction (`4s` omitted points vs "at most `s` singular") FAILS:
  unibranch singularities (cusps, `r = 1`) contribute `0` to `s`, so all
  `4s` omitted points could a priori hide at cusps, whose local
  complements have knot groups (not `Z`), where the fixed-sheet argument
  breaks. The gap is *narrowed* by verified group theory: the local
  monodromy image at a unibranch point is normally generated by a
  meridian-class element inside itself — for `D₅` the options are
  `{C₂, D₅}`, for `F₂₀` they are `{C₄, F₂₀}` (machine-enumerated). In
  the abelian cases the Hartogs kill still runs; so **escape at a cusp
  requires FULL nonabelian local monodromy — for `D₅` a 5-colorable
  cusp knot (`det ≡ 0 mod 5`, Fox); the ordinary cusp `(2,3)` has
  `det 3` and is killed.** Conditional Theorem E: a `D₅/F₂₀`
  counterexample with irreducible `E` must channel all `4s` omitted
  points through such special cusps; if `E` has none, only `A₅/S₅`
  remain (`C₅` dead by the Galois case). **Closing the cusp case is the
  new sharpest local target.**
* **Caveats kept honest:** (i) reducible `E` allows "silent components"
  (trivial meridian, only `d_C ≤ 4`) — the ledger constrains but does not
  yet close them; (ii) Chau `s ≥ 1` is used as the round-13-confirmed
  statement that exceptional components cannot be `≅ C`; (iii) `A₅/S₅`
  ledgers are strictly looser — the solvable cases remain the right first
  target.

## Session 5: the double-cover tower and the cusp census (2026-07-24)

Machine parts in [`src/n2/degree5_ledger.py`](../src/n2/degree5_ledger.py)
(`cusp_capability`); round-16 adversarial audit passed with upgrades.

* **The tower theorem (necessary condition, audited).** For `G = D₅`:
  the inertia over `E` is a reflection (order 2), so on the double cover
  `W = {w² = δ_E}` of the target the meridian pushes to `μ² ↦ r² = 1`:
  the `C₅`-cover `X_N → W` is **unramified in codimension 1**. Hence
  `D₅` monodromy ⟹ `H₁(W_sm; Z/5) ≠ 0` in the `(−1)`-eigenspace of the
  deck involution — global Fox 5-coloring data. `F₂₀` analogue via the
  quartic cyclic cover; local criterion (necessary AND sufficient,
  Boden–Friedl): `Δ_K(α) ≡ 0 mod 5` with `α² = −1`, i.e.
  `5 | |Δ_K(i)|²`.
* **The cusp census (audited, with closed formulas).**
  `det T(m,n) = 1` (both odd) / `n` (`m` even) / `m` (`n` even);
  cabling: `Δ_cab(t) = Δ_{T(p,q)}(t)·Δ_K(t^p)`. Consequences:
  odd–odd cusps never host `D₅`; **minimal `D₅` cusp = `(2,5)` (A₄,
  `δ = 2`); minimal `F₂₀` cusp = `(4,5)` (`δ = 6`)** — minimal among
  ALL plane branches (two-Puiseux-pair germs already have `δ ≥ 8`).
  Subtlety: a `p ≡ 2 mod 4` cabling stage can convert inner
  `D₅`-capability into `F₂₀`-capability.
* **δ-budget bounds (new).** The surviving configuration needs `4s`
  capable cusps + `s` multibranch points: `Σδ_aff ≥ 9s` for `D₅`
  (degree of `E` ≥ 6 when `s = 1`), `Σδ_aff ≥ 25s` for `F₂₀`
  (degree ≥ 9).
* **Longitude theorem (audited).** A knot longitude lies in the
  commutator subgroup and commutes with the meridian; in `D₅` (and
  `F₂₀`) `C(μ-image) ∩ [G,G] = 1`, so **every full Frobenius-image
  representation kills the longitude**: `ρ(λ) = 1`. For torus cusps
  this re-derives the odd–odd exclusion (no new kill; deprioritized).
* **Multibranch matching equations (new weapon).** At a retained
  multibranch point, branches with intersection multiplicity `I`
  satisfy `2I(c₁ − c₂) ≡ 0 mod 5`: a **node forces equal colors**;
  distinct colors need `5 | I`. Every multibranch point imposes linear
  matching conditions on the global 5-coloring eigenspace.
* **Near-model warning (round 16).** `D₁₀`-special irreducible sextics
  with `4A₄ + 2A₁` exist (Akyol–Degtyarev geography): four `(2,5)`
  cusps in special position DO support global dihedral 5-coloring.
  Not the exact model (two nodes ⟹ `s = 2` would demand eight cusps;
  one-place-at-infinity fails), but it shows **topology alone is
  unlikely to close the gap** — Keller-specific input is the missing
  ingredient.
* **Ranked plan (round 16):** (1) modular (`F₅`) Libgober/Fitting +
  Abhyankar–Moh semigroup enumeration under the δ-budgets; (2)
  multibranch matching equations; (3) model search from the
  `4A₄ + 2A₁` sextic family; (4) **Keller dicritical data** — pole
  orders along the unique dicritical divisor determine the infinity
  semigroup and may beat abstract one-place rationality.

### Round 17 (same session): section lemma audited, source-side `H₁ = Z`, literature corrections

* **Monochromatic section lemma (retained, corrected form):** *the
  section reduces the peripheral monodromy over the smooth locus of `E`
  to the point stabilizer* (`⟨r₀⟩` for `D₅`, `C₄` for `F₂₀` — the
  latter needs an orientation/continuity supplement). Consequences: all
  branch colors at multibranch points coincide (round-16 matching
  equations auto-satisfied — that weapon dies); the `C₅`-datum `φ`
  vanishes near the ramification curve (simpler proof: `τ` fixes `R`
  pointwise, anti-invariance gives `2φ = 0 = φ` over `Z/5`). No prior
  name found; related to Tokunaga's splitting-curve formalism.
* **Source-side constraint (strong, global):** the Keller map itself is
  the 5-fold irregular dihedral cover attached to `(ρ, φ)`, and
  `H₁(C² ∖ Ẽ) = Z` (irreducible curve complement, total linking
  number). No per-cusp decomposition exists (Fox matrix has global
  braid/infinity relations) — exploiting it needs a Zariski–van Kampen
  presentation. Control experiment available: Degtyarev's `4A₄+2A₁`
  sextic has complement group of order **960** (metabelian quotient
  `D₁₀ × C₃`).
* **Literature corrections (important):** Orevkov's analytic
  realization of the Vitushkin covering is **3-sheeted** (monodromy
  `S₃`); the 5-sheeted exotic cover is **Egorov 2002, topological,
  simple-branched ⟹ monodromy necessarily `S₅`**. So no analytic
  `D₅/F₂₀` exotic 5-cover is known — and no theorem forbids one: the
  solvable degree-5 case is genuinely open territory, not neutralized
  by known examples.
* **Generic-line Hurwitz (verified twice, independently):** with
  `d = deg E`: `D₅` gives `g(f⁻¹(L)) = d−4 / d−2 / d−3` (by
  `σ_∞ = 1` / 5-cycle / reflection) with `2d+5 / 2d+1 / 2d+3` places
  at infinity; `F₂₀` table analogous; only nonnegativity bounds
  (`d ≥ 4`-ish) — no contradiction from one line. Caveat: only the
  PARITY of the finite-meridian product survives basing-path changes.
* **Ranked next moves (round 17):** (1) global Reidemeister–Schreier /
  Fox computation imposing `H₁ = Z`; (2) **pencil bookkeeping** — the
  motion of the escaping places must factor through the dicritical
  covers `D_i → E`, `Σk_i = 4` (much more rigid than one line); (3)
  **encode the section constraint into the Fox matrix** — best chance
  for a genuinely new lemma; (4) the sextic control experiment; (5)
  valuation equations on the dicritical resolution (where Keller enters
  beyond topology).

## Session 6: prediction-driven mode (2026-07-24)

Registered predictions (each is a falsifiable bet with a concrete test;
adjudicate honestly, win or lose):

| # | prediction | confidence | test |
|---|---|---|---|
| P1 | the `s=1` `D₅` configuration (4 `(2,5)`-cusps + 1 multibranch pt on a rational one-place curve) cannot satisfy the global collapse `H₁ = Z` | 0.60 | ZvK/Fox computation with section constraint |
| P2 | escaping-sheet μ-orbits force the dicritical transverse profile: `D₅` ⟹ two boundary points over a generic `y ∈ E`, each of transverse multiplicity 2 (`Σk_i = 2`); `F₂₀` ⟹ ONE boundary point of multiplicity 4 on a single dicritical **birational onto E** | 0.85 | local-model proof + round-18 audit |
| P3 | the `4A₄+2A₁` sextic's 5-fold irregular cover has `H₁ ≠ Z` (control: even known special position fails the source constraint) | 0.50 | Degtyarev presentation + RS computation (subagent) — **ADJUDICATED: WIN (literal), with caveat.** `π₁(P²∖B)` has order 960 (derived series matches Degtyarev Thm 1.2.1 4-for-4); the unique `D₁₀`-epimorphism gives index-5 `H` of order 192 with **`H₁(H) = Z/2⊕Z/2⊕Z/6 ≠ Z`** (disk-filled: `Z/2⊕Z/2`). Caveat: `π` finite ⟹ rank 0 automatic — confirms the literal prediction but does not probe the collapse mechanism; the affine group is a TODO. Full write-up: [`work_sextic_control.md`](work_sextic_control.md). |
| P4 | the `F₂₀` case dies on δ-budget + Bézout + Abhyankar–Moh semigroup arithmetic alone at all degrees | 0.40 | feasibility enumeration `d ≤ 16` (subagent) — **ADJUDICATED: LOSS.** `d = 5..8` rigorously impossible, but `d ≥ 9` passes every arithmetic test (budget and the conic-through-5-points Bézout bound tie exactly at 9). Salvage: **`deg E ≥ 9` (`F₂₀`) and `deg E ≥ 6` (`D₅`)** are now clean bounds; bonus lemma: `deg g = deg f − 1` makes the point at infinity smooth (`δ_∞ = 0`). Full write-up: [`work_f20_feasibility.md`](work_f20_feasibility.md). The sieve ignores the dicritical/Keller structure — necessary conditions only. |

**P2 derivation (to audit).** Over generic `y ∈ E` the 4 escaping
sheets spiral into boundary points `p` of the resolved source
`X̄ → P²`, lying on dicritical divisors over `E`; the local monodromy
cycle containing the sheets escaping to one point `p` has length
`e_p` = the transverse multiplicity of `f̄` at `p`. The μ-escape cycle
type is `(2,2)` for `D₅` (reflection) and `(4)` for `F₂₀` (4-cycle),
hence `{e_p} = {2,2}` resp. `{4}`: for `D₅` exactly two boundary
points over `y` (dicritical degree profile `{1,1}` or `{2}`); for
`F₂₀` exactly one — **a single dicritical divisor mapping birationally
onto `E` with constant transverse multiplicity 4**. Correction of the
earlier bookkeeping `Σk_i = 4`: the sheet count is `Σ_p e_p = 4`, so
`Σ_i k_i` (covering degrees) is `2` (`D₅`) resp. `1` (`F₂₀`).

### Round-18 adjudication: P2 WON, and strengthened

* **Dicritical profile theorem (audited).** Correct identity
  `Σᵢ kᵢeᵢ = 4` (`5 = 1 + Σkᵢeᵢ`, degree conservation). `D₅`: all
  escape clusters have `e = 2`, `Σk = 2`; `F₂₀`: a **single dicritical
  with `(k,e) = (1,4)` — it IS the normalization `P¹ → Ē`** (at a
  `(4,5)`-cusp it restricts to `t ↦ (t⁴+…, t⁵+…)`, the normalization,
  not an immersion). Vertical components affect only special fibers.
* **`D₅` profile forced to `(1,2) + (1,2)`.** The peripheral image
  lies in `⟨r₀⟩` (monochromatic lemma), which preserves each 2-cycle
  of `r₀` separately, so the monodromy on the two boundary clusters is
  trivial; an irreducible `k = 2` dicritical would give a connected
  double cover of `E_sm` — contradiction. Hence **two distinct
  dicriticals, each birational onto `Ē`, each with `e = 2`.**
* **Keller valuation identity (audited):**
  `a(Dᵢ) := ord_{Dᵢ}(du∧dv) = eᵢ − 1` — the codimension-1
  ramification formula fused with the Keller form equality. `D₅`
  dicriticals: `a = 1`; the `F₂₀` dicritical: `a = 3`.
  Favre–Jonsson dictionary: thinness `A(ν_D) = (a(D)+1)/b_D`;
  blowup recurrences `a ↦ a+1` (free) / `a₁+a₂+1` (satellite).
  Thinness alone cannot characterize dicritical-onto-curve divisors —
  deprioritized as a kill route.
* **The missing incidence datum (next target):** at an omitted cusp
  `q`, where does the closure of the SECTION sheet land — the same
  boundary point `p ∈ D₁` over `q`, another point of `D₁`, or a
  vertical component over `q`? Determining this closes the local jet
  and divisor equations at `F₂₀` cusps (`det Df̄ = u³·unit` or
  `u³t^{a(V)}·unit`). The `D₅` boundary tree needs decorated pullback
  divisors (`E`, target `L_∞`, generic line) with the projection
  formula — connectivity alone does not kill.

### The decorated-tree equation system (session-6 framework)

On the SNC completion `X̄ ⊃ C²` (boundary = tree of rational curves)
with resolved `f̄: X̄ → P²`, the counterexample data must satisfy the
closed system:

1. **Canonical decoration:** `K_{X̄} = Σ_D a(D)·D` over boundary
   components only (`div(du∧dv)`; the affine part is étale, so the
   ramification divisor is purely at the boundary). Adjunction then
   fixes every self-intersection: `D² = −2 − Σ_{D′} a(D′)(D′·D)`.
2. **Principal-divisor equations:** `div(z∘f̄) = Ẽ̄ + e·ΣDᵢ + Σm_V V`
   (`z` = defining equation of `E`) has zero intersection with EVERY
   complete curve: one linear equation per boundary component; the
   coefficients `Ẽ̄·D` encode exactly the section-end incidences.
3. **Form equation:** `Σ a(D)·D = −3·f̄*(L_∞) + R`, `R ≥ 0` boundary-
   supported; on dicriticals (`m_{L_∞} = 0`) it returns `a = e−1`; on
   components over the target `L_∞` it gives `a(D) = −3m_D + r_D`.
4. **Group-theoretic decorations:** two `a = 1` dicriticals birational
   onto `Ē` (`D₅`) resp. one `a = 3` normalization dicritical (`F₂₀`);
   `4s` cusp packets; blowup recurrences `a ↦ a+1 / a₁+a₂+1` along the
   tree.

The counterexample's boundary is a finite decorated tree satisfying
1–4: a machine-enumerable satisfiability problem (with the caveat that
tree size is unbounded a priori — a kill must come from equations that
close globally, e.g. summed intersection identities, not exhaustion).

### Round 19: the Lê–Weber fusion (session 6)

* **Every infinity-type pencil dicritical has `a(D) = −m−1 < 0`**
  (`dP∧dQ = (mp′q + O(u))u^{−m−1}du∧dt`; matches the form equation
  with `r_D = 2m−1`). All of them are negative-`a` Lê–Weber targets.
* **Survival forces complete splitting:** `n_D > 1` ⟹ ramification ⟹
  critical point ⟹ strongly non-equisingular + `a < 0` ⟹ LW kill.
  So every coordinate pencil of the counterexample must have its
  residual infinity part split into **`N_∞ ∈ {1,3,5}` degree-one,
  isolated (length-1 bamboo) dicriticals.** The `E`-dicriticals have
  restriction degree `k_i·d` (`= d ≥ 6/9`), are automatically
  ramified/strongly non-equisingular, but evade LW (positive `a`,
  degree > 1).
* **`λ(P) = 4d − 4`** (Suzuki–Gavrilov; the affine part is
  critical-point-free so the whole defect sits at infinity). Sharpened
  adjunction: `D² = (−2 − Σ_{C≠D} a(C)(C·D))/(a(D)+1)` — integrality
  congruences with denominators 2 (`D₅`) / 4 (`F₂₀`).
* **Section incidence deferred** (round-19 correction: `H(0,0) = 0`
  does not force a vertical component — the extra branch can be `Ẽ̄`
  itself; principal-divisor equations alone cannot sign `Ẽ̄·D_i`).
* **λ-budget decomposition (session-6 closing computation, TO AUDIT):**
  per-special-value jumps: simple tangent line `λ_c = 4`; omitted-cusp
  line `λ_c = 3`; node line `λ_c = 4`. Ramification budget of
  `x|_{E^ν}`: `d − 1` total, each `(2,5)`-cusp eats 1 (multiplicity),
  nodes eat 0, so `T = d−1−4s` simple tangencies. Summing:
  `4d−4 = 4T + 12s + 4n_mb + λ_∞` ⟹ **`λ_∞ = 4s − 4n_mb`**; with all
  multibranch points nodes (`n_mb = s`): `λ_∞ = 0` — the budget closes
  EXACTLY. No contradiction, but the rigidity is now extreme: no
  atypical value at infinity, all tangencies simple, completely split
  degree-one infinity dicriticals. **New sharpest question (round-19
  rank 1): can a degree-one, length-one infinity dicritical occur for
  a nontrivial Keller pair at all?** (It does for the identity map;
  the question is whether it coexists with `E`-dicriticals.)

### Round 23: the frontier — the degree-5 solvable case reduces to two named open lemmas

Three kill-routes examined (node, Fix=0, degree upper bound); verdict: **none
closes the case now**, but the residual gap is now two *precise* statements.

* **Clean new fact:** `Fix(σ_E) = 0 ⟹ f⁻¹(E) = ∅` **exactly** (not just
  generically): a Keller map is étale hence open, so `f(C²) ∩ E` is Zariski
  open in the irreducible `E`; generic omission forces total omission. So the
  `Fix=0` cases (`A₅` 5-cycle, `S₅` `(2,3)`) have **no section anywhere** —
  `E` is entirely omitted, the direct 2D analogue of Alpoge's missing curve
  `Z`. Chau forces `E` to have a self-intersection (its normalization `A¹`
  can't inject), but does **not** kill it.
* **The node (Fix=1) is locally consistent:** exactly one finite point over
  the node (`#f⁻¹(q₀)=1`, else `d_E≥2`); `f⁻¹(E)` has the same nodal germ
  (étale base change). **Nothing forces `s ≥ 2`** — the parametrization
  `t ↦ (t²−1, t³−t)` gives a rational one-place curve with exactly one node,
  so the `F₂₀` `d≥46` (`s=2`) window is not reachable this way.
* **No degree upper bound:** `deg E < max(deg P, deg Q)` (Jelonek Thm 15),
  and the algebraic degrees are uncontrolled; geometric degree 5 and the
  dicritical count do not bound `deg E`. So the log-BMY *lower* bound has no
  *upper* partner — no pincer.

* **THE REDUCTION (the campaign's current headline).** A degree-5 plane
  Keller counterexample with irreducible `E` is excluded **if either** of
  these open lemmas holds:
  > **(L1)** An irreducible Keller Jelonek curve is **unibranch** (no
  > self-intersection). — Then Chau (`E` not `≅ C`) forces a cusp-only `E`,
  > and Koras–Palka's "≤ 4 cusps, the unique `A₆+3A₂` quintic" **kills every
  > `D₅`/`F₂₀` config** (verified: our cusp types/degrees never match).
  >
  > **(L2)** An étale polynomial map `A²→A²` cannot **totally omit** an
  > irreducible divisorial component of its nonproperness set. — Then the
  > `Fix=0` cases die outright.
  Jelonek's 2020 preprint attempted a statement near (L1) — **withdrawn with
  recorded errors** (arXiv:2011.03472) — so (L1) is genuinely hard/open.
  These two lemmas are the exact residual gap between our structural
  encirclement and a full proof of the degree-5 solvable case.

### Rounds 21–22: the rational-cuspidal / log-BMY front (session 7, verified + one over-claim corrected)

The Jelonek curve `E` is rational with one place at infinity; in the
`Fix=1` cases it has `4s` omitted capable cusps (`(2,5)` for `D₅`,
`(4,5)` for `F₂₀`) and, by Chau, a mandatory multibranch point (`s ≥ 1`).
So `Ē` is an irreducible **rational plane curve with cusps AND a node**.

* **Mixed log-BMY (Orevkov–Zaidenberg), verified.** For an irreducible
  rational plane curve of degree `d` with branch excess `s`:
  `Σ_p M̄ᵖ ≤ 3d − 4 + 2s`, summed over ALL singular points (including at
  infinity), where the **original Orevkov invariant** of a one-Puiseux
  cusp is `M̄ᴼ(m,q) = m + q − m/q − q/m − 1` (so `M̄ᴼ(2,5)=31/10`,
  `M̄ᴼ(4,5)=119/20`, node `= 1`). Calibrated against known curves
  (cuspidal cubic, 3-cuspidal quartic, `A₆+3A₂` quintic — all pass with
  slack).
* **F₂₀, d=9, s=1 is EXCLUDED** (rigorous): four `(4,5)`-cusps
  (`119/5`) + remaining `δ=4` at branch-excess 1 (min `M̄ᴼ = 4`, e.g.
  an `A₇` tacnodal point) `= 27.8 > 25`.
* **Dramatic new degree lower bounds** (corrected computation, optimizing
  the leftover `δ` into one balanced big cusp — the efficient packing):

  | | `s=1` | `s=2` | `s=3` |
  |---|---|---|---|
  | `F₂₀` survives from | `d ≥ 21` | `d ≥ 46` | `d ≳ 70` |
  | `D₅` survives from | `d = 6` | `d ≥ 22` | `d ≥ 39` |

  (Up from the P4 bounds `d≥9`/`d≥6`.) The forced-contribution sieve
  `F₂₀: Σ M̄ ≥ (124/5)s`, `D₅: Σ M̄ ≥ (67/5)s` gives the clean rigorous
  exclusion `(124/5)s > 3d−4+2s` resp. `(67/5)s > …`.
* **Koras–Palka (2019), the crux.** A complex plane curve *homeomorphic
  to a line* (purely unibranch, no node) has **≤ 4 singular points**;
  exactly 4 ⟹ degree 5, the unique `A₆+3A₂` quintic. **If `E` had no
  node this is a DIRECT KILL** of every `D₅`/`F₂₀` config. The mandatory
  node (multibranch ⟹ not homeomorphic to a line) is the *single feature*
  that puts `E` outside Koras–Palka, Palka's 6-cusp, Tono's 8-cusp, and
  the whole semigroup-distribution / Heegaard–Floer machinery — all
  literally restricted to the no-node case. **No published bound covering
  the cusp+node case was found** (a genuine literature gap).
* **Over-claim corrected (adversarial verification did its job).** My
  intermediate claim "the whole `F₂₀` branch falls / reduces to a single
  sextic" was **wrong**: `s` counts branch excess, not `δ`, so the
  leftover `δ` can sit in one *efficient* big cusp (`M̄/δ → 0`), and
  high-degree packages pass (explicit: `s=1, d=27`, four `(4,5)`-cusps +
  node + one `(25,26)`-cusp, `Σ M̄ ≈ 72.8 < 79`). log-BMY is a strong
  degree-window sieve, **not** a full kill.
* **Strategic pointer:** the node is **load-bearing**. The kill routes
  are now (i) an upper bound on `d` (to pincer against the growing
  log-BMY lower bound), or (ii) a rigidity theorem that tolerates one
  node, or (iii) showing the Keller/monodromy structure forces the node
  away or forces `s` large (log-BMY then bites hard).

### The degree-5 reduction theorem (session 7, workflow + verified) — the whole battlefield on one page

For a hypothetical degree-5 plane Keller counterexample with **irreducible**
Jelonek curve `E`, the meridian of `E` is a single conjugacy class that must
**normally generate** the monodromy `G` (section principle). Classifying by
that class (all data machine-verified, `src/n2/a5s5_ledger.py` + independent
recheck) organizes the ENTIRE problem:

| `G` | normally-generating meridian classes | `Fix = d_E` | status |
|---|---|---|---|
| `C₅` | 5-cycle | 0 | **dead** (Galois ⟹ automorphism) |
| `D₅` | reflection `(2,2)` | **1** | cusp collapse: `\|E∖f\|=4s`, `(2,5)`-cusps |
| `F₂₀` | 4-cycle | **1** | cusp collapse: `\|E∖f\|=4s`, `(4,5)`-cusps |
| `A₅` | `(2,2)` | **1** | **cusp collapse VERBATIM** (census open — `A₅` perfect) |
| `A₅` | 3-cycle | 2 | NEW: two degree-1 Hartogs-protected sections |
| `A₅` | 5-cycle | 0 | NEW: `E` generically OUTSIDE the image |
| `S₅` | 4-cycle | **1** | **cusp collapse VERBATIM** |
| `S₅` | transposition | 3 | NEW: three degree-1 sections |
| `S₅` | `(2,3)` | 0 | NEW: `E` generically outside the image |

* **Universal Hartogs mechanism (the session's structural win).** The
  cusp-collapse derivation (`theorem_D`: unique section + `\|E∖f\| = 4s`)
  used ONLY `d_E = Fix(σ_E) = 1` — never anything solvable-specific. So
  **every `Fix = 1` meridian class, in any group, collapses to the same
  "4s omitted points at cusps" structure.** `A₅`-`(2,2)` and `S₅`-4-cycle
  join `D₅`/`F₂₀` verbatim.
* **What does NOT transfer:** the cusp-capability census (Fox-coloring /
  Alexander) is a metabelian tool; `A₅` is perfect and `S₅' = A₅`, so no
  abelian kernel survives for a coloring invariant — which cusps host
  `A₅`/`S₅` escape is OPEN.
* **Genuinely new cases:** `Fix ≥ 2` (multiple degree-1 sections, all
  Hartogs-protected — the bookkeeping of how many are affine is new) and
  `Fix = 0` (`E` a "purely exceptional" curve, entirely outside the
  generic image — no `D₅`/`F₂₀` analogue).
* **Strategic verdict (all four workflow lanes agree):** the
  topological / combinatorial / group-theoretic encirclement has
  **saturated**. The abstract decorated-tree recurrences impose no
  obstruction (explicit minimal 6/7-blowup witnesses; negative-`a`
  isolated leaves realizable at Fibonacci descent rate — machine
  search, `src/n2/tree_sat.py`); `λ` provably cannot see `N_∞` (a
  degree-1 isolated dicritical is a Suzuki/Hà–Lê "regular point at
  infinity", contributing exactly 0 — independent of the round-20
  Riemann–Hurwitz proof); the coexistence question is OPEN/PERMITTED
  in the literature (Borisov frameworks corroborate). **Any remaining
  obstruction must come from the map `f̄` itself** — the interlock
  `Σ n_D m_D = 5` with the actual pole/discriminant data is the sharpest
  map-level lever.

### Round 20: the P–Q interlock (session 7) — new weapon, one line closed, one error corrected

* **Interlock equations (new, sharp).** On a generic `P`-fiber `Ĉ_c` the
  other coordinate `Q` has degree 5 (the geometric degree), and its
  poles sit only on the infinity dicriticals `I_P`. Hence
  **`Σ_{D∈I_P} n_D·m_D = 5`** (and symmetrically for `Q`), where
  `n_D = deg(P|_D)`, `m_D = −v_D(Q)`. With `n_D = 1` the pole partitions
  of 5 are: `N_P = 1 → (5)`; `N_P = 3 → (3,1,1)` or `(2,2,1)`;
  `N_P = 5 → (1,1,1,1,1)`. This controls pole orders sharply but does
  **not** force `N_P = N_Q`.
* **Genus / λ (audited via Riemann–Hurwitz on `Q: Ĉ_c → P¹`):**
  `2g_P = A_P − N_P − 3` where `A_P = Σ h_i(e_i−1)`, `h_i = deg(P|_{D_i}) = d`.
  So `λ(P) = A_P + B_P − 4 = Σ h_i e_i − 4 = 4d − 4` (the `N_P` term
  cancels — λ cannot distinguish `N_P = 1,3,5`). **New parity:** for
  `F₂₀`, `2g_P = 3d − N_P − 3` ⟹ **`d + N_P` odd**. A contradiction
  *iff* `d` and `N_P` parities can be independently pinned to clash —
  not yet available.
* **Rank-1 question CLOSED (not a kill):** a degree-1 isolated infinity
  dicritical does not just coexist with the `E`-dicriticals — it is
  **forced** (else `Q` is constant on a generic `P`-fiber, contradicting
  degree 5). Abhyankar–Moh permits it. So "exclude the coexistence" is
  dead as a route.
* **Error corrected (my round-19 λ-budget):** the per-value jumps
  (`simple tangent = 4`, `cusp = 3`, `node = 4`) are **unsupported**.
  The real formula is Gwoździewicz–Płoski
  `λ_t(P) = N − deg_X disc_Y(P(X,Y) − t)` (monic coords) — needs the
  discriminant degrees, which the profile does not supply. The
  `λ_∞ = 4s − 4n_mb` claim is **withdrawn**.
* **Caveat on round-19 "complete splitting":** Lê–Weber is stated on the
  minimal single-coordinate resolution; resolving `Q` too can lengthen a
  bamboo that is equisingular on the `P`-resolution. The
  degree-1/length-1 conclusion holds on the minimal `P`-resolution; its
  transfer to the simultaneous `P,Q`-resolution needs care.
* **`F₂₀` section landing:** at an omitted `(4,5)`-cusp `q`, the section
  has a UNIQUE limit `s_q ∈ f̄⁻¹(q)` (since `E^ν → Ē` is bijective over
  the unibranch cusp); it lands either on `D₁` at the single point over
  `q̃`, or on a vertical component over `q`. Puiseux data + `a = 3` do
  not decide — needs the full local resolution.

### Literature-sweep adjudication (subagent C, session 6)

* **Moh-1983 conflation corrected:** "JC2 true for max deg < 100"
  bounds the ALGEBRAIC degree. Our "degree 5" is the GEOMETRIC degree
  (sheet count, the Vitushkin–Orevkov–Domrina ladder). No conflict: a
  geometric-degree-5 counterexample simply has algebraic degree > 100.
* **Lê–Weber 1994 (full text read):** origin of "dicritical" for JC2.
  Their Main Theorem excludes Jacobian pairs with a *strongly
  non-equisingular* dicritical `D₀` (bamboo length ≥ 2 or a critical
  point of `φ` on `D₀`) whose canonical multiplicity is negative, or
  positive with **coordinate-pencil restriction degree one**. Our
  `F₂₀` dicritical has `a = 3 > 0` but `deg(φ|D₀) = k·deg(x̃|_E) ≫ 1`
  generically — the theorem does not fire directly (`k = 1 ≠` their
  degree-1 condition; translation gap flagged). **Usable new fact:**
  their Ehresmann argument + Keller (`∇P ≠ 0`) shows every nontrivial
  Keller coordinate `P` has a critical point of its pencil `φ` on some
  dicritical of `φ` — partial strong-non-equisingularity for free.
* **Abhyankar dicritical school:** general-pencil realizability only —
  no constant-Jacobian hypothesis anywhere in that line; it neither
  clears nor kills our profiles. Gwoździewicz–Płoski: local polar
  theory, NOT-TRANSLATABLE as anticipated. Chau arXiv:0801.4138 is
  withdrawn (do not cite).

## Log

* **2026-07-24**: campaign opened. Phase 1 executed and CLOSED same day
  (Moskowicz rejected; Orevkov secures `d ≥ 4`). Phase 2 sharpened to the
  boundary-completion problem. Synthesis program adopted as master plan.
  Next session: begin synthesis step 1 (boundary configuration of the 3D
  example) + vet arXiv:2607.20210.
* **2026-07-24 (session 2)**: synthesis step 1 completed (S₃ + square-root
  escape data card, machine-measured). Literature: minimal open degree
  likely 5 (Orevkov 3; Domrina–Orevkov 4 — to confirm; exotic 5-covers
  exist). Phase 2 re-aimed at excluding solvable degree-5 monodromy.
  Next: confirm Domrina–Orevkov scope; synthesis step 2 (2D tree
  obstruction vs transposition-wrapping escape); vet arXiv:2607.20210.
* **2026-07-24 (session 3)**: minimal open degree = 5 confirmed
  peer-reviewed (Domrina Izvestiya 64 (2000)); Moskowicz audit complete
  (hinge is an example, not a classification — prime-degree theorem
  unproven); NEW: index-`p` rare-property family for every prime `p`;
  root-closed rare-property lemma isolated as the sharpest target.
* **2026-07-24 (session 4)**: the **degree-5 escape ledger** built and
  machine-verified (`src/n2/degree5_ledger.py`): sheet-fix bound
  `d_C ≤ Fix(σ_C)`; section principle for solvable monodromy (`d_C ≤ 1`);
  **omitted-points theorem**: irreducible-`E` + `D₅/F₂₀` forces the image
  to omit **exactly `4s ≥ 4`** isolated points of `E` (round-14 audit:
  branch-packet lemma closes the count; Peretz 1999 cofinite-image
  consistency). **Hartogs section lemma** proved and round-15-audited
  sound (sections cannot escape at smooth points; affine fiber count
  locally constant on the smooth locus; sharpness: `Sing({A=0}) = Z`
  exactly in 3D). **Theorem E conditional**: `D₅/F₂₀` with irreducible
  `E` survive only if ALL omitted points sit at cusps with full
  nonabelian local monodromy (5-colorable cusp knots for `D₅`; ordinary
  `(2,3)` cusps killed). Next: close the special-cusp case (global
  argument or knot-theoretic exclusion); reducible `E` / silent
  components via smooth-locus local constancy; `A₅/S₅` ledger
  (higher-degree components — Hartogs applies only to sections).
