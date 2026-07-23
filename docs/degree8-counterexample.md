# A constant-bracket graded lift: an imprimitive degree-8 Keller counterexample on C⁴

**Date: 2026-07-24.** The non-realizability conjecture of
[`degree4-obstruction.md`](degree4-obstruction.md) §5d is **refuted — by
explicit construction**. Every claim below is machine-verified by
[`src/verify_degree8.py`](../src/verify_degree8.py) (exact sympy; the fiber
census at 40 digits over two independent targets).

## The map

With variables `(x, y, z, w)` on `C⁴`:

```
b0 = 3wx⁴y⁴ + 12wx³y³ + 18wx²y² + 12wxy + 3w + 3x³y⁴z − 12x²y⁵
     + 12x²y³z − 22xy⁴ + 15xy²z − 10y³ + 6yz
b1 = −4wx⁴y³ − 12wx³y² − 12wx²y − 4wx − 4x³y³z + 16x²y⁴ − 12x²y²z
     − 6xyz − 14y² + 2z
b2 = 20xy² − 3xz + 2y
e  = wx⁴ + x³z − 4x²y + 2x
```

**Facts (verified):**

* `det DF = 24` identically — `F = (b0, b1, b2, e)` is a **Keller map**.
* `F(1, 1, 1, 1) = F(−1, 3, 193/3, 235/3) = (40, −50, 19, 0)` — an exact
  rational collision: **`F` is not injective.**
* The fiber quartic identity holds: with `t = y + 1/x`,
  `e·t⁴ − 2t³ + b2·t² + b1·t + b0 ≡ 0`.
* Generic fibers have **eight** points (four quartic roots `t'`, then `z, w`
  eliminate linearly and `x` satisfies an effective quadratic per root):
  **geometric degree 8 = 2³**.

## Exact geometric degree 8 = 4 × 2 (round-11 proof)

The degree is **exactly 8**, by a clean field-tower argument (GPT round 11,
key identity machine-verified): with `t = y + 1/x` and target coordinates
`(α,β,γ,ε)`:

* **Quartic step, degree exactly 4**: `α = −εt⁴ + 2t³ − γt² − βt` exhibits
  `α` as a degree-4 rational function of `t` over `C(β,γ,ε)`, so
  `[L(t) : L] = 4` (one-variable function-field theorem — the fiber quartic
  is irreducible over the target field).
* **Quadratic step, degree exactly 2**: `z, w` are rational in `(x, t)` and
  the remaining relation is the machine-verified identity
  ```
  x²·(b1 − 6t² + 4e·t³ + 2b2·t) = 2 ,
  ```
  i.e. `x² = 2/Q` with `Q` prime (linear in `β`) — not a square in `L(t)`,
  so `[K : L(t)] = 2` and `K = L(t)(x)`: no uncounted sheets.

Hence `[C(x,y,z,w) : C(F)] = 4 × 2 = **8**`, with a degree-4 intermediate
field: the monodromy is **imprimitive** (blocks of size 2). Over `ε = 0` the
quartic degenerates to a cubic: `3 × 2 = 6` — exactly the collision fiber.

## Novelty, honestly (post round-11 audit)

The field is moving at astonishing speed. A public **counterexample atlas**
(jacobianfun.org/counterexamples, updated 2026-07-22 — two days before this
work) already realizes **every geometric degree `3 ≤ n ≤ 100` in dimension
3**, with exact certificates; a MathOverflow thread includes a degree-4
example. So we claim **no priority** on degree realizability, on degree 8,
or on non-`3^k` degrees. What remains distinctive about this construction
(none of it found in the indexed public sources, per the round-11 audit —
with the standard caveat that searches cannot prove priority):

* the **valuation classification** (every polynomial solution of the graded
  quartic tower has `Φ ≡ −λ` and `E` squarefree; `E` constant is impossible);
* the **collapse to a single constant-Poisson-bracket equation**
  `{A,E}₂₃ = const` — we call the family **constant-bracket graded lifts**;
* the exact **imprimitive `4 × 2` field tower** — a structural discriminator:
  the atlas's degree-8 example (if its reported full-symmetric monodromy is
  independently confirmed) is *inequivalent* to ours, which would make these
  genuinely different degree-8 mechanisms;
* the **collision-preserving infinite family** below.

What the degree does still rule out: this map cannot be assembled from copies
of *Alpoge's original map itself* by products/compositions/automorphisms
(those realize only `3^k`).

## How it was found: the identity chain that overturned our own conjecture

The route is a three-step exact reduction — each step machine-verified —
which turned the *proof attempt* for the non-realizability conjecture into
its refutation:

**Step 1 (round-10 factorization).** The graded quartic tower reduces to:
polynomials `E, A, P₁` (weights `deg(S₁,S₂,S₃) = (1,2,3)`) with support
conditions and `Φ·J(AE, P₁E², HE) = δE³`, where
`Φ = 3λH² − 4EH³ − 2AH − P₁`, `H = 1 + S₁`.

**Step 2 (valuation lemma — the conjecture's proof attempt).** For any
irreducible `q | E` with multiplicity `m`: writing each gradient row as
`∇(q^a g) = q^{a−1}(ag∇q + q∇g)` and noting the reduced rows are all
proportional to `∇q` modulo `q`, one gets `v_q(J) ≥ 4m − 1` (and `≥ 4m` for
`q ~ H`). Since `v_q(Φ) + v_q(J) = 3m`, nonnegativity forces `m = 1`,
`v_q(Φ) = 0`, `H ∤ E`. Hence `gcd(Φ, E) = 1`, and the divisibility `Φ | E³`
forces **`Φ ≡ −λ` constant**: every polynomial solution lives in the
`Φ`-constant stratum with `E` squarefree.

**Step 3 (collapse identity — the reversal).** Substituting
`P₁ = 3λH² − 4EH³ − 2AH + λ` into the multilinear expansion of
`J(AE, P₁E², HE)` cancels *everything* except one term:

```
J(AE, P₁E², HE) = 2λ·E³·{A, E}₂₃ ,       {A,E}₂₃ := A_{S₂}E_{S₃} − A_{S₃}E_{S₂}.
```

So the entire graded quartic tower is **equivalent to the plane-bracket
equation `{A, E}₂₃ = const ≠ 0`** plus four linear support conditions — and
that equation is trivially solvable:

```
E = 2 − 4S₁ + S₂ + S₃ ,      A = 2S₁ + 20S₁² − 3S₂      (λ = 2, δ = 24).
```

Since `{A,E}₂₃ = const` has infinitely many polynomial solutions, this yields
an **infinite family** of Keller maps; and the explicit shift
`A ↦ A + E(E−λ)³·R(E−λ, S₁)` (any `R`) preserves the bracket, all supports,
`det DF = 24`, **and the rational collision itself** (machine-verified for
`R = 1`) — infinitely many counterexample *formulas* sharing one collision.
Also verified impossible: `E` constant (it forces `{A,P₁}₂₃ = 0`), so the
classification has no degenerate branch.

## The post-mortem we owe the record

Nineteen numerical truncation searches (12 general patterns + 7 rigid-case
sizes, up to 124 unknowns vs 1041 equations) had "floored" at `O(1)` residual
and supported the non-realizability conjecture — including patterns that
*contain* the explicit solution above. Those floors were **optimizer
failures on a thin solution set**, not mathematics. The exact identity chain
overturned them in an afternoon. Lesson, stated plainly: **numerical floors
are evidence, never proof — and this repository now contains a concrete case
where they pointed the wrong way.**

## Open questions this creates

* Confirm the monodromy discriminator: is the public atlas's degree-8 example
  really full-symmetric (then provably inequivalent to this imprimitive one)?
* Does the constant-bracket mechanism descend to `C³` (round-11 analysis:
  no evident slice/quotient — the bracket needs both `S₂, S₃` with `S₁` as a
  parameter)?
* Classify constant-bracket graded lifts up to equivalence; run the same
  valuation + collapse program for degree-`d` towers, `d ≥ 5` (does every
  tower collapse to a constant-bracket equation?).
* The realizable-degree question in dimension 3 is settled publicly (every
  `3 ≤ n ≤ 100` per the atlas); the *classification* of mechanisms is wide
  open — imprimitive vs primitive monodromy is now a live invariant.
