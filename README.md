# Verifying and extending the 2026 Jacobian-Conjecture counterexample (n = 3)

In July 2026 **Levent Alpoge**, with AI assistance, announced an explicit
polynomial map that refutes the **Jacobian Conjecture** in dimension 3 — an
87-year-old open problem. This repository is a small, honest companion to that
result:

1. it **independently re-verifies** the counterexample, exactly and reproducibly;
2. it **reproduces the fiber mechanism** (already public — see references) with
   runnable, machine-checked algebra, stating the caveats carefully; and
3. it **extends it computationally**: explicit *infinite families* of rational
   triple-collisions, and the suspension to every `n >= 3`.

Every mathematical claim is checked by [`src/verify.py`](src/verify.py) with exact
symbolic arithmetic (sympy). The work was done by **Claude (Opus 4.8)** in an
adversarial dialogue with **GPT‑5.6**, which caught two real errors and an
over-claim; see [`docs/gpt-consultation.md`](docs/gpt-consultation.md).

> ### What this is, and is not
> * It is **not** a solution to the Jacobian Conjecture, and **not** the discovery
>   of the counterexample or its mechanism. The counterexample is Alpoge's; the
>   degree-3 fiber structure was public within a day of the announcement
>   (references below).
> * It **is** an independent, exact, one-command verification, a careful write-up
>   with the subtleties made precise, and new explicit collision computations.
> * `n = 2` remains **open**. Only `n >= 3` is settled (negatively).

## The counterexample

With `u = 1 + x*y`, the map `F : C^3 -> C^3` is
```
f = u^3 z + y^2 u (4 + 3xy)
g = y + 3x u^2 z + 3x y^2 (4 + 3xy)
h = 2x - 3x^2 y - x^3 z
```
* **Keller:** `det(DF) = -2` (nonzero constant) — the hypothesis holds exactly.
* **Not injective:** `(0,0,-1/4)`, `(1,-3/2,13/2)`, `(-1,3/2,13/2)` all map to
  `(-1/4,0,0)`.

A non-injective Keller map is a counterexample. Hence the conjecture is false for
`n = 3`.

## The mechanism, in one paragraph

`F` is étale everywhere yet generically **3-to-1** (geometric degree 3 — exactly
what the conjecture forbids). Over a target `(a,b,c)` the fiber is governed by the
cubic `P(T) = c T^3 - 2 T^2 + b T - 2a` in the variable `t = y + 1/x`, with
`P'(t) = 2/x` and `Disc_T(P) = -4A`, where
`A = 27a^2c^2 - 18abc + 16a + b^3c - b^2`; the genuine branch locus is `A = 0`.
`F` is weighted-homogeneous for `deg(x,y,z) = (-1,1,2)`. Full details, including
why the `x`-projection is subtler than it looks, are in
[`docs/mechanism.md`](docs/mechanism.md).

## What this repo adds

* An exact, self-contained **verification suite** (`src/verify.py`, 24 checks).
* A globally-correct `fiber()` routine (the `t`-model plus the `x=0` sheet).
* Two **infinite families of rational triple-collisions** — a clean
  square-condition-free `a=0` family `(0, 2pq/(p+q), 2/(p+q))`, and a general
  `a != 0` scan — tabulated and re-verified in [`data/`](data).
* The **suspension** to all `n >= 3`, and a careful account of why `n = 2` is
  untouched.

## The Dixmier conjecture falls too

The **Dixmier conjecture** (1968) — every endomorphism of a Weyl algebra
`A_n(C)` is an automorphism — is **false for all `n ≥ 3`** as a consequence of
Alpoge's map. The explicit Weyl-algebra counterexample was first written down by
**Omniscience Research Agent & Jeff Pickhardt** (19 July 2026); this repo
independently reproduces it with exact machine verification, and adds the
symplectic side ([`docs/dixmier.md`](docs/dixmier.md)):

* **Symplectic step** (to our knowledge not explicitly written elsewhere): the
  cotangent lift `Fhat(q,p) = (F(q), ((DF)^T)^{-1}p)` is an *exact-symplectic
  étale* polynomial self-map of `C^6` — it preserves the Liouville one-form
  (`Fhat*λ = λ`), has `det ≡ 1` — yet is non-injective, with an explicit
  rational 3-point collision. The Jacobian Conjecture fails even for
  exact-symplectic unimodular maps, and the **Poisson Conjecture** of
  Adjamagbo–van den Essen fails in dimension 6.
* **Quantum step**: `phi(q_i) = f_i(q)`, `phi(p_j) = Σ_k ((DF)^T)^{-1}[j,k](q)·p_k`
  is a well-defined endomorphism of `A_3` (all relations reduce to verified
  commutative identities), injective (simplicity), and **not surjective** — by
  an elementary centralizer argument: surjectivity would force
  `C[f,g,h] = C[q]`, contradicting the three-point collision. Hence `A_n`
  (`n ≥ 3`) embeds properly into itself (not co-Hopfian).
* **Status map**: `A_1` — announced proof of the conjecture (Zheglov,
  [arXiv:2410.06959](https://arxiv.org/abs/2410.06959), preprint) · `A_2` open ·
  `A_n (n≥3)` **false** — paralleling the Jacobian Conjecture itself.

Verification: `python src/dixmier/verify_dixmier.py` (exact, sympy only).

## The n = 2 program

The plane Jacobian Conjecture remains **open**. [`docs/n2-program.md`](docs/n2-program.md)
documents an honest attack on it, extracting everything the `n = 3` counterexample
teaches about the plane:

* **The shadow.** Alpoge's map is hyperbolically `C*`-equivariant; passing to
  invariant rings induces an explicit **plane polynomial map** `phi` with
  `det J_phi = 2(3s+w-2)²` — a perfect square vanishing on one line, which `phi`
  contracts to the origin; `phi` is generically 3-to-1 with rational triple
  collisions. The general **shadow principle** `det J_phi = -Ph²·det DF` (proven
  symbolically) shows the entire 3D Keller condition compresses to a two-variable
  bracket identity `-2Pf{Pg,Ph} + Pg{Pf,Ph} + Ph{Pf,Pg} = const`, and locates the
  obstruction to descending the mechanism to a plane Keller map in the factor `Ph²`.
* **Plane hyperbolic rigidity (small theorem).** Every hyperbolically
  `C*`-equivariant Keller map of `A²` is a linear automorphism — so no plane
  counterexample has the symmetry that Alpoge's `C³` counterexample enjoys.
  Machine-checked case analysis; elementary, but it makes the `n=2` vs `n=3`
  dimension gap precise.
* **Dead ends, documented**: the `S₃`/quadratic-resolvent descent fails
  (`E ⊄ L`, and resolvent covers must ramify since `A²` is simply connected);
  monic cubic models die by simple connectedness; the essential open difficulty
  is isolated as *boundary completion*.

Verification: `python src/n2/verify_n2.py` (all exact, sympy only).

## Reproduce

```bash
pip install sympy
python src/verify.py                  # n=3 counterexample: 24 exact checks
python src/collisions.py              # rational triple-collision families
python src/export_data.py             # rebuild data/ tables
python src/n2/verify_n2.py            # n=2 program: shadow + rigidity
python src/dixmier/verify_dixmier.py  # Dixmier + symplectic C^6 package
```
Expected tail of `verify.py`:
```
========================================================================
RESULT: ALL CHECKS PASSED.
```

## Layout
```
src/counterexample.py   the map; fiber cubic (t-model); reconstruction; fiber()
src/collisions.py       rational triple-collision generators (two families)
src/verify.py           self-contained exact verification (24 checks)
src/export_data.py      writes the data/ tables
src/n2/shadow.py        the hyperbolic C*-shadow and the shadow principle
src/n2/rigidity.py      plane hyperbolic rigidity (theorem + proof data)
src/n2/verify_n2.py     exact verification of the n=2 program (30+ checks)
src/dixmier/dixmier.py  cotangent lift; the explicit Weyl endomorphism of A_3
src/dixmier/verify_dixmier.py  exact verification of the Dixmier package
docs/dixmier.md         Dixmier conjecture: explicit counterexample + proof
data/                   verified collision tables (JSON + Markdown)
docs/mechanism.md       the n=3 mathematics, with caveats
docs/n2-program.md      the n=2 program: shadow, rigidity, dead ends
docs/gpt-consultation.md how the GPT-5.6 adversarial review shaped this
```

## References (context and prior public analysis)

* Jacobian Conjecture — [Wikipedia](https://en.wikipedia.org/wiki/Jacobian_conjecture),
  [Wolfram MathWorld](https://mathworld.wolfram.com/JacobianConjecture.html).
* Public analysis of this counterexample (generic degree 3, the fiber cubic, the
  discriminant `A`, the weighted grading), appearing within a day of the
  announcement:
  *Secret Blogging Seminar*, "The new counterexample to the Jacobian conjecture"
  (2026-07-20); the *jacobianfun.org* explainer; and the MathOverflow thread on the
  Galois structure of the fiber cubic.
* H. Bass, E. Connell, D. Wright, *The Jacobian conjecture: reduction of degree and
  formal expansion of the inverse*, Bull. AMS 7 (1982).
* T.-T. Moh (plane Keller maps of degree ≤ 100); Appelgate–Onishi, Nagata (shape of
  plane counterexamples); S. Pinchuk (1994, the **real** plane counterexample).

## Attribution & honesty

Counterexample: **L. Alpoge (2026)**. Fiber mechanism: public prior analysis
(above). This repository's contribution is independent verification, careful
exposition, and the explicit collision families — all reproducible from source. See
[`docs/gpt-consultation.md`](docs/gpt-consultation.md) for what the AI collaboration
did and did not do.

## License
MIT — see [LICENSE](LICENSE).
