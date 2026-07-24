# S7: the escape ledger for the unsolvable cases `A5`, `S5`

**Date: 2026-07-24. Method: direct group-theory computation
(`sympy.combinatorics`), extending the audited D5/F20 machinery — no new
literature dependence.** Machine parts:
[`src/n2/a5s5_ledger.py`](../src/n2/a5s5_ledger.py) (run with
`python src/n2/a5s5_ledger.py`; every numeric claim below is either an
`assert` in that file or a direct transcript of its output, not a hand
computation quoted without a check). Builds on
[`src/n2/degree5_ledger.py`](../src/n2/degree5_ledger.py) (Lemma A/B,
Theorem C/D/E, `cusp_capability()`), which is treated here as an audited
black box, not re-derived.

This is a **session-7 companion** — the *unsolvable-monodromy* half of the
program the task background calls "preparing the A5/S5 battlefield",
alongside the same-day D5/F20-side notes
[`work_s7_tree_sat.md`](work_s7_tree_sat.md),
[`work_s7_keller_infinity.md`](work_s7_keller_infinity.md) and
[`work_s7_lambda_localization.md`](work_s7_lambda_localization.md).

**Bottom line up front.** The Hartogs-forces-cusps *mechanism* is not a
solvability phenomenon at all — it rests on a single group-independent fact
(`Fix(σ) always equals the union of the singleton ⟨σ⟩-orbits`, verified
below for all 215 elements of `{C5,D5,F20,A5,S5}`), so **Theorem D applies
verbatim, unchanged, to any meridian class with `Fix = 1`** — which includes
`A5`'s double-transposition class and `S5`'s 4-cycle class. Those two
sub-cases genuinely **do collapse to the same cusp-gap analysis as D5/F20.**
But three things are honestly new and none of them is a copy of the D5/F20
story: (1) `Fix ≥ 2` classes (`A5`'s 3-cycle, `S5`'s transposition) give
**several simultaneous, individually Hartogs-protected sections**, and the
elementary ledger does *not* pin down how many of them are genuinely
affine — a combinatorial gap absent from the `Fix = 1` case; (2) `Fix = 0`
classes (`A5`'s 5-cycle, `S5`'s `(2,3)`-class) **normally generate all by
themselves** in `A5`/`S5` (unlike D5/F20's non-generating 5-cycle), so an
irreducible `E` that is *generically entirely outside the image of `f`* is
a logically live new configuration; (3) the cusp-**capability** census
(*which* torus cusps can supply the escalation) has no classical handle
once `G` is non-solvable — `D5`/`F20` are metabelian and Fox-coloring /
Alexander-polynomial machinery is exactly a solvable-group tool, but
`A5' = A5` (perfect) and `S5' = A5`, so the derived-series tower that made
`cusp_capability()` work terminates after at most one step. This part is
left **open**, with a structural hint (the `(2,3,5)` triangle group ≅ `A5`)
flagged as a direction, not a result.

---

## 0. Setup recap

`F = (P,Q): C² → C²` is a hypothetical degree-5 plane Keller map (`det DF`
a nonzero constant), `E` the Jelonek/exceptional curve, and
`ρ: π₁(C²∖F⁻¹(E)) ↠ G ≤ S5` the monodromy, `G` transitive. `E` is assumed
**irreducible** throughout (as in the task). Three tools, already proved
and audited in `degree5_ledger.py`, are used as black boxes:

* **Lemma A** (never-empty preimage): `χ(f⁻¹(E)) = 5χ(E) − 4`, forcing
  `f⁻¹(E) ≠ ∅` for any component of `E`.
* **Lemma B** (sheet-fix bound): over a component `C` with meridian `σ_C`,
  the number `d_C` of *affine* (finite) preimage sheets satisfies
  `d_C ≤ Fix(σ_C)` — because an affine preimage point `p` is a point where
  `F` is a local biholomorphism onto a **full** neighborhood of `F(p)`
  (not just onto `E`), so its local inverse branch is single-valued on
  that whole neighborhood and trivially returns to itself around any loop.
  The **converse fails in general**: a fixed sheet need not be affine (a
  "silently escaping" fixed sheet is possible — flagged already in
  `degree5_ledger.py` and reconfirmed as a live gap for `A5`/`S5` in §3
  below).
* **Hartogs section lemma** (audited sound, round 15): if `q` is a
  **smooth** point of `E` and a **degree-1** (single-valued) affine section
  is defined over a punctured neighborhood of `q`, its inverse extends over
  `q` too (Riemann/Hartogs extension in dimension 2) — so `q` is *not*
  omitted. This is the engine behind Theorem D/E.

**Section principle**: since `E` is irreducible, all its meridians are
conjugate to a *single* class `[σ_E]`, and `ρ(π₁) = G` forces that one
class to **normally generate** `G`.

---

## 1. Conjugacy classes, `Fix`, and normal generation — machine table

```python
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup, AlternatingGroup

def class_table(g):                       # from degree5_ledger.py
    rows, seen = [], set()
    for el in g.elements:
        if el.is_identity: continue
        cyc = tuple(sorted(len(c) for c in el.cyclic_form))
        fix = 5 - sum(len(c) for c in el.cyclic_form)
        if (cyc, fix) in seen: continue
        seen.add((cyc, fix))
        nc = g.normal_closure(PermutationGroup([el]))
        rows.append((cyc, fix, nc.order() == g.order()))
    return sorted(rows)
```

Output (verbatim, `python src/n2/degree5_ledger.py`):

```
A5   | (2, 2) Fix=1 gen=Y; (3,) Fix=2 gen=Y; (5,) Fix=0 gen=Y
S5   | (2,) Fix=3 gen=Y; (2, 2) Fix=1 gen=n; (2, 3) Fix=0 gen=Y;
       (3,) Fix=2 gen=n; (4,) Fix=1 gen=Y; (5,) Fix=0 gen=n
```

| `G` | class | `Fix` | normally generates `G`? |
|---|---|---|---|
| `A5` (order 60, **simple**) | `(2,2)` | 1 | **yes** |
| `A5` | `(3,)` | 2 | **yes** |
| `A5` | `(5,)` | 0 | **yes** |
| `S5` (order 120) | `(2,)` transposition | 3 | **yes** |
| `S5` | `(2,2)` | 1 | no |
| `S5` | `(2,3)` | 0 | **yes** |
| `S5` | `(3,)` | 2 | no |
| `S5` | `(4,)` | 1 | **yes** |
| `S5` | `(5,)` | 0 | no |

Confirms the task's calibration exactly: `max Fix = 2` for `A5` (achieved
only by 3-cycles — and since `A5` is simple, *every* nontrivial class
normally generates: `assert all(gen for _,_,gen in rows)` in
`theorem_C()`); `max Fix = 3` for `S5` (achieved only by transpositions).
`S5`'s normally-generating classes are exactly `{(2,), (2,3), (4,)}` — the
same three found already in `theorem_C()`'s assertion
`gens == {(2,), (4,), (2, 3)}`.

Why `A5` has *no* non-generating classes but `S5` has three: `A5` is
simple, so the normal closure of any nonidentity element is all of `A5`.
`S5`'s three non-generating classes — `(2,2)`, `(3,)`, `(5,)` — are exactly
the ones consisting entirely of **even** permutations; their normal
closure is trapped inside the unique proper nontrivial normal subgroup
`A5 ⊲ S5`.

---

## 2. The generic meridian of an irreducible Jelonek curve

**Clarification the task explicitly asked for.** In a classical branched
cover, "generic point of the discriminant ⟹ simple branching
(transposition)" is a **ramification** statement — it uses that the
covering map has a critical point there. Our `F` is **unramified
everywhere** (`det DF` a nonzero constant ⟹ local biholomorphism at every
point of `C²`, with no exceptions on or off `E`). `E` is not a branch locus
at all; it is the locus of **non-properness** — where sheets run off to
infinity rather than colliding. So there is **no** a priori restriction to
transpositions here: `σ_E` can be **any** nontrivial conjugacy class of
`G`, and which one occurs is fixed entirely by the section principle
(§1's "normally generates" column) plus whatever the honest geometry of
the specific counterexample supplies.

Given `σ_E`, write its cycle type as `Fix(σ_E)` many 1-cycles plus a
partition of `5 − Fix(σ_E)` into the nontrivial cycles. **`d_E ≤
Fix(σ_E)`** (Lemma B) — with equality *not* automatic for `Fix ≥ 2` (see
§3). The **possible `(class, Fix = d_E upper bound)` pairs for irreducible
`E`** (i.e. restricted to the normally-generating rows of §1's table):

| `G` | meridian class | `Fix` (`= d_E` upper bound) | non-fixed orbit degrees (escaping) |
|---|---|---|---|
| `A5` | `(2,2)` | 1 | `2, 2` (two independent 2-orbits) |
| `A5` | `(3,)` | 2 | `3` (one 3-orbit) |
| `A5` | `(5,)` | 0 | `5` (one 5-orbit — **all** sheets escape) |
| `S5` | `(2,)` | 3 | `2` (one 2-orbit) |
| `S5` | `(2,3)` | 0 | `2, 3` (two escaping orbits — **all** sheets escape) |
| `S5` | `(4,)` | 1 | `4` (one 4-orbit) |

---

## 3. Orbit decomposition, the singleton-orbit fact, and the generalized
   Hartogs argument

### 3.1 The group-independent fact that makes everything below work

```python
for name, g in transitive_subgroups_of_S5().items():
    for e in g.elements:
        fix = sorted(x for x in range(5) if e(x) == x)
        singles = sorted(o[0] for o in orbit_decomposition(e) if len(o) == 1)
        assert fix == singles
```

**Verified for all `5+10+20+60+120 = 215` element-checks across
`{C5, D5, F20, A5, S5}`** (some permutations literally recur across these
nested groups — e.g. the identity, or the 5-cycle generator shared by
`C5 ⊂ D5, F20` — but the check is run element-by-element regardless, so
it holds in particular for every one of `A5`'s 60 and `S5`'s 120
elements): `Fix(σ)` is *always*
exactly the union of the singleton `⟨σ⟩`-orbits — trivially true (a fixed
point *is* by definition a length-1 orbit) but worth stating because
**every consequence below is just this fact plus Lemma B/Hartogs, with no
further input from `G`.**

Consequently: **every individual affine/fixed sheet, for any meridian
class in any transitive `G ≤ S5`, is on its own a degree-1 local section**
— it never shares an orbit with another fixed sheet, however many there
are. The Hartogs section lemma's hypothesis ("a degree-1 section defined
over a punctured neighborhood of `q`") is therefore available **section by
section**, independent of `Fix(σ_E)`'s size and independent of `G`.

**Corollary (Theorem D transfers verbatim to `Fix = 1` cases in `A5`/`S5`).**
`degree5_ledger.theorem_D()`'s symbolic derivation —
`χ(Ẽ) = 5·χ(E) − 4` ⟹ `β′ = 5s − s̃` ⟹ `4s ≤ β′ ≤ 5s` ⟹ the
branch-packet refinement `|E ∖ f(C²)| = 4s` exactly — **never references
`D5` or `F20` in its sympy code**; its only external input is `Fix(σ_E) =
1` (which forces `d_E = 1` via Lemma A + quasi-finiteness, hence `Ẽ`
irreducible, hence the ZMT open-immersion step). It therefore applies,
unchanged, word for word, to:

* **`A5` with meridian `(2,2)`** (`Fix = 1`, normally generates — same
  cycle type as D5's own generating class, just inside a bigger ambient
  group), and
* **`S5` with meridian `(4,)`** (`Fix = 1`, normally generates — literally
  the *same conjugacy-class type* as `F20`'s own generating class).

Both collapse to **exactly** the D5/F20 "omitted points confined to
`4s ≥ 4` cusps" theorem, with no new bookkeeping needed at this step.

### 3.2 The worked example the task asked for: `A5`, meridian a 3-cycle

`Fix((3,)) = 2`: cycle type `(3,) + (1,1)`, i.e. **two fixed points +
one 3-orbit**. By §3.1, *both* fixed points are, individually, degree-1
local sections — **not** one shared degree-2 orbit (a common
misconception the task's own phrasing flags and the code above
`assert`s away): a 3-cycle on `{0,1,2,3,4}` fixing (say) `3,4` gives
orbits `{(3,), (4,), (0,1,2)}` — two singleton orbits, one 3-orbit, never
a 2-orbit. **So yes: both finite sheets are individually degree-1
sections, each independently Hartogs-killable at smooth points of `E`,
exactly as the task anticipated** — and each one's *own* omitted-point set
is therefore confined to singular points of `E`, by the same
smooth-point argument as the D5/F20 case, run twice (once per section).

**What is genuinely new here, and not resolved by the elementary ledger:**
Lemma A + quasi-finiteness only forces **at least one** of the two
candidate fixed sheets to be genuinely affine somewhere generically over
`E` (an affine curve dominating `E` must exist at all — that is all Lemma
A gives); Lemma B only forces **at most two**. Unlike the `Fix = 1` case,
where this sandwich (`0 ≤ d_E ≤ 1`, `d_E ≥ 1` from Lemma A) pins `d_E`
down to exactly `1`, here the sandwich `1 ≤ d_E ≤ 2` leaves **two
sub-cases genuinely open**:

* **`d_E = 2`** — both fixed points are honestly affine everywhere
  generically: two independent degree-1 sections, each with its own
  (possibly different) confined-to-cusps omitted-point set, doubling the
  bookkeeping of Theorem D (and raising an unresolved question the
  elementary ledger does not answer: do the two sections assemble, as you
  transport around `E_sm`, into **one** connected double cover of `E` or
  **two** separate copies of `E`? — a "vertical monodromy" datum not
  determined by the abstract conjugacy class of `σ_E` at all, genuinely
  new territory relative to D5/F20's `d_E=1` case where the question is
  vacuous);
* **`d_E = 1`** — one of the two candidate fixed sheets is a **"silently
  escaping" fixed sheet** (fixed by `σ_E`, i.e. returns to itself around
  the meridian loop, but never converges to a finite point as the loop
  shrinks — legal, since Lemma B's converse fails in general). Then only
  **one** genuine section exists and Theorem D's `Fix=1` bookkeeping
  applies to it essentially unchanged, while the other candidate simply
  never mattered.

**Neither sub-case is excluded by group theory alone.** This is the first
concrete respect in which `Fix ≥ 2` classes are *not* a free repetition of
the D5/F20 story — closing it needs the same kind of boundary/Hurwitz-at-
infinity data the original ledger already flagged as needed for "silent
components" in general.

### 3.3 `S5`, meridian a transposition (`Fix = 3`) — the mildest escape

Orbits: three singletons + one 2-orbit. By the same reasoning, **up to
three** independent degree-1 sections are candidates (Lemma B), with
**at least one** forced genuinely affine (Lemma A), and the same "how many
of the `Fix` candidates are honestly affine, and do the honest ones fuse
under vertical monodromy" gap as §3.2, now with three candidates instead
of two. Only a single 2-orbit's worth of monodromy (`2` sheets) is
available to do any escaping at all — the mildest configuration in the
whole menu.

### 3.4 `Fix = 0` classes — the genuinely new "totally non-proper `E`" case

`A5`'s 5-cycle and `S5`'s `(2,3)`-class have **no fixed points at all**:
every sheet is in a nontrivial orbit (one 5-orbit, or a 2-orbit + a
3-orbit respectively). Hartogs never gets a foothold (there is no local
section to protect anywhere). This parallels `D5`/`F20`'s own 5-cycle
class (also `Fix = 0`) — **but with one crucial difference**: `D5`'s and
`F20`'s 5-cycle does **not** normally generate (§1 of `degree5_ledger.py`),
so a lone 5-cycle-meridian `E` is *impossible on its own* there (it needs
a second component to reach the rest of the group) — this is exactly why
that case was interpreted as "the 2D analogue of the missing curve `Z`" —
a component, not the whole story. For `A5` (simple) **and** for `S5`'s
`(2,3)`-class, the `Fix=0` class **does** normally generate all by itself.
So an **irreducible `E` that is generically entirely outside the image of
`f`** — zero affine crossing sheets anywhere on the smooth locus of `E`,
with Lemma A's nonemptiness of `f⁻¹(E)` satisfied *only* through isolated
points over `Sing(E)` — is a logically live configuration for `A5`/`S5`
that has **no counterpart at all** in the D5/F20 ledger. This is the most
exotic new case in the menu, and is flagged here, not resolved.

---

## 4. Local-image (cusp-capability) census — the `A5`/`S5` analogue of
   Theorem E

`degree5_ledger.theorem_E()` asks, for each `Fix ≥ 1` class: which
subgroups `H ≤ G` can be the local monodromy image at a **unibranch**
singular (cuspidal) point of `E`, given that a knot group's meridian
normally generates the *whole* knot group (Wirtinger), so `H` must satisfy
`H = normal_closure_H(⟨meridian representative⟩)`? Brute-forced by
`local_image_census()` in `src/n2/a5s5_ledger.py` (unordered pairs
`(a,b) ∈ G×G`, `H = ⟨a,b⟩`, filtered to those containing a class
representative with `H` self-normally-generated by it):

```python
def local_image_census(g, mer_type):
    els = list(g.elements)
    meridians = [e for e in els if cycletype(e) == mer_type]
    subs = {PermutationGroup([a,b]) for a,b in combinations_with_replacement(els,2)}
    return {h.order(): h.is_abelian
            for h in subs if any(m in h.elements and
                h.normal_closure(PermutationGroup([m])).order()==h.order()
                for m in meridians)}
```

| `G` | meridian | `Fix` | local-image orders found | abelian? |
|---|---|---|---|---|
| `A5` | `(2,2)` | 1 | **{2, 6, 10, 60}** | 2:Y · 6:N (`S3`) · 10:N (`D5`) · 60:N (`A5`) |
| `A5` | `(3,)` | 2 | **{3, 12, 60}** | 3:Y · 12:N (`A4`) · 60:N (`A5`) |
| `A5` | `(5,)` | 0 | **{5, 60}** | 5:Y · 60:N (`A5`) |
| `S5` | `(2,)` | 3 | **{2, 6, 24, 120}** | 2:Y · 6:N (`S3`) · 24:N (`S4`) · 120:N (`S5`) |
| `S5` | `(2,3)` | 0 | **{6, 120}** | 6:Y · 120:N (`S5`) |
| `S5` | `(4,)` | 1 | **{4, 20, 24, 120}** | 4:Y · 20:N (`F20`) · 24:N (`S4`) · 120:N (`S5`) |

(Runtimes: ~80s per `A5` class; `S5` classes took 284–352s with the
`O(|G|²/2)` implementation actually used, cross-checked against an
independent `O(|G|²)` implementation which agreed exactly on **both** the
`(2,)` and `(2,3)` rows — the `O(|G|²)` run for `(4,)` was still in
progress at the time of writing and is not needed for the conclusions
below, which already rest on two independently-agreeing implementations.)

**Raw transcript** (both search implementations shown for `S5`'s `(2,)`
and `(2,3)` rows — the rest are the `O(|G|²/2)` implementation only):

```
A5 (2,2) Fix=1: local-image orders {2: True, 6: False, 10: False, 60: False}   (~78s)
A5 (3,)  Fix=2: local-image orders {3: True, 12: False, 60: False}             (78.5s)
A5 (5,)  Fix=0: local-image orders {60: False, 5: True}                       (78.0s)
S5 (2,)   Fix=3: local-image orders {24: False, 120: False, 6: False, 2: True} (696.6s, O(|G|^2) impl.)
S5 (2,)   Fix=3: local-image orders {24: False, 120: False, 6: False, 2: True} (352s,   O(|G|^2/2) impl.)
S5 (2,3)  Fix=0: local-image orders {120: False, 6: True}                     (569.2s, O(|G|^2) impl.)
S5 (2,3)  Fix=0: local-image orders {120: False, 6: True}                     (284s,   O(|G|^2/2) impl.)
S5 (4,)   Fix=1: local-image orders {24: False, 120: False, 20: False, 4: True} (286s, O(|G|^2/2) impl.)
```

**Reading `A5`'s `(2,2)` row (the direct analogue of `D5`'s own case,
Theorem E: `{C2, D5}` only).** `A5` gives a **strictly richer** lattice:
`{C2, S3, D5, A5}` — an escape at a cusp can escalate only *partway*
(to `S3` or `D5`) without needing the full nonabelian `A5`. This matches
`A5`'s classical maximal-subgroup structure (`A4`, `D5`, `S3` are exactly
`A5`'s three conjugacy classes of maximal subgroups); only `D5` and `S3`
qualify as local images, `A4` does not, for a clean reason: `A4`'s
double-transpositions form its unique normal Klein-four subgroup `V4`
(order 4), and since `V4` is **abelian**, the normal closure of any single
one of its elements *within `V4`* is just the order-2 subgroup that
element generates — not all of `V4`. So `V4` fails the
`H = normal_closure_H(⟨meridian⟩)` filter and is correctly *excluded*
(order 4 is absent from the found set, `{2, 6, 10, 60}`), and `A4` itself
is never generated by a `(2,2)`-pair reaching only as far as `V4` inside
it — leaving `C2`, `S3`, `D5`, `A5` as the four survivors.)

**Reading `A5`'s `(3,)` row (the task's headline example).** Local image
in `{C3, A4, A5}`. `A4` (order 12) is the minimal nonabelian escalation —
the unique subgroup of `A5` that is normally self-generated by a 3-cycle
(standard fact: `A4`'s normal subgroups are `{e, V4, A4}`; a 3-cycle is
not in `V4`, so its normal closure within `A4` must be all of `A4`). No
intermediate order-6 (`S3`) option here, unlike the `(2,2)` row — a
3-cycle's normal closure within an order-6 subgroup containing it would
have to be a subgroup of order divisible by 3 properly between `⟨3-cycle⟩`
and `S3`; `S3`'s only subgroups are `{e, C2, C3, S3}`, and the normal
closure of a 3-cycle within `S3` is `A3 = C3` (index 2, abelian) — not
`S3` — so `S3` itself is excluded here too, consistent with `12` (not `6`)
being the reported minimal nonabelian jump.

**Reading `A5`'s `(5,)` row.** Local image in `{C5, A5}` only — `D5`
(order 10) does **not** appear, because the normal closure of a 5-cycle
*within* `D5` is just the rotation subgroup `C5` (index 2 in `D5`), not
`D5` itself. This exactly reproduces `degree5_ledger`'s own `D5`
cusp-capability finding (`cusp_capability()`: minimal `D5` cusp is
`(2,5)`) using the identical group-theoretic fact, now inside the bigger
ambient `A5` — a genuine, independent cross-check of both computations
against each other.

**Reading `S5`'s `(2,)` row (mildest-escape case, §3.3).** Local image in
`{C2, S3, S4, S5}` — precisely the classical symmetric-group tower
(transpositions normally self-generate `S_n` for every `n ≥ 2`, and *no*
other subgroup of `S5` containing a transposition is normally
self-generated by it, since a subgroup containing an odd permutation and
equal to its own normal closure of that permutation cannot sit inside
`A5`, and the only overgroups of `⟨transposition⟩` built this way turn out
to be `S2, S3, S4, S5` themselves — confirmed by the search, not assumed).
Notably **absent**: `D5`, `F20`, `A5` — none of them contains a bare
transposition at all (`D5`, `A5` ⊆ even permutations; `F20`'s order-2
elements are double-transpositions, not transpositions).

**Reading `S5`'s `(2,3)` row (the `Fix = 0` "totally escaping" class,
§3.4).** Local image in `{C6, S5}` only — a stark two-point dichotomy, no
intermediate nonabelian subgroup at all: `A5` is excluded (a `(2,3)`-class
element is odd, so it cannot lie in `A5`); `D5` and `F20` are excluded
(neither contains a `(2,3)`-cycle-type element at all — direct check:
`{e.cyclic_form for e in D5.elements}` gives only cycle types
`{(), (2,2), (5,)}`, and for `F20` only `{(), (2,2), (4,), (5,)}` — no
`(2,3)` in either); the point-stabilizer copies of `S4` (order 24)
are excluded too, since a `(2,3)`-element (support size 5, no fixed
points) cannot lie in any point stabilizer. So escalation from the trivial
cyclic option (`C6`, generated by the meridian itself, `lcm(2,3)=6`) jumps
**straight to all of `S5`** — no partial escalation is available for this
class, unlike every other row in this table.

**Reading `S5`'s `(4,)` row (the direct `F20` analogue, §3.1's Theorem-D
transfer).** Local image in `{C4, F20, S4, S5}`. This **exactly reproduces
`F20`'s own Theorem E finding `{C4, F20}` as a sub-lattice** (`F20`'s
4-cycle meridian and `S5`'s 4-cycle meridian are literally the same
conjugacy-class type, and `F20 ≤ S5`) — a genuine independent cross-check
of the upstream `degree5_ledger.theorem_E()` computation against a
completely different code path — **plus two escalation levels invisible
from inside `F20` alone**: the point-stabilizer `S4` (order 24: a 4-cycle
normally self-generates `S4`, since `S4`'s only normal subgroups are
`{e,V4,A4,S4}` and a 4-cycle, being odd, forces the closure past `A4`),
and finally `S5` itself. So an `S5`-monodromy counterexample with a
`(4,)`-meridian has **strictly more room to escalate at a cusp** than an
`F20`-monodromy one with the same local Fix-count — the `F20` cusp census
(`(4,5)` minimal, `δ = 6`) answers only whether the *smallest* rung
(`F20`) is reachable, not the two larger `S5`-only rungs.

---

## 5. Why the cusp-capability census does **not** extend the way §3 did

`degree5_ledger.cusp_capability()` decides, for a torus cusp of type
`(m,n)`, whether it can carry the **full** (nonabelian) local image needed
— `5 | det(Δ_K(−1))` for `D5`, `5 | |Δ_K(i)|²` for `F20` — via the
classical **Fox `n`-coloring / Alexander-polynomial** criterion. This
machinery is not a generic tool for "does a knot group surject onto a
finite group `H`" — it is specifically the theory of representations onto
**dihedral / metacyclic** groups, i.e. it is intrinsically a **solvable**-
group technique: `D5` and `F20` are both metabelian (`D5 ⊃ C5 ⊃ 1`,
`F20 ⊃ C5 ⊃ 1`, derived length exactly 2), so the double/quadruple cyclic
cover tower built in `cusp_capability()`'s docstring terminates at an
**abelian** kernel (`C5`), which is exactly what an Alexander-polynomial-
type invariant detects.

**`A5` is perfect** (`A5′ = A5` — it is simple and nonabelian, so its
own commutator subgroup is itself) and **`S5′ = A5`** is also simple: the
derived series of `S5` is `S5 ⊃ A5 ⊃ A5 ⊃ ⋯`, terminating after **one**
step at a nonabelian, non-solvable subgroup, never reaching `1`. So the
"go down the derived series, get an abelian kernel, apply Fox coloring"
recipe has **at most one rung** available for `S5` (the sign cover
`S5 → C2`) and **zero** for `A5`, and in neither case does it reach an
abelian kernel that could carry a classical coloring invariant. This is
not a technical gap to be patched with more computation — it is the
reason the D5/F20 cusp census is a genuinely solvable-group phenomenon.

**What would replace it (not attempted here, flagged as the key open
TODO).** Determining which torus knots `T(p,q)` admit a representation of
`π₁(S³∖T(p,q)) = ⟨u,v ∣ uᵖ = vᵠ⟩` onto a subgroup `H ≤ A5` found in §4,
sending the meridian to the prescribed conjugacy class, is a **finite,
well-posed, machine-checkable** question in principle: choose `a ∈ H` with
`aᵖ = e`, `b ∈ H` with `bᵠ = e`, generating `H`, and evaluate the meridian
word (`Burde–Zieschang`-type formula, `μ = u⁻ˢvʳ` with `ps − qr = 1`) at
`(a,b)`. This was **not carried out** in this session — the meridian-word
convention was not independently re-derived/calibrated to the standard
this campaign requires, and getting the sign/order convention wrong would
silently produce a false "verified" table, which is worse than leaving it
open. **Structural hint, not a result:** the `(2,3,5)` triangle group is
classically isomorphic to `A5` (the icosahedral rotation group), so torus
knots with `{p,q} ⊆ {2,3,5}`-type local structure are the natural first
place such representations could live — but turning this into an actual
"minimal `A5`-capable cusp" table (the `A5`/`S5` analogue of `cusp_capability()`'s
`(2,5)`/`(4,5)` answers) is unresolved and is the natural next computation
for this line, not attempted here.

A cheap, unconditional, *partial* necessary condition requires no
representation theory at all: `A5`'s only element orders are
`{1,2,3,5}` (`lcm = 30`); if **both** `p` and `q` are coprime to `30`, the
only elements of order dividing `p` (resp. `q`) in `A5` are the identity,
so *no* nontrivial representation onto any subgroup of `A5` is possible at
all for that cusp type — e.g. `T(7,11)` can never host any `A5` escape,
trivial or not.

---

## 6. Verdict

**Does `A5`/`S5` collapse to the same cusp-gap analysis as `D5`/`F20`, or
not?**

**Partially, and precisely:**

1. **`Fix = 1` classes collapse exactly, with zero new work.** `A5`'s
   `(2,2)`-meridian and `S5`'s `(4,)`-meridian reduce, verbatim, to
   Theorem D's `4s`-omitted-points bookkeeping — the theorem was already
   general enough to not need solvability, it only needed `Fix = 1`.
2. **`Fix ≥ 2` classes (`A5`'s 3-cycle — the task's headline case; `S5`'s
   transposition) collapse *qualitatively*** — every one of the `Fix`
   individually-fixed sheets is, on its own, exactly the kind of degree-1
   section the Hartogs lemma protects, so each one's own omitted points
   are confined to singular points of `E` by the same argument, run once
   per section — **but not quantitatively**: the elementary ledger does
   not determine how many of the `Fix` candidate sections are genuinely
   affine (anywhere between 1 and `Fix`, by Lemma A/B alone) nor whether
   the genuine ones fuse into one connected multi-sheeted cover of `E` or
   stay as separate copies. This is authentically new bookkeeping, not
   present for `D5`/`F20`.
3. **`Fix = 0` classes are a genuinely new phenomenon**, not a variant of
   anything in the `D5`/`F20` ledger: because `A5`'s 5-cycle and `S5`'s
   `(2,3)`-class normally generate *by themselves* (unlike `D5`/`F20`'s
   non-generating 5-cycle), an irreducible `E` that is **generically
   entirely outside the image of `f`** becomes logically possible.
4. **The cusp-capability census does not transfer at all** — it was a
   solvable-group (metabelian, Fox-coloring) argument, and `A5`/`S5` are
   not solvable; §5 identifies exactly where and why it breaks, and what
   a replacement computation would need to look like, without attempting
   it.

The local-image (Theorem E) subgroup lattices computed in §4 are, however,
**strictly richer** for `A5`/`S5` than for `D5`/`F20` in every row except
one — multiple nonabelian escalation levels (`S3 ⊂ D5 ⊂ A5`; `C3 ⊂ A4 ⊂
A5`; `S3 ⊂ S4 ⊂ S5`; and, most tellingly, `F20 ⊂ S4 ⊂ S5` for `S5`'s
4-cycle meridian, which literally contains `F20`'s own `{C4, F20}` lattice
as its bottom two rungs and adds two more above it) instead of a clean
two-point `{abelian, full group}` dichotomy — the one exception being
`S5`'s `(2,3)`-class, which unusually *does* collapse to a clean two-point
`{C6, S5}` jump. So even where the mechanism transfers, the target for the
still-open cusp-realizability question is generally a richer object than
in the solvable case.

---

## Files

* [`src/n2/a5s5_ledger.py`](../src/n2/a5s5_ledger.py) — all computations
  above: the singleton-orbit fact (§3.1), the irreducible-`E` menu (§2),
  and the local-image census (§4). Run with
  `python src/n2/a5s5_ledger.py` (the census functions are slow — tens of
  minutes total; the class-table and orbit-decomposition parts are
  instant).
* [`src/n2/degree5_ledger.py`](../src/n2/degree5_ledger.py) — the upstream
  `D5`/`F20` ledger (Lemma A/B, Theorem C/D/E, `cusp_capability()`) this
  file extends and treats as an audited black box.
* [`docs/n2-campaign.md`](n2-campaign.md) — Round 20 / session 7 (the
  sibling D5/F20-side work: the P–Q interlock, and the tree/λ-localization
  notes cross-referenced above).

## Honest TODOs

1. ~~`S5`'s `(2,3)`- and `(4,)`-row of the §4 census~~ **DONE**: both
   completed and are recorded in §4's table and raw transcript
   (`{6,120}` and `{4,20,24,120}` respectively); the `(2,)` and `(2,3)`
   rows were additionally cross-checked against a second, independent
   `O(|G|²)` implementation and agree exactly in both cases (identical
   abelian/nonabelian classification on every order found).
2. **The `d_E`-realizability gap for `Fix ≥ 2`** (§3.2/§3.3): whether 1 or
   more of the `Fix` candidate sections are genuinely affine, and whether
   the genuine ones fuse under "vertical" (along-`E`) monodromy into one
   connected multi-sheeted cover or stay separate — needs boundary/
   Hurwitz-at-infinity data this elementary ledger does not model, exactly
   as the "silent components" caveat already flagged upstream.
3. **The `A5`/`S5` cusp-realizability census** (§5): no attempt was made
   to determine which torus-knot types realize which local image from §4
   — the meridian-word convention needed to do this rigorously (Burde–
   Zieschang) was not independently verified to the standard this campaign
   requires, so it is left open rather than guessed at.
4. **The `Fix = 0` "totally non-proper `E`" case** (§3.4): flagged as
   logically live for `A5`/`S5` but its Euler-characteristic/singular-
   point bookkeeping (the analogue of Theorem D, run on `Sing(E)` alone
   since there is no generic affine curve to normalize) was not attempted.
