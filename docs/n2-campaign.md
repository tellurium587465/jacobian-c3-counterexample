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

## Log

* **2026-07-24**: campaign opened. Phase 1 executed and CLOSED same day
  (Moskowicz rejected; Orevkov secures `d ≥ 4`). Phase 2 sharpened to the
  boundary-completion problem. Synthesis program adopted as master plan.
  Next session: begin synthesis step 1 (boundary configuration of the 3D
  example) + vet arXiv:2607.20210.
