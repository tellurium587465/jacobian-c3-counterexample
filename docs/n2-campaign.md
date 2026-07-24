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
