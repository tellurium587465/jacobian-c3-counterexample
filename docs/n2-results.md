# The degree-5 plane Jacobian program: results and the precise remaining gap

**Status as of 2026-07-25.** This is the honest, consolidated summary of the
`n=2` campaign (full working log: [`n2-campaign.md`](n2-campaign.md)). It
states what is **proved** (machine-verified and/or adversarially audited over
23 GPT-5.6-sol rounds), and the **exact two open lemmas** that stand between
this structural encirclement and a full proof of the minimal open case of the
plane Jacobian conjecture.

We did **not** prove the plane Jacobian conjecture, nor the degree-5 case. We
built a sharp reduction of it. That distinction is kept scrupulously below.

## The problem

The **plane Jacobian conjecture** (open since Keller 1939): a polynomial map
`F = (P,Q): C² → C²` with `det DF =` nonzero constant is invertible. The
`n ≥ 3` analogue is now **false** (Alpoge 2026; verified and extended
elsewhere in this repo), but `n = 2` remains open. By Orevkov and
Domrina–Orevkov, a counterexample must have **geometric degree** (sheet count)
`≥ 5`; degree 5 is the **minimal open case**. A counterexample `F` has an
irreducible **Jelonek curve** `E` (the locus over which `F` is not proper),
and a **monodromy group** `G ⊆ S₅` (transitive).

## What is proved

**1. The degree-5 reduction theorem** (`src/n2/degree5_ledger.py`,
`a5s5_ledger.py`; group data machine-verified). For irreducible `E`, the
meridian class of `E` must normally generate `G`, and `d_E := Fix(σ_E)` = the
number of non-escaping sheets over a generic point of `E`. This organizes
*every* monodromy group:

| `G` | meridian class | `Fix` | status |
|---|---|---|---|
| `C₅` | 5-cycle | 0 | **dead** (Galois ⟹ automorphism) |
| `D₅` | reflection | 1 | cusp collapse |
| `F₂₀` | 4-cycle | 1 | cusp collapse |
| `A₅` | `(2,2)` | 1 | cusp collapse (verbatim) |
| `A₅` | 3-cycle | 2 | new (two sections) |
| `A₅` | 5-cycle | 0 | new (`E` omitted) |
| `S₅` | 4-cycle | 1 | cusp collapse (verbatim) |
| `S₅` | transposition | 3 | new (three sections) |
| `S₅` | `(2,3)` | 0 | new (`E` omitted) |

**2. The universal Hartogs mechanism** (round 15, audited). A degree-1
"section" sheet cannot escape at a smooth point of `E` (the section + its
monodromy-fixed covering component map biholomorphically onto a punctured
ball; the inverse extends by Hartogs). Corollary: the finite-fibre count is
locally constant on the smooth locus of `E`. This uses only `Fix = 1`, so
**every `Fix = 1` case (all four groups) collapses identically**: the omitted
points are exactly `4s` cusps of `E` (`s` = branch excess), and they must be
capable cusps — `(2,5)` for `D₅`, `(4,5)` for `F₂₀` (Fox/Alexander
`5`-colouring census, `src/n2/degree5_ledger.py`).

**3. The dicritical profile theorem + Keller valuation identity** (round 18).
On a resolution `f̄: X̄ → P²`, the boundary divisors over `E` satisfy
`Σ kᵢeᵢ = 4`; `D₅` gives two dicriticals each birational onto `E` (`e=2`),
`F₂₀` gives one (`= P¹`, the normalization, `e=4`). The Keller identity
`f̄*(dx∧dy) = c·(du∧dv)` forces `a(Dᵢ) = ord_{Dᵢ}(du∧dv) = eᵢ − 1`.

**4. The P–Q interlock** (round 20). On a generic `P`-fibre, `Q` has degree 5
with poles only on the infinity dicriticals: `Σ_{I_P} n_D m_D = 5`. Every
residual infinity dicritical has `a = −m−1 < 0` (round 19), so Lê–Weber forces
them degree-1 and isolated. `λ(P) = 4d − 4`.

**5. The mixed log-BMY bounds** (rounds 21–22, verified; one over-claim
corrected by adversarial audit). `Σ_p M̄ᴼ_p ≤ 3d − 4 + 2s` with
`M̄ᴼ(m,q) = m + q − m/q − q/m − 1`. This **excludes `F₂₀, d=9, s=1`** and
gives strong degree lower bounds (`F₂₀`: `d ≥ 21` at `s=1`, `d ≥ 46` at
`s=2`; `D₅`: `d ≥ 22` at `s=2`). It is **not** a full kill — high-degree
packages with one efficient big cusp survive.

## The precise remaining gap: two open lemmas

The entire degree-5 case (irreducible `E`) is closed **if either** holds:

> **(L1) Unibranch lemma.** *An irreducible Keller Jelonek curve has no
> self-intersection point.*
> ⟹ (with Chau: `E ≇ C`) `E` is rational cuspidal, and **Koras–Palka 2019**
> (≤ 4 cusps; exactly 4 ⟹ the unique `A₆+3A₂` quintic) kills every
> `D₅`/`F₂₀` configuration — verified, since our cusp types and degrees never
> match the quintic.

> **(L2) No-total-omission lemma.** *An étale polynomial map `A²→A²` cannot
> totally omit an irreducible divisorial component of its nonproperness set.*
> ⟹ the `Fix = 0` cases (`A₅` 5-cycle, `S₅` `(2,3)`) die outright.

The mandatory **node** of `E` (forced by Chau, since `E ≇ C`) is the *single*
feature keeping `E` outside Koras–Palka. Jelonek's 2020 preprint attempted a
statement near (L1) and was **withdrawn with recorded errors**, so (L1) is a
genuine open problem, not an oversight.

## Honest assessment

This is a **reduction, not a proof**. Each of (L1), (L2) is itself a
substantial open statement (proving (L1) would resolve much of the plane
Jacobian conjecture on its own). What the campaign contributes is: a complete
case-organization of the minimal open degree; several new structural theorems
(universal Hartogs mechanism, dicritical profile + Keller valuation identity,
the P–Q interlock, the mixed-log-BMY degree bounds); and the isolation of the
gap to two named lemmas. Every quantitative claim here is machine-checked or
audited; two intermediate over-claims were caught and corrected by adversarial
review, which is recorded rather than hidden.
