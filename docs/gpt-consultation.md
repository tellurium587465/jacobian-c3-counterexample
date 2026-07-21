# GPT-5.6 adversarial consultation

This project was carried out by **Claude (Opus 4.8)** and deliberately stress-tested
by **GPT-5.6** acting as an *adversarial reviewer*. The dialogue materially changed
the results: it caught two real errors, corrected an over-claim of novelty, and
supplied a cleaner construction. This file records what happened, honestly.

## What Claude proposed
* Independent symbolic verification of Alpoge's map: `det(DF) = -2`; the three-point
  collision over `(-1/4,0,0)`; generic fiber size 3.
* A "resolvent cubic" `Q(x) = A x^3 + (4-3bc)x - 2c` for the `x`-coordinates, with
  `A = 27a^2c^2 - 18abc + 16a + b^3c - b^2`, plus rational formulas `y(x)`, `z(x)`.
* An 8-parameter deformation that stays Keller — found to collapse to the original
  under diagonal scaling.
* 24 new rational triple-collisions via a discriminant-square condition.

## What GPT-5.6 corrected (all re-verified by Claude in `verify.py`)
1. **Use `t = y + 1/x`, not `x`.** The globally valid fiber model is
   `P(T) = c T^3 - 2 T^2 + b T - 2a`, with `P'(t) = 2/x`, `Disc_T(P) = -4A`, and an
   explicit reconstruction from each simple root. Claude verified `P(t)=0`,
   `P'(t)=2/x`, and `Disc=-4A` symbolically.
2. **The `y(x)` formula is only *generically* valid.** Its denominator can hit `0/0`;
   then one `x`-root carries two preimages. GPT's witness `(a,b,c)=(0,8/9,1)`,
   `x=9/4` (a double root of `Q`) was confirmed: the fiber has **three distinct
   points**, two sharing `x = 9/4`, while `A ≠ 0`. Hence the squared factor of
   `disc_x Q` is a **projection artifact**; the true branch locus is `A = 0`.
3. **"`x1+x2+x3 = 0` on every fiber" needs a qualifier** — it holds when there are
   three *finite* sheets; at `A = 0` a sheet escapes to infinity and `Q` drops
   degree. Adopted.
4. **Terminology.** "resolvent cubic" has a specific classical meaning; use
   "fiber cubic / x-eliminant". Adopted.
5. **Novelty, honestly.** GPT's literature check (corroborated by Claude fetching the
   *Secret Blogging Seminar* post) showed the cubic reduction, generic degree 3, the
   discriminant `A`, and the weighted grading were **already public** within a day of
   the announcement. So this repo does **not** claim the mechanism; it verifies,
   caveats, and extends it. The over-claim was removed from the README and docs.
6. **A cleaner infinite family.** GPT supplied the square-condition-free
   parametrization `P(T) = (2/(p+q)) T(T-p)(T-q) ⇒ (a,b,c) = (0, 2pq/(p+q),
   2/(p+q))`. Claude verified it and made it the primary generator
   (`collisions.py:family`), producing 308 targets in the default box.
7. **`n = 2`.** GPT gave the sharp safe framing now in `mechanism.md` §6
   (`d>=3` for any plane counterexample; the Moskowicz 2024 preprint cited as a
   preprint claim, not settled).

## Takeaway
The adversarial pass improved correctness (fixed a false global formula and a
mis-stated invariant), improved honesty (removed a novelty over-claim), and improved
the mathematics (a cleaner family). Every adopted claim is machine-checked in
`src/verify.py` — Claude took nothing on GPT's word, and GPT took nothing on Claude's.

---

# Round 2: n = 2 strategy triage

Claude proposed four attack directions on the (open) plane case and asked for
adversarial triage. GPT-5.6's verdicts (all subsequently verified or adopted):

1. **D1 — the hyperbolic `C*`-shadow: execute.** GPT independently re-derived
   Claude's shadow map and *improved* it: the `(τ,ρ) = (Ph·(s+1), 2Ph)` normal
   form factoring `φ` through the universal marked cubic
   (`τ³−2τ²+Bτ−2C = 0`, `ρ = 3τ²−4τ+B`, `det Dψ = −2Ph`, `det Dχ = −ρ/2`),
   the inverse formulas on `ρ ≠ 0`, and the prediction that the nonproperness
   set is the discriminant curve `Δ(B,C) = 0`. All verified exactly in
   `src/n2/verify_n2.py` §6.
2. **D3 — the `S₃`/quadratic-resolvent descent: killed with precision.** The
   quadratic resolvent field is *not* an intermediate field of the cubic
   extension (`E = N^{A₃}` vs `L = N^H`; neither contains the other), and any
   resolvent double cover must *ramify* because `A²` has no nontrivial
   connected finite étale covers. So "degree-3 counterexample ⟹ degree-2 Keller
   map ⟹ contradiction" is unfixable; only a weak unconditional shape statement
   survives.
3. **D2 — linear-coefficient cubic models: not finite-dimensional** without
   arbitrary degree bounds; but the clean sub-result stands: a *monic* cubic
   model would give a connected finite étale degree-3 cover of `A²` —
   impossible by simple connectedness. Any cubic mechanism in the plane must
   have a rational primitive element plus boundary corrections.
4. **D4 — classify hyperbolic equivariant plane Keller maps: worth doing** —
   this became the rigidity theorem below.

# Round 3: adversarial review of the rigidity theorem

Claude proved: *every hyperbolically `C*`-equivariant Keller map of `A²` is
linear (`(αx,βy)` or `(αy,βx)`)* — and submitted the proof for review.
GPT-5.6's verdict: **"The theorem is true as stated… the proof survives"**, with
three substantive improvements, all adopted and re-verified:

* **The all-degrees identity** — Claude's Step 2 rested on a finite-degree
  symbolic check; GPT supplied the general identity
  `E(v) = (ad−bc)AB + v[(ap−bq)AB' + (qd−pc)A'B]`
  (the `v²A'B'` terms cancel identically), which Claude verified with symbolic
  exponents and generic functions — upgrading the check to a complete proof.
* **Hypothesis trimming** — `gcd(p,q) = 1` is not load-bearing (reduce to the
  effective action); algebraic closedness unnecessary; characteristic 0 is what
  the top-coefficient argument actually uses.
* **Sharper framing** — say "the shadow *does* descend; what fails is
  *preservation of étaleness*, measured exactly by `Ph²`", not "failure to
  descend". Plus the elliptic-weights corollary (resonant shears only) and the
  character-twist corollary (`r = 0` forced).
* **Novelty honesty** — "presumably standard to experts" is the defensible
  wording for the rigidity lemma (negative-weight methods are classical); no
  exact citation was found by either model.

# Round 4: adversarial review of the Dixmier package

Claude proposed the symplectic + Weyl package (cotangent lift on `C^6`; explicit
endomorphism of `A_3`; centralizer non-automorphism proof) and asked GPT-5.6 to
break it and to hunt for prior work. Verdict: **"the core constructions are
correct... no fatal mathematical flaw"**, with four repairs, all adopted:

* **Transpose fix** — the centralizer lemma's displayed equation is
  `DF*grad_p(sigma) = 0`, not `(DF)^T*...` (harmless, both invertible; fixed).
* **Wording** — `Fhat` is not a "symplectomorphism" (it is not invertible): say
  *exact-symplectic etale polynomial self-map*. GPT also supplied the sharper
  cheap fact `Fhat*(Liouville form) = Liouville form`, now verified as a check.
* **Generic degree** — "generically 3:1" needs the fiber-cubic argument, not
  just the collision; wired to the main suite's verified degree-3 computation
  (fibers of `Fhat` biject with fibers of `F`).
* **Novelty collision (decisive)** — GPT located *Omniscience Research Agent &
  Jeff Pickhardt, "An Explicit Counterexample to the Dixmier Conjecture in
  A_3", 19 July 2026* — the same Weyl lift, injectivity-by-simplicity,
  centralizer non-surjectivity, all `n >= 3`. Claude fetched and read the PDF
  to confirm. All Dixmier-side claims were reframed as **independent
  reproduction with exact machine verification**; the explicit exact-symplectic
  `C^6` package with rational momentum collisions remains, to both models'
  knowledge, not written down elsewhere. GPT also supplied the precise
  citations (Bass-Connell-Wright p.297; Bavula 2024; Tsuchimoto 2005;
  Belov-Kanel--Kontsevich 2007; Adjamagbo--van den Essen 2007 for the Poisson
  Conjecture; Zheglov's `DC_1` as *announced preprint*, not settled fact).

## Overall takeaway
Across four rounds the two models alternated proposer/verifier roles. Every
error found (two mathematical, one of framing, one of proof completeness) was
found by the *other* model, and every fix was independently machine-verified
before adoption. The result — shadow principle + normal form + rigidity theorem + documented
dead ends + the symplectic/Weyl package with honest attribution — is stronger
than what either model produced alone. Round 4's most important catch was not
mathematical but scholarly: the two-day-old prior note that priority belongs to.
