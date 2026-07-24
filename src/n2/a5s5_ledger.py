"""
a5s5_ledger.py -- extending the degree-5 escape ledger to the UNSOLVABLE
monodromy cases G = A5, S5 (n=2 campaign, session 7).

Upstream: src/n2/degree5_ledger.py builds the ledger for the SOLVABLE cases
G = C5 (dead), D5, F20 and proves, for E irreducible:

  * the single meridian class must normally generate G (section principle);
  * for D5/F20 the only normally-generating class has Fix = 1, so the
    affine/finite part of the fiber over a generic point of E is a SINGLE
    section (d_E = 1);
  * the Hartogs section lemma then forces every point where that lone
    section fails to extend (an "omitted point") to sit at a SINGULAR point
    of E -- and the cusp-capability census (Fox coloring / Alexander
    polynomial) further pins these to specific torus-cusp types.

This module asks: does the SAME machinery survive for A5 and S5, where
Fix can be 0, 1, 2 (A5) or 0, 1, 3 (S5), i.e. the affine part of the fiber
over E can have MORE than one sheet?  The upstream docstring already
flagged the answer schematically ("A5 allows d_C <= 2, S5 allows d_C <= 3");
here we work out what those extra sheets actually look like.

KEY GENERAL FACT (verified below, group-independent): Fix(sigma) is always
the union of the SINGLETON <sigma>-orbits.  Consequently, however large
Fix(sigma_E) is, EVERY affine/fixed sheet is on its own, individually a
DEGREE-1 local section near E -- never sharing an orbit with another fixed
sheet.  The Hartogs section lemma (a degree-1 section's inverse extends
across a SMOOTH point of E by Riemann/Hartogs removable-singularity in
dimension 2) therefore applies SECTION BY SECTION, regardless of how many
fixed sheets there are and regardless of which group G is realized.  This
is the reason Theorem D/E's chain of reasoning (once Fix(sigma_E) is known)
never actually used solvability of G -- only the VALUE of Fix(sigma_E) for
the (unique, since E is irreducible) normally-generating meridian class.

What genuinely changes for A5/S5:
  (1) more than one normally-generating class can occur (A5: ALL nontrivial
      classes, since A5 is simple);
  (2) the "escaping" (non-fixed) part of the fiber can itself split into
      SEVERAL nontrivial orbits (e.g. a (2,2)-meridian gives two independent
      escaping 2-orbits, not one connected 4-orbit as for D5/F20's own
      Fix=1 classes) -- a genuinely new bookkeeping question about how many
      independent "escaping components" dance around E;
  (3) the cusp-CAPABILITY census (which specific cusp types can carry a
      given class as FULL, non-abelian local monodromy) loses its classical
      handle: D5 and F20 are METABELIAN (derived length 2), so Fox
      n-colorability / the Alexander polynomial -- an abelian invariant --
      exactly detects capability.  A5 is SIMPLE (perfect: A5' = A5) and
      S5' = A5 is also simple, so neither group has a solvable derived
      series beyond one step; there is no abelian tower for a classical
      coloring invariant to bite on.  Representability of a torus-knot
      group onto A5 (or a subgroup with a prescribed meridian conjugacy
      class) is a question about actual finite quotients of the torus-knot
      group <u,v | u^p = v^q>, decidable in principle (choose images of
      order dividing p, q respectively) but NOT attempted here as a
      verified census -- flagged as TODO, with the classical fact that the
      (2,3,5) triangle group IS A5 (icosahedral rotation group) noted as a
      structural hint, not a proof of anything about our setting.

Machine-verified below: the class/Fix/normal-generation table (shared with
degree5_ledger.py); the singleton-orbit fact; the orbit decomposition of
every viable meridian; and (SLOW: tens of minutes total) the local-image
subgroup census generalizing degree5_ledger.theorem_E to A5 and S5.
"""
import itertools
import time

from sympy.combinatorics import Permutation, PermutationGroup

from degree5_ledger import transitive_subgroups_of_S5, class_table


def orbit_decomposition(perm, n=5):
    """<perm>-orbits on {0,...,n-1} as a sorted list of tuples."""
    seen, orbits = set(), []
    for x in range(n):
        if x in seen:
            continue
        orb = [x]
        y = perm(x)
        while y != x:
            orb.append(y)
            seen.add(y)
            y = perm(y)
        seen.add(x)
        orbits.append(tuple(sorted(orb)))
    return sorted(orbits, key=len)


def singleton_orbit_fact():
    """GENERAL FACT: Fix(sigma) == union of the singleton <sigma>-orbits,
    for every permutation sigma in every transitive subgroup of S5.  Hence
    every affine/fixed sheet is, on its own, a degree-1 local section --
    the hypothesis the Hartogs lemma needs -- with NO dependence on G or on
    how many OTHER fixed sheets there are."""
    print("=== Singleton-orbit fact (group-independent input to Hartogs) ===")
    checked = 0
    for name, g in transitive_subgroups_of_S5().items():
        for e in g.elements:
            fix = sorted(x for x in range(5) if e(x) == x)
            orbs = orbit_decomposition(e)
            singles = sorted(o[0] for o in orbs if len(o) == 1)
            assert fix == singles, (name, e)
            checked += 1
    print(f"  verified Fix(sigma) = union of singleton orbits for all "
          f"{checked} elements across {{C5,D5,F20,A5,S5}}.")
    print("  => EVERY affine/fixed sheet is individually a degree-1 local")
    print("  section, for ANY meridian class, in ANY transitive G <= S5.")
    print("  The Hartogs section-lemma argument (degree5_ledger.theorem_E)")
    print("  therefore applies section-by-section regardless of G or Fix.")


def irreducible_E_menu():
    """THE A5/S5 MENU.  For E irreducible, the (unique) meridian class must
    normally generate G (section principle).  Tabulate, for every such
    class in A5 and S5: Fix = d_E (number of individually-fixed / degree-1
    sections), and the orbit-degree multiset of the ESCAPING (non-fixed)
    part -- the analogue of the "omitted points" bookkeeping's input."""
    print("\n=== The A5/S5 menu: normally-generating meridian classes ===")
    menu = {}
    for name in ("A5", "S5"):
        g = transitive_subgroups_of_S5()[name]
        rows = class_table(g)
        viable = [(cyc, fix) for cyc, fix, gen in rows if gen]
        menu[name] = viable
        print(f"\n  {name} (order {g.order()}):")
        for cyc, fix in sorted(viable, key=lambda r: -r[1]):
            escaping = list(cyc)  # the non-fixed orbit degrees
            tag = ("ALL escape (no section)" if fix == 0 else
                   f"{fix} degree-1 section(s) + escaping orbit(s) {escaping}")
            print(f"    class {cyc!s:8} Fix=d_E={fix}  ->  {tag}")
    # sanity: the non-generating classes (would need E reducible)
    print("\n  (non-generating classes -- excluded for irreducible E, would")
    print("   need a SECOND component of E to appear at all, as for D5/F20's")
    print("   own 5-cycle class):")
    for name in ("A5", "S5"):
        g = transitive_subgroups_of_S5()[name]
        rows = class_table(g)
        excluded = [(cyc, fix) for cyc, fix, gen in rows if not gen]
        print(f"    {name}: {excluded if excluded else '(none -- A5 simple)'}")
    return menu


def local_image_census(g, mer_type, expected_orders=None, label=""):
    """Generalization of degree5_ledger.theorem_E's subgroup census: which
    subgroups H <= g, containing a representative of conjugacy class
    mer_type, satisfy H = normal_closure_H(<that representative>)?  (I.e.
    H is a subgroup that COULD be the image of a unibranch cusp's knot
    group, whose meridian is normally generating by Wirtinger.)  Returns
    {order: is_abelian}."""
    t0 = time.time()
    els = list(g.elements)
    meridians = [e for e in els
                 if tuple(sorted(len(c) for c in e.cyclic_form)) == mer_type]
    subs = {}
    # unordered pairs suffice: PermutationGroup([a,b]) == PermutationGroup([b,a])
    for a, b in itertools.combinations_with_replacement(els, 2):
        h = PermutationGroup([a, b])
        key = tuple(sorted(str(x) for x in h.elements))
        subs.setdefault(key, h)
    found = {}
    for h in subs.values():
        hels = set(h.elements)
        for m in meridians:
            if m in hels:
                if h.normal_closure(PermutationGroup([m])).order() == h.order():
                    found.setdefault(h.order(), []).append(h.is_abelian)
    result = {order: all(vals) for order, vals in found.items()}
    dt = time.time() - t0
    print(f"  {label or mer_type}: local-image orders {result}  "
          f"({dt:.0f}s, {len(els)}^2/2 pair search)")
    if expected_orders is not None:
        assert set(result) == expected_orders, (label, result, expected_orders)
    return result


def cusp_gap_generalization():
    """Run the local-image census for every Fix >= 1 (section-bearing)
    normally-generating class of A5 and S5, i.e. the direct A5/S5 analogue
    of degree5_ledger.theorem_E.  SLOW (~5-30 min total): full O(|G|^2)
    subgroup search per class."""
    print("\n=== Local-image subgroup census (A5/S5 analogue of Theorem E) ===")
    G = transitive_subgroups_of_S5()

    print("\n  A5 meridians (all 3 nontrivial classes normally generate):")
    local_image_census(G['A5'], (2, 2), {2, 6, 10, 60}, "A5 (2,2) Fix=1")
    local_image_census(G['A5'], (3,), {3, 12, 60}, "A5 (3,)  Fix=2")
    local_image_census(G['A5'], (5,), {5, 60}, "A5 (5,)  Fix=0")

    print("\n  S5 meridians (only (2,), (2,3), (4,) normally generate):")
    local_image_census(G['S5'], (2,), {2, 6, 24, 120}, "S5 (2,)   Fix=3")
    local_image_census(G['S5'], (2, 3), {6, 120}, "S5 (2,3)  Fix=0")
    local_image_census(G['S5'], (4,), {4, 20, 24, 120}, "S5 (4,)   Fix=1")

    print("\n  Reading (A5, Fix=1, meridian (2,2)): local image in")
    print("  {C2, S3, D5, A5} -- i.e. a RICHER lattice of possible cusp")
    print("  escalations than D5's own {C2, D5} dichotomy (Theorem E): an")
    print("  A5-hosted cusp could open only PART of the way (S3 or D5)")
    print("  without needing the full nonabelian A5.")
    print("  Reading (A5, Fix=2, meridian (3,)): local image in")
    print("  {C3, A4, A5} -- the 2 SEPARATE degree-1 sections are each")
    print("  individually Hartogs-killable at smooth points; escalation to")
    print("  A4 (order 12, the unique subgroup normally generated by a")
    print("  3-cycle within itself) is the minimal nonabelian channel.")
    print("  Reading (A5, Fix=0, meridian (5,)): local image in {C5, A5}")
    print("  only -- D5 (order 10) is NOT available here (the 5-cycle's")
    print("  normal closure inside D5 is just C5, not D5 itself) -- matches")
    print("  degree5_ledger's D5 cusp census using the SAME (2,5) cusp.")
    print("  Reading (S5, Fix=1, meridian (4,)): local image in")
    print("  {C4, F20, S4, S5} -- CONTAINS F20's own {C4, F20} dichotomy as")
    print("  its bottom two rungs (F20's 4-cycle meridian is the SAME class)")
    print("  plus two escalation levels invisible from inside F20 alone.")
    print("  Reading (S5, Fix=0, meridian (2,3)): local image in {C6, S5}")
    print("  only -- a stark two-point jump (no A5, D5, F20, or S4 option:")
    print("  none of them contains a (2,3)-cycle-type element at all).")
    print("  Reading (S5, Fix=3, meridian (2,)): local image in")
    print("  {C2, S3, S4, S5} -- the classical symmetric-group tower; no")
    print("  A5/D5/F20 option (none contains a bare transposition).")


if __name__ == '__main__':
    singleton_orbit_fact()
    irreducible_E_menu()
    cusp_gap_generalization()
    print("\nA5/S5 LEDGER EXTENSION: group theory machine-verified; cusp-")
    print("REALIZABILITY (which torus-knot types achieve which local image)")
    print("remains open -- see docs/work_s7_a5s5_ledger.md Section 5.")
