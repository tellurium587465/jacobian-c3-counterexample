# The mechanism of Alpoge's Jacobian-Conjecture counterexample

Every displayed identity here is checked exactly by
[`src/verify.py`](../src/verify.py).

> **Attribution.** The counterexample is L. Alpoge's (July 2026). The structural
> picture in §1–§3 (generic degree 3, the fiber cubic, the discriminant `A`, the
> weighted grading) was already **public** within a day of the announcement — see
> the *Secret Blogging Seminar* post, the *jacobianfun.org* explainer, and the
> MathOverflow thread linked in the [README](../README.md). This note reproduces
> that picture with exact, runnable checks, states some caveats carefully, and
> then adds explicit rational collision families (§4). It does **not** claim the
> mechanism as original.

## 0. What is being violated

**Jacobian Conjecture** (Keller, 1939): a polynomial map `F : C^n -> C^n` with
`det(DF)` a nonzero constant (a *Keller map*) is invertible — in particular
injective. Proven only for `n = 1`; open for every `n >= 2` until dimension 3.

With `u = 1 + x*y`, Alpoge's map is
```
f = u^3 z + y^2 u (4 + 3xy)
g = y + 3x u^2 z + 3x y^2 (4 + 3xy)
h = 2x - 3x^2 y - x^3 z
```
* `det(DF) = -2` — nonzero constant, so `F` is Keller.
* `F(0,0,-1/4) = F(1,-3/2,13/2) = F(-1,3/2,13/2) = (-1/4,0,0)` — not injective.

A non-injective Keller map is a counterexample. So the Jacobian Conjecture is
**false for `n = 3`** (and, by §5, for all `n >= 3`).

## 1. Geometric degree 3

`F` is étale everywhere (`det DF ≡ -2 ≠ 0`) yet a generic fiber has **three**
points: the *geometric degree* is
`d = [C(x,y,z) : C(f,g,h)] = 3`. For a Keller map, `d = 1` would force
invertibility (the birational Keller theorem), so `d > 1` is exactly what a
counterexample looks like.

## 2. The fiber cubic (t-model)

The clean fiber coordinate is `t = y + 1/x` (`x ≠ 0`). Over a target `(a,b,c)`,
`t` is a root of
```
P(T) = c T^3 - 2 T^2 + b T - 2a ,     with     P'(t) = 2/x .
```
From a **simple** root `t` the whole preimage is reconstructed:
```
r = P'(t) = 3c t^2 - 4t + b ,   x = 2/r ,   y = t - r/2 ,
z = 5/4 r^2 - 3/2 t r - c/8 r^3 .
```
The discriminant is
```
Disc_T(P) = -4 A ,     A = 27 a^2 c^2 - 18 a b c + 16 a + b^3 c - b^2 ,
```
so the **genuine branch locus** (two finite sheets meeting) is exactly `A = 0`.
When `A ≠ 0`, `P` has three distinct roots ⇒ three distinct preimages ⇒ degree 3.

### The `x = 0` sheet
`h(0,y,z) = 0`, so a preimage can have `x = 0` only when `c = 0`, where
`F(0,y,z) = (z + 4y^2, y, 0)` gives the single extra point `(0, b, a - 4b^2)`.
Alpoge's `(0,0,-1/4)` is exactly this sheet on the `c = 0` slice. `src/counterexample.py:fiber`
assembles the `t`-sheets and this `x = 0` sheet into the complete fiber.

## 3. The x-eliminant, and a caveat

Eliminating `y` and `z` instead (the "eliminate two variables, get a cubic in the
third" computation) yields exactly `res = -9 c x · Q(x)` with the depressed cubic
```
Q(x) = A x^3 + (4 - 3 b c) x - 2 c        (no x^2 term).
```
So the `x`-coordinates of the finite preimages are the roots of `Q`, and — when
there are three finite sheets — **they sum to zero** (`x1 + x2 + x3 = 0`).

**Caveat (why the `t`-model is the correct one).** Projecting to `x` can merge two
genuine sheets that happen to share an `x`-value. Concretely, over `(0, 8/9, 1)`
the fiber is the three *distinct* points `(9/4,-4/9,656/729)`, `(-9/2,8/9,512/729)`,
`(9/4,8/9,-640/729)` — but two share `x = 9/4`, so `Q` has a *double* root there
even though **no sheets actually collide** (`A ≠ 0`). Hence
```
disc_x Q = -4 (27 a c^2 - 9 b c + 8)^2 · A :
```
the factor `A` is the real branch locus; the squared factor is a **projection
artifact**. Do not read `y, z` as global rational functions of `x`, and do not say
"`x1+x2+x3 = 0` on every fiber" without the "three finite sheets" qualifier (when
`A = 0` a sheet escapes to infinity and `Q` drops degree).

## 3½. Weighted homogeneity

`F` is homogeneous for the grading `deg(x,y,z) = (-1, 1, 2)`, with
`deg(f,g,h) = (2, 1, -1)`; equivalently `deg(a,b,c) = (2,1,-1)`. (Public; verified
in `verify.py`.) This is the symmetry organizing the formulas above.

## 4. Infinitely many rational triple-collisions

Alpoge gave one rational triple-collision; here are explicit infinite families,
generated in [`src/collisions.py`](../src/collisions.py) and tabulated (and
re-verified) in [`data/`](../data).

**Square-condition-free family (`a = 0` slice).** Choose rationals `p, q` with
`p q (p-q)(p+q) ≠ 0` and *prescribe* the split cubic
`P(T) = (2/(p+q)) T (T-p)(T-q)`. Matching coefficients forces
```
(a, b, c) = ( 0 ,  2pq/(p+q) ,  2/(p+q) ) ,
```
with **no** discriminant-square side condition. The three preimages are
`reconstruct(·)` at `t ∈ {0, p, q}`. (This clean parametrization came out of the
GPT‑5.6 collaboration; see [`gpt-consultation.md`](gpt-consultation.md).)

**General family (`a ≠ 0`).** Prescribing three rational `x`-roots `{r, s, -(r+s)}`
(forced sum zero) makes `A`'s definition a quadratic in `a`; rational roots give
targets with `a ≠ 0`, complementary to the slice above.

Both families are verified exactly; e.g. over `(-1/9, -1/3, 3)`:
`(1,-4/3,3)`, `(2,1/6,-1/8)`, `(-3,2/3,1)`.

## 5. All dimensions `n >= 3`

`F × id_{C^{n-3}}` has block-diagonal Jacobian, so `det = -2`, and any collision
lifts by copying the extra coordinates. Thus the conjecture fails in **every**
`n >= 3` (checked for `n = 4` in `verify.py`).

## 6. Why `n = 2` is untouched (and remains open)

The plane Jacobian Conjecture is **open**, and this construction says nothing
about it. The strongest *safe* statements:

* A plane counterexample must have geometric degree `d >= 3`: `d = 1` is
  impossible (birational Keller theorem); `d = 2` is impossible because a
  separable quadratic extension is Galois and the Galois case is known
  (Bass–Connell–Wright).
* A degree-3 plane counterexample would need a non-normal cubic function-field
  extension (generic monodromy `S_3`) — a depressed cubic with non-square
  discriminant is compatible with that.
* There is **no** settled classical theorem saying "a cubic mechanism cannot
  occur in two variables." The obstacle is realizing it by an actual *polynomial*
  plane Keller map; in the 3-variable example the third coordinate is doing
  essential work absorbing the rational denominators of the reconstruction.
* Degree bounds: T.-T. Moh verified `n = 2` for plane Keller maps of degree
  `<= 100`; a hypothetical plane counterexample `(P,Q)` needs
  `gcd(deg P, deg Q) >= 16` (Appelgate–Onishi, Nagata, successors).
* A 2024 preprint (Moskowicz, arXiv:2407.13795) claims plane Keller maps cannot
  have prime field-extension degree, which would exclude `d = 3` — cite as a
  *preprint claim*, not settled.

Honest status: **`n >= 3` false; `n = 2` open.** The degree obstructions are
exactly why a small, low-degree example is possible in three variables but not
(so far, if ever) in two.
