"""
degree5_ledger.py -- the degree-5 escape ledger (n=2 campaign, session 4).

Machine-verifies the group-theoretic core of three statements about a
hypothetical plane Keller counterexample f: C^2 -> C^2 of geometric degree 5
(the minimal open degree), with exceptional (Jelonek) curve E and monodromy
group G = a transitive subgroup of S5.

  LEMMA A (nonempty affine preimage).  f is a degree-d covering off E, so
    chi(f^{-1}(E)) = d*chi(E) - (d-1).
  If f^{-1}(E) were empty the left side is 0, forcing chi(E) = (d-1)/d,
  which is not an integer for any d >= 2.  Hence f^{-1}(E) is NEVER empty:
  the exceptional curve always has a curve of affine preimages.

  LEMMA B (sheet-fix bound).  Let C be an irreducible component of E with
  meridian monodromy sigma_C in S_5, and let d_C be the number of affine
  preimage points over a generic point of C.  Each affine crossing sheet
  extends f^{-1} to a single-valued branch near C (etaleness), so it is
  FIXED by sigma_C:
        d_C  <=  Fix(sigma_C).
  (Calibration below: for Alpoge's 3D map the branch monodromy is a
  transposition in S3, Fix = 1, and the measured affine fiber over the
  branch surface is exactly 1 point; over the triple-root curve Z the
  monodromy context gives 0.)

  THEOREM C (section principle for solvable monodromy).  Meridians generate
  pi_1 of a plane-curve complement, so the meridian classes of the
  components of E must normally generate G.  The verified class data:

    - D5 : classes (5-cycle, Fix 0), (reflection = double transposition,
           Fix 1).  Only the reflection class normally generates.
    - F20: classes (5-cycle, Fix 0), (double transposition, Fix 1),
           (4-cycle, Fix 1).  Only the 4-cycle class normally generates.

  Hence for G in {D5, F20}: EVERY component of E with nontrivial meridian
  carries at most ONE affine sheet (d_C <= 1) -- its affine preimage is a
  section or empty -- and at least one component must carry the designated
  generating class (reflection resp. 4-cycle).  Components with 5-cycle
  meridians have d_C = 0: they are generically OUTSIDE the image of f
  (the 2D analogue of the missing curve Z in dimension 3).  For the
  unsolvable remainder: A5 allows d_C <= 2 (3-cycles), S5 allows
  d_C <= 3 (transpositions).

Caveat kept explicit: a component of E could a priori carry TRIVIAL
meridian monodromy (a fixed sheet escaping without wrapping); such "silent
components" are constrained only by nonproperness (d_C <= 4), not by
Lemma B.  Closing them out needs the boundary (Hurwitz-at-infinity) data,
not the affine ledger alone.
"""
import numpy as np
from sympy.combinatorics import Permutation, PermutationGroup
from sympy.combinatorics.named_groups import SymmetricGroup, AlternatingGroup


def transitive_subgroups_of_S5():
    c5 = Permutation([1, 2, 3, 4, 0])
    refl = Permutation([0, 4, 3, 2, 1])   # pentagon reflection fixing 0
    four = Permutation([0, 2, 4, 1, 3])   # x -> 2x mod 5 on {1..4}, fixes 0
    return {
        'C5': PermutationGroup([c5]),
        'D5': PermutationGroup([c5, refl]),
        'F20': PermutationGroup([c5, four]),
        'A5': AlternatingGroup(5),
        'S5': SymmetricGroup(5),
    }


def class_table(g):
    """[(cycle_type, Fix, normally_generates)] for nontrivial classes."""
    rows, seen = [], set()
    for el in g.elements:
        if el.is_identity:
            continue
        cyc = tuple(sorted(len(c) for c in el.cyclic_form))
        fix = 5 - sum(len(c) for c in el.cyclic_form)
        if (cyc, fix) in seen:
            continue
        seen.add((cyc, fix))
        nc = g.normal_closure(PermutationGroup([el]))
        rows.append((cyc, fix, nc.order() == g.order()))
    return sorted(rows)


def lemma_A():
    print("=== Lemma A: f^{-1}(E) is never empty ===")
    for d in range(2, 12):
        assert (d - 1) % d != 0
    print("  chi identity: chi(f^{-1}E) = d*chi(E) - (d-1); empty preimage")
    print("  needs chi(E) = (d-1)/d, non-integer for all d >= 2.  VERIFIED.")


def lemma_B_calibration():
    """3D calibration: over a generic point of the branch surface {A=0},
    the affine fiber of Alpoge's map has exactly Fix(transposition) = 1
    point (the double-root sheet has x = 2/P'(t) = infinity)."""
    print("\n=== Lemma B calibration on the 3D counterexample ===")
    b, c = 0.4, 0.7
    # solve A(a; b, c) = 0 for a: 27 c^2 a^2 + (16 - 18 b c) a + (b^3 c - b^2)
    roots_a = np.roots([27 * c**2, 16 - 18 * b * c, b**3 * c - b**2])
    a = roots_a[0]
    P = np.array([c, -2.0, b, -2.0 * a])
    ts = np.roots(P)
    dP = np.polyder(P)
    xs = [2.0 / np.polyval(dP, t) for t in ts]
    finite = sum(1 for x in xs if abs(x) < 1e4)
    print(f"  target on {{A=0}}: fiber sheets |x| = {[f'{abs(x):.3g}' for x in xs]}")
    print(f"  affine (finite-x) sheets: {finite}  ==  Fix(transposition in S3) = 1:"
          f"  {'PASS' if finite == 1 else 'FAIL'}")
    assert finite == 1


def theorem_C():
    print("\n=== Theorem C: the degree-5 ledger, per monodromy group ===")
    print(f"  {'G':4} | nontrivial classes (cycle type, Fix, normally generates)")
    expectations = {
        'C5': {((5,), 0, True)},
        'D5': {((5,), 0, False), ((2, 2), 1, True)},
        'F20': {((5,), 0, False), ((2, 2), 1, False), ((4,), 1, True)},
    }
    for name, g in transitive_subgroups_of_S5().items():
        rows = class_table(g)
        print(f"  {name:4} | " + "; ".join(
            f"{cyc} Fix={fx} gen={'Y' if gen else 'n'}" for cyc, fx, gen in rows))
        if name in expectations:
            assert set(rows) == expectations[name], name
        if name == 'A5':
            assert all(gen for _, _, gen in rows)          # simple group
            assert max(fx for _, fx, _ in rows) == 2
        if name == 'S5':
            gens = {cyc for cyc, _, gen in rows if gen}
            assert gens == {(2,), (4,), (2, 3)}
            assert max(fx for _, fx, _ in rows) == 3
    print("\n  CONSEQUENCES (D5 / F20 = the solvable cases):")
    print("  * every nontrivial-meridian component of E keeps <= 1 affine sheet")
    print("    (its affine preimage is a SECTION or empty);")
    print("  * D5 needs a reflection-meridian component; F20 needs a 4-cycle one")
    print("    (the only normally-generating classes);")
    print("  * 5-cycle-meridian components are generically outside the image")
    print("    (d_C = 0): the 2D analogue of the missing curve Z;")
    print("  * A5 allows d_C <= 2, S5 allows d_C <= 3 (looser ledger).")


def theorem_D():
    """THEOREM D (omitted-points theorem, irreducible E, solvable monodromy).

    Assume E irreducible and G in {D5, F20}.  Then the single meridian class
    must normally generate G, so it is the reflection (resp. 4-cycle) class,
    with Fix = 1; Lemma B gives d_E <= 1, Lemma A gives Etilde nonempty, and
    every component of Etilde dominates E (etale maps are quasi-finite), so
    d_E = 1 and Etilde is IRREDUCIBLE, mapping birationally onto its image;
    on normalizations Etilde^nu -> E^nu = C is birational etale, hence an
    open immersion (ZMT): Etilde^nu = C minus beta' points.

    Euler bookkeeping (chi(E) = 1 - s with s = branch excess of Sing E,
    s >= 1 by Chau; chi(Etilde) = 1 - beta' - stilde, stilde <= s since
    local branches inject):
        1 - beta' - stilde = 5(1 - s) - 4   ==>   beta' = 5s - stilde,
    so   4s <= beta' <= 5s,  and in particular  beta' >= 4:

    THE IMAGE OF f OMITS AT LEAST FOUR ISOLATED POINTS ON E (exactly
    5s - stilde on the normalization) -- over each, even the surviving
    section sheet escapes to infinity."""
    import sympy as sp
    s, st = sp.symbols('s stilde', positive=True)
    beta = sp.symbols("beta'", nonnegative=True)
    chi_E = 1 - s
    chi_Et = 1 - beta - st
    sol = sp.solve(sp.Eq(chi_Et, 5 * chi_E - 4), beta)[0]
    assert sp.simplify(sol - (5 * s - st)) == 0
    lo = sp.simplify(sol.subs(st, s))       # stilde <= s  ==> beta' >= 4s
    hi = sp.simplify(sol.subs(st, 0))       # stilde >= 0  ==> beta' <= 5s
    assert lo == 4 * s and hi == 5 * s
    # Round-14 branch-packet refinement (GPT-5.6-sol audit): for y in E,
    # either ALL normalization points over y are punctures or NONE (a point
    # of Etilde over y reproduces all r_y branches via the ambient local
    # biholomorphism; at most one such point by the open immersion).  With
    # M = E \ f(C^2), s = s_hit + s_miss, n_miss = #(M ∩ Sing E):
    #   beta = m_smooth + (s_miss + n_miss),   stilde = s_hit,
    #   |M| = m_smooth + n_miss,
    # and beta + stilde = 5s closes to |M| = 4s EXACTLY.
    m_sm, s_hit, s_miss, n_miss = sp.symbols('m_smooth s_hit s_miss n_miss',
                                             nonnegative=True)
    s_total = s_hit + s_miss
    beta_pack = m_sm + s_miss + n_miss
    st_pack = s_hit
    M_size = sp.simplify(
        sp.solve(sp.Eq(beta_pack + st_pack, 5 * s_total),
                 m_sm)[0] + n_miss)
    assert sp.simplify(M_size - 4 * s_total) == 0
    print("\n=== Theorem D: omitted-points theorem (E irreducible, D5/F20) ===")
    print("  forced chain: meridian = generating class (Fix 1) -> d_E = 1")
    print("  -> Etilde irreducible, open immersion on normalizations.")
    print(f"  Euler bookkeeping: beta' = {sol}  (verified symbolically)")
    print(f"  bounds: {lo} <= beta' <= {hi}  with s >= 1 (Chau)")
    print("  branch-packet refinement (round 14): |E \\ f(C^2)| = 4s EXACTLY")
    print("  (verified symbolically).  Multibranch singular points number")
    print("  <= s, but UNIBRANCH ones (cusps, r=1) are NOT bounded by s")
    print("  (round-15 correction) -- see theorem_E for the consequence.")


def hartogs_sharpness_3d():
    """The Hartogs section lemma (see docs) forbids omitted points at
    SMOOTH points of the exceptional curve wherever a section exists.
    Sharpness witness in dimension 3: Alpoge's omitted curve Z lies
    entirely inside Sing({A=0}) -- the full gradient of the discriminant
    vanishes along Z -- so the 3D escape happens exactly where the
    lemma's smoothness hypothesis fails.  Machine check:"""
    import sympy as sp
    a, b, c, t = sp.symbols('a b c t')
    A = 27*a**2*c**2 - 18*a*b*c + 16*a + b**3*c - b**2
    sub = {c: t, b: sp.Rational(4, 3)/t, a: sp.Rational(4, 27)/t**2}
    vals = [sp.simplify(A.subs(sub))] + [
        sp.simplify(sp.diff(A, v).subs(sub)) for v in (a, b, c)]
    assert all(v == 0 for v in vals), vals
    # round-15 strengthening (GPT-5.6-sol): Sing({A=0}) EQUALS Z.
    # c = 0: A_a = 16 there, no singular points; c != 0: with B = bc,
    # C = ac^2, A = c^{-2} H(B,C), and eliminating C from H_C = H_B = 0
    # gives exactly (3B-4)^2 = 0, i.e. Z.
    B, C = sp.symbols('B C')
    H = 27*C**2 - 18*B*C + 16*C + B**3 - B**2
    assert sp.simplify(sp.diff(A, a).subs(c, 0) - 16) == 0
    Csol = sp.solve(sp.diff(H, C), C)[0]
    elim = sp.factor(sp.diff(H, B).subs(C, Csol))
    assert elim == sp.Rational(1, 3) * (3*B - 4)**2, elim
    print("\n=== Hartogs lemma sharpness (3D witness) ===")
    print("  A and grad A vanish identically on Z:  Z inside Sing({A=0}).")
    print(f"  Conversely (round 15): elimination gives {elim} = 0,")
    print("  so Sing({A=0}) = Z EXACTLY.  The 3D omitted curve escapes")
    print("  only through the singular locus -- the hypothesis is sharp.")


def theorem_E():
    """THEOREM E (conditional; round-15 adjudication).

    Hartogs section lemma (AUDITED SOUND): if q is a SMOOTH point of E
    and the affine preimage contains a section over a punctured
    neighborhood of q in E, the fixed-sheet degree-1 component V1 union
    the section maps biholomorphically onto B_eps \\ {q}; the inverse
    extends over q by Hartogs/Riemann extension in dimension 2, so q is
    NOT omitted.  Corollary: the affine fiber count is locally constant
    on the smooth locus of E (statement not located in the literature;
    a close claim of Jelonek, arXiv:2011.03472, is WITHDRAWN with
    recorded errors and must not be cited).

    ROUND-15 BUG FIX: #Sing E <= s is FALSE -- unibranch singularities
    (cusps) have r = 1 and do not contribute to s.  The omitted points
    |M| = 4s could a priori all hide at unibranch singular points, where
    the local complement has a KNOT group (not Z) and the fixed-sheet
    argument fails.  Hence Theorem E is CONDITIONAL, with the gap
    narrowed by the subgroup facts verified below:

    the local monodromy image at a unibranch point is a subgroup H <= G
    that is the normal closure of a meridian-class element inside H
    (knot groups are normally generated by the meridian).  Verified:
    for D5 with meridian class (2,2) the options are {C2, D5}; for F20
    with meridian class (4,) the options are {C4, F20}.  If H is ABELIAN
    (C2/C4) the section sheet is fixed by the whole image, V1 is again
    degree 1, and the Hartogs kill runs.  So escape at a unibranch point
    requires FULL nonabelian local monodromy -- for D5 a dihedral cover
    of the cusp knot, i.e. a 5-COLORABLE knot: det of the local knot
    divisible by 5 (Fox).  An ordinary cusp (2,3) has det 3: killed.

    CONDITIONAL THEOREM E: a degree-5 plane Keller counterexample with
    irreducible exceptional curve and solvable monodromy must channel
    ALL 4s omitted points through unibranch singularities of E whose
    local knots admit full D5 (resp. F20) representations.  In
    particular, if E has no such cusps, D5/F20 are impossible and only
    A5/S5 remain (C5 being dead by the Galois case)."""
    from sympy.combinatorics import PermutationGroup
    print("\n=== Theorem E (conditional) + the cusp gap subgroup facts ===")
    for name, mer_type in (('D5', (2, 2)), ('F20', (4,))):
        g = transitive_subgroups_of_S5()[name]
        els = list(g.elements)
        meridians = [e for e in els
                     if tuple(sorted(len(c) for c in e.cyclic_form)) == mer_type]
        # subgroups of g generated by <= 2 elements (covers the full
        # lattice for these metacyclic groups), containing a meridian,
        # equal to the normal closure of that meridian inside themselves
        found = set()
        subs = {}
        for a in els:
            for b in els:
                h = PermutationGroup([a, b])
                subs[tuple(sorted(str(x) for x in h.elements))] = h
        for h in subs.values():
            hels = set(h.elements)
            for m in meridians:
                if m in hels:
                    if h.normal_closure(PermutationGroup([m])).order() == h.order():
                        found.add(h.order())
        print(f"  {name}: meridian-normally-generated local images have "
              f"orders {sorted(found)}")
        assert found == {2, 10} if name == 'D5' else found == {4, 20}
    print("  abelian option (order 2/4) -> Hartogs kill still runs;")
    print("  escape at a cusp needs FULL D5/F20 local monodromy")
    print("  (for D5: a 5-colorable cusp knot, det = 0 mod 5; the")
    print("  ordinary cusp (2,3) has det 3 -> killed).")
    print("  CONDITIONAL: no D5/F20 counterexample unless every omitted")
    print("  point sits at such a special cusp.  A5/S5 remain the target.")


def cusp_capability():
    """SESSION-5: which cusps can host the escape (the cusp-gap census).

    THE DOUBLE-COVER TOWER (necessary condition).  For G = D5 the Galois
    closure gives K < K2 < N with [K2:K] = 2, Gal(N/K2) = C5.  Let W be
    the double cover of the target plane branched along E (w^2 = delta_E;
    connected since the meridian maps to the reflection class, nontrivial
    in D5^ab = C2).  The meridian of the branch curve upstairs pushes to
    mu^2, and rho(mu^2) = r^2 = 1: so the C5-cover X_N -> W is UNRAMIFIED
    IN CODIMENSION 1.  Removing points from a smooth surface does not
    change pi_1, so the cover is detected by pi_1 of the smooth part W_sm:

        D5 monodromy exists  ==>  H_1(W_sm; Z/5) != 0,

    which by Fox's correspondence localizes over the singularities of E:
    5-torsion of the double-branched-cover homology = 5-colorability data.
    For F20 the same tower with the quartic cyclic cover W4 (meridian ->
    4-cycle, order 4 in F20^ab = C4; rho(mu^4) = sigma^4 = 1) gives:

        F20 monodromy  ==>  Z/5 in the C4-twisted homology of W4_sm,

    the classical metabelian criterion: 5 | |Delta_K(i)|^2 locally.

    THE CENSUS (machine-computed): for a torus-knot cusp (m,n),
    det = |Delta(-1)| and |Delta(i)|^2 decide capability:
      * both m,n odd  ->  det = 1: NO D5 escape ever;
      * D5 needs 5 | det: minimal cusp (2,5), i.e. A4: y^2 = x^5, delta=2;
      * F20 needs 5 | |Delta(i)|^2: minimal cusp (4,5), delta = 6.
    So an F20 counterexample with irreducible E must pack 4s cusps of
    delta >= 6 EACH (plus >= 1 multibranch point) into a RATIONAL curve
    with one place at infinity."""
    import sympy as sp
    t = sp.symbols('t')

    def alex_torus(m, n):
        num = (t**(m*n) - 1) * (t - 1)
        den = (t**m - 1) * (t**n - 1)
        return sp.Poly(sp.cancel(sp.simplify(num / den)), t)

    print("\n=== Session 5: cusp capability census ===")
    rows = []
    for (m, n) in [(2, 3), (2, 5), (2, 7), (3, 4), (3, 5), (2, 15),
                   (4, 5), (2, 25), (5, 6), (4, 7), (3, 7), (5, 7)]:
        D = alex_torus(m, n)
        det1 = abs(D.eval(-1))
        det4 = sp.Integer(sp.expand(D.eval(sp.I) * sp.conjugate(D.eval(sp.I))))
        rows.append(((m, n), det1, det4, det1 % 5 == 0, det4 % 5 == 0))
    for (mn, d1, d4, d5ok, f20ok) in rows:
        print(f"  T{mn}: det={d1} {'D5' if d5ok else '--'}  "
              f"|D(i)|^2={d4} {'F20' if f20ok else '---'}")
    # verified structural facts used in the docs:
    assert all(not d5 for (mn, _, _, d5, _) in rows
               if mn[0] % 2 == 1 and mn[1] % 2 == 1)       # odd-odd: det 1 or odd nondiv? assert no-D5
    assert dict((mn, d5) for (mn, _, _, d5, _) in rows)[(2, 5)] is True
    assert dict((mn, f) for (mn, _, _, _, f) in rows)[(4, 5)] is True
    assert dict((mn, f) for (mn, _, _, _, f) in rows)[(2, 5)] is False
    print("  minimal D5 cusp = (2,5) [delta 2]; minimal F20 cusp = (4,5)")
    print("  [delta 6]; odd-odd cusps can never host a D5 escape.")


if __name__ == '__main__':
    lemma_A()
    lemma_B_calibration()
    theorem_C()
    theorem_D()
    hartogs_sharpness_3d()
    theorem_E()
    cusp_capability()
    print("\nDEGREE-5 ESCAPE LEDGER: all group-theoretic facts machine-verified.")
