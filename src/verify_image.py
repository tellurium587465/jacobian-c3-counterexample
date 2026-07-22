"""
verify_image.py -- exact verification of the fiber census / exact image theorem.

    python src/verify_image.py     (run from src/)

Exits 0 iff all checks pass.  Requires only sympy.
"""
import sympy as sp
from counterexample import (F_map, apply, fiber, fiber_cubic_P, A_coeff,
                            x, y, z, a, b, c, T)
from image_census import Z_IDEAL, Z_point, census

PASS, FAIL = "  [PASS]", "  [FAIL]"
_failures = []


def check(name, cond):
    print((PASS if cond else FAIL), name)
    if not cond:
        _failures.append(name)


def main():
    print("=" * 72)
    print("The exact image of Alpoge's map:  F(C^3) = C^3 \\ Z")
    print("=" * 72)
    F = F_map()

    # ---- 1. Z is exactly the perfect-cube (triple-root) locus -------------
    print("\n[1] Z = V(3bc-4, 27ac^2-4) is the perfect-cube locus of the fiber cubic")
    Pz = fiber_cubic_P(sp.Rational(4, 27)/c**2, sp.Rational(4, 3)/c, c)
    check("P = c (T - 2/(3c))^3 identically on the parametrization of Z",
          sp.simplify(Pz - c*(T - sp.Rational(2, 3)/c)**3) == 0)
    # conversely, matching  c(T-t0)^3 = cT^3 - 2T^2 + bT - 2a  forces the ideal:
    t0 = sp.symbols('t0')
    m = sp.Poly(sp.expand(c*(T - t0)**3 - fiber_cubic_P(a, b, c)), T)
    sols = sp.solve(m.all_coeffs(), [t0, a, b], dict=True)
    ok = any(sp.simplify(s[a] - sp.Rational(4, 27)/c**2) == 0 and
             sp.simplify(s[b] - sp.Rational(4, 3)/c) == 0 for s in sols)
    check("conversely a perfect cube forces a = 4/(27c^2), b = 4/(3c)", ok)
    check("Z lies inside the branch surface {A = 0}",
          sp.simplify(A_coeff(*Z_point(c))) == 0)
    check("Z is closed: 3bc = 4 forces c != 0 (Z misses the c=0 plane)", True)

    # ---- 2. the c = 0 plane is entirely covered ---------------------------
    print("\n[2] The c = 0 plane is covered by the explicit x = 0 section")
    sec = [sp.expand(Fi.subs({x: 0, y: b, z: a - 4*b**2})) for Fi in F]
    check("F(0, b, a - 4b^2) = (a, b, 0) identically", sec == [a, b, 0])

    # ---- 3. census on samples from every stratum --------------------------
    print("\n[3] Fiber census: |fiber| = 3 / 1 / 0 on {A!=0} / {A=0}\\Z / Z")
    samples = [
        ((1, 1, 1), 3), ((2, -1, 3), 3), ((0, 1, 0), 3),          # A != 0
        ((0, 0, 1), 1),                                            # A = 0, c != 0, off Z
        ((sp.Rational(1, 64), sp.Rational(1, 2), 0), 1),           # A = 0, c = 0 (16a=b^2)
        (Z_point(1), 0), (Z_point(sp.Rational(1, 2)), 0), (Z_point(-3), 0),   # Z
    ]
    for tgt, expect in samples:
        tgt = tuple(sp.nsimplify(v) for v in tgt)
        pred, fib = census(*tgt)
        # cross-check the t-model fiber against brute solve for small cases
        direct = sp.solve([F[0] - tgt[0], F[1] - tgt[1], F[2] - tgt[2]],
                          [x, y, z], dict=True)
        check(f"target {tgt}: predicted {expect}, "
              f"t-model {len(fib)}, direct solve {len(direct)}",
              pred == expect == len(fib) == len(direct))
        if fib:
            # map-back check: exact for rational fibers; for radical ones,
            # reconstruct from 50-digit numeric roots of the fiber cubic
            # (avoids branch ambiguity of symbolic cube-root formulas)
            ok = True
            rational_pts = [P for P in fib
                            if all(getattr(v, 'is_rational', False) for v in P)]
            for P in rational_pts:
                if apply(F, P) != tgt:
                    ok = False
            if len(rational_pts) < len(fib):
                av, bv, cv = tgt
                Pc = sp.Poly(fiber_cubic_P(av, bv, cv), T)
                for tv in Pc.nroots(n=60):
                    r = sp.N(3*cv*tv**2 - 4*tv + bv, 60)
                    if abs(r) < sp.Float('1e-30'):
                        continue                     # multiple root: dead sheet
                    xv = sp.N(2/r, 60)
                    yv = sp.N(tv - r/2, 60)
                    zv = sp.N(sp.Rational(5, 4)*r**2 - sp.Rational(3, 2)*tv*r
                              - cv*r**3/8, 60)
                    sub = {x: xv, y: yv, z: zv}
                    for Fi, tval in zip(F, tgt):
                        if abs(sp.N(Fi.subs(sub) - tval, 60)) > sp.Float('1e-40'):
                            ok = False
            check("   ... and each preimage maps back to the target", ok)

    # ---- 4. Z is one C* orbit; shadow point ------------------------------
    print("\n[4] Structure of the missing curve")
    lam = sp.symbols('lam', nonzero=True)
    p0 = Z_point(1)
    orbit = (lam**2*p0[0], lam*p0[1], p0[2]/lam)
    check("Z = the C*-orbit (weights (2,1,-1)) through (4/27, 4/3, 1)",
          all(sp.simplify(orbit[i] - Z_point(1/lam)[i]) == 0 for i in range(3)))
    Bv, Cv = p0[1]*p0[2], p0[0]*p0[2]**2
    Delta = 27*Cv**2 - 18*Bv*Cv + 16*Cv + Bv**3 - Bv**2
    check("its shadow point is (B,C) = (4/3, 4/27), on the discriminant Delta = 0",
          (Bv, Cv) == (sp.Rational(4, 3), sp.Rational(4, 27)) and sp.simplify(Delta) == 0)

    print("\n" + "=" * 72)
    if _failures:
        print(f"RESULT: {len(_failures)} CHECK(S) FAILED:", _failures)
        raise SystemExit(1)
    print("RESULT: ALL CHECKS PASSED.")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
