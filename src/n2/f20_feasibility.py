"""
f20_feasibility.py -- P4 feasibility test (n=2 campaign, session 6 prediction).

PREDICTION UNDER TEST (docs/n2-campaign.md, Session 6 table, P4, confidence
0.40): "the F20 case dies on delta-budget + Bezout + Abhyankar-Moh semigroup
arithmetic alone at all degrees" d = deg E, tested for d <= 16.

QUESTION.  Can an irreducible RATIONAL plane curve E of degree d, with ONE
PLACE AT INFINITY, carry:
  - exactly 4 cusps of type (4,5) (semigroup <4,5>, delta = 6, multiplicity 4
    each) -- the minimal F20-capable torus cusp (see cusp_capability() in
    degree5_ledger.py);
  - at least 1 more singular point with >= 2 branches (delta >= 1);
  - geometric genus 0?

This script is a NECESSARY-CONDITION SIEVE, not an existence proof.  It
implements three elementary, fully rigorous filters and one partially-proved
lemma about the point at infinity; it does NOT attempt the deep question of
whether a polynomial parametrization actually realizing the prescribed
AFFINE singularities exists (that is the genuine open problem, flagged in
the TODOs at the bottom).

  (1) GENUS / DELTA BUDGET.  For a rational (genus 0) plane curve,
        sum_{P in Sing(closure)} delta_P = (d-1)(d-2)/2,
      the sum running over ALL singular points of the PROJECTIVE closure,
      including the point(s) at infinity.  With delta_infinity = 0 (see (3)
      below for why this is always achievable) the affine points alone must
      carry (d-1)(d-2)/2 exactly, so a NECESSARY condition is
        (d-1)(d-2)/2  >=  4*delta_cusp + 1.
      The "+1" is realizable by an ordinary node OR, for larger slack, by a
      2-branch point of arbitrarily high delta (two smooth branches with
      high-order tangency have delta = their intersection number, which can
      be ANY positive integer, while the point's multiplicity stays exactly
      2 -- see delta_budget_is_flexible()).  So this bound is tight: any
      d with (d-1)(d-2)/2 >= min_affine is NOT excluded by the budget alone.

  (2) BEZOUT / MULTIPLICITY.  Any plane curve F of degree k not sharing a
      component with E satisfies, for every point P,
        (F.E)_P  >=  mult_P(F) * mult_P(E),
      and Bezout gives  sum_P (F.E)_P <= k*d.  Existence of an F with
      prescribed multiplicities r_P >= 0 at a finite point set is
      GUARANTEED (pure linear algebra: passing through P with multiplicity
      >= r is exactly r(r+1)/2 linear conditions on the k(k+3)/2 + 1
      coefficients of a degree-k curve; a homogeneous linear system with
      more unknowns than equations always has a nonzero solution) whenever
      sum_P r_P(r_P+1)/2 <= k(k+3)/2.  bezout_search() below brute-forces
      small (k, {r_P}) to find the BEST (largest) forced lower bound on d.

  (3) THE POINT AT INFINITY (partial Abhyankar-Moh / Suzuki theory).
      A rational curve with one place at infinity is exactly a polynomial
      parametrization t -> (f(t), g(t)); the branch at infinity carries a
      numerical semigroup (the "Abhyankar semigroup" / delta-sequence of
      Abhyankar-Moh, reproved by Suzuki, Ann. Inst. Fourier 49 (1999)
      375-404; effectivized by Assi-Garcia Sanchez, arXiv:1407.0490) whose
      first generator is deg(f), and whose genus (= delta_infinity) is
      given by a Frobenius-number formula analogous to (1)'s two-generator
      case but for a whole chain of "approximate roots".  Enumerating that
      full semigroup theory for every d <= 16 is NOT attempted here (TODO).
      What IS proved (elementarily, no semigroup machinery needed): choosing
      deg(f) = d, deg(g) = d-1 (leading coefficients both nonzero, lower
      coefficients arbitrary) makes the branch at infinity SMOOTH, hence
      delta_infinity = 0, for every d.  smooth_infinity_lemma() verifies
      this by direct power-series computation (the local coordinate at
      infinity has order exactly 1).  Since delta_infinity = 0 is the
      BEST case for the budget in (1) (any delta_infinity > 0 only shrinks
      the affine allowance), this lemma shows the genus-budget bound in (1)
      is already the sharpest available from this angle -- the deeper
      semigroup theory would only be needed to either (a) rule out
      delta_infinity = 0 for some structural reason (it can't -- (3) is a
      constructive existence proof) or (b) attempt an actual realizability
      argument for the specific affine cusps, which is out of scope.

  Combining (1)+(2)+(3): a candidate degree d survives this sieve iff
  d >= max(bezout_min_degree, genus_min_degree).  Degrees that fail are
  RIGOROUSLY IMPOSSIBLE (for a curve of exactly this singular content).
  Degrees that survive are merely NOT EXCLUDED by these tools -- existence
  is open.
"""
import itertools
import math
from fractions import Fraction

import sympy as sp


# ---------------------------------------------------------------------------
# (0) numerical-semigroup delta invariants, with a brute-force self-check
# ---------------------------------------------------------------------------

def delta_two_generator(p, q):
    """delta invariant of a plane branch with semigroup <p,q>, gcd(p,q)=1
    (a single Puiseux pair (p,q)): classical Sylvester-Frobenius formula
    genus(<p,q>) = (p-1)(q-1)/2."""
    assert math.gcd(p, q) == 1, (p, q)
    assert (p - 1) * (q - 1) % 2 == 0
    return (p - 1) * (q - 1) // 2


def delta_two_generator_bruteforce(p, q, cap=4000):
    """Independent check: count gaps of the numerical semigroup <p,q> by
    direct sieve up to `cap` (cap must exceed the Frobenius number)."""
    assert math.gcd(p, q) == 1
    reachable = bytearray(cap)
    reachable[0] = 1
    for n in range(1, cap):
        if (n >= p and reachable[n - p]) or (n >= q and reachable[n - q]):
            reachable[n] = 1
    gaps = sum(1 for n in range(cap) if not reachable[n])
    return gaps


def self_check_semigroups():
    print("=== self-check: semigroup delta invariants ===")
    for (p, q) in [(2, 3), (2, 5), (4, 5), (3, 5), (3, 4)]:
        formula = delta_two_generator(p, q)
        brute = delta_two_generator_bruteforce(p, q)
        status = "PASS" if formula == brute else "FAIL"
        print(f"  <{p},{q}>: formula delta={formula}, brute-force delta={brute}  {status}")
        assert formula == brute
    print("  F20 cusp (4,5): delta = 6 confirmed.")
    print("  D5  cusp (2,5): delta = 2 confirmed.")


# ---------------------------------------------------------------------------
# (1) genus / delta budget
# ---------------------------------------------------------------------------

def min_affine_delta(cusp_delta, num_cusps=4, extra_min_delta=1):
    return num_cusps * cusp_delta + extra_min_delta


def genus_budget(d):
    """(d-1)(d-2)/2, the arithmetic genus of a plane curve of degree d
    (= total delta for a rational curve, summed over ALL singular points
    of the projective closure)."""
    return (d - 1) * (d - 2) // 2


def genus_min_degree(min_affine, d_max=200):
    """Smallest d with genus_budget(d) >= min_affine, i.e. the smallest
    degree admitting delta_infinity = 0 AND enough affine budget."""
    for d in range(2, d_max):
        if genus_budget(d) >= min_affine:
            return d
    return None


def delta_budget_is_flexible():
    """A 2-branch point made of two SMOOTH branches meeting with
    intersection multiplicity I (I = order of tangency) has:
      - multiplicity (of the union, as a point of the reduced curve) = 2
        for EVERY I >= 1 (mult of a reduced curve at a point = sum of the
        branch multiplicities; two smooth branches contribute 1+1=2
        regardless of how tangent they are);
      - delta = I (delta of a 2-branch germ with branches C1, C2, each
        smooth, equals their intersection number (C1.C2)_0, standard fact,
        e.g. Casas-Alvero, "Singularities of Plane Curves", Thm 3.5.1 /
        the additivity delta = sum(branch deltas) + sum(pairwise
        intersections), branch deltas = 0 for smooth branches).
    Hence ANY extra affine delta budget B >= 1 is realizable by a SINGLE
    multibranch point of multiplicity exactly 2 (never forcing the
    Bezout multiplicity bound in (2) above 2 for this point, independent
    of how large d needs to be)."""
    print("=== delta-budget flexibility: 2 smooth branches, tangency I ===")
    print("  mult(point) = 2 for all I >= 1; delta(point) = I (unbounded).")
    print("  => the '+1' (or more) extra affine delta never forces the")
    print("     multibranch point's multiplicity above 2, at any degree d.")


# ---------------------------------------------------------------------------
# (2) Bezout / multiplicity search
# ---------------------------------------------------------------------------

def dof(k):
    """Projective dimension of the linear system of degree-k plane curves
    ((k+1)(k+2)/2 coefficients, minus 1 for overall scaling)."""
    return (k + 1) * (k + 2) // 2 - 1


def num_coeffs(k):
    return (k + 1) * (k + 2) // 2


def cost(r):
    """Linear conditions to force multiplicity >= r at a point
    (order-r vanishing: value + all partials up to order r-1)."""
    return r * (r + 1) // 2


def bezout_search(mult_list, k_max=6, r_max=4):
    """Search degree-k auxiliary curves F (k = 1..k_max) and multiplicity
    assignments r_i in [0, r_max] at each of the special points of E (whose
    own multiplicities are mult_list), subject to the dimension-count
    existence guarantee  sum_i cost(r_i) <= dof(k) (a nonzero F with those
    multiplicities is GUARANTEED to exist, unconditionally, by linear
    algebra -- no general-position assumption needed).  For each valid
    (k, r) returns the forced lower bound  d >= ceil( sum_i r_i*mult_list[i] / k ),
    and reports the best (largest) one found, which is a rigorous necessary
    condition on d (as long as k < d, so F cannot share E as a component;
    checked by the caller)."""
    best = {"required_d": 0, "k": None, "r": None, "bound": None}
    n = len(mult_list)
    for k in range(1, k_max + 1):
        budget = dof(k)
        for r in itertools.product(range(0, r_max + 1), repeat=n):
            c = sum(cost(ri) for ri in r)
            if c > budget or c == 0:
                continue
            bound = sum(ri * mi for ri, mi in zip(r, mult_list))
            if bound <= 0:
                continue
            required_d = math.ceil(Fraction(bound, k))
            if required_d > best["required_d"]:
                best.update(required_d=required_d, k=k, r=r, bound=bound)
    return best


# ---------------------------------------------------------------------------
# (3) the point at infinity: smoothness lemma (deg g = deg f - 1)
# ---------------------------------------------------------------------------

def smooth_infinity_lemma(d, order_check=3, seed=1):
    """Verify, by direct power-series computation, that for
    f(t) = t^d + (generic lower terms), g(t) = t^(d-1) + (generic lower
    terms), the local coordinate u(s) at the point at infinity (s = 1/t)
    has order EXACTLY 1 in s -- i.e. the branch at infinity is smooth,
    delta_infinity = 0 -- for ANY choice of the lower-order coefficients
    (as long as the two leading coefficients are nonzero, which holds by
    definition of "degree").

    Derivation used (see module docstring (3)): in the chart where the
    dominant projective coordinate is normalized to 1, the other affine
    coordinate is  u(s) = s * G(s) / F(s)  with F(s) = s^d f(1/s),
    G(s) = s^(d-1) g(1/s) both POWER SERIES WITH F(0) = G(0) = 1 (the
    leading coefficients of f, g, normalized to 1).  Hence u(s) = s * (power
    series with nonzero constant term) has order exactly 1 in s, for any
    lower-order coefficients whatsoever: no genericity assumption is even
    needed here, unlike the general (deg f, deg g) case.
    """
    s = sp.symbols('s')
    rng_a = [((seed * (i + 3)) % 7) - 3 for i in range(d)]       # deterministic "arbitrary" coeffs
    rng_b = [((seed * (i + 5)) % 7) - 3 for i in range(d - 1)]
    f_rev = 1 + sum(rng_a[i] * s**(i + 1) for i in range(d - 1))   # s^d f(1/s), degree d-1 tail
    g_rev = 1 + sum(rng_b[i] * s**(i + 1) for i in range(d - 2)) if d >= 3 else sp.Integer(1)
    F = sp.series(f_rev, s, 0, order_check + 2).removeO()
    G = sp.series(g_rev, s, 0, order_check + 2).removeO()
    u = sp.series(s * G / F, s, 0, order_check + 1).removeO()
    poly = sp.Poly(sp.expand(u), s) if u != 0 else None
    coeff0 = poly.coeff_monomial(1) if poly and poly.degree() >= 0 else 0
    coeff1 = poly.coeff_monomial(s) if poly else 0
    smooth = (coeff0 == 0) and (coeff1 != 0)
    return smooth, coeff0, coeff1


def run_smooth_infinity_checks(degrees):
    print("=== smoothness-at-infinity lemma: deg f = d, deg g = d-1 ===")
    all_ok = True
    for d in degrees:
        smooth, c0, c1 = smooth_infinity_lemma(d)
        status = "PASS (delta_infinity = 0)" if smooth else "FAIL"
        print(f"  d={d:2d}: u(s) = {c0} + {c1}*s + O(s^2)   {status}")
        all_ok = all_ok and smooth
    assert all_ok
    print("  (arbitrary lower-order coefficients each time -- the result")
    print("   does not depend on genericity, only deg g = deg f - 1.)")


# ---------------------------------------------------------------------------
# putting it together: the feasibility table
# ---------------------------------------------------------------------------

def feasibility_table(name, cusp_p, cusp_q, extra_mult=2, d_range=range(5, 17)):
    cusp_delta = delta_two_generator(cusp_p, cusp_q)
    min_affine = min_affine_delta(cusp_delta)
    cusp_mult = min(cusp_p, cusp_q)  # multiplicity of a (p,q) branch is min(p,q)
    mult_list = [cusp_mult, cusp_mult, cusp_mult, cusp_mult, extra_mult]

    genus_d = genus_min_degree(min_affine)
    bz = bezout_search(mult_list, k_max=6, r_max=4)
    bezout_d = bz["required_d"]
    combined_min = max(genus_d, bezout_d)

    print(f"\n=== {name}: cusp type ({cusp_p},{cusp_q}), delta={cusp_delta}, "
          f"mult={cusp_mult}; extra point mult={extra_mult} ===")
    print(f"  min affine delta needed (4 cusps + 1 extra) = {min_affine}")
    print(f"  genus-budget minimal degree (delta_infinity=0)      : d >= {genus_d}")
    print(f"  best Bezout bound found: k={bz['k']} (degree-{bz['k']} aux. curve), "
          f"r={bz['r']} (mult. reqd at the 5 special pts),")
    print(f"    forced intersection >= {bz['bound']}  =>  k*d >= {bz['bound']}  =>  d >= {bezout_d}")
    print(f"  COMBINED minimal degree surviving the sieve: d >= {combined_min}")
    if genus_d == bezout_d:
        binding = "TIE (genus budget and Bezout coincide)"
    elif genus_d > bezout_d:
        binding = "genus/delta budget"
    else:
        binding = "Bezout/multiplicity"
    print(f"  binding constraint: {binding}")

    rows = []
    for d in d_range:
        g_ok = genus_budget(d) >= min_affine
        # Bezout: only trust the search's k < d (so F can't share E as a
        # component); recompute restricted to k < d for full rigor.
        bz_d = bezout_search(mult_list, k_max=min(6, d - 1), r_max=4)
        b_ok = d >= bz_d["required_d"]
        feasible = g_ok and b_ok
        if not g_ok and not b_ok:
            binding_d = "both (genus & Bezout)"
        elif not g_ok:
            binding_d = "genus/delta budget"
        elif not b_ok:
            binding_d = "Bezout/multiplicity"
        else:
            binding_d = "-- (survives sieve)"
        rows.append((d, genus_budget(d), g_ok, bz_d["required_d"], b_ok, feasible, binding_d))
    return rows, dict(cusp_delta=cusp_delta, min_affine=min_affine,
                       genus_d=genus_d, bezout_d=bezout_d,
                       combined_min=combined_min, bz=bz)


def print_table(rows):
    print(f"  {'d':>3} | {'genus budget':>12} | {'genus OK':>8} | {'Bezout min d':>12} | "
          f"{'Bezout OK':>9} | {'FEASIBLE':>8} | binding (if excluded)")
    print("  " + "-" * 100)
    for (d, gb, g_ok, bmd, b_ok, feas, binding) in rows:
        print(f"  {d:>3} | {gb:>12} | {str(g_ok):>8} | {bmd:>12} | {str(b_ok):>9} | "
              f"{str(feas):>8} | {binding}")


if __name__ == '__main__':
    self_check_semigroups()
    delta_budget_is_flexible()
    run_smooth_infinity_checks(list(range(5, 17)))

    f20_rows, f20_summary = feasibility_table("F20 configuration", 4, 5, extra_mult=2)
    print_table(f20_rows)

    d5_rows, d5_summary = feasibility_table("D5 configuration", 2, 5, extra_mult=2)
    print_table(d5_rows)

    print("\n=== summary ===")
    print(f"  F20: minimal degree surviving sieve = {f20_summary['combined_min']} "
          f"(feasible for d in [{f20_summary['combined_min']}, 16] out of tested range)")
    print(f"  D5 : minimal degree surviving sieve = {d5_summary['combined_min']}")
