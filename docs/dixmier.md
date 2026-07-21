# From the Jacobian counterexample to the Dixmier conjecture

Every identity below is machine-checked by
[`src/dixmier/verify_dixmier.py`](../src/dixmier/verify_dixmier.py).

> **Attribution, up front.** The Weyl-algebra counterexample below was first
> written down by **Omniscience Research Agent and Jeff Pickhardt**, *"An
> Explicit Counterexample to the Dixmier Conjecture in A₃"*, dated **19 July
> 2026** ([omniscienceproject.com](https://omniscienceproject.com/papers/an-explicit-counterexample-to-the-dixmier-conjecture-in-a-3-jfLENtXF/pdf)) —
> same inverse-Jacobian lift, injectivity by simplicity, non-surjectivity by
> centralizers, all `n ≥ 3`. We found their note only after completing our own
> construction; priority is theirs. What this directory adds: an **independent
> exact verification** (every algebraic identity machine-checked in sympy), a
> unified symplectic → Poisson → Weyl presentation, and — to our knowledge not
> written down elsewhere — the **explicit exact-symplectic C⁶ counterexample
> with rational momentum collisions** (§1). The transfer machinery itself is
> classical: Bass–Connell–Wright (1982, p. 297), Bavula (2024), Belov-Kanel–
> Kontsevich (2007, p. 2).

## 0. Background

The **Dixmier conjecture** `DC_n` (1968): every unital endomorphism of the Weyl
algebra `A_n(k)` (char 0) is an automorphism. Classical facts:

* `DC_n ⟹ JC_n`, dimension-preservingly (a Keller map pulls back to a Weyl
  endomorphism; an automorphism there forces invertibility) — Bass–Connell–
  Wright; convenient modern source: Bavula.
* `JC_{2n} ⟹ DC_n` (Tsuchimoto; Belov-Kanel–Kontsevich) — the *stable*
  converse; **not used** here.
* Zheglov has *announced* a preprint proof of `DC_1`
  ([arXiv:2410.06959](https://arxiv.org/abs/2410.06959), v5, Jan 2026) — not
  treated as established here.

Since `JC_3` is now **false** (Alpoge, July 2026), the contrapositive of
`DC_3 ⟹ JC_3` refutes `DC_3` — abstractly immediate; the point of this
directory (and of the Omniscience–Pickhardt note) is the explicit object.

## 1. The symplectic step: an exact-symplectic non-injective map of C⁶

Let `F = (f,g,h)` be Alpoge's map (`det DF = -2`) and
`G := ((DF)^T)^{-1}` — polynomial entries, since the determinant is the unit
`-2`. The **cotangent lift**

```
Fhat(q, p) = ( F(q), G(q)·p )      on  C^6 = T*C^3
```

satisfies (all verified exactly):

* **`Fhat*λ = λ`** for the Liouville one-form `λ = Σ P_i dQ_i` — the sharpest
  statement, and it implies the next two;
* `(D Fhat)^T Ω (D Fhat) = Ω` — the standard symplectic form is preserved;
* `det D(Fhat) = 1` identically — **unimodular**;
* `Fhat` is étale and **not injective**, with explicit rational 3-point
  collisions, e.g.
  ```
  (0, 0, -1/4,  1,   0,    0  )
  (1, -3/2, 13/2, -17/4, -3/2, -1/2)
  (-1, 3/2, 13/2, -17/4, -3/2,  1/2)   all ↦  (-1/4, 0, 0, 0, 0, 1/2);
  ```
* fibers of `Fhat` biject with fibers of `F` (the momentum is uniquely solved:
  `p = (DF)(q)^T·P`), so `Fhat` has geometric degree 3, inherited from `F`
  (generic fiber 3 is verified in the main suite, `src/verify.py` §3).

**Consequence.** The Jacobian Conjecture fails on `C^6` even for
*exact-symplectic étale* polynomial maps with Jacobian determinant ≡ 1.
Equivalently, `Fhat^*` is a Poisson endomorphism of `(C[x_1..x_6], {,})` —
injective (its components are algebraically independent since `det ≠ 0`) but
**not surjective**: were it surjective, each coordinate would be a polynomial in
the six components, which would then separate the three collision points. So the
**Poisson Conjecture** `PC(3, C)` of Adjamagbo–van den Essen (every Poisson
endomorphism of the canonical Poisson polynomial algebra in `2n` variables is an
automorphism) **fails for `n = 3`**.

(Terminology: `Fhat` is not a "symplectomorphism" — it is not invertible; it is
an exact-symplectic étale self-map.)

## 2. The quantum step: an explicit endomorphism of A₃

`A_3 = C⟨q_1..q_3, p_1..p_3⟩ / ([q_i,q_j], [p_i,p_j], [p_j,q_i] − δ_ij)`.
By this universal presentation, an assignment on generators extends (uniquely)
to a unital endomorphism iff the images satisfy the relations. Define

```
phi(q_i) = f_i(q1, q2, q3)          (the components of Alpoge's map)
phi(p_j) = Σ_k G[j,k](q) · p_k      (G = ((DF)^T)^{-1}, polynomial)
```

(full expanded formulas printed by `verify_dixmier.py`). The images of the
`p_j` are *derivations* `v_j = Σ_k G[j,k] ∂_k` — first-order operators with no
multiplication part — so their commutators are again derivations and everything
reduces to **commutative** chain-rule identities, verified exactly:

* `[phi(p_j), phi(q_i)] = v_j(f_i) = δ_ij`;
* `[phi(p_i), phi(p_j)] = [v_i, v_j] = 0`: each `v_j` is the unique vector
  field with `v_j(f_i) = δ_ij` (étaleness), i.e. `F`-related to `∂/∂a_j`, and
  relatedness preserves brackets — `[v_i,v_j](f_ℓ) = 0` with `DF` invertible
  forces `[v_i,v_j] = 0`;
* `[phi(q_i), phi(q_j)] = 0` inside the commutative `C[q]`.

So `phi` is a well-defined unital endomorphism of `A_3`.

## 3. `phi` is injective but not surjective

**Injective**: `A_3(k)` is simple (char 0) and `phi(1) = 1`, so `ker phi = 0`.

**Not surjective.** Since `phi` is injective, surjectivity would make it an
automorphism, and automorphisms carry centralizers **onto** centralizers. Two
routes, both elementary:

*Short route.* Only the classical maximal-commutativity fact
`Centralizer_{A_3}(C[q]) = C[q]` is needed:

```
Centralizer(C[f,g,h]) = Centralizer(phi(C[q])) = phi(Centralizer(C[q])) = phi(C[q]) = C[f,g,h].
```

But `C[f,g,h] ⊆ C[q]` and `C[q]` is commutative, so
`C[q] ⊆ Centralizer(C[f,g,h]) = C[f,g,h] ⊆ C[q]`, forcing `C[f,g,h] = C[q]`.

*Or the direct lemma* (which also proves the maximal-commutativity fact, at
`F = id`):

> **Lemma.** `Centralizer_{A_3}(C[f,g,h]) = C[q]`.
>
> *Proof.* `⊇` is clear. For `⊆`, let `T` have order `m ≥ 1` in the order
> filtration (degree in `p`) with principal symbol `σ_m`, homogeneous of degree
> `m` in `p`. `[T, f_i] = 0` forces the order-`(m−1)` symbol `{σ_m, f_i}` to
> vanish; for `q`-only `f_i` this reads `DF·∇_p σ_m = 0` (convention
> `(DF)_{ik} = ∂f_i/∂q_k`). Since `det DF = -2` is a unit of `C[q,p]`,
> `∇_p σ_m = 0`, and Euler's identity (`m·σ_m = Σ p_k ∂σ_m/∂p_k`, char 0)
> gives `σ_m = 0` — contradiction. So `T ∈ C[q]`. ∎

Either way `C[f,g,h] = C[q]`: in particular `q_1 = W(f,g,h)` for some
polynomial `W`. Evaluate at the three collision points — `F` takes a *single*
value there, so the right side is one number, while `q_1` takes the values
`0, 1, -1`. Contradiction. ∎

## 4. Consequences

* **The Dixmier conjecture is false for `A_3(k)`, char 0** — explicit,
  machine-verified endomorphism, injective and not surjective.
* **False for every `A_n`, `n ≥ 3`**: `phi ⊗ id` on `A_n ≅ A_3 ⊗ A_{n-3}` is
  injective with image `phi(A_3) ⊗ A_{n-3}`, proper because
  `(A_3/phi(A_3)) ⊗ A_{n-3} ≠ 0`. (Equivalently: run the whole argument on
  `F × id`, still a non-injective Keller map — verified.)
* **`A_n` is not co-Hopfian for `n ≥ 3`**: it embeds properly into itself.
* The Poisson analogue `PC(3, C)` fails (§1).
* Status map:
  ```
  A_1 : announced proof (Zheglov, preprint)    A_2 : open    A_n (n ≥ 3) : false
  ```
  paralleling the Jacobian Conjecture (`n=1` trivial, `n=2` open, `n≥3` false).

## References

* J. Dixmier, *Sur les algèbres de Weyl*, Bull. SMF 96 (1968), 209–242.
* H. Bass, E. Connell, D. Wright, *The Jacobian conjecture: reduction of degree
  and formal expansion of the inverse*, Bull. AMS 7 (1982), 287–330 (p. 297).
* Y. Tsuchimoto, *Endomorphisms of Weyl algebra and p-curvatures*, Osaka J.
  Math. 42 (2005), 435–452.
* A. Belov-Kanel, M. Kontsevich, *The Jacobian conjecture is stably equivalent
  to the Dixmier conjecture*, Moscow Math. J. 7 (2007), 209–218
  ([arXiv:math/0512171](https://arxiv.org/abs/math/0512171)).
* P. K. Adjamagbo, A. van den Essen, *A proof of the equivalence of the
  Dixmier, Jacobian and Poisson conjectures*, Acta Math. Vietnam. 32 (2007),
  205–214.
* V. V. Bavula, *Holonomic modules and 1-generation in the Jacobian
  Conjecture*, C. R. Math. 362 (2024), 731–738.
* A. Zheglov, *The Conjecture of Dixmier for the first Weyl algebra is true*,
  preprint, [arXiv:2410.06959](https://arxiv.org/abs/2410.06959) (v5, 2026) —
  announced, unrefereed.
* Omniscience Research Agent, J. Pickhardt, *An Explicit Counterexample to the
  Dixmier Conjecture in A₃*, 19 July 2026,
  [omniscienceproject.com](https://omniscienceproject.com/papers/an-explicit-counterexample-to-the-dixmier-conjecture-in-a-3-jfLENtXF/pdf) —
  **the first explicit write-up of the Weyl part; found by us post hoc**.
* L. Alpoge, announcement of the `JC_3` counterexample, 19–20 July 2026.
