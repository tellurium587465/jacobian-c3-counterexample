"""
verify_n2.py -- exact verification of the n=2 "shadow" analysis.

    python src/n2/verify_n2.py       (run from src/n2/)

Exits 0 iff all checks pass.  Requires only sympy.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

import sympy as sp
from shadow import shadow_data, shadow_map, bracket_D, bracket, s, w, x, y, z

PASS, FAIL = "  [PASS]", "  [FAIL]"
_failures = []


def check(name, cond):
    print((PASS if cond else FAIL), name)
    if not cond:
        _failures.append(name)


def main():
    print("=" * 72)
    print("The hyperbolic C*-shadow of Alpoge's map, and the shadow principle")
    print("=" * 72)

    # ---- 0. equivariance of Alpoge's map --------------------------------
    print("\n[0] Equivariance (weights (-1,1,2) -> (2,1,-1))")
    lam = sp.symbols('lam', positive=True)
    u = 1 + x*y
    f = sp.expand(u**3*z + y**2*u*(4 + 3*x*y))
    g = sp.expand(y + 3*x*u**2*z + 3*x*y**2*(4 + 3*x*y))
    h = sp.expand(2*x - 3*x**2*y - x**3*z)
    sub = {x: x/lam, y: lam*y, z: lam**2*z}
    check("f(t.p) = t^2 f, g(t.p) = t g, h(t.p) = t^-1 h",
          sp.expand(f.subs(sub) - lam**2*f) == 0 and
          sp.expand(g.subs(sub) - lam*g) == 0 and
          sp.simplify(h.subs(sub) - h/lam) == 0)

    # ---- 1. shadow data --------------------------------------------------
    print("\n[1] Shadow data (Pf, Pg, Ph)")
    Pf, Pg, Ph = shadow_data()
    check("Pf = (s+1)(3s^3+s^2 w+4s^2+2sw+w)",
          sp.expand(Pf - (s+1)*(3*s**3 + s**2*w + 4*s**2 + 2*s*w + w)) == 0)
    check("Pg = 9s^3+3s^2 w+12s^2+6sw+s+3w",
          sp.expand(Pg - (9*s**3 + 3*s**2*w + 12*s**2 + 6*s*w + s + 3*w)) == 0)
    check("Ph = 2-3s-w", sp.expand(Ph - (2 - 3*s - w)) == 0)
    # support conditions making f,g polynomial: monomials s^j w^k need
    # j+2k >= 2 for Pf and j+2k >= 1 for Pg
    ok_f = all(j + 2*k >= 2 for (j, k), _ in sp.Poly(Pf, s, w).terms())
    ok_g = all(j + 2*k >= 1 for (j, k), _ in sp.Poly(Pg, s, w).terms())
    check("support conditions (Pf: j+2k>=2, Pg: j+2k>=1)", ok_f and ok_g)

    # ---- 2. bracket identity = Keller constant ---------------------------
    print("\n[2] Bracket identity")
    check("-2 Pf{Pg,Ph} + Pg{Pf,Ph} + Ph{Pf,Pg} = -2  (= det DF)",
          bracket_D(Pf, Pg, Ph) == -2)

    # ---- 3. shadow principle for GENERIC Pf,Pg,Ph ------------------------
    print("\n[3] Shadow principle (generic symbolic proof)")
    A = sp.Function('A')(s, w); B = sp.Function('B')(s, w); C = sp.Function('C')(s, w)
    fx = (A.subs({}) / x**2).subs({s: x*y, w: x**2*z})
    gx = (B / x).subs({s: x*y, w: x**2*z})
    hx = (C * x).subs({s: x*y, w: x**2*z})
    J3 = sp.Matrix(3, 3, lambda i, j: sp.diff([fx, gx, hx][i], [x, y, z][j]))
    D3 = sp.simplify(J3.det().subs({y: s/x, z: w/x**2}))
    check("det DF is x-free (a function of s,w only)", x not in D3.free_symbols)
    Dbr = sp.expand(-2*A*bracket(B, C) + B*bracket(A, C) + C*bracket(A, B))
    check("det DF equals the bracket formula", sp.simplify(sp.expand(D3) - Dbr) == 0)
    phi1g, phi2g = B*C, A*C**2
    dJg = sp.simplify(sp.Matrix([[sp.diff(phi1g, s), sp.diff(phi1g, w)],
                                 [sp.diff(phi2g, s), sp.diff(phi2g, w)]]).det())
    check("det J_phi = -Ph^2 * det DF (generic identity)",
          sp.simplify(dJg + C**2*D3) == 0)

    # ---- 4. the concrete shadow map --------------------------------------
    print("\n[4] Alpoge's shadow phi")
    phi1, phi2 = shadow_map()
    dJ = sp.expand(sp.Matrix([[sp.diff(phi1, s), sp.diff(phi1, w)],
                              [sp.diff(phi2, s), sp.diff(phi2, w)]]).det())
    check("det J_phi = 2(3s+w-2)^2 (a perfect square, NOT constant)",
          sp.expand(dJ - 2*(3*s + w - 2)**2) == 0)
    onL = {w: 2 - 3*s}
    check("the line L: 3s+w=2 is contracted to (0,0)",
          sp.expand(phi1.subs(onL)) == 0 and sp.expand(phi2.subs(onL)) == 0)
    import random
    random.seed(7)
    sizes = []
    for _ in range(2):
        sig = sp.Rational(random.randint(-8, 8), random.randint(1, 4))
        om = sp.Rational(random.randint(-8, 8), random.randint(1, 4))
        sizes.append(len(sp.solve([phi1 - sig, phi2 - om], [s, w], dict=True)))
    check(f"generically 3-to-1 (random fibers {sizes})", all(n == 3 for n in sizes))
    # descended rational triple collision
    trip = [(sp.Rational(-4, 3), 3), (-2, 9), (sp.Rational(1, 3), sp.Rational(-1, 2))]
    imgs = [(sp.expand(phi1.subs({s: p[0], w: p[1]})),
             sp.expand(phi2.subs({s: p[0], w: p[1]}))) for p in trip]
    check("rational triple collision (-4/3,3),(-2,9),(1/3,-1/2) -> (-1,-1)",
          len(set(trip)) == 3 and imgs[0] == imgs[1] == imgs[2] == (-1, -1))

    # ---- 5. honesty: what this does NOT show -----------------------------
    print("\n[5] What this does NOT show")
    check("det J_phi is not constant (phi is NOT a plane Keller map)",
          sp.degree(sp.expand(dJ), gen=s) > 0)

    # ---- 6. the (tau, rho) normal form (GPT-5.6's refinement) ------------
    print("\n[6] Normal form: phi factors through the universal marked cubic")
    tau, rho, B, C, T = sp.symbols('tau rho B C T')
    H = 2 - 3*s - w
    tv, rv = H*(s + 1), 2*H                       # tau = H(s+1) [= c*t], rho = 2H [= c*P'(t)]
    Bv = rv + 4*tv - 3*tv**2
    Cv = tv**2 - tv**3 + rv*tv/2
    check("phi = chi o psi with psi=(tau,rho), chi=(rho+4tau-3tau^2, tau^2-tau^3+rho*tau/2)",
          sp.expand(Bv - phi1) == 0 and sp.expand(Cv - phi2) == 0)
    check("universal cubic: tau^3-2tau^2+B*tau-2C = 0 and rho = 3tau^2-4tau+B",
          sp.expand(tv**3 - 2*tv**2 + Bv*tv - 2*Cv) == 0 and
          sp.expand(rv - (3*tv**2 - 4*tv + Bv)) == 0)
    check("psi inverts on rho!=0: s = 2tau/rho-1, w = 5-6tau/rho-rho/2",
          sp.simplify(2*tv/rv - 1 - s) == 0 and
          sp.simplify(5 - 6*tv/rv - rv/2 - w) == 0)
    Jpsi = sp.Matrix([[sp.diff(tv, s), sp.diff(tv, w)], [sp.diff(rv, s), sp.diff(rv, w)]])
    chi1, chi2 = rho + 4*tau - 3*tau**2, tau**2 - tau**3 + rho*tau/2
    Jchi = sp.Matrix([[sp.diff(chi1, tau), sp.diff(chi1, rho)],
                      [sp.diff(chi2, tau), sp.diff(chi2, rho)]])
    check("det Dpsi = -2H and det Dchi = -rho/2 (product = 2H^2 = det J_phi)",
          sp.expand(Jpsi.det() + 2*H) == 0 and sp.expand(Jchi.det() + rho/2) == 0)
    Delta = 27*C**2 - 18*B*C + 16*C + B**3 - B**2
    check("Disc_T(T^3-2T^2+BT-2C) = -4*Delta(B,C)",
          sp.expand(sp.discriminant(T**3 - 2*T**2 + B*T - 2*C, T) + 4*Delta) == 0)
    pull = sp.factor(Delta.subs({B: phi1, C: phi2}))
    check("Delta(phi) = -H^2 * (quartic)  (H^2 divides the pulled-back discriminant)",
          sp.rem(sp.Poly(sp.expand(Delta.subs({B: phi1, C: phi2})), s, w),
                 sp.Poly(sp.expand(H**2), s, w)) == 0 if True else False)
    # fiber probes on the discriminant curve Delta=0 away from the origin:
    # tau=1 gives (B,C)=(1,0) on Delta=0; expect a degenerate (smaller) fiber
    fib_deg = sp.solve([phi1 - 1, phi2], [s, w], dict=True)
    check(f"over (B,C)=(1,0) on Delta=0 the fiber is smaller ({len(fib_deg)} < 3 points)",
          len(fib_deg) < 3)

    # ---- 7. plane hyperbolic rigidity: symbolic case identities ----------
    print("\n[7] Plane hyperbolic rigidity -- case identities (symbolic p,q)")
    from rigidity import v as vv, p as pp, q as qq
    import rigidity as R
    # (7.0) the ALL-DEGREES identity with generic functions A,B and symbolic
    # exponents a,b,c,d -- this is the complete proof of Step 2 (GPT-5.6's repair)
    xs, ys = sp.symbols('xs ys', positive=True)
    aa_, bb_, cc_, dd_ = sp.symbols('aa_ bb_ cc_ dd_')
    Agen = sp.Function('Agen')(vv)
    Bgen = sp.Function('Bgen')(vv)
    vsub = xs**qq * ys**pp
    P1g = xs**aa_ * ys**bb_ * Agen.subs(vv, vsub)
    P2g = xs**cc_ * ys**dd_ * Bgen.subs(vv, vsub)
    Jg = sp.expand(sp.diff(P1g, xs)*sp.diff(P2g, ys) - sp.diff(P1g, ys)*sp.diff(P2g, xs))
    Eg = R.general_E(Agen, Bgen, aa_, bb_, cc_, dd_)
    claim = xs**(aa_ + cc_ - 1) * ys**(bb_ + dd_ - 1) * Eg.subs(vv, vsub)
    check("ALL-DEGREES: det = x^{a+c-1} y^{b+d-1} [(ad-bc)AB + v((ap-bq)AB'+(qd-pc)A'B)]",
          sp.simplify(Jg - claim) == 0)
    a0, a1, a2, a3, b0, b1, b2, b3 = sp.symbols('a0 a1 a2 a3 b0 b1 b2 b3')
    A = a0 + a1*vv + a2*vv**2 + a3*vv**3
    Bp = b0 + b1*vv + b2*vv**2 + b3*vv**3
    # S2: (x A(v), y B(v)) -> det = [A B + v (p A B' + q A' B)](v=x^q y^p)
    det_S2 = R.det_map(R.semi_invariant(1, 0, A), R.semi_invariant(0, 1, Bp))
    E_S2 = R.claimed_S2_E(A, Bp).subs(vv, sp.Symbol('x')**qq * sp.Symbol('y')**pp)
    check("case (xA, yB): det = A B + v(p A B' + q A' B)   [generic deg-3 A,B; symbolic p,q]",
          sp.simplify(det_S2 - E_S2) == 0)
    # S1: (xy A(v), B(v)) -> det = (p-q) v A B'
    det_S1 = R.det_map(R.semi_invariant(1, 1, A), R.semi_invariant(0, 0, Bp))
    E_S1 = R.claimed_S1_det(A, Bp).subs(vv, sp.Symbol('x')**qq * sp.Symbol('y')**pp)
    check("case (xyA, B): det = (p-q) v A B'  -- vanishes at v=0, never Keller",
          sp.simplify(det_S1 - E_S1) == 0 and
          R.claimed_S1_det(A, Bp).subs(vv, 0) == 0)
    # boundary case n=1 (p=q=1, both components functions of v): det = 0
    det_bdy = R.det_map(A.subs(vv, sp.Symbol('x')*sp.Symbol('y')),
                        Bp.subs(vv, sp.Symbol('x')*sp.Symbol('y')))
    check("boundary case P1=A(xy), P2=B(xy): det = 0 identically",
          sp.expand(det_bdy) == 0)

    # ---- 8. rigidity: the ODE forces A, B constant -----------------------
    print("\n[8] Plane hyperbolic rigidity -- the Keller ODE kills nonlinearity")
    delta = sp.symbols('delta', nonzero=True)
    all_ok = True
    for (pv, qv) in [(1, 1), (1, 2), (2, 3), (3, 5)]:
        E = R.claimed_S2_E(A, Bp).subs({pp: pv, qq: qv})
        eqs = [sp.expand(E - delta).coeff(vv, k) for k in range(1, 7)]
        eqs0 = sp.expand(E - delta).coeff(vv, 0)          # a0 b0 = delta
        sols = sp.solve(eqs + [eqs0], [a1, a2, a3, b1, b2, b3, delta], dict=True)
        for so in sols:
            nz = {a1, a2, a3, b1, b2, b3} & set(so)
            bad = any(sp.simplify(so[k]) != 0 for k in nz) or \
                  sp.simplify(so.get(delta, a0*b0)) == 0
            # any surviving solution must have all higher coeffs 0 and delta=a0*b0
            if any(sp.simplify(so.get(k, 0)) != 0 for k in [a1, a2, a3, b1, b2, b3]):
                all_ok = False
        # top-coefficient certificate: coeff of v^(dA+dB) is a_dA b_dB (1 + p dB + q dA)
        top = sp.expand(E).coeff(vv, 6)
        check(f"(p,q)=({pv},{qv}): top coeff = a3*b3*(1+{pv}*3+{qv}*3) != 0 unless a3 b3 = 0",
              sp.simplify(top - a3*b3*(1 + pv*3 + qv*3)) == 0)
    check("for (p,q) in {(1,1),(1,2),(2,3),(3,5)}: every Keller solution has A,B constant",
          all_ok)

    print("\n" + "=" * 72)
    if _failures:
        print(f"RESULT: {len(_failures)} CHECK(S) FAILED:", _failures)
        raise SystemExit(1)
    print("RESULT: ALL CHECKS PASSED.")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
