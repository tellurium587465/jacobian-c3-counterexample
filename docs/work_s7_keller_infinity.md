# S7: Keller pairs at infinity — the degree-1 isolated dicritical / E-dicritical coexistence question

Date of sweep: 2026-07-24. Method: WebSearch + WebFetch (arXiv/ar5iv, AMS/Crelle mirrors,
direct PDF download + Read tool where WebFetch's summarizer was unreliable on dense math
PDFs — flagged inline every time this happened). This note is a companion to, and leans
heavily on, the earlier sweep [`work_dicritical_lit.md`](work_dicritical_lit.md) (Lê–Weber,
Chau, Abhyankar/Luengo/Artal Bartolo school) — that file is NOT re-derived here, only cited.
It also directly continues an already-open question the campaign itself registered: see
[`n2-campaign.md`](n2-campaign.md), Round 19, "New sharpest question (round-19 rank 1): can
a degree-one, length-one infinity dicritical occur for a nontrivial Keller pair at all? (It
does for the identity map; the question is whether it coexists with `E`-dicriticals.)" —
this document is the literature-side answer attempt to exactly that question.

**Housekeeping correction to the task's own citation.** The task asks to cite
"Abhyankar–Moh J. Reine Angew. Math. 260 & 261 (1975)." This is *not quite* right and I want
to flag it rather than silently "fix" it: Crelle **260** (pp. 47–83) and **261** (pp. 29–54)
are Abhyankar–Moh's **"Newton–Puiseux expansion and generalized Tschirnhausen
transformation I, II"**, both dated **1973**, not 1975 (confirmed independently via EUDML
and De Gruyter listings, and again via the bibliography of El Hilany's 2025 survey, item
below). These two papers build the approximate-root/semigroup machinery. The **epimorphism
theorem** itself ("embedding of the line in the plane") is a *different, later* paper:
**S.S. Abhyankar & T.T. Moh, "Embeddings of the line in the plane," J. Reine Angew. Math.
276 (1975), 148–166** — confirmed three independent ways (Wikipedia's Abhyankar–Moh theorem
page, a Bulletin Korean Math. Soc. paper title, and — most reliably — reference [1] in the
bibliography of B. El Hilany, *"Around the topological classification problem of polynomial
maps: a survey,"* arXiv:2501.03828v2 (2025), which gives the exact citation string
`Journal fur die reine und angewandte Mathematik, 1975(276):148–166, 1975`). So: **260/261
(1973)** = technical machinery; **276 (1975)** = the actual embedding/epimorphism theorem.
Both lines matter below, so both are covered.

---

## 1. Abhyankar–Moh: what it actually says, and what it does *not* say

### 1.1 The epimorphism theorem, precisely

Verbatim theorem statement (as reconstructed from Wikipedia's Abhyankar–Moh theorem page,
cross-checked against the paper title/venue in El Hilany's bibliography, and against the
degree-divisibility corollary quoted independently by a UIAMath.15.001.3727 paper found via
search):

> **Abhyankar–Moh embedding-of-the-line theorem.** If `L` is a complex line embedded in the
> complex affine plane `C²` (i.e. a closed algebraic embedding `C¹ ↪ C²`), then this embedding
> extends to a polynomial automorphism of `C²` (equivalently: `L` can be moved by an
> automorphism to the standard line `{y=0}`).
>
> **Degree corollary (the "AM inequality"/AM semigroup form).** If `F=(P,Q): C → C²` is such
> an embedding with `m := deg P > 0`, `n := deg Q > 0`, and `gcd(m,n)` prime to the
> characteristic, then **`m | n` or `n | m`.**

This is the theorem that later became "Abhyankar–Moh–Suzuki" once M. Suzuki gave an
independent analytic proof (1974) and it was reproved many times since (Kang 1991 in Amer.
J. Math 113 — could not retrieve full statement, only publication data; a topological proof
by A'Campo–Oka 2003 in Math. Z.; Kaliman-style proofs; etc. — this whole reproof cottage
industry is well documented and not repeated here).

**What this theorem is about, precisely, and what it is NOT about.** The hypothesis is that
a specific *abstract algebraic curve* — the affine line `C¹` itself, no singularities, one
place at infinity in the strongest possible sense (the curve is smooth everywhere including
at infinity, since it *is* `P¹` minus one point) — is realized as a closed embedded
subvariety of `C²`. This is a much **stronger** hypothesis than "the generic fiber of a
polynomial `P` has a degree-1 (isolated) dicritical at infinity," which only constrains the
behavior of the pencil *at infinity* and says **nothing** about affine smoothness/genus of
the fiber. A fiber `P = c` can be unibranch and transverse-multiplicity-1 at its single
point at infinity (exactly the task's "degree-1 dicritical") while still carrying arbitrary
affine singularities (nodes, cusps, higher genus after normalization) — in which case it is
manifestly **not** abstractly isomorphic to `C¹`, and the Abhyankar–Moh epimorphism theorem
simply does not apply to it. **This is the central scope-limiting fact for item 1 of the
task**: AM's theorem is the historical ancestor of "one place at infinity" theory, but by
itself it constrains only the (rare, very rigid) case where the fiber is *also* an embedded
line — it does not directly say anything about a general polynomial `P` merely having a
degree-1 dicritical divisor, in the presence of other, unrelated boundary structure (e.g.
`E`-dicriticals of the pair). The bridge from AM to the general "few places at infinity"
statements is via Moh 1974 (§4 below) and the Suzuki/Chau line proved later (already logged
in `work_dicritical_lit.md` §2.3, §2.5: Chau's "simple polynomial ⇒ automorphism" and
"irreducible-fibers-of-constant-genus ⇒ coordinate" theorems), not via AM 1975 itself.

### 1.2 A second, independently-confirmed modern citation for the same "one-place ⇒ coordinate" family

B. El Hilany's 2025 survey (arXiv:2501.03828v2, full text obtained — dense general-position
PDF, read directly via the Read tool since WebFetch's summarizer could not parse the
compressed text stream) collects, as **Theorem 4.17**, the clean state-of-the-art list of
*sufficient conditions* under which a 2D Keller pair is known to be an automorphism.
Verbatim:

> **Theorem 4.17.** Let `f : C² → C²` be a polynomial map such that `f′(x) ≠ 0` for all
> `x ∈ C²`. Then, invertibility of `f` holds true in each of the following cases:
> 1. `deg f ≤ 100`, [Moh 1983]
> 2. `gcd(deg f₁, deg f₂) = 1`, [Nagata 1989]
> 3. **for every line `L ⊂ C²`, the map `f|_L : L → f(L)` is injective**, [Abhyankar–Moh
>    1975 + Gwoździewicz 1993].

Item (3) is a clean, citable, modern restatement of exactly the "coordinate-forcing via
one-place/embedded-line behavior" family that also contains Chau's "simple polynomial"
theorem already logged in the prior sweep. Its own citation is `[1,75]` in El Hilany's
numbering = **Abhyankar–Moh 1975** (the embedding theorem, used on the affine part) **+
J. Gwoździewicz, "Injectivity on one line," arXiv:alg-geom/9305008 (1993)** (this exact
arXiv identifier is given in El Hilany's own bibliography entry [75]; not independently
refetched here, flagged as a priority follow-up if the interior mechanism is needed).
**Assessment: DIRECT, checklist item, same family as Chau's "simple" theorem** — again a
*global* condition (injectivity on *every* line, hence in particular on the coordinate axes
themselves), not a statement about one isolated boundary divisor coexisting with others.

---

## 2. Structure of the divisor at infinity of a Keller map: three independent schools, one convergent picture

### 2.1 van den Essen's book — an honest gap

I was **not** able to retrieve the internal section/chapter content of A. van den Essen,
*Polynomial Automorphisms and the Jacobian Conjecture* (Birkhäuser, Progress in Mathematics
190, 2000; reissued/expanded as *…: New Results from the Beginning of the 21st Century*,
Frontiers in Mathematics, 2021, with S. Kuroda and A. Crachiola) beyond confirming its
existence, publisher, and that El Hilany's survey cites it twice (as refs [172]/[173] — an
odd exact duplicate in his own bibliography, harmless but noted) purely as a general-purpose
survey pointer, with no specific section singled out. Google Books / search snippets did not
surface the table of contents at chapter-and-verse granularity, and I did not have
paywalled/institutional access to open the PDF itself. **TODO, explicitly flagged**: if the
project needs van den Essen's own treatment of "dicritical at infinity" / Newton-polygon
techniques for the 2D case (the task's item 2 explicitly asks for this), it must be pulled
from the physical/library copy — I could not verify it here, and I will not guess at section
numbers.

### 2.2 The Lê–Weber / Chau / Abhyankar school — already logged, load-bearing here

Not re-derived; see `work_dicritical_lit.md` for the full sweep. The two facts from that
document that this note leans on hardest:

- **Lê–Weber 1994's Main Theorem** excludes a Jacobian pair if it has a dicritical `D₀` that
  is *strongly non-equisingular* (bamboo length ≥ 2, **or** the coordinate's own pencil `φ`
  has a critical point on `D₀`) **and** either `a(D₀) < 0`, or `a(D₀) > 0` with
  `deg(φ|_{D₀}) = 1` (`a(D)` = canonical multiplicity, i.e. the coefficient of `D` in
  `K + Σ(boundary)`).
- **Moh's 1974 theorem** (Proc. AMS 44, 22–24) is the technical engine Lê–Weber invoke to
  pin the degree to exactly 1 in the special case of a *single, global* dicritical with *no*
  critical points anywhere on the pencil map (`ℓ=1`) — see §4 below for its own verbatim
  content and, crucially, why this special case is **not** the task's coexistence case.

### 2.3 A third, independent formalism: Borisov's "type 1/2/3/4" divisor classification (2014–2019) — direct hit, newly surfaced this sweep

**A. Borisov, "Frameworks for two-dimensional Keller maps," arXiv:1901.04073v2 (2019).**
Full text obtained (PDF downloaded, read directly via the Read tool — WebFetch's summarizer
could not parse the compressed PDF stream on this one either). This paper independently
reinvents essentially the same object as Lê–Weber's dicritical/bamboo theory, but built from
a different starting point (Mumford intersection theory on normal surfaces, plus two new
numerical invariants — the "`K̄` label" and the "determinant label" — introduced in
Borisov's own earlier papers **"On the Stein factorization of resolutions of
two-dimensional Keller maps," Beitr. Algebra Geom. 56 (2015), 299–312** and **"On two
invariants of divisorial valuations at infinity," J. Algebraic Combin. 39 (2014), 691–710**,
cited as [4] and [5] in this paper — not independently refetched, but their content is
recounted at length and used throughout the "Frameworks" paper, so I am confident of it at
one remove).

**The four-way divisor classification (verbatim, §1 of the paper):** for a hypothetical
Keller map `φ: Z → Y` between resolved compactifications of `C²`, every exceptional
("at-infinity") curve `E` is one of:
- type 1: `φ(E)` is a curve entirely in the target's boundary (`φ(E) ∩ A² = ∅`),
- type 2: `φ(E)` is a point outside `A²`,
- **type 3: `φ(E)` is a curve meeting `A²` — i.e. exactly a *dicritical* component** ("cf.
  e.g. [Abhyankar 2010], [Orevkov 1986]" — Borisov's own citation, matching the standard
  terminology this whole literature line uses),
- type 4: `φ(E)` is a point inside `A²`.

**Directly on-topic quote (Introduction):** *"A trivial topological argument implies that
such [a dicritical, type-3] curve must exist in any counterexample to the Jacobian
Conjecture. A slightly stronger result, that the map must be ramified in at least one
di-critical component, was proved (possibly, reproved) in [Beitr. Algebra Geom. 56 (2015)],
Theorem 3.1."* This is an **independent primary source** for exactly the fact the campaign's
own Round-19 audit already used (there attributed loosely to "their Ehresmann argument +
Keller") — i.e. Borisov's Theorem 3.1 (2015) is a second, separately-citable proof that
**every nontrivial Keller pair has at least one dicritical divisor on which the pencil map
is ramified.** Good independent cross-validation of an already-logged campaign fact; cite
both Lê–Weber's Ehresmann-argument route (`work_dicritical_lit.md`) and Borisov 2015
Theorem 3.1 side by side going forward.

**The "K̄ label" is literally Lê–Weber's `a(D)` under a different name.** Definition 2.1 of
Borisov's paper: *"The `K̄` label of a curve at infinity is the coefficient in the expansion
of `K̄ = K + ΣEᵢ` in the basis `{Eᵢ}`."* This is `a(D) := ord_D(du∧dv)` up to notation —
exactly the invariant the campaign's own decorated-tree equation system (n2-campaign.md,
"Canonical decoration," item 1) already computes. **Lemma 2.1** of Borisov's paper: for a
type-1 curve `Eᵢ` mapping with ramification index `eᵢ` onto `Fⱼ`, the `K̄` label of `Eᵢ` is
`eᵢ` times the `K̄` label of `Fⱼ` — a clean multiplicativity law that is a candidate extra
tool for the campaign's own equation system if not already derived there independently.

### 2.4 Borisov's "Frameworks" paper as a *direct, constructive* data point on the coexistence question

This is the single most useful new find of this sweep for the task's central question. In
§2–§5, Borisov builds several fully explicit **combinatorial "frameworks"** — complete
decorated boundary trees for both source (`Z`) and (blown-up) target (`Y`), together with
explicit degree/ramification data for the map `φ` on every branch — each one satisfying
*every currently known necessary condition* for being the resolution of an honest Keller
map: the **Keller Map Adjunction Formula** `K̄_W = ρ*(K̄_Y) + Σ eᵢRᵢ` (his analogue of the
campaign's own "Canonical decoration" + "Principal-divisor equations" system), the
projection formula, and non-negativity of all the derived determinant labels.

**Crucially, every one of his "Frameworks" is built with *both* kinds of divisor
coexisting on the same tree**:
- degree-1 ("`f=1`", i.e. mapped **birationally**, unramified) type-1 boundary components —
  dozens of them in each framework (e.g. "the other three `(-2)`-curves are mapped
  1-to-1"; "the eight length-1 branches from the `(-5)`-curve are sent … with degree 2"; many
  literal `f=1` branch maps throughout Figs. 11–14, 23–26), **and**
- a small number of genuinely dicritical (**type 3**) divisors of **high degree**
  (`deg(φ|D)=16` and `13` in the First Framework; `28` and `23` in the Second; `5` in the
  Three-dessin framework), i.e. exactly the "`E`-dicritical" side of the task's question.

So: **at the level of every linear/adjunction/projection-formula constraint currently known
to be necessary for a Keller map's boundary structure, the coexistence of isolated
degree-1 divisors with high-degree dicriticals is not merely "not excluded" — Borisov
positively constructs several fully consistent combinatorial models exhibiting it.** This is
independent, constructive corroboration of the campaign's own Round-19 conclusion (§3
below) from a completely different research program (Borisov works with general Keller maps
of any monodromy type, not the D₅/F₂₀-specific setup).

**The crucial caveat, stated by Borisov himself, and directly relevant to calibrating how
much this "permits."** Having built the *combinatorial* model, Borisov attempts to actually
solve for the polynomial coefficients realizing his First Framework (a degree-`(99,66)` pair,
via explicit dessins d'enfant / Belyĭ maps and a large linear system in the coefficients,
solved with Maple/Gröbner bases). Verbatim: *"So, in all likelihood, there is no map `φ`
that satisfies our framework, but we currently do not have a simple reason for this."* He
explicitly connects this to Moh's theorem: **"Back in 1983 T.-T. Moh published a proof that
there are no Keller maps of degrees up to 100 … In fact, the `(99,66)` pair of degrees was
the last troublesome case that he had to discard."** — and separately confirms via his own
independent Maple computation that no map realizes this particular framework, consistent
with (though not literally re-deriving) Moh 1983's `deg < 100` exclusion. **This means the
one concrete coexistence-exhibiting combinatorial model that was actually degree-checked
turned out to sit exactly inside the known dead zone (`deg = 99 < 100`)** — so its failure to
lift to an actual polynomial map is fully explained by Moh 1983 and is *not* evidence against
coexistence being possible at higher degree. Borisov's **other** frameworks reach total
algebraic degree pairs `(135,90)`, `(171,114)`, `(207,138)`, `(243,162)`, `(435,290)`, and
`(108,72)` — several of these **already exceed** the `100` threshold (e.g. `(108,72)`,
`(135,90)`, …) and, as far as I can tell from the paper, **have not been checked
computationally for actual realizability** — Borisov does not report having run the
Gröbner-basis search on them. **This is therefore a live, unresolved combinatorial + Diophantine
search problem, explicitly left open by its own author** (his closing "Question 6.7," "The
biggest question of all": *"Can one actually use our frameworks to construct a Keller map?"*).
For the campaign's own project (algebraic degree `≫ 100` per the geometric-degree-5 ladder,
already noted in n2-campaign.md's "Moh-1983 conflation corrected" item), this means the one
place where coexistence was actually tested empirically and failed is *not* informative about
the campaign's own (much higher algebraic degree) regime.

### 2.5 A fourth, independent formalism: toric/Newton-polytope "dicritical faces" (Némethi–Zaharia 1990 → El Hilany 2017–2024)

B. El Hilany's 2025 survey (arXiv:2501.03828v2, §5.1.1) recounts a **third, independent**
precise definition of "dicritical," built from Newton polytopes/toric compactifications
rather than blow-up sequences: a coherent face `Γ` of a Newton polytope tuple `A` is called
**dicritical** if an outward normal vector `(α₁,…,αₙ)` of one of its supporting hyperplanes
has `αᵢ > 0` and `αⱼ ≤ 0` for some `i,j` (Némethi–Zaharia 1990, "On the bifurcation set of a
polynomial function and Newton boundary," and El Hilany's own generalization, Theorem 5.5:
*"a generic map `f ∈ K^A` satisfies `S(f) = ⋃ R_Γ(f)`, where the union runs over all
dicritical coherent faces of `A`"* — i.e. the non-properness set is *exactly* the union of
face-resultants over dicritical faces). **Assessment: SUPPORTING, a third convergent
formalism, no direct Keller-pair-coexistence theorem found in this line either** — same
recurring gap as the Abhyankar/Luengo/Artal Bartolo school (`work_dicritical_lit.md` §3):
rich general dicritical machinery, but with no constant-Jacobian hypothesis built into any
of the theorem statements. Flagged mainly to record that (at least) **three separately
developed schools** — Lê–Weber/Abhyankar (blow-up divisors), Borisov (Mumford
intersection/Stein factorization), Némethi–Zaharia/El Hilany (toric/Newton-polytope faces) —
converge on the same underlying "dicritical" concept from different directions, with
essentially no cross-citation between the Borisov and Némethi–Zaharia/El Hilany lines found
in this sweep (the Lê–Weber line does cite Abhyankar's algebraic dicritical school, per the
prior sweep).

### 2.6 Pinchuk's example — what its dicritical/asymptotic structure actually looks like, and the honest limits of the analogy

**Essential framing, stated up front since it is easy to get wrong (and the task's own
framing already flags this correctly):** Pinchuk's map is **not** a complex Keller map. It
is a **real** polynomial map `F=(P,Q): R² → R²` whose Jacobian determinant `det DF` is a
polynomial that is **everywhere positive on R²** but is **not** a nonzero constant — it is a
non-constant polynomial with complex zeros off the real locus. So Pinchuk's construction is a
counterexample to the **Strong Real Jacobian Conjecture**, a different (weaker) conjecture
than JC2; it says nothing directly about the complex Keller/JC2 problem, and its
compactification/dicritical structure is *not* subject to the Keller identity `det = const`
that drives the whole `a(D) = e−1` / `a(D) = −m−1` machinery in §2.2–2.3 above and in the
campaign's own Round-19 valuation identities. Any use of Pinchuk's structure here is
explicitly an **analogy for intuition**, not a source of a directly-applicable theorem — I
confirmed the task's own caution on this point rather than overriding it.

**What is actually known about its structure (verified, primary + secondary sources):**

- **S. Pinchuk, "A counterexample to the strong real Jacobian conjecture," Math. Z. 217
  (1994), 1–4.** The original construction. Per B. El Hilany's 2025 survey (§4.3.1, full
  text obtained): **"The original Pinchuk map is of degree 40, and has `deg f₁ = 10`."**
  Subsequent refinements lowered `deg f₂` (called `deg q` in that literature): L.A. Campbell
  (2011, `deg q = 25` — this is the specific map studied in the paper below), F. Fernandes
  (2022, `deg q = 15`), and **F. Braun & F. Fernandes, "Very degenerate polynomial
  submersions and counterexamples to the real Jacobian conjecture," J. Pure Appl. Algebra
  227 (2023), 107345**, achieving the smallest known pair **`(deg f₁, deg f₂) = (9,15)`**.
  It remains **open** whether a Pinchuk map exists with `deg f₁ ∈ {5,6,7,8}` (lower bounds
  ruling out `deg f₁ ≤ 3` are due to F. Braun & J.R. dos Santos Filho, 2010, building on
  J. Gwoździewicz's 2001 proof that the Strong Real JC holds for `deg ≤ 3`; `deg = 4` is
  handled by Braun & Oréfice-Okamoto, 2016).
- **L.A. Campbell, "The asymptotic variety of a Pinchuk map as a polynomial curve," Appl.
  Math. Lett. 24 (2011), 62–65** (= arXiv:1001.3318, full text obtained via ar5iv). This is
  the paper that describes the **asymptotic variety** `A(F)` (the real, semi-algebraic
  analogue of the Jelonek/non-properness set `E`) for a specific degree-`(10,25)` Pinchuk
  map explicitly: `A(F)` is "a closed curve in the image `(P,Q)`-plane," and **"the points
  `(−1,−163/4)` and `(0,0)` of `A(F)` have no inverse image under `F`, all other points of
  `A(F)` have one inverse image, and all points of the image plane not on `A(F)` have two."**
  Its Zariski closure is described by an explicit degree-7 curve equation with one singular
  point. **This paper does not use dicritical-divisor or blow-up language at all** — it works
  entirely in the affine target plane with the closed-form parametrization of the asymptotic
  variety. So while it does give exact, quotable structural data about "how many points of
  the target curve have how many real preimages" (directly analogous in *spirit* to the
  campaign's own "omitted points"/multiplicity-profile bookkeeping for `E`), **I could not
  find a paper that explicitly resolves a Pinchuk map's source-side compactification into
  boundary divisors and classifies which are dicritical of which degree** — this is a
  genuine gap, flagged honestly as **TODO**, not filled by anything located in this sweep.
- **F. Fernandes & Z. Jelonek, "The Pinchuk example revisited," Comptes Rendus Mathématique
  362 (2024), G4, 449–452.** Per El Hilany's survey: constructs two further Pinchuk maps
  addressing whether non-surjectivity is *necessary* for non-injectivity — one of the two
  new examples **is surjective**, the other has **non-dense image**. This directly bears on
  "what can the image/escape structure of a near-Keller real map look like" but again is not
  phrased in dicritical-divisor terms in the summary I could obtain.
- **J. Gwoździewicz, "Real Jacobian mates," Ann. Polon. Math. 117 (2016), 207–213**
  (Theorem 4.19 in El Hilany's numbering, full text of the *statement* obtained via the
  survey, not the original paper itself — flagged as one remove). Verbatim:

  > **Theorem.** Assume that the Newton polygon of a polynomial `f₁ ∈ R[x₁,x₂]` has an edge
  > that: begins at `(0,1)`, has a positive inclination, and has no lattice points in its
  > relative interior. Then, there does not exist a polynomial `f₂ ∈ R[x₁,x₂]` for which
  > `f₁` and `f₂` are Jacobian mates.

  ("Positive inclination" = the edge's outer normal `(v₁,v₂)` has `v₁>0, v₂<0`; "Jacobian
  mates" = `f₁,f₂` with everywhere-positive Jacobian, Gwoździewicz's own 2016 coinage.)
  **This is, as far as I found, the single closest thing in the entire literature search to
  a direct theorem of the requested shape** — it is a genuine **local-structure-at-infinity
  ⇒ no completion to a full (real) Jacobian pair** result, phrased via one Newton-polygon
  edge of *one* coordinate alone. An edge with "no lattice points in its relative interior"
  is precisely the toric/Newton-polygon signature of a **smooth (multiplicity/degree-1-type)
  piece of the boundary at infinity** in that direction (cf. §2.5's toric dicritical-face
  formalism) — i.e. this theorem says: *if `f₁` alone has an isolated "clean"/primitive
  direction at infinity of a specific orientation, no `f₂` can complete it into a real
  Jacobian pair.* **Important translation caveats, stated plainly:** (a) this is the **real**
  Strong-Jacobian-mate setting, not the complex Keller/constant-Jacobian setting the task
  asks about; (b) "positive inclination" is a directional condition (roughly: the edge
  points toward `Q`-escaping-while-`P`-bounded or similar) that is not obviously the same
  condition as "isolated bamboo, degree-1 restriction of `φ`, `Q` has a pole" — translating
  one to the other would require redoing the toric-vs.-blow-up dictionary explicitly, which
  I did not attempt here; (c) the theorem's *conclusion* is an **exclusion**, but only for
  edges of one *specific* orientation (positive inclination) — it is silent on edges of the
  opposite/other orientations, so it is not a blanket "no degree-1 edge can ever appear in a
  real Jacobian pair" statement. **Assessment: DIRECT-adjacent, real-analogue, translation
  gap explicitly flagged** — this is the most concrete piece of evidence I found that a
  *local, orientation-specific* degree-1/primitive boundary structure *can* obstruct
  completion to a full (real) Jacobian pair, which is evidence on the "maybe EXCLUDE, at
  least in some directions/orientations" side of the ledger — but it does not, by its own
  stated hypotheses, cover the general case, and it is real-not-complex.

---

## 3. The KEY question (task item 3): does the literature contain a theorem forbidding an isolated degree-1 dicritical alongside E-dicriticals in a Keller pair?

**Short answer: no such theorem was found. Every relevant theorem located has a hypothesis
the sought local coexistence configuration can evade.** Walking through the candidates:

1. **Lê–Weber 1994's Main Theorem** (full statement and translation caveats already in
   `work_dicritical_lit.md`) excludes a dicritical only if it is *strongly
   non-equisingular* (bamboo length ≥ 2, or the pencil `φ` itself has a critical point on
   that divisor) **and** the sign/degree condition fires. An **isolated** bamboo (length 1)
   on which `φ` has **no** critical point is, **by the theorem's own stated hypotheses**,
   simply not covered — the theorem is silent, not permissive by proof, but *inapplicable*.
   The campaign's own Round-19 analysis (n2-campaign.md) already worked out, independently,
   the sharpest form of this: every pole-type (`a(D) < 0`) dicritical of a Keller coordinate
   in the D₅/F₂₀ setting is *automatically killed by Lê–Weber* **unless** it is exactly an
   isolated, degree-1, unramified bamboo — i.e. survival of the whole configuration *forces*
   this exact local shape onto every non-`E` dicritical. That is a strong internal
   consistency argument that the sought configuration is not just "not excluded" but is
   **the specific shape survival requires**, though it remains the project's own derivation,
   not an external citation, and does not itself prove existence.

2. **Chau's "simple polynomial" theorem** (arXiv:0711.3894, logged previously) and **El
   Hilany's Theorem 4.17(3)** (`f|_L` injective on every line ⇒ automorphism, via
   Abhyankar–Moh 1975 + Gwoździewicz 1993) are both **global** conditions: they require
   **every** boundary component under the coordinate `P` (resp. every line's restriction) to
   be simple/injective. Neither excludes a mixed profile where `P` has *one* isolated
   degree-1 dicritical **and**, elsewhere on the boundary, higher-degree (`E`-type)
   dicriticals — that mixed case is exactly outside what these "P entirely simple" theorems
   cover.

3. **Gwoździewicz's real Newton-polygon theorem** (§2.6) is the one genuine *local*
   exclusion result found, but it lives in the real Strong-Jacobian-mate world, is
   orientation-specific, and its translation to the complex blow-up-divisor language used
   by the rest of this note was not carried out (flagged explicitly as a gap, not resolved
   here — a natural next step if this line is pursued further).

4. **Borisov's explicit combinatorial frameworks** (§2.4) are **positive, constructive**
   evidence that the coexistence pattern is realizable at the level of every currently known
   *necessary* linear/adjunction condition on the boundary tree — with the caveat that the
   one framework actually solved-for at the polynomial level (degree `(99,66)`) failed to
   lift to a genuine map, for a reason (Moh 1983's `deg<100` theorem) that is orthogonal to
   the coexistence question itself and does not touch the (much higher degree) frameworks
   left unchecked.

**No paper was found that states, proves, or even conjectures directly: "a Keller pair
cannot have an isolated degree-1 dicritical for one coordinate coexisting with dicriticals
over a nonempty Jelonek/exceptional curve."** Nor did I find a paper constructing a genuine
complex Keller (constant-Jacobian) example exhibiting it — because, of course, any such
genuine example would itself resolve JC2's 2D case (in the negative), so its absence from
the literature is expected regardless of whether the configuration is secretly excludable.

---

## 4. Moh's 1974 theorem, verbatim, and its precise (non-)bearing on the coexistence question

**T.T. Moh, "On analytic irreducibility at infinity of a pencil of curves," Proc. Amer.
Math. Soc. 44 (1974), 22–24.** Full text was **not** obtained from a clean primary PDF (the
AMS PDF and a direct r.jina.ai mirror of it both returned HTTP 403; a scispace-hosted mirror
was fetched and its AI-summarized rendering is what is quoted below — flagged accordingly as
**one level removed from the primary text**, though its content matches, word-for-word in
substance, the independent paraphrase Lê–Weber give of it, already logged and quoted in
`work_dicritical_lit.md`, which gives me reasonable confidence in the *content* even without
a clean primary-source PDF in hand):

> **Theorem I.** *The curve defined by `f(x,y)+p(x)` with `deg p(x) < d` has only one place
> at ∞.*
>
> **Corollary.** *`f(x,y)+c` is analytically irreducible at ∞ for arbitrary constant `c` in
> `k`.*

Setup: `f(x,y)` a degree-`n` polynomial **already assumed to have** only one place at
infinity, centered at the infinite point of the `x`-axis direction; `d` a specific
"maximal-contact"/approximate-root invariant of `f` (defined via the paper's own `φ(f,dᵣ)`
notation, referencing Abhyankar–Moh's 260/261 machinery — this is exactly where those two
1973 papers feed into Moh 1974, confirming they are the right thing to cite alongside it);
ground field algebraically closed, characteristic 0.

**What this says, in plain terms:** *given* that `f` already has one place at infinity, the
**entire pencil** `f = const` (every member, not just the generic one) is preserved as
one-place-at-infinity under adding any lower-order-in-`x` perturbation, in particular under
just shifting by a constant. It is a **preservation-under-deformation** lemma about a
*single, already-simple* pencil — **not** a theorem about when a *mixed* multi-dicritical
configuration (some divisors degree-1, others not) can or cannot arise.

**Its precise role in Lê–Weber, and why that role does not reach the coexistence question.**
Lê–Weber invoke Moh's theorem only inside the special sub-case where (a) the pencil map `φ`
has **no critical point anywhere** (`C(f)=0`, the strongest possible non-ramification
hypothesis) and (b) there is **exactly one dicritical total** (`ℓ=1`) forced by an
Euler-characteristic/Ehresmann argument. Under those two hypotheses, Moh's theorem is what
lets them conclude the unique dicritical restricts with degree exactly 1. **Both hypotheses
fail in the task's coexistence setting on their face**: the campaign's own Round-19 audit
(and Borisov's Theorem 3.1, §2.3 above, independently) already establish that a nontrivial
Keller coordinate is **forced to have a critical point of its own pencil** on some
dicritical (violating (a)), and the whole point of the coexistence question is a scenario
with **more than one** dicritical total (violating (b), since there must be at least one
isolated degree-1 one *and* at least one `E`-type one). **Conclusion for task item 4: Moh's
1974 theorem neither constrains nor permits the requested coexistence configuration — it is
simply addressed to a different, strictly simpler regime (`ℓ=1`, fully unramified pencil)
that the coexistence question's own hypotheses already fall outside of.** Its only real
service to this note is confirming, via its role inside Lê–Weber, exactly *why* that other,
simpler regime collapses to degree 1 — which is useful context but not itself an answer.

---

## 5. Final answer

**Does the literature EXCLUDE, PERMIT, or leave OPEN the coexistence of a degree-1 isolated
infinity dicritical with `E`-dicriticals in a Keller pair?**

**OPEN, leaning PERMITTED / not excluded.** No paper, classical or recent, states a theorem
that forbids this exact local configuration. The two theorems that come closest to a direct
hit either (a) require a *global* hypothesis (all of `P`'s boundary components simple/degree-1,
or injectivity on every line — Chau 0711.3894; El Hilany's Theorem 4.17(3) via Abhyankar–Moh
1975 + Gwoździewicz 1993) that the coexistence scenario is explicitly designed to evade by
having the degree-1 divisor be only *one* of several, or (b) apply to a provably different
regime (Lê–Weber's Main Theorem needs "strongly non-equisingular," which an isolated,
unramified bamboo is not, by construction; Moh 1974 itself needs the strictly simpler `ℓ=1`
totally-unramified case, which the coexistence scenario is not). The one genuinely *local*
exclusion result found — Gwoździewicz's 2016 real Newton-polygon-edge theorem (§2.6) — lives
in the real Strong-Jacobian-mate setting, is orientation-specific, and its translation to the
complex blow-up-divisor language was not carried out here, so it cannot be cited as settling
the complex question either way. On the constructive side, Borisov's explicit combinatorial
"frameworks" (arXiv:1901.04073, §2.4 above) **positively exhibit** boundary trees satisfying
every currently known necessary linear/adjunction/projection-formula condition with isolated
degree-1 (type-1) divisors coexisting alongside high-degree dicritical (type-3) divisors on
the same tree — the one such framework actually solved for at the polynomial level failed,
but for a reason (Moh 1983's independent `deg<100` theorem) that has nothing to do with the
coexistence pattern itself and does not touch Borisov's higher-degree frameworks, which he
leaves explicitly unresolved. Finally, and specific to this project's own D₅/F₂₀ campaign:
the Round-19 derivation already in `n2-campaign.md` shows that, far from being merely
*permitted*, an isolated degree-1 unramified bamboo on every non-`E` dicritical is exactly
the shape **survival of Lê–Weber's Main Theorem forces** on the hypothetical configuration —
i.e., in this campaign's specific setting, the coexistence is not just unexcluded but is a
*necessary condition* for the configuration to have any chance at all.

**Decisive items to cite going forward:**
- Lê–Weber 1994 Main Theorem (`work_dicritical_lit.md` §1) — the strongly-non-equisingular
  exclusion, and why it doesn't fire on an isolated bamboo.
- T.T. Moh, Proc. AMS 44 (1974), 22–24 — Theorem I verbatim above; its `ℓ=1` scope limit.
- S.S. Abhyankar & T.T. Moh, J. Reine Angew. Math. **276** (1975), 148–166 — the actual
  epimorphism theorem (not 260/261, which are the 1973 Newton–Puiseux papers).
- N.V. Chau, arXiv:0711.3894 — "simple polynomial ⇒ automorphism" (global condition).
- B. El Hilany, arXiv:2501.03828v2 (2025) — Theorem 4.17 (three sufficient conditions for
  JC2, incl. the AM+Gwoździewicz line-injectivity route); §4.3.1/§5 for the Pinchuk-map and
  toric-dicritical-face material.
- A. Borisov, arXiv:1901.04073 (2019) + Beitr. Algebra Geom. 56 (2015) + J. Algebraic
  Combin. 39 (2014) — the type-1/2/3/4 classification, the `K̄`/determinant-label
  invariants, and the explicit coexisting-divisor "frameworks."
- S. Pinchuk, Math. Z. 217 (1994), 1–4; L.A. Campbell, Appl. Math. Lett. 24 (2011), 62–65
  (arXiv:1001.3318); F. Braun & F. Fernandes, J. Pure Appl. Algebra 227 (2023), 107345;
  J. Gwoździewicz, Ann. Polon. Math. 117 (2016), 207–213 — the real-analogue family, with
  the real/complex distinction kept explicit throughout.
- van den Essen's book — cited by title/publisher only; its specific internal treatment of
  this exact question is an honest **TODO**, not resolved by this sweep.

File: `docs/work_s7_keller_infinity.md`.
