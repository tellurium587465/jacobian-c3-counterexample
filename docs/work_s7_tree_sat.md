# S7: the decorated boundary tree — a machine model and a satisfiability search

**Date: 2026-07-24. Method: direct construction + exhaustive machine search
(no literature dependence for the main results; one external reference
fetched and cross-checked, not merely cited).** Machine parts:
[`src/n2/tree_sat.py`](../src/n2/tree_sat.py) (run with
`python src/n2/tree_sat.py`; every claim below is an assertion in that file,
not a hand computation quoted without a check).

This is a **session-7 companion** to the campaign's decorated-tree equation
system (`docs/n2-campaign.md`, "The decorated-tree equation system", session
6, and Round 19's Lê–Weber fusion) and sits alongside two sibling S7 notes
written the same day from the *literature* side —
[`work_s7_keller_infinity.md`](work_s7_keller_infinity.md) (does any theorem
forbid an isolated degree-1 dicritical coexisting with `E`-dicriticals?) and
[`work_s7_lambda_localization.md`](work_s7_lambda_localization.md) (can the
`λ`-invariant see `N_inf`?). This note attacks the same coexistence question
from the *combinatorial/computational* side: build the abstract decorated
tree that any SNC completion of `C²` obtained by boundary blowups must carry,
and ask whether the D5/F20 decorations can be simultaneously realized on it.

**Bottom line up front.** The abstract tree recurrences place **no
obstruction** on the required D5/F20 configurations: explicit 6- and
7-blowup witnesses exist and are confirmed **minimal** by exhaustive
canonicalized search (not merely "a" witness — genuinely the smallest). The
"isolated leaf with negative discrepancy" requirement, which looks at first
glance like it might be in tension with "free blowups only increase `a`", is
in fact cheap and unobstructed for **every** negative integer, and — a genuine
new fact found by the search, not assumed — the *fastest* possible descent is
not linear but **exactly Fibonacci/golden-ratio-rate**. This converges with
`work_s7_keller_infinity.md`'s literature verdict ("OPEN, leaning PERMITTED")
and with Borisov's explicit combinatorial "frameworks" (arXiv:1901.04073):
**whatever obstructs a genuine D5/F20 counterexample is not visible in the
abstract (discrepancy, self-intersection, adjacency) tree data alone** — it
must come from the map `f̄` itself. That extra structure is flagged as TODO
throughout, not modeled.

---

## 0. The model, and why it needs no extra validity checks

`Xbar` is built from `P²` (boundary = the single line `L` at infinity,
`L² = +1`, `a(L) := ord_L(dx∧dy) = -3`) by a finite sequence of blowups at
points of the (evolving) boundary. Two kinds of blowup:

* **Free point** on a single component `D` (not a node): new exceptional
  `E₀` has `E₀² = -1`, `a(E₀) = a(D)+1`; `D² -= 1`; `a(D)` itself
  **unchanged**; `E₀` meets only `D`.
* **Node** `D₁ ∧ D₂`: new `E₀` has `E₀² = -1`,
  `a(E₀) = a(D₁)+a(D₂)+1`; `D₁²` and `D₂²` each `-= 1`; `a(D₁), a(D₂)`
  themselves **unchanged**; `E₀` meets both `D₁, D₂`, which no longer meet
  each other.

Since every state built this way is *by construction* a bona fide smooth SNC
completion of `C²` reached from `P²` by an honest sequence of point blowups,
**no separate "is this a legitimate boundary" check is needed** — the code
never has to validate a tree found by search against some independent
criterion; correctness is inherited from the operations. The one structural
invariant worth recording (`BoundaryTree.assert_tree_consistent`, checked
after every construction below): `#edges = #vertices - 1` and the graph is
connected — i.e. it really is a tree, automatically preserved since a free
blowup attaches a leaf and a node blowup subdivides an edge, both of which
keep a tree a tree. This matches the classical fact (Gizatullin) that
completions of `C²` have tree-shaped SNC boundary; it is not separately
proved here, just consistent with everything the recurrences produce.

## 1. Verifying the recurrences (not citing them blindly)

The task asked that the recurrences be checked against a reference before
trusting the search. Two independent checks, both in
[`src/n2/tree_sat.py`](../src/n2/tree_sat.py) §0–1:

**(a) Re-derivation from the local geometry (sympy).** Near a boundary point
`p`, write `ω := dx∧dy = x₁^{a₁} x₂^{a₂} U(x₁,x₂) dx₁∧dx₂` in local analytic
coordinates (`a₂ = 0` at a free point of `D₁`; both nonzero at a node
`D₁∧D₂`; `U` a unit). Blow up `p` with the standard chart
`(s,y) → (x,y) = (s·y, y)` (exceptional `E = {y=0}`; strict transform of
`{x=0}` is `{s=0}`, meeting `E` transversally). `verify_blowup_jacobian()`
confirms the chart's Jacobian determinant is exactly `y` (order 1 — the
universal "+1"); `verify_exponent_algebra()` confirms, for 10 concrete
integer `(a₁,a₂)` samples (both signs, both the free-point case `a₂=0` and
genuine node cases), the identity

```
(s·y)^{a1} · y^{a2} · y   =   s^{a1} · y^{a1+a2+1}
```

i.e. the pulled-back form is `s^{a1} y^{a1+a2+1} U(sy,y) ds∧dy`: order along
the *surviving* strict transform is `a1` (**unchanged** — matches "`a(D)`
itself unchanged"), order along the *new* exceptional is `a1+a2+1`. Setting
`a2=0` gives the free-point recurrence `a(E)=a(D)+1`; both nonzero gives the
node recurrence `a(E)=a(D1)+a(D2)+1`. The self-intersection recurrence
(`D² -= (mult_p D)² = 1` since SNC transversality forces multiplicity 1) is
classical and not re-derived symbolically, but cross-checked against the
textbook fact `Bl_pt(P²) ≅ F₁` (Hirzebruch surface): the strict transform of
a line through the blown-up point becomes the self-intersection-0 ruling
curve, i.e. `1 → 0`, matching `D² → D²-1`.

**(b) Cross-check against Favre–Jonsson, arXiv:0711.2770** (fetched
directly, not from memory — WebFetch on the abstract page returned only
metadata, so the PDF was fetched and passed through the `r.jina.ai` text
mirror per the task's fallback instruction). Their §1.3 defines the
**thinness** `A(ν_E) = a_E/b_E` with `a_E := 1 + ord_E(dx∧dy)`. In our
notation `a(D) := ord_D(dx∧dy)`, so **`a_E = a(D) + 1`** exactly — matching
the campaign's own dictionary note in `n2-campaign.md`
("thinness `A(ν_D) = (a(D)+1)/b_D`"). Their Lemma 1.4 (blowing up a point of
an existing divisor, `A(ν) = A(ν_E) + 1/b_E`) is exactly our free-point
recurrence after translating conventions. **Both independent checks agree.**

**(c) Two known-example sanity tests** (`check_single_free_blowup`,
`check_hirzebruch_jung_chain` — both pass as executable assertions):

* One free blowup of a point of `L`: `a(E₀) = -2`, `E₀² = -1`, `L²: 1→0`
  (task's own requested check, reproduced exactly).
* A Hirzebruch–Jung-style chain: starting from a node and repeatedly
  blowing up "the corner nearest `D1`" (the standard toric continued-fraction
  recipe, e.g. Fulton §2.6) for 5 rounds produces final self-intersections
  `[-2,-2,-2,-2,-1]` — the hallmark HJ pattern (interior `-2`s, `-1` only at
  the currently-active fresh end) — exactly as asserted.

## 2. Task 2: searching for the D5 / F20 decorated trees

**Target predicates** (abstract-tree part only — see §4 for what is
deliberately *not* modeled):

* **D5**: `≥ 2` distinct components with `a = 1` (the two `E`-dicriticals),
  **and** `≥ 1` isolated leaf (`degree 1`, `≠ L`) with `a ≤ -2` (an
  "infinity dicritical", `a = -m-1`, `m ≥ 1`).
* **F20**: `≥ 1` component with `a = 3` (the `E`-dicritical), **and** the
  same isolated-negative-leaf clause.

**Explicit witnesses** (`build_D5_witness`, `build_F20_witness`, both
asserted correct):

```
D5  (6 blowups):  L(-3) -- E1(-2, LEAF)                      <- the m=1 infinity dicritical
                  L -- E2(-2) -- E3(-1) -- E4(0) -- E5(+1, LEAF)
                                              \-- E6(+1, LEAF)   <- the two a=1 E-dicriticals

F20 (7 blowups):  L(-3) -- E1(-2, LEAF)                      <- the m=1 infinity dicritical
                  L -- E2(-2) -- E3(-1) -- E4(0) -- E5(+1) -- E6(+2) -- E7(+3, LEAF)  <- the a=3 E-dicritical
```

Both use nothing but the simplest possible construction — a straight
ascending chain of free blowups off one child of `L`, plus one untouched
sibling leaf — and land at **6** and **7** blowups respectively, comfortably
inside the task's `≤ 12` bound.

**Exhaustive confirmation of minimality.** Rather than trust that these hand
constructions are optimal, `bfs_min_witness` runs a genuine breadth-first
search over **every** legal sequence of blowups, deduplicated at each depth
by a canonical (AHU-style) signature of the decorated rooted tree (so
isomorphic decorated states are never explored twice), and reports the first
depth at which the predicate is satisfied by *any* reachable state:

| depth | # distinct canonical states (full level) | D5 satisfied by some state? | F20 satisfied by some state? |
|---|---|---|---|
| 0 | 1 | no | no |
| 1 | 1 | no | no |
| 2 | 3 | no | no |
| 3 | 10 | no | no |
| 4 | 41 | no | no |
| 5 | 180 | no | no |
| 6 | 859 | **yes** (found after enumerating 118 of the 859) | no (all 859 checked) |
| 7 | not fully enumerated (search stops once found) | — | **yes** (found after enumerating 600) |

(The D5 search returns as soon as it finds a witness, so it does not itself
enumerate the full 859-state depth-6 level; that exact count comes from the
F20 search, which — since F20 is *not* satisfied at depth 6 — continues past
it and reports the full level before moving to depth 7.) The state space is
small and well-behaved (growth factor ≈ `4`–`5`× per level in this range; no
truncation was needed), so this is a genuine, complete proof that **6
blowups is the true minimum for D5 and 7 for F20** — not merely "found within
the search bound." Both are far under the task's `≤ 12` ceiling, with 5–6
blowups of slack.

**Reading this result honestly.** This says the *abstract* decoration
(discrepancy values + adjacency + leaf-status) required by the D5/F20 group
theory is realized by a boundary tree that is a completely generic, almost
minimal-complexity object — nothing about the numerology `{1,1,-m-1}` (D5)
or `{3,-m-1}` (F20) forces any tension at the level of the blow-up
recurrence. **This is a negative result for anyone hoping the abstract tree
alone would obstruct D5/F20** — it does not. See §5 for what this leaves
open.

## 3. Task 3 (the key sub-question): which `a`-values can an isolated leaf carry?

**Structural fact (proved, not just observed).** A component created by a
*node* blowup is **always born at degree 2** (`E0` meets *both* `D1, D2`),
and degree is non-decreasing thereafter (it only ever goes up, via later free
blowups targeting that component). **Hence a node-blowup output is never a
leaf, at any later time either.** The *only* components that can ever be
leaves are free-blowup outputs, and such a component remains a leaf forever
unless it is itself later chosen as the target of a free blowup — critically,
its neighbor's identity or its own self-intersection *can* change (via a
node blowup subdividing its single edge) without disturbing its degree or
its own `a`-value (which, per the recurrences, never changes once the
component is created).

This one fact answers the "how can `a<0` recur" puzzle directly: **it is not
that free blowups can decrease `a` — they can't — it is that the *node*
recurrence `a(E)=a(D1)+a(D2)+1` can produce a value more negative than
*either* input**, whenever both inputs are already `≤ -2`. Since `a(L)=-3`
is always available and is never consumed (`L` can be re-used as one
endpoint of arbitrarily many blowups over time, so long as each uses a fresh
point/edge), repeatedly combining a growing chain value with `L` drives `a`
to `-∞`, and one more *free* blowup off any such vertex creates a genuine
isolated leaf at that value.

**Two explicit constructions (both executed, both assertion-checked):**

* **Ascending chain** (free blowups only): `a` increases by exactly 1 each
  step, `a(w_i) = i - 3`, reaching every integer `≥ -2` as a leaf by
  freezing the chain at that point.
* **Descending chain** (repeated node blowups on the edge incident to `L`):
  `v1 = -2` (forced first move), then `v_k = a(L) + a(v_{k-1}) + 1 = v_{k-1}-2`,
  closed form `v_k = -2k`. **`v1` itself remains an isolated leaf of the
  final tree for every `k`** (checked: its degree stays 1 throughout, since
  each subsequent node blowup subdivides the *other* end of the chain, not
  `v1`'s own edge) — so `a=-2` (`m=1`) is trivially available alongside an
  arbitrarily long chain built elsewhere. One further free blowup off any
  `v_k` gives a fresh leaf at `v_k+1 = -2k+1`, covering every odd negative
  integer too.

**Union**, already at `n=12` blowups: every integer in `[-24, 9]` is realized
as *some* isolated-leaf `a`-value — far more than the D5/F20 requirement
(`m ≥ 1`, i.e. `a ≤ -2`) needs.

### A bonus discovery: the true extremal rate is Fibonacci, not linear

Running the exhaustive canonical search of §2 further (no early stopping,
tracking the minimum `a`-value over *all* vertices at each depth) gives:

| depth | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|---|
| true min `a` (exhaustive) | -3 | -4 | -6 | -9 | -14 | -22 | -35 | -56 |
| naive linear chain (`-2k`) | -2 | -4 | -6 | -8 | -10 | -12 | -14 | -16 |

The exhaustive minimum pulls sharply ahead of the naive descending chain
starting at depth 4. Extracting the actual optimal witness trees
(`E4: a=-9, nbrs=[E2,E3]`, `E5: a=-14, nbrs=[E3,E4]`, `E6: a=-22,
nbrs=[E4,E5]`, …) reveals the mechanism: **once two chain values are both
more negative than `a(L)=-3`, it becomes better to node-blow the edge
between the two most recently created vertices than to keep re-using `L`.**
This is exactly the classical continued-fraction chain "all partial
quotients 1" (the golden-ratio/Fibonacci extremal case). Explicitly
(`fibonacci_descent_chain` in the code): `E1=free(L)` (`a=-2`, kept aside as
the isolated infinity-dicritical leaf), `E2=node(L,E1)` (`a=-4`),
`E3=node(L,E2)` (`a=-6`), and from `E4` on, **always combine the two most
recent**: `E_k = node(E_{k-2},E_{k-1})`. Substituting `d_k := a(E_k)+1` turns
the recurrence into the **literal Fibonacci recursion** `d_k=d_{k-1}+d_{k-2}`
(`k≥4`), giving the closed form

> **`a(E_k) = -Fibonacci(k+2) - 1`** for all `k ≥ 2` (standard indexing
> `F₁=F₂=1`),

verified by the code against the recursive construction for `k` up to 12
(`-2,-4,-6,-9,-14,-22,-35,-56,-90,-145,-234,-378`) and matching the
independent exhaustive search *exactly* for every depth up to 8 (where the
exhaustive search remains complete) — strong evidence this construction is
the genuine global optimum, though a closed-form optimality proof for all
`n` was not attempted (flagged TODO; the exhaustive match through depth 8 is
real evidence, not a proof for all `n`). Crucially, `E1` remains an isolated
leaf throughout, exactly as needed for D5/F20 — so this sharper, exponential
descent coexists with the required decoration just as cheaply as the linear
one.

**Conclusion for the key sub-question.** The abstract discrepancy recurrence
places **no lower bound whatsoever** on `a(D)` for an isolated leaf `D`
(other than the trivial one set by how many blowups you spend): every
integer occurs, and the *fastest* achievable descent is not the naively
expected `-2` per blowup but an **exponential, golden-ratio-rate** descent
(`a ~ -φ^k`). "Isolated leaf with `a<0`" is, on this evidence, one of the
*cheapest* possible decorations to arrange — not a source of rigidity. This
directly and rigorously confirms the campaign's own deprioritization note
(session 6: "thinness alone cannot characterize dicritical-onto-curve
divisors").

## 4. What this does NOT model (honest scope limits)

1. **The map `f̄` itself is not modeled.** The tree carries `a(D)`,
   self-intersections, and adjacency only. It does *not* carry: the degree
   of `P|_D` or of `f̄|_D` (the "birational onto `E`", "degree-1 restriction"
   labels that distinguish an `E`-dicritical from an arbitrary `a=1` or `a=3`
   component); which components are dicritical *at all* (dicritical = the
   map is non-constant on `D`, a property of `f̄`, not of the abstract
   surface); or the requirement that contracting the tree the "other way"
   recovers the specific target `P²` (rather than some other completion) in
   a manner compatible with `f̄` having the prescribed monodromy. Task
   instructions flagged this gap explicitly in advance, and it is real: the
   witnesses in §2 only prove the *numerology* of `a`-values and tree
   positions is simultaneously satisfiable, not that a genuine map realizing
   them exists.
2. **No global consistency constraint from the group theory beyond the raw
   `a`-value/leaf requirements is encoded** (e.g. the precise count and
   mutual position of infinity dicriticals, `N_inf ∈ {1,3,5}`, or the
   `Σ k_i e_i = 4` dicritical-degree identity from `n2-campaign.md` Round 18
   — genuinely extra structure, not modeled here).
3. **Self-intersections are tracked and verified but not used as a
   constraint** in the §2 search (the D5/F20 predicates depend only on
   `a`-values and leaf status, per the task's literal wording); a sharper
   search folding in a required self-intersection profile (if the campaign's
   map-theoretic analysis pins one down) is a natural next step and is not
   attempted here.
4. **Optimality of the Fibonacci-descent construction for all `n`** (not
   just the exhaustively-checked `n ≤ 8`) is asserted only on the strength
   of an exact match at every checked depth, not a closed-form proof.

## 5. Convergence with the literature-side S7 notes (important cross-check)

Independently, the same day, a literature sweep
([`work_s7_keller_infinity.md`](work_s7_keller_infinity.md)) asked the *same*
qualitative question — can an isolated degree-1 infinity dicritical coexist
with `E`-dicriticals in a genuine Keller pair? — by searching the published
record rather than building the tree directly. Its verdict: **"OPEN, leaning
PERMITTED / not excluded"**, and in particular it surfaces **A. Borisov**
(arXiv:1901.04073; Beitr. Algebra Geom. 56 (2015); J. Algebraic Combin. 39
(2014)) as having already constructed explicit combinatorial "frameworks"
that **positively exhibit** boundary trees satisfying every known necessary
linear/adjunction/projection-formula condition, with isolated degree-1
divisors coexisting alongside high-degree dicritical divisors on the same
tree — i.e. essentially the same kind of abstract-tree satisfiability result
this note derives independently by direct computation, arrived at from a
different formalism (Borisov works with Mumford intersection theory / Stein
factorization "type-1/2/3/4" labels, not the raw `(a, D², adjacency)` data
used here). Borisov's own closing question ("Question 6.7: can one actually
use our frameworks to construct a Keller map?") is exactly this note's §4
item 1 — the real bottleneck, in both independent treatments, is realizing
the abstract combinatorics by an honest polynomial map, not the combinatorics
itself. **Two independent methods, on the same day, reached the same
conclusion: the abstract obstruction is not there; the map-theoretic one is
the open problem.**

## 6. Verdict

* **Recurrences: verified**, both by first-principles local computation
  (sympy, §1a) and against Favre–Jonsson arXiv:0711.2770 (§1b), and sanity
  checked against two known examples (single free blowup on `L`; a
  Hirzebruch–Jung continued-fraction chain).
* **D5 and F20 decorated trees: realizable**, in the abstract-tree sense, at
  **6** and **7** blowups respectively — proved minimal by exhaustive
  canonicalized search, well under the task's 12-blowup bound.
* **Key sub-question: answered.** Every integer is reachable as an isolated
  leaf's `a`-value; negative values are *cheap*, not obstructed, and in fact
  reachable at an exponential (Fibonacci/golden-ratio) rate rather than the
  naively expected linear one. The "isolated leaf with `a<0`" decoration is
  not a source of rigidity at the level of the abstract discrepancy
  recurrence.
* **What remains open**: whether the numerically-satisfiable abstract tree
  can be realized by an actual map `f̄` with the required dicritical-degree
  data — not addressed here, converges with the companion literature note's
  same conclusion, and is the natural next target (most concretely: attempt
  to translate one of Borisov's explicit "frameworks," or build a
  degree-tracking layer on top of `BoundaryTree` that also carries
  `deg(f̄|_D)` and checks the projection-formula / principal-divisor
  equations from `n2-campaign.md`'s "decorated-tree equation system").

## Files

* [`src/n2/tree_sat.py`](../src/n2/tree_sat.py) — `BoundaryTree` data
  structure and the two blowup operations (§1); reference re-derivation and
  Favre–Jonsson cross-check (§0); known-example sanity checks (§1);
  explicit D5/F20 witnesses + exhaustive canonicalized minimality search
  (§2–3); the ascending/descending-chain and Fibonacci-descent reachability
  theory (§4). Run with `python src/n2/tree_sat.py` (takes well under a
  minute; the full 8-level unbounded-minimum-tracking experiment referenced
  in §3's table takes about 10 seconds and is reproducible via the
  `fibonacci_descent_chain` / `bfs_min_witness` functions, not wired into a
  single flag — see the module docstring for how each figure above was
  produced).
* [`docs/n2-campaign.md`](n2-campaign.md) — session 6 ("decorated-tree
  equation system") and Round 19 (Lê–Weber fusion, the `a(D)=-m-1` infinity
  dicritical formula) that this note's search directly targets.
* [`docs/work_s7_keller_infinity.md`](work_s7_keller_infinity.md),
  [`docs/work_s7_lambda_localization.md`](work_s7_lambda_localization.md) —
  companion session-7 literature sweeps; §5 above records the convergence.
