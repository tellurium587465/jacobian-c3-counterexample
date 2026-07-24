# Literature sweep: dicritical divisor structure vs. hypothetical degree-5 plane Keller maps

Date of sweep: 2026-07-24. Method: WebSearch + WebFetch (arXiv abstracts/ar5iv, direct PDF
download + Read tool for papers that WebFetch's summarizer mangled). Scope per assignment:
Lê–Weber, Nguyen Van Chau, Abhyankar/Luengo/Artal Bartolo school, Gwoździewicz–Płoski,
Cassou-Noguès, plus whatever turned up on realizability of dicritical covering degrees.

Context assumed (as given in the task): a hypothetical plane Keller map of geometric degree 5,
irreducible Jelonek/exceptional curve E, dicritical boundary divisors mapping onto E, with two
candidate escaping-sheet profiles at a generic point of E: **{2,2}** (D5 monodromy, two boundary
points each of transverse multiplicity 2) vs. **{4}** (F20 monodromy, one boundary point of
multiplicity 4, on a divisor mapping *birationally* onto E).

Rating key: **DIRECT** (bears on this exact question), **SUPPORTING** (relevant background,
no sharp bound), **NOT-TRANSLATABLE** (real theorem, but its hypotheses don't match our
setting without extra argument — flagged explicitly), **UNVERIFIED** (could not confirm the
precise statement; best URL given).

---

## 0. Single most decisive fact found (not about dicriticals per se)

**T.T. Moh, "On the Jacobian conjecture and the configuration of roots," J. Reine Angew. Math.
340 (1983), 140–212.**

Cited secondhand (could not retrieve the paper itself — De Gruyter paywall; see
<https://www.degruyterbrill.com/document/doi/10.1515/crll.1983.340.140/html> and
<https://eudml.org/doc/152524>), but the result is quoted verbatim, with citation, inside
Drużkowski's 1995 survey (full text obtained, see §1 below):

> "Recall that the two dimensional complex Jacobian Conjecture is true if
> max{deg f, deg g} < 100, cf. [Mo]." (L. M. Drużkowski, *The Jacobian Conjecture: survey of
> some results*, Banach Center Publications 31 (1995), p. 169)

**Rating: DIRECT, and decisive if the map is meant as an actual JC2 counterexample.** Moh's
theorem (proved by an enormous but finite configuration-of-roots case analysis, exactly the
kind of "escaping sheet" combinatorics the task is asking about, at infinity) already rules out
*any* genuine plane Jacobian pair of geometric degree 5 — degree 5 is far inside the proven range
deg < 100. So a hypothetical degree-5 Keller map with a {2,2}- or {4}-dicritical profile cannot
be an actual counterexample to JC2; if the project's degree-5 map is intended as a real
counterexample, it is already dead on arrival independent of the dicritical analysis. (If instead
it is a toy/structural model used for some other purpose — e.g. an analogy carried over from the
n=3 project in this same account, or a controlled test case for auditing the KV/dicritical
machinery — this caveat should be stated explicitly wherever the degree-5 example is used, since
readers will otherwise assume it is being proposed as a real counterexample.) I could not
independently verify Moh's proof method beyond this one quoted sentence — flagging the primary
paper as **UNVERIFIED in its interior details**, only the "deg < 100 ⇒ JC2 true" headline is
confirmed (twice, independently quoted in two different secondary sources).

---

## 1. Lê Dũng Tráng & Claude Weber — the primary geometric source

**Lê Dũng Tráng and C. Weber, "A geometrical approach to the Jacobian conjecture for n = 2,"
Kodai Math. J. 17 (1994), 374–381.** Full text obtained (PDF downloaded via
<https://projecteuclid.org/journals/kodai-mathematical-journal/volume-17/issue-3/A-geometrical-approach-to-the-Jacobian-conjecture-for-n2/10.2996/kmj/1138040028.pdf>,
read directly — WebFetch's summarizer garbled this paper on first pass; the PDF itself is clean).

This is the paper that actually defines "dicritical" for the Jacobian problem in the sense the
task describes, and it is the direct ancestor of the whole Abhyankar–Luengo–Artal Bartolo
dicritical-divisor industry (their own bibliographies cite it as [LeW]).

Setup, verbatim (their notation): for a polynomial `f` of degree `d`, minimal compactification
`π: X → C²`'s boundary divisor is `D∞(X)`, with intersection tree `A`; `φ := F/T^d ∘ π`; **"a
component of `D∞(X)` on which `φ` is not constant is called *dicritical*."** Key structural facts
they prove:

- **Bamboo theorem**: "Each connected component of `A − A∞` is a bamboo which contains a unique
  dicritical component of `φ` and this dicritical component is the only irreducible component of
  the bamboo which meets `A∞`." — i.e. dicriticals are isolated one-per-bamboo; this matches the
  task's setup (D5: two separate dicritical boundary points; F20: one).
- **Case 2 (exactly our F20-type shape)**: "all the connected components [of `A − A∞`] have only
  one vertex (which is a dicritical component of `φ`) and the restriction of `φ` on at least one
  dicritical component has degree strictly greater than one." Their own worked example of this
  case is `f(X,Y) = X − X⁴Y⁴`.
- **The key Proposition (DIRECT hit)**: "Assume that `f` has no critical point and that `f` is
  not a locally trivial fibration. If all the connected components of `A − A∞` contain only one
  vertex, there is at least one dicritical component `D` of `φ` on which `φ` has a critical
  point." Proof sketch: if `φ` had *no* critical point anywhere, Ehresmann's lemma forces `φ` to
  be a locally trivial fibration on `C`, forcing Euler characteristic of the general fiber
  `= 1 + ℓ` where `ℓ` = number of dicritical components; since the fiber is `C` (χ = 1),
  **necessarily `ℓ = 1`**, and then "**a result of T.T. Moh ([Mo] = Moh, *On analytic
  irreducibility at ∞ of a pencil of curves*, Proc. AMS 44 (1974), 22–24) interpreted in our
  setting implies that the restriction of `φ` to this unique component must be of degree 1**,"
  contradicting the assumed critical point. I.e.: *a single-dicritical (ℓ=1), critical-point-free
  pencil is automatically forced to restrict with degree 1 on that one dicritical* — degree 1
  is not an extra assumption, it is a *consequence* of ℓ=1 plus no critical points on the whole
  pencil map φ (not the same statement as "birational" restricted to a Jacobian pair's escaping
  sheets — see translation caveat below).
- **Main Theorem (the actual exclusion criterion, DIRECT)**: for a Jacobian pair `(f,g)` with `f`
  having `C(f)=0` (no critical points) and `I(f)≠0` (not a fibration), `(f,g)` **cannot** be a
  Jacobian pair if either (1) there's a "strongly non-equisingular" component of `φ` not
  dicritical for `ψ = G/T^d'`, or (2) there's a strongly non-equisingular dicritical component
  `D0` for `φ` where `φ|D0` **or** `ψ|D0` has **degree one**. ("Strongly non-equisingular" means:
  `D0` sits in a bamboo of length ≥2, or `φ` itself has a critical point on `D0`.)
- **Sharpest single corollary (DIRECT, exactly of the requested shape)**: "`f` cannot be a
  Jacobian polynomial if there exists a dicritical component `D0` of `φ` in `X` which is strongly
  non-equisingular and such that the multiplicity of `D0` in the canonical divisor of `X`
  confined at infinity **either 1) is strictly negative or 2) is positive and the restriction of
  `φ|D0` is of degree one**." This is a real theorem of exactly the form the task asked to hunt
  for ("Keller map cannot have a dicritical … birational onto its image"). It is *conditional*:
  it fires only if `D0` is strongly non-equisingular, i.e. only if the source-side resolution
  puts `D0` at the end of a length-≥2 bamboo, or `φ` has a critical point on `D0` itself.

**Translation caveat (must flag to the audit team).** Lê–Weber's `φ` is the projectivized
extension of a *single* coordinate polynomial `f` (its own pencil `f = const`, compactified via
one coordinate function to `P¹`), and "dicritical" here means non-constant restriction of *that
one function's* pencil map, on the *source-side* resolution of `f` alone. The task's setup is
about boundary divisors of a resolution of the **map** `F=(P,Q)` mapping onto the **target-side**
Jelonek curve `E`. These are related (a target-side dicritical for `F` is presumably dicritical
for at least one of `φ = P/T^{deg P}` or `ψ = Q/T^{deg Q}` on a common resolution) but are not
verbatim the same object, and the "multiplicity 4" in the task (a *transverse* ramification
order of the map along the fiber direction) is not obviously the same number as Lê–Weber's
"multiplicity of `D0` in the canonical divisor confined at infinity" (a discrepancy/adjunction
type invariant computed purely from the blow-up sequence, independent of `φ,ψ`). **Actionable
item for the audit**: check (a) whether the F20 candidate's single dicritical is "strongly
non-equisingular" for either coordinate function alone, and (b) compute its canonical-divisor
multiplicity at infinity; if strongly non-equisingular **and** (negative mult., or positive mult.
with degree-1 restriction of either coordinate function alone), Lê–Weber's 1994 Main Theorem
already excludes the configuration outright, with no further dicritical theory needed. If it is
*not* strongly non-equisingular (e.g. bamboo length 1 and no critical point of φ or ψ on D0), this
theorem is simply silent — it does not clear the configuration, it just doesn't apply.

**Related/derivative paper (UNVERIFIED, could not fetch)**: Lê Dũng Tráng & C. Weber,
*"Polynômes à fibres rationnelles et conjecture jacobienne à 2 variables,"* C. R. Acad. Sci.
Paris Sér. I Math. 320 (1995), 581–584. Only the title/venue was confirmed via search; this is
presumably where "nice rational polynomial" is formalized and where the statement "Lê proved a
Keller map is invertible if P is a rational polynomial and simple" (per secondhand paraphrase,
see §2 below) is actually proved. Flagging for a follow-up fetch if a French-language database
is available (Numdam/Gallica).

---

## 2. Nguyen Van Chau — non-proper value set / exceptional-value-set papers

All items below were independently confirmed via arXiv abstract/full-text fetch (ar5iv mirror),
not just secondary paraphrase, except where marked.

### 2.1 arXiv:math/0305088, *"Non-proper value set and the Jacobian condition"* (Ann. Polon.
Math., per venue check)

Verbatim abstract: **"The non-proper value set of a nonsingular polynomial map from `C²` into
itself, if non-empty, must be a curve with one point at infinity."** This is exactly the
"one point at infinity" fact the task says is already assumed/used — **confirmed as a real,
citable theorem**, not folklore.

Further structural content (full text via ar5iv), **DIRECT / SUPPORTING for the escaping-sheet
question**:
- **Theorem 1**: every irreducible component of the non-proper value set has a parametrization
  `ξ ↦ (Aξ^{md} + …, Bξ^{me} + …)`, `m ∈ N`, where `d/e = deg P / deg Q` in lowest terms.
- **Corollary 1**: the defining polynomial of the non-proper value set has the shape
  `R₀(u,v) = C(A^e u^e − B^d v^d)^M + Σ c_ij u^i v^j` with `0 ≤ id+je < Mde`.
- **Corollary 2**: branches at infinity of the value curve have Newton–Puiseux type
  `u = c v^{d/e} + …`.

**Assessment: SUPPORTING, translation needed.** This gives exactly the kind of "degree of the
parametrization of E near infinity by the escaping variable" data the task's `e_p` multiplicities
concern, but it's stated for the *value curve itself* (one coordinate chart of the *target*), not
directly as a per-boundary-point transverse multiplicity list. The exponent `m` here is a
*global* integer for a whole branch of the value curve, and the way it splits into a sum over
several dicritical source divisors (i.e. whether it can appear as `m=2` twice, from two different
source points, vs. `m=4` once from a single birational-onto-E source divisor) is not answered in
the abstract/theorem statements retrieved — would need the actual proof (Lemma 3, dicritical
series comparison) to see whether `M` (or `m`) is forced to be prime, or can be composite and
realized either way. Flag as an open translation gap, not a settled exclusion.

### 2.2 arXiv:math/0408048, *"Two remarks on non-zero constant Jacobian polynomial maps of C²"*
(Ann. Polon. Math. 82 (2003), 39–44)

Verbatim abstract: "We present some estimations on geometry of the exceptional value sets of
non-zero constant Jacobian polynomial maps of `C²` and its components." Full-text content
retrieved (ar5iv):
- **Theorem 1**: `u₀` belongs to the exceptional value set `E_P` iff "the line `u=u₀` [is]
  tangent to an irreducible local branch of `E_f`" (the compactified exceptional curve).
- **Theorem 2 / Corollary 3 (DIRECT-adjacent)**: the exceptional value set **cannot** be
  parametrized as `t ↦ (t^k, q(t))` for any `k∈N, q∈C[t]`; consequently **"the exceptional value
  set … cannot be a simply connected curve."**
- Technical machinery: dicritical Newton–Puiseux series `φ` of `f` with
  `f(x,φ(x,ξ)) = f_φ(ξ) + …`, `deg f_φ > 0`; non-dicritical series constrained to
  `deg p_φ(ξ)=1, q_φ(ξ)≡const≠0, b_φ>0`.

**Assessment: SUPPORTING.** Rules out the exceptional curve `E` being *simply connected*
(e.g. rules out `E ≅ C` = affine line as the image of the whole exceptional locus under a naive
single global parametrization of the stated shape), which is a genuine topological constraint on
`E`, but doesn't by itself distinguish {2,2} from {4} at a single generic point.

### 2.3 arXiv:0711.3894, *"Plane Jacobian conjecture for simple polynomials"*

Verbatim abstract: **"A non-zero constant Jacobian polynomial map `F=(P,Q):C²→C²` has a
polynomial inverse if the component `P` is a simple polynomial, i.e. if, when `P` extended to a
morphism `p:X→P¹` of a compactification `X` of `C²`, the restriction of `p` to each irreducible
component `C` of the compactification divisor `D=X−C²` is either degree 0 or 1."**

**Assessment: DIRECT, checklist item.** "Simple" is exactly a statement that *no* boundary
component of the source compactification, under the coordinate map `P` alone, has degree ≥2 onto
`P¹`. If either coordinate function of the hypothetical degree-5 map turns out to be simple in
this sense, the whole map is automatically invertible (excluded as a counterexample) — regardless
of the target-side E/dicritical story. Note again the translation gap versus the task's
target-side "birational onto E, multiplicity 4" language: "simple" bounds the *degree of D→P¹* for
a single coordinate's own pencil, not the *transverse multiplicity* of the full map `F` along `D`
in the direction transverse to `E`. A degree-1 (simple) component for `P` alone is compatible in
principle with a transverse multiplicity 4 for the pair `(P,Q)` jointly — these are different
axes and this paper does not itself settle whether our F20 profile forces or forbids `P` or `Q`
individually to be non-simple. (It almost certainly *must* force at least one to be non-simple,
by contrapositive, but that alone doesn't pin down which divisor or degree.)

### 2.4 arXiv:0905.3939, *"Pencil of irreducible rational curves and Plane Jacobian conjecture"*

Verbatim abstract: "We are concerned with the behavior of the polynomial maps `F=(P,Q)` of `C²`
with finite fibres and satisfying the condition that all of the curves `aP+bQ=0`, `(a:b)∈P¹`, are
irreducible rational curves. The obtained result shows that such polynomial maps `F` is
invertible if `(0,0)` is a regular value of `F` or if the Jacobian condition holds." **Assessment:
SUPPORTING** — relevant if the whole pencil `aP+bQ=0` is assumed irreducible-rational (plausible
for a degree-5 map with a single rational Jelonek curve E), but doesn't isolate a dicritical
multiplicity profile.

### 2.5 arXiv:1005.3866, *"A note on the plane Jacobian conjecture"*

Verbatim abstract: **"It is shown that every polynomial function `P:C²→C` with irreducible fibres
of [the] same genus is a coordinate. In consequence, there does not exist counterexamples
`F=(P,Q)` to the Jacobian conjecture such that all fibres of `P` are irreducible curves of [the]
same genus."** **Assessment: SUPPORTING**, another "coordinate-forcing" sufficient condition,
not dicritical-multiplicity-specific.

### 2.6 arXiv:0804.3172, *"Plane Jacobian Conjecture for rational polynomials"*

Verbatim abstract: **"A non-zero constant Jacobian polynomial maps `F=(P,Q)` of `C²` is
invertible if `P` and `Q` are rational polynomials"** (rational polynomial ≡ generic fiber
diffeomorphic to a sphere with finitely many punctures, per a companion search result).
**Assessment: SUPPORTING**, same family as 2.3/2.5.

### 2.7 arXiv:0801.4138, *"Plane Jacobian problem for rational polynomials"* — **WITHDRAWN**

Verbatim: **"This paper has been withdrawn by the author due to a crucial error in the last lines
in the proof of Lemma 3.3."** **Do not cite as a valid result** — flagging explicitly since it
turned up prominently in searches and could be mistakenly folded into the "rational polynomials"
family above.

### 2.8 arXiv:0710.5212, *"A note on singularity and non-proper value set of polynomial maps of
C²"*

Full text (ar5iv). **Theorem 1.1**: relates a non-singular horizontal series `ψ` preceding a
dicritical series `φ` via degree constraints `(deg p_ψ, deg q_ψ) = (Nd, Ne)` for coprime `d,e`,
and leading-coefficient relations `p_φ(ξ) = Lcoeff(p_ψ)·C^d·ξ^{Dd} + …`. **Theorem 1.2**: for a
dicritical series with `a_φ=0, b_φ<0`, either `φ` is itself a singular series of `f`, or there's a
horizontal series `ψ` of `Q` that is singular for `f` with `ψ ≺ φ`. **Assessment: SUPPORTING,
NOT-TRANSLATABLE without more work** — genuine Newton–Puiseux constraints tying dicritical series
to singular (ramification) series, exactly the flavor of object the task's `e_p` are, but stated
in Chau's own coordinate/series bookkeeping that I was not able to map cleanly onto "how many
boundary points, what multiplicities" in the time available. Flagging as the single most promising
follow-up read for anyone trying to actually derive a {2,2}-vs-{4} exclusion from Chau's series
calculus.

---

## 3. Abhyankar / Luengo / Artal Bartolo / Heinzer — algebraic dicritical-divisor school

This entire school (papers listed below) grew out of Abhyankar's 2008 exposure to Lê–Weber-style
topological dicritical theory (explicitly stated in [AA1]'s own commentary, see below), and was
explicitly motivated by "getting control on the fibers of a Jacobian pair" — but the actual
theorems proved are almost all about **general** 2-generated ideals / pencils in an arbitrary
2-dimensional regular local ring, with **no Jacobian-condition hypothesis built into any theorem
statement** I could locate. This is an important, repeated translation gap across the whole
school — flagged once here rather than per-paper.

- **S.S. Abhyankar, "Dicritical Divisors and Jacobian Problem," Indian J. Pure Appl. Math. 41
  (2010), 77–97.** [Reference [Ab10] in the Abhyankar–Artal Bartolo papers below.] **UNVERIFIED**
  — could not retrieve full text or abstract (Springer-hosted, no open abstract found); only
  its existence/citation is confirmed, secondhand quote: "the dicritical divisor coming out of
  integrable holonomic systems gets married to the jacobian problem of algebraic geometry" (a
  colloquial line from a secondary summary, not a theorem statement). This is plausibly the
  single most directly on-topic Abhyankar paper by title, but I was unable to pin down its
  content — flagging as a priority follow-up if institutional access to Indian J. Pure Appl.
  Math. is available.

- **S.S. Abhyankar & I. Luengo, "Algebraic theory of dicritical divisors," Amer. J. Math. 133
  (2011), 1713–1732.** [AL1] Full text not retrieved (only secondary description: "the
  topological theory of dicritical divisors is algebraicized, making it valid for nonzero and
  mixed characteristic"). **UNVERIFIED in detail.**

- **S.S. Abhyankar & I. Luengo, "Spiders and multiplicity sequences," Proc. AMS 141 (2013),
  4071–4085.** [AL2] Cited repeatedly inside the curvette papers (below) as the source of the key
  lemma that for two curvettes `c, c'` of the *same* dicritical divisor `V`, the multiplicity
  sequences along the blow-up tower are *proportional*: `D'_j / θ(R,T,c') = D_j / θ(R,T,c)` for
  all `j`. **Not independently fetched — UNVERIFIED**, but directly cited (with this exact
  statement) inside [AA1] (§3, Example 3.8 discussion), which I did read in full — see next item.

- **S.S. Abhyankar & E. Artal Bartolo, "Algebraic theory of curvettes and dicriticals," Proc. AMS
  141 (2013), 4087–4102.** Full text obtained (downloaded PDF, read directly). This is dense
  commutative-algebra machinery (quadratic transforms, dicritical sets `D(R,J)` of a 2-generated
  ideal `J` in a 2-dim RLR `R`, contact numbers, curvette/arc bundles, Zariski index, a "Yoga
  Theorem" about brothers/cousins/friends of a curvette-bundle root). Its Theorem (2.7) gives the
  factorization of the integral closure `J^{-R} = GCD(J) · Π_V ζ_R(V)^{n(R,J,V)}` over all prime
  divisors `V`, with `n(R,J,V)` the "Zariski index" — this is the general machinery for how an
  ideal (pencil) factors through its dicritical divisors, each with an associated multiplicity.
  **No statement anywhere in this paper constrains the *number* of dicriticals or the specific
  *value* of a multiplicity for a Jacobian pair** — the closest it gets is generic existence/
  realizability results (Theorems 5.1/5.2: given any prescribed finite sequence of prime divisors
  `V_1,...,V_r` and any positive integers `n_1,...,n_r`, one can always construct a "curvette
  bundle" / ideal realizing exactly that multiplicity data). **Assessment: SUPPORTING /
  NOT-TRANSLATABLE.** If anything, the realizability direction of this paper is *mildly
  encouraging* for the {4}-profile's abstract combinatorial possibility (a single dicritical of
  any prescribed multiplicity is realizable *as a general pencil*), but says nothing about
  whether such a configuration can arise from a *constant-Jacobian pair* specifically — the extra
  Jacobian condition is exactly the missing ingredient this whole school doesn't address.

- **S.S. Abhyankar & E. Artal Bartolo, "Analytic theory of curvettes and dicriticals"** (posthumous,
  completed by Artal Bartolo after Abhyankar's death on 2012-11-02, per the paper's own preface;
  downloaded from Artal Bartolo's Zaragoza page,
  <https://riemann.unizar.es/geotop/WebGeoTo/Profes/eartal/papers/AnalyticDicritical.pdf>, read in
  full). Introductory/setup sections read; same character as above (curvette existence via
  completions, complementary curvettes) — **no Jacobian-specific content found** in the sections
  retrieved.

- **E. Artal Bartolo, I. Luengo, A. Melle-Hernández, "High-school algebra of the theory of
  dicritical divisors: atypical fibres for special pencils and polynomials,"** arXiv:1408.0743
  (J. Algebra Appl.). Verbatim abstract: "…we provide some elementary proofs of some S.S.
  Abhyankar and I. Luengo results for dicriticals in the framework of formal power series. Based
  on these ideas we give a constructive way to find the atypical fibres of a special pencil and
  give bounds for its number, which are sharper than the existing ones. Finally, we answer a
  question of J. Gwoździewicz finding polynomials that reach his bound." **Assessment:
  SUPPORTING** — this is specifically about counting/bounding *atypical fibers* of a "special
  pencil" (a term of art in this school, roughly a pencil with a distinguished dicritical
  structure), and constructs *sharp* examples achieving Gwoździewicz's bound — i.e. this line of
  work is oriented toward showing bounds are *tight*, which if anything supports the abstract
  realizability of unusual multiplicity profiles for special pencils in general, again without a
  Jacobian-pair-specific theorem.

- **S.S. Abhyankar & W.J. Heinzer, "Existence of dicritical divisors," Amer. J. Math. 134 (2012),
  171–192**, and **"Existence of Dicritical Divisors Revisited," Proc. Indian Acad. Sci. 121
  (2011), 267–290** (also mirrored as arXiv:1508.06015, verbatim abstract: **"We characterize the
  diacriticals of special pencils. We also initiate higher dimensional dicritical theory."**).
  **Assessment: SUPPORTING** — realizability/characterization results for special pencils in
  general, not Jacobian-pair-specific; full theorem statements not retrieved (abstract only).

- **E. Artal Bartolo & W. Veys, "Dicritical divisors and hypercurvettes," arXiv:2505.24648
  (2025).** Verbatim abstract: "…In a series of papers, Abhyankar and the first named author
  studied this setting in dimension 2, where the main result is that, **for any given `π`, there
  is a rational function `h` with a prescribed subset of exceptional components that are
  dicritical of some given degree**. … Here we use this concept to generalize the above result to
  arbitrary dimension." **Assessment: SUPPORTING, translation gap explicit.** This is a clean
  *general realizability* theorem: for any fixed resolution `π` of a point, you can always find
  *some* rational function realizing a prescribed dicritical pattern with prescribed degrees. This
  says the {4}-profile (one dicritical, birational onto its image, transverse multiplicity 4) is
  certainly realizable for *some* rational function on *some* surface — but again gives zero
  information about whether it's realizable for the very restrictive pair (P,Q) forming a Keller
  map (constant nonzero Jacobian everywhere, both P,Q polynomials, degree exactly 5, image curve
  E irreducible and rational, etc.). This is the recurring structural gap in the entire
  Abhyankar/Luengo/Artal Bartolo/Heinzer/Veys line: they solve the *pencil realizability* problem
  in full generality, which is necessary but nowhere near sufficient for the Jacobian problem.

- **W. Heinzer & D. Shannon, "Abhyankar's Work on Dicritical Divisors,"** arXiv:1707.06733 (survey).
  Verbatim abstract: "We discuss the work of Abhyankar on dicritical divisors with a special focus
  on the algebraic aspects of this work. We also discuss related work on local quadratic
  transforms, infinitely near points and Rees valuation rings of an ideal." **Assessment:
  UNVERIFIED in detail** (only abstract retrieved) but likely the best available *entry point/
  roadmap* into this literature if someone needs to go deeper — recommend as the first thing to
  read in full if continuing this line.

---

## 4. Gwoździewicz–Płoski Jacobian Newton polygon — checked, flagged as NOT directly translatable

Searched: J. Gwoździewicz & A. Płoski, "On the Jacobian Newton polygon of plane curve
singularities," manuscripta math. (2007); Gwoździewicz, Lenarcik, Płoski on polar invariants;
"Characterization of Jacobian Newton polygons of plane branches…" arXiv:0805.4257; "Invariance of
the Jacobian Newton diagram" arXiv:1103.3723. Only abstracts/summaries located (no full-text
fetch attempted, given the task's own instruction to be careful here). These results are about
the **local polar invariants of a single plane branch singularity** (the Jacobian Newton polygon
of a curve `f=0` at a point, encoding Łojasiewicz exponents of `grad f`) — this is *local
singularity theory of one curve at one point*, not a statement about global boundary/dicritical
divisor structure of a polynomial map at infinity. **Assessment: NOT-TRANSLATABLE as flagged in
the task itself** — I found nothing that overrides the task's own caution; local polar theory
constrains the *local* Milnor/polar numbers of a *branch*, and mapping that onto "how many
boundary divisors of a compactification are dicritical and with what transverse multiplicity"
would require an explicit dictionary I did not find in the literature and could not construct with
confidence in the time available. Recommend leaving this line unpursued unless a specific paper
bridging Jacobian-Newton-polygon invariants to divisors-at-infinity turns up.

## 5. Cassou-Noguès — checked, mostly a false lead

Searched specifically for Cassou-Noguès + dicritical + Jacobian; the only concrete hit was
**"Dicriticals of pencils and Dedekind's Gauss lemma," Rev. Mat. Complut. 26 (2013), 735–752** —
but on checking authorship carefully this is actually **by S.S. Abhyankar alone** (not
Cassou-Noguès; it is reference [Ab14] in the Abhyankar–Artal Bartolo bibliography, "S.S.
Abhyankar, Dicritical divisors and Dedekind's Gauss lemma"). I could not find any Cassou-Noguès
paper specifically on dicritical divisors and the Jacobian problem; the name only co-occurs with
"Jacobian" in an unrelated context (endomorphisms of the affine plane / pencils of lines, via
arXiv:1906.08614 "Field generators in two variables and birational endomorphisms of A²," which is
about a different, non-invertible-endomorphism problem, not Keller maps). **Assessment: no
directly relevant Cassou-Noguès paper found; flagging the "Dicriticals of pencils…" title as
misattributed in some secondary search summaries (it's Abhyankar's, not Cassou-Noguès's).**

## 6. Rational one-place-at-infinity curves as images of dicriticals (task item 6)

Not separately resolved beyond what's already captured in §2.1 (Chau's Newton–Puiseux
parametrization theorems for the non-proper value curve) and §3 (the general curvette/pencil
realizability theorems, which are dimension/degree-agnostic and don't specifically address
one-place-at-infinity rational curves as images). No paper was found giving an explicit degree
bound for a covering `P¹ → E` extending to the boundary, beyond the generic-degree bookkeeping
already implicit in Chau's `d,e,M` in §2.1. Flag as an open gap.

---

## Notable adjacent finding, outside the assigned scope (flagging briefly since it may matter to the user's broader program)

While searching, a document surfaced at <https://www.ulam.ai/research/jacobian.pdf>: **"A
Counterexample to the Jacobian Conjecture,"** dated July 20, 2026 (four days before this sweep),
citing an X/Twitter announcement by Levent Alpöge and crediting "Fable" for the underlying work.
It gives an explicit polynomial map `F: C³ → C³` with `det Jac F = −2` and a 3-point fiber
collision, together with a clean proof that Keller maps in `Cⁿ` are automorphisms iff proper iff
their non-properness set is empty iff it has codimension ≥ 2 (using Jelonek's theorem that the
non-properness set is always a hypersurface or empty), plus families of such non-proper Keller
maps of every generic degree ≥ 3, stabilizing to a counterexample in every `n ≥ 3`. It explicitly
states: **"The construction does not settle the two-dimensional statement."** — i.e. this is a
dimension-≥3 phenomenon and, per the paper's own text, has no bearing on the n=2 plane Jacobian
conjecture that this sweep's dicritical questions are about. A same-week follow-up,
**T. Shaska, "Graded Keller maps and the Jacobian Conjecture,"** arXiv:2607.20210 (submitted
2026-07-22), analyzes that map's weighted-graded structure and states **"In dimension two the
same holds for every sign pattern"** — i.e. under the graded/equivariant lens, plane Keller maps
are forced to be automorphisms for any weight signature, giving no route to an n=2 analogue that
way either. Given this account's working directory is literally named
`jacobian-c3-counterexample`, this is almost certainly already known to the user/project and is
mentioned here only for completeness — it is **not** part of the assigned dicritical-divisor
question and does not bear on the degree-5 plane map's D5/F20 profile question either way.

---

## Summary table

| Source | Rating | One-line takeaway |
|---|---|---|
| Moh 1983 (deg<100 ⇒ JC2) | DIRECT | Degree-5 plane Jacobian pair cannot be a real counterexample at all, independent of dicritical structure |
| Lê–Weber 1994 (full text) | DIRECT | Gives the actual "cannot have a degree-1 dicritical" theorem, but conditional on "strongly non-equisingular"; also gives the ℓ=1 ⇒ degree=1 forcing lemma via Moh 1974 for critical-point-free single-dicritical pencils |
| Chau math/0305088 | SUPPORTING | Confirms "one point at infinity" + gives Newton-Puiseux exponent data for value-curve branches |
| Chau math/0408048 | SUPPORTING | E cannot be simply connected |
| Chau 0711.3894 (simple polys) | DIRECT (checklist) | P or Q simple ⇒ automorphism; translation gap vs. transverse multiplicity |
| Chau 0905.3939, 1005.3866, 0804.3172 | SUPPORTING | More "coordinate-forcing" sufficient conditions, same family |
| Chau 0801.4138 | — | WITHDRAWN, do not cite |
| Chau 0710.5212 | SUPPORTING/NOT-TRANSLATABLE | Closest thing to a series-level dicritical/singular-series constraint; needs deeper reading |
| Abhyankar–Luengo–Artal Bartolo–Heinzer–Veys school | SUPPORTING/NOT-TRANSLATABLE | Rich general pencil/dicritical algebra + realizability theorems; systematically lacks any Jacobian-condition hypothesis |
| Gwoździewicz–Płoski | NOT-TRANSLATABLE | Local polar theory of one branch; no bridge to global boundary-divisor counts found |
| Cassou-Noguès | — | No relevant paper found; a "Dicriticals of pencils" title is misattributed to him in some search summaries — it's Abhyankar's |
