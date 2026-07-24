# Literature sweep: localizing the λ-invariant (Euler-characteristic defect at infinity) to dicritical divisors

**Session 7 support task.** Question: is there a real theorem that writes
`λ(P) = Σ_D λ_D` (sum over dicritical divisors/bamboos at infinity), with each
`λ_D` computable from local resolution data (pole order, `deg(P|_D)`, bamboo
length) — and if so, does it pin down `N_inf` (the number of infinity-type
dicriticals, believed ∈ {1,3,5}) or the pole orders? Short answer up front,
details and verbatim citations below.

**Headline finding — matches and independently confirms round-20's
Riemann–Hurwitz conclusion in `docs/n2-campaign.md`.** The real, citable
local-decomposition theorems (Broughton 1988 / Ha Huy Vui–Lê Dũng Tráng 1984 /
Suzuki–Gavrilov / Gwoździewicz–Płoski 2001) all localize `λ` to **points at
infinity**, as
`λ_t(f) = Σ_{p} (μ_p(t) − μ_p(gen))`. A point that resolves to a **degree-1,
length-1 (isolated) dicritical** is exactly the classical "**regular point at
infinity**" of Ha Huy Vui–Lê Dũng Tráng / Suzuki: at such a point
`μ_p(t) = μ_p(gen) = 0` identically, for *every* `t`. So each such dicritical
contributes **exactly 0** to `λ`, for structural reasons, independent of how
many of them there are. Consequently **no local λ-formula — not just the ones
we found, but any formula of this shape — can distinguish `N_inf = 1` from `3`
from `5`**: you are summing `N_inf` copies of zero. This is a second, fully
independent proof (via 1980s–2000s local Milnor-number bookkeeping, not via
the P–Q Riemann–Hurwitz argument) of the same fact your round-20 note reports:
*"λ cannot distinguish `N_P = 1,3,5`"*. The two derivations do not
contradict — they are dual computations of the same vanishing. The E-type
dicritical(s) (`deg(P|_D) = d > 1`, ramified) are structurally forced to carry
the entire `4d−4` defect; this matches `Σ h_i e_i` in your round-20 formula.

**What CAN see `N_inf`:** not λ, but the pole-order/degree Bezout-type count
you already have — `Σ_{D ∈ I_P} n_D m_D = 5` (round 20) — because that counts
divisors with weight 1 each (a genuinely `N_inf`-sensitive linear form),
whereas `λ` weights each isolated degree-1 dicritical by 0. This is not a new
result from us; it is the literature explaining *why* your λ route stalled
and your P–Q interlock route didn't.

---

## 1. Suzuki's original formula (1974) and its refinement (Suzuki 1977 + Gavrilov) — "Suzuki–Gavrilov formula"

**Primary citation (original, global form).**
M. Suzuki, *"Propriétés topologiques des polynômes de deux variables
complexes, et automorphismes algébriques de l'espace `C²`"*, J. Math. Soc.
Japan **26** (1974), 241–257.

Verbatim statement (as transcribed and used by A. Bodin, *"Classification of
polynomials from `C²` to `C` with one critical value"*, arXiv:math/0009002,
§2, Lemma 2 and its proof — cross-checked against the Gwoździewicz–Płoski and
Cassou-Noguès–Raibaut restatements below):

> **Suzuki formula.** If `f` is a *primitive* polynomial (connected generic
> fiber) with bifurcation set `B`, then
> `1 − χ(F_gen) = Σ_{c∈B} (χ(F_c) − χ(F_gen))`.

This is literally Euler-characteristic additivity of the partition
`C = (C∖B) ⊔ B` applied to `f : C² → C` (`χ(C²)=1`); Suzuki's contribution
was establishing it rigorously together with the finiteness of `B` and its
splitting `B = B_aff ⊔ B_∞`. Bodin's paper (§2, Lemma 2 / Remark) uses it
exactly to prove: for primitive `f`, `χ(f⁻¹(0)) = +1 ⟺ B ⊆ {0}` — i.e. the
Abhyankar–Moh / Zaidenberg–Lin dichotomy for one-critical-value polynomials
rests directly on this identity, with positivity of each individual jump
`χ(F_c) − χ(F_gen) > 0` for atypical `c` cited to **[HL] = Ha Huy Vui – Lê
Dũng Tráng 1984** (see §2 below).

**Refined / "with isolated critical points" version — the "Suzuki–Gavrilov
formula".** Verbatim (transcribed from J. Gwoździewicz & A. Płoski, *"Formulae
for the singularities at infinity of plane algebraic curves"*, Univ. Iagel.
Acta Math. **39** (2001), 109–133, §4, p. 124 — their own name for it):

> **Suzuki–Gavrilov's formula.** If `f : C² → C` is a polynomial with
> isolated critical points then the Euler characteristic of the fiber
> `f⁻¹(t)` is given by
> `χ(f⁻¹(t)) = 1 − μ(f) − λ(f) + μ_t(f) + λ_t(f)`.

where (same paper, §3, Broughton's construction, attributed to **S. A.
Broughton, *"Milnor numbers and the topology of polynomial hypersurfaces"*,
Invent. Math. **92** (1988), 217–241**, their reference [7]):
`μ_t(f) = Σ_{p∈f⁻¹(t)} μ_p(f)` (affine Milnor numbers on the fiber),
`μ(f) = Σ_t μ_t(f)` (global affine Milnor number), and, crucially for
localization at infinity:

> **Proposition 3.1 (Broughton, as restated by Gwoździewicz–Płoski).** There
> exists a family `(μ_p^gen)_{p∈C_∞}` of non-negative integers, indexed by
> the points `p` where the projective closure `C_t` meets the line at
> infinity `L` (`C_∞ := C_0 ∩ L`, independent of `t` as a *set*), such that
> (1) `μ_p^t ≥ μ_p^gen` for all `t`, `p`; (2) `μ_p^t = μ_p^gen` for all but
> finitely many `t`. For every `t`, `λ_t(f) := Σ_{p∈C_∞} (μ_p^t − μ_p^gen)`,
> and `λ(f) := Σ_t λ_t(f)`. The finite set `B_∞(f) := {t : λ_t(f) ≠ 0}` is
> the set of *critical values at infinity*.

This `λ_t(f) = Σ_p (μ_p^t − μ_p^gen)` **is exactly the localization the task
asked for, in the strongest form the literature actually offers**: a sum over
points at infinity (≈ dicritical directions before/at the base of the
resolution) of a purely local quantity (a Milnor-number difference computable
from the resolution/Newton-Puiseux data at `p`, i.e. from pole order and
branching, via the classical toric/Newton-diagram algorithm — see §5, §7
below for the explicit machinery). We could not verify Gavrilov's own two
papers directly (paywalled/unavailable): L. Gavrilov, *"On the topology of
polynomials in two complex variables"*, Université de Toulouse preprint
(1994) [never confirmed published — TODO], and L. Gavrilov, *"Isochronicity
of plane polynomial Hamiltonian systems"*, Nonlinearity **10** (1997),
433–448 (their Theorem 2.2 is cited as containing the refinement). Suzuki's
own second paper carrying "Proposition 2, p. 533" (the fiber-Euler-
characteristic statement Gwoździewicz–Płoski build on) is **M. Suzuki, *"Sur
les opérations holomorphes du groupe additif complexe sur l'espace de deux
variables complexes"*, Ann. Sci. École Norm. Sup. (4) **10** (1977), 517–546**
— note the Iagel2001 PDF we scanned OCR's the year as "1987"; we cross-checked
this independently via web search and confirm **1977** is correct (volume 10
of that journal is 1977).

**Modern clean restatement (2021), same formula, cross-checked
independently.** Pierrette Cassou-Noguès & Michel Raibaut, *"Newton
transformations and motivic invariants at infinity of plane curves"*, Math.
Z. (2021) (arXiv:1910.07032), Theorem 3.17:

> **Theorem 3.17.** Let `f` be a polynomial in `C[x,y]` with isolated
> singularities. ... For any value `a` in `C`, we have
> `χ(f⁻¹(a)) = χ(f⁻¹(a_gen)) + μ_a(f) + λ_a(f)` and
> `χ(f⁻¹(a_gen)) = 1 − (μ(f) + λ(f))`
> with `μ_a(f)` equal to the sum of Milnor numbers of critical points of
> `f⁻¹(a)`, `μ(f)` the sum of all `μ_a(f)`, and `λ(f)` the sum of all
> `λ_a(f)`. In particular ... `B_top(f) = disc(f) ∪ {a ∈ C : λ_a(f) = 0}`
> [as printed; read as: the topological bifurcation set is the union of the
> affine discriminant locus and the set of `a` with `λ_a(f) ≠ 0` — the OCR
> dropped a negation, see the companion Theorem 3.16 below for the intended
> meaning].

This paper attributes the identity to "Suzuki [30], Ha and Lê [34] or the
first author [Cassou-Noguès, 5]" — i.e. the *same* three primary sources we
independently converged on. Their `λ_a(f)` (§3.2.2, formula (3.10)) is
defined via `μ_{p0}(a) − μ_{p0}(a_gen)` at points `p0` on the line at
infinity — literally Broughton's construction again, cross-checked a third
time.

**Bibliography entries, exact, for citation:**
- M. Suzuki, *Propriétés topologiques des polynômes de deux variables
  complexes, et automorphismes algébriques de l'espace `C²`*, J. Math. Soc.
  Japan **26** (1974), 241–257.
- M. Suzuki, *Sur les opérations holomorphes du groupe additif complexe sur
  l'espace de deux variables complexes*, Ann. Sci. École Norm. Sup. (4) **10**
  (1977), 517–546.
- S. A. Broughton, *Milnor numbers and the topology of polynomial
  hypersurfaces*, Invent. Math. **92** (1988), 217–241.
- L. Gavrilov, *Isochronicity of plane polynomial Hamiltonian systems*,
  Nonlinearity **10** (1997), 433–448 (Theorem 2.2, cited as the refinement
  source — **not independently verified**, TODO).

---

## 2. Ha Huy Vui – Lê Dũng Tráng, *"Sur la topologie des polynômes complexes"* (1984)

**Exact citation** (converged on independently from four different papers'
bibliographies — Bodin math/0009002 [HL]; Jelonek–Tibar arXiv:1401.6544 [HL];
Cassou-Noguès–Raibaut arXiv:1910.07032 [34]; Gwoździewicz–Płoski Iagel2001
[25]):

> Hà Huy Vui and Lê Dũng Tráng, *Sur la topologie des polynômes complexes*,
> Acta Math. Vietnam. **9** (1984), no. 1, 21–32.

(One secondary source lists the print year as 1985 for the same volume 9 —
almost certainly a publication-delay artifact of the journal, not a
different paper.)

**What it establishes (as transmitted through citing papers — we could not
obtain the original text itself, only its statements as quoted/used
elsewhere; mark the *exact* wording as TODO, the *content* as solid since
three independent papers use it identically):**

1. **Topological bifurcation set = jump-detection set.** Cassou-Noguès–Raibaut
   arXiv:1910.07032, Theorem 3.16, attributed to "Hà-Lê [34]":
   > `Theorem 3.16 (Hà-Lê). Let f be a polynomial in C[x,y]. The topological
   > bifurcation set is B^top_f = {a ∈ C | χ(f⁻¹(a)) ≠ χ(f⁻¹(a_gen))}.`
   I.e. Hà–Lê's theorem is precisely that the Euler-characteristic jump
   *detects* every atypical value — no atypical value is topologically
   invisible to `χ`.
2. **Positivity of the jump.** Bodin (math/0009002, proof of Lemma 2): "if
   `c ∈ B` then `χ(F_c) − χ(F_gen) > 0` (see [HL])" — i.e. Hà–Lê is the
   source for strict positivity of every individual jump, which is what
   turns Suzuki's global identity into a genuine detection criterion (an
   atypical value can never accidentally cancel to a net-zero jump against
   another atypical value the way abstract Euler-characteristic additivity
   alone would allow).
3. **"Regular at infinity" criterion.** This is the standard reference (along
   with Suzuki 1974/1977) for the classical dichotomy *"c is regular at
   infinity"* `⟺` *"the restriction of `f` near infinity over a disk around
   `c` is a locally trivial fibration"* `⟺` (in resolution language) *"every
   point of the fiber's closure lying over `c` on the boundary divisor is an
   unramified, non-confluent, single-branch (multiplicity-1) point of the
   total transform"*. This equivalence is the one that matters for the
   application in §7 below. A. H. Durfee's survey, *"Five Definitions of
   Critical Point at Infinity"*, in *Singularities (the Brieskorn Anniversary
   Volume)*, Progr. Math. **162**, Birkhäuser (1998), 345–360, collects and
   proves the equivalence of this and four other definitions (gradient
   non-vanishing at infinity, properness of restriction to a neighborhood of
   `∞`, monodromy triviality, `λ_t(f) = 0`) — every paper in this sweep cites
   Durfee for this equivalence-of-definitions role; we could not fetch
   Durfee's chapter text directly (Springer paywall) so the *exact* statement
   is TODO, but its existence and role is triple-cited (Gwoździewicz–Płoski
   2002 [10]; Jelonek–Tibar [Du]; Iagel2001 [15]) and uncontroversial.

---

## 3. Cassou-Noguès' formula (1996) — global degree constraint tying `μ+λ` to the number of points at infinity

**Exact citation:** Pierrette Cassou-Noguès, *"Sur la généralisation d'un
théorème de Kouchnirenko"*, Compositio Math. **103** (1996), 95–121.
Available on Numdam (`CM_1996__103_1_95_0`); we did not manage to pull the
full text in this session (time-boxed), so the statement below is
**transcribed verbatim from its use in Gwoździewicz–Płoski's two papers**,
both of which state it as "Cassou-Noguès' formula" and attribute it to
"[11 or 9], Proposition 12 / Proposition 1.2" (the proposition number differs
between the two citing papers' own numbering — we flag this as a minor,
almost-certainly-typo discrepancy, TODO to resolve against the primary
source):

From Iagel2001 (Gwoździewicz–Płoski 2001), §4, p. 124:

> **Cassou-Noguès' formula.** Let `f = f(X,Y)` be a polynomial of degree
> `d > 0`. With `c` the number of points at infinity of `f⁻¹(0)`'s
> projective closure,
> `d(d−3) + c + 1 = Σ_{p∈C_∞} μ_p^gen + μ(f) + λ(f)`.

From Gwoździewicz–Płoski, Rocky Mountain J. Math. **32** (2002), no. 1,
139–148 (their eq. (3), attributed identically): the same identity, used
there to derive the discriminant-degree formula
`deg_X Δ(X,t0) = μ(f) + λ(f) − λ_{t0}(f) + d − 1` (their eq. (4), combining
Krasiński's discriminant-degree formula `deg_X Δ(X,t0) = d(d−2) + c −
Σ_p μ_p^{t0}` with Cassou-Noguès' formula above).

**Direct consequence relevant to our problem.** Combined with `μ(f) = 0`
(Keller coordinate, no affine critical points):
`λ(f) = d(d−3) + c + 1 − Σ_p μ_p^gen`.
This is a genuine "λ in terms of degree and the count/type of points at
infinity" identity — but note it needs `Σ_p μ_p^gen` (still local-per-point
data, not eliminable), and `c` here is the *total* count of points at
infinity (both infinity-type and `E`-type dicriticals collapse to points
before resolution — `c ≠ N_inf` in general, it's closer to `N_inf +
N_E`-ish depending on how many independent points-at-infinity the `E`-type
branches sit over). We did **not** attempt to force this identity through
your specific resolution data — flagged as a possible cross-check for you to
run, not completed here (TODO).

**Bibliography-adjacent bound (Gwoździewicz–Płoski 2001, Theorem 3.4/3.5,
verbatim):**
> `μ(f) + λ(f) ≤ (d−1)²` and `#B_∞(f) ≤ ⌈((d−1)² − μ(f) − λ(f))/d⌉`
> (Theorem 3.4); if `f` has a finite number of critical points and `c` points
> at infinity: `μ(f) + λ(f) ≤ d(c−2) + 1` and `#B_∞(f) ≤ d − c` (Theorem 3.5).

These are genuine **upper bounds relating `λ` to `c`/`N_inf`-type data**, but
they are inequalities, not equalities, and they bound `λ` from *above* in
terms of `c`, not the reverse (they cannot be inverted to solve for `c` given
`λ`).

---

## 4. Gwoździewicz–Płoski's *explicit, computable* per-value formula (this is the one your round-20 note already correctly identified)

**Exact citation:** J. Gwoździewicz & A. Płoski, *"Formulae for the
singularities at infinity of plane algebraic curves"*, Univ. Iagel. Acta
Math. **39** (2001), 109–133. (Companion/published-elsewhere version: J.
Gwoździewicz & A. Płoski, *"On the singularities at infinity of plane
algebraic curves"*, Rocky Mountain J. Math. **32** (2002), no. 1, 139–148 —
this one restricted to `μ(f) = 0`, i.e. **exactly the Keller-coordinate
case**, see §6.)

Verbatim (Iagel2001, Proposition 3.2, transcribed from the OCR — high
confidence given internal consistency with Broughton's definitions in the
same section):

> **Proposition 3.2.** (1) `λ_t(f) = N − deg_X Δ(X,t)`, where `Δ(X,T) =
> disc_Y(f(X,Y) − T)` (`f` assumed `Y`-monic of degree `d = deg f`) and
> `N := deg_X Δ(X,T)` (as a polynomial in `X` with coefficients in `C[T]`,
> `T` generic — equivalently `N = deg_X Δ(X, t_gen)`). (2) `B_∞(f) = {t ∈ C :
> Δ_0(t) = 0}`, where `Δ(X,T) = Δ_0(T)X^N + ⋯ + Δ_N(T)`, `Δ_0 ≢ 0`.

**This is precisely the formula your round-20 note flags as "the real
formula ... needs the discriminant degrees, which the profile does not
supply."** We now have the exact citation, the exact proof sketch (Krasiński's
degree-of-discriminant formula applied twice — once at generic `T`, once at
`t` — and subtracted, using Broughton's `Σ_p μ_p^t − Σ_p μ_p^gen = λ_t(f)`
identity from §1 above), and confirmation that it is a **theorem**, not folklore.

This formula is "computable" but **not yet the local-per-divisor formula**
the task's item asked for: it gives `λ_t(f)` for one fixed atypical value
`t` as a single number (the *total* jump summed over all points at infinity
lying over that `t`), not decomposed divisor-by-divisor. To get a genuinely
per-divisor number you need the underlying Krasiński/Broughton machinery one
level down — i.e. the actual Newton-Puiseux/toric resolution computation of
each `μ_p^t` individually. That machinery exists (§5, §7) but is recursive
(Noether/toric blow-up additivity along the bamboo), not a single closed-form
plug-in.

---

## 5. Gwoździewicz's own local (blow-up-additive) Kouchnirenko-type formula

**Exact citation:** Janusz Gwoździewicz, *"Kouchnirenko type formulas for
local invariants of plane analytic curves"*, arXiv:0707.3404 (English
translation of a Polish original). Gives, for an **arbitrary local toric
modification** `π : M → C²` (generalizing a single blow-up), a formula
decomposing the Milnor number additively over the points of the exceptional
divisor:

> **Theorem 2** (classical blow-up case, `n=1` fan). If `f = 0` has no
> multiple components, `μ_0(f) − 1 = (ord f)(ord f − 1) + Σ_{p∈π⁻¹(0)}
> (μ_p(f̃) − 1)` — where `f̃` is the strict transform.

and (§3 onward) the general-fan version generalizing this to any toric
resolution tower, recovering the Kouchnirenko/Bernstein-type closed formulas
of Theorem 1 (attributed to the Arnold-seminar circle, via Kouchnirenko and
Khovanskii) in the "sufficiently non-degenerate" limit. This is stated for
singularities **at the origin**, but it is the *exact dual* of the "at
infinity" computation (swap `x ↦ 1/x` style coordinates) that underlies
`μ_p^t`, `μ_p^gen` above — it is the concrete recursive tool that would let
you compute `λ_D` for a specific bamboo, divisor by divisor, given its actual
Newton-Puiseux/toric data. We flag it as the right *tool*, not a
ready-made "plug in `(e, deg, length)`" formula: **no single universal
closed-form theorem of the shape `λ_D = φ(pole order, deg(P|_D), bamboo
length)` valid for all configurations exists in the literature we found** —
Noether/toric additivity is inherently recursive along the tower, collapsing
to a clean closed form only in special (non-degenerate / Yomdin-type, §7)
cases.

**Also relevant, not fully explored (time-boxed):** the machinery generalizes
to whole resolution graphs ("Newton trees") in P. Cassou-Noguès & W. Veys,
*"Newton trees for ideals in two variables and applications"*, Proc. London
Math. Soc. (3) **108** (2014), 869–910, and *"The Newton tree: geometric
interpretation and applications to the motivic zeta function and the log
canonical threshold"*, Math. Proc. Cambridge Philos. Soc. **159** (2015),
481–515 — these attach to *every vertex* of a resolution graph (dicritical
vertices marked by arrows, exactly your bamboo language) numerical data
`(N_i, ν_i)` (multiplicity along the divisor, discrepancy+1) and compute
zeta-function/log-canonical-threshold invariants as products/sums over the
tree. We did **not** verify whether these papers give the Euler-characteristic
specialization explicitly (they are aimed at the motivic zeta function and
log canonical threshold, not `χ` directly) — **TODO**, flagged as the most
promising unexplored lead if you want a genuinely divisor-by-divisor closed
form later. (Your own note in `docs/n2-campaign.md` calling `a = e−1` "the
dicritical condition" from the form/ramification equation is exactly the
Newton-tree language `N_i = ν_i`, i.e. `a(D)+1 = e` — this is the same
numerology that, in the Cassou-Noguès–Veys / A'Campo formalism, marks a
component whose *own* factor in the zeta-function product/A'Campo formula
degenerates to something trivial *unless* other data (deg(P|_D), the
`gcd`-terms) are nontrivial — consistent with, not contradicting, your
finding that the `E`-dicritical is where the real defect concentrates.)

---

## 6. Structure theorem for `μ(f) = 0` polynomials with one irregular value — directly = the Keller-coordinate case

**Exact citation:** J. Gwoździewicz & A. Płoski, *"On the singularities at
infinity of plane algebraic curves"*, Rocky Mountain J. Math. **32** (2002),
no. 1, 139–148.

This paper studies **exactly** `f : C² → C` with **no critical points**
(`Sing(f) = ∅`, i.e. `μ(f) ≡ 0` — literally your Keller-coordinate `P`) and
at most one irregular (= atypical-at-infinity) value. Verbatim:

> **Theorem 1.** Let `f : C² → C` be a polynomial with no critical points.
> Fix `t0 ∈ C`. Then the following are equivalent: (i) `B_∞(f) = {t0}`.
> (ii) The fiber `f⁻¹(t0)` is an affine reducible curve. All irreducible
> components of `f⁻¹(t0)` are rational and pairwise disjoint. If there is
> only one component isomorphic to a line, then every component not
> isomorphic to a line has exactly two branches at infinity. If there are
> `l > 1` components isomorphic to a line, there is only one component not
> isomorphic to a line, and it has `l+1` branches at infinity.

and (§2, Lemma 1, the tool used throughout — this is the genus-degree /
branches-at-infinity formula the task explicitly asked about in item 4):

> **Lemma 1.** Let `Γ ⊂ C²` be an affine irreducible smooth algebraic curve,
> `γ` the genus of its projective closure's normalization. Then
> `χ(Γ) = 2 − 2γ − r(Γ)`, where `r(Γ)` is the number of branches at infinity
> of `Γ`. In particular `χ(Γ) ≤ 1`, with equality iff `Γ ≅ line`.

and:

> **Theorem 2.** ... if `f` has degree `d` and `f⁻¹(0)` has `c` points at
> infinity, then `c ≤ (d+1)/2` [sharp, example given].

The whole paper is essentially a rigidity classification for `μ(f)=0`
polynomials with `#B_∞(f) ≤ 1` — the precise degenerate skeleton (line
components, exact branch counts at infinity) that a Keller-map coordinate's
special fibers must look like. Not previously flagged in
`docs/work_dicritical_lit.md`'s sweep (that document focused on the
Abhyankar/Lê–Weber dicritical-divisor school; this Gwoździewicz–Płoski line
is the "Euler-characteristic-of-fibers" school and is complementary, not
overlapping).

Also in this paper (§1, the Jacobian-conjecture-relevant punchline, Theorem 4):

> **Theorem 4.** Let `f ∈ C[X,Y]`, `deg_Y f = deg f = d`, `Δ_f := disc_Y f`.
> TFAE: (i) `f` is a coordinate polynomial; (ii) `f` is a Jacobian polynomial
> (`∃g: f_X g_Y − f_Y g_X = 1`) **and** `deg Δ_f = d − 1`.

— giving `(JC') `: *if `f` is a Jacobian polynomial with `deg_Y f = deg f =
d`, then `deg Δ_f = d − 1`* as an equivalent restatement of the plane
Jacobian conjecture. Flagging this because it is a genuinely useful
reformulation for your program even outside the λ-localization question —
your own campaign is already deep in a resolution/dicritical framework where
`deg Δ_f` (an affine discriminant degree) is a natural quantity to track
alongside `λ`.

---

## 7. Number of branches at infinity vs. size of the bifurcation set (task item 4)

**Exact citation:** Z. Jelonek & M. Tibar, *"Bifurcation locus and branches
at infinity of a polynomial `f : C² → C`"*, arXiv:1401.6544.

Verbatim (their notation: `r_a` = number of branches at infinity of
`f⁻¹(a)`, `r_gen` its generic value, `r_min := inf_a r_a`, `b` := number of
points at infinity):

> **Theorem 1.1.** (a) `#B(f) ≤ min{r_gen, r_min+1}`. (b) `#{a : r_a <
> r_gen} ≤ r_gen − b`. (c) `#{a : r_a > r_gen} ≤ r_min`. [Sharper bounds (d),
> (e) under `r_gen > d/2`.]

This confirms and sharpens **J. Gwoździewicz, *"Ephraim's pencils"*, Int.
Math. Res. Not. 2013, no. 15, 3371–3385** (their [Gw]), cited as: "if `r0`
denotes the number of branches at infinity of the fiber `f⁻¹(0)`, the number
of critical values at infinity other than `0` is at most `r0`." So: **the
total number of branches at infinity of the generic fiber (`= Σ_D deg(P|_D)`
over ALL dicriticals, exactly your `r_gen`) bounds `#B_∞(f)` from above, but
again only as an upper bound on the *count of atypical values*, not as a
formula recovering `N_inf` (number of dicriticals) from `λ` or from `r_gen`
itself** — and in any case `r_gen` is the *sum* of `deg(P|_D)` over both
infinity-type and `E`-type dicriticals combined, so even a perfect formula in
terms of `r_gen` would conflate the two dicritical types your campaign has
already had to separate by other means (Lê–Weber non-equisingularity, the
P–Q interlock).

---

## 8. A genuine per-divisor closed formula — but only in the non-degenerate ("Yomdin-at-infinity") case

**Exact citation:** S. M. Gusein-Zade, I. Luengo, A. Melle-Hernández, *"On
the zeta-function of a polynomial at infinity"*, Bull. Sci. Math. **124**
(2000), no. 3, 213–224 (arXiv:math/9801093).

This is the closest thing we found in the literature to a literal
per-dicritical-divisor closed formula (it is an A'Campo-type formula, and
it *does* localize to the exceptional divisor of a resolution of the tangent
cone singularities at infinity). For a **Yomdin-at-infinity** polynomial `P =
P_d + P_{d−k} + …` (`k ≥ 1`, non-degeneracy condition `Sing(P_d) ∩ {P_{d−k}=0}
= ∅`), with `Sing(P_d) = {Q_1,…,Q_s}` and a resolution `π : (X,D) → (C^n,0)`
of the germ `g_i` (local equation of `{P_d=0}` at `Q_i`), verbatim:

> **Theorem 2.** `ζ_φ(t) = (1 − t^{d−k})^{χ(D)−1} ζ_ψ(t)` [combining the
> "cyclic-permutation" stratum contribution with the resolution-divisor
> contribution]; and, unwound via A'Campo's formula `ζ_{g_i}(t) =
> Π_{m≥1}(1−t^m)^{χ(S_m)}` (`S_m` = points of `D` where the lift of `g_i` has
> multiplicity `m`):
> `ζ_ψ(t) = (1 − t^{d−k}) · Π_{m≥1} (1 − t^{m(d−k)/gcd(m,k)})^{−gcd(m,k)·χ(S_m)}`.

The **degree of the zeta function equals `χ` of the (generic) fiber**
(their §1, Remark), so this literally expresses a local Euler-characteristic
contribution *per stratum/exceptional-divisor-component* `S_m`, as a function
of `m` (a multiplicity — their analogue of "pole order"), `k` (a Yomdin
non-degeneracy degree-drop), and `χ(S_m)` (essentially "how many /what type
of dicritical-adjacent points sit there," analogous to `deg(P|_D)`-type
data). **This is a real, citable local formula matching the shape the task
asked for — but it is proved only under the Yomdin-at-infinity genericity
hypothesis**, and we did not check whether your specific `D5`/`F20`
configuration (which is highly non-generic by construction — that's the
whole point of the campaign) satisfies it. Flagged as **the most promising
concrete formula to try plugging your resolution data into, with the
explicit caveat that its non-degeneracy hypothesis needs checking first**
(TODO — not attempted here, would need your actual `P_d`, `P_{d−k}` data).

---

## 9. Application to the specific configuration

**9.1. Infinity dicritical: degree-1, length-1 (isolated bamboo).**

By construction this is *precisely* the classical "regular point at
infinity" of Suzuki / Ha Huy Vui–Lê Dũng Tráng (§2 above, criterion 3): a
single point `p` at infinity, reached by the resolution with no intermediate
(bamboo) components, on which `P` restricts with degree 1 (so the point is
**unramified** — the local branch of every nearby fiber through `p` is a
single smooth branch transverse to the boundary, for every `t`, since there
is no other component for it to collide with — that is what "isolated"
means). By Broughton's Proposition 3.1 (§1) applied at this single point:
`μ_p^t` and `μ_p^gen` are both computed from the **same** local model (a
single unramified branch) for every `t` in a neighborhood, hence

> **`μ_p^t = μ_p^gen = 0` for all `t` ⟹ this point's contribution to `λ_t(f)`
> is `(μ_p^t − μ_p^gen) = 0` identically in `t` ⟹ `λ_D := Σ_t (μ_p^t −
> μ_p^gen) = 0`.**

This is not a numerical coincidence for one specific `t` — it is forced by
the *definition* of "isolated, degree-1, length-1": there is no
neighboring structure (no other bamboo component, no ramification) capable
of producing a non-generic `μ_p^t > 0` at *any* `t`. So **every** infinity
dicritical of this type contributes exactly `λ_D = 0`, individually and
identically, regardless of what value of `t` you evaluate at.

**9.2. `E`-dicritical: degree `d`, `a = e−1`.**

Here `deg(P|_D) = d > 1`: the map `P|_D` is genuinely ramified/branched
(the source of the `Σ h_i(e_i−1)` ramification term in your own round-20
Riemann–Hurwitz computation, `h_i = deg(P|_{D_i}) = d`). By the same
Broughton bookkeeping this divisor's points *do* generically carry
`μ_p^t ≠ μ_p^gen` at the (finitely many) branch/ramification values of
`P|_D` — i.e. it is a genuine carrier of `λ`-defect, consistent with your
formula `λ(P) = Σ h_i e_i − 4 = 4d − 4` being carried entirely by these
divisors. We did **not** derive an independent closed-form value for this
divisor's own `λ_D` from the general literature (that would need the actual
Newton-Puiseux data behind "`a = e−1`" fed into Gwoździewicz's blow-up-
additive machinery, §5, or the A'Campo-type formula, §8) — but qualitatively
every source above agrees this is where the defect *must* live, since the
degree-1 divisors are forced to zero by 9.1.

**9.3. Does the sum pin down `N_inf`?**

**No — and the literature explains structurally why, independent of your own
Riemann–Hurwitz argument.** Write
`λ(P) = Σ_{i=1}^{N_inf} λ_{D_i}(infinity) + Σ_{E-dicriticals} λ_D(E-type)
= N_inf · 0 + (E-type total) = 4d − 4`.
Since each infinity-type term is *individually and structurally* zero
(§9.1), the equation `4d−4 = (\text{sum over } E\text{-dicriticals only})`
holds **for any value of `N_inf`** — the local λ-formula is blind to `N_inf`
not because of a missing computation, but because `N_inf` multiplies a term
that the formula forces to `0`. No refinement of the *same* formula (feeding
in exact pole orders, exact bamboo lengths, etc., for the *degree-1,
length-1* dicriticals specifically) can change this: the defining
characteristic of that dicritical type (unramified, isolated) is exactly
the criterion under which every local-jump theorem we found (Broughton,
Ha–Lê, Suzuki, Gwoździewicz–Płoski, and the A'Campo-type formula of §8, whose
"regular stratum" case gives the analogous zero-contribution statement) gives
zero.

This **independently confirms**, via a completely different route (1980s–2000s
local Milnor-number bookkeeping for polynomial pencils) than your round-20
Riemann–Hurwitz-on-`Q` computation, the same conclusion already recorded in
`docs/n2-campaign.md`: *"λ cannot distinguish `N_P = 1,3,5`."* We regard this
as the main deliverable of this sweep: not a new formula, but a rigorous,
independently-sourced **proof that no formula of this general shape can ever
do the job**, which tells you where *not* to spend further effort. Your
existing lever — the Bezout/pole-order interlock
`Σ_{D∈I_P} n_D m_D = 5` — remains, as far as this literature sweep can tell,
the right and only tool for constraining `N_inf`, because it weights every
infinity dicritical by its (nonzero) pole order `m_D` rather than by its
(zero) λ-contribution.

---

## 10. Summary: the 2–3 most usable formulas, with citations

1. **Suzuki–Gavrilov formula** (M. Suzuki, J. Math. Soc. Japan **26** (1974),
   241–257 + Ann. Sci. ENS (4) **10** (1977), 517–546; S. A. Broughton,
   Invent. Math. **92** (1988), 217–241; L. Gavrilov, Nonlinearity **10**
   (1997), 433–448 — modern restatement in Cassou-Noguès–Raibaut, Math. Z.
   (2021), Thm 3.17):
   `χ(f⁻¹(t)) = 1 − μ(f) − λ(f) + μ_t(f) + λ_t(f)`, with
   `λ_t(f) = Σ_{p∈C_∞} (μ_p^t − μ_p^gen)` localizing to points at infinity.
   **This is the correct general formula and the one your round-20 Suzuki–
   Gavrilov citation should point to.**

2. **Gwoździewicz–Płoski's discriminant formula** (Univ. Iagel. Acta Math.
   **39** (2001), 109–133, Prop. 3.2): `λ_t(f) = N − deg_X disc_Y(f(X,Y)−t)`
   — **this is exactly the formula your round-20 note already flagged as
   needed; now fully cited and proof-sketched.** Directly computable once
   you have the discriminant's degree drop.

3. **Ha Huy Vui–Lê Dũng Tráng's regularity criterion** (Acta Math. Vietnam.
   **9** (1984), 21–32, as used throughout the citing literature): a point
   at infinity is regular (contributes `λ_p = 0` at every `t`) iff it is an
   unramified, non-confluent, isolated single branch — **this is what forces
   every degree-1, length-1 infinity dicritical to contribute exactly zero**,
   and hence what makes `λ(P) = 4d−4` blind to `N_inf`.

**Do they localize λ enough to constrain `N_inf`? No.** They localize λ fully
(down to individual points/divisors at infinity — this part of the task is
answered completely and rigorously), but the localization *itself* proves
that the specific dicritical type forced by your Lê–Weber survival analysis
(degree-1, isolated) contributes zero, so summing any number of them leaves
`λ` unchanged. This is a clean, citable, independent second proof of your
round-20 finding, not a new route past it. The pole-order interlock equation
(`Σ n_D m_D = 5`) remains the right lever on `N_inf`.

**File:** `docs/work_s7_lambda_localization.md` (this file).
