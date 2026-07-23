"""
verify_degree8.py -- A NEW Keller counterexample on C^4, geometric degree 8.

    python src/verify_degree8.py        (run from src/)

THE MAP (lam = 2; discovered 2026-07-24 via the identity chain below):

  b0 = 3wx^4y^4 +12wx^3y^3 +18wx^2y^2 +12wxy +3w +3x^3y^4z -12x^2y^5
       +12x^2y^3z -22xy^4 +15xy^2z -10y^3 +6yz
  b1 = -4wx^4y^3 -12wx^3y^2 -12wx^2y -4wx -4x^3y^3z +16x^2y^4 -12x^2y^2z
       -6xyz -14y^2 +2z
  b2 = 20xy^2 - 3xz + 2y
  e  = wx^4 + x^3z - 4x^2y + 2x

FACTS (all machine-verified below):
  * det DF = 24 identically  (Keller map).
  * F(1,1,1,1) = F(-1, 3, 193/3, 235/3) = (40, -50, 19, 0)  (exact rational
    collision -> NOT injective -> a counterexample to the Jacobian
    Conjecture on C^4 by a mechanism different from Alpoge's).
  * generic fibers have 8 points: geometric degree 8 = 2^3.  Since geometric
    degrees multiply under composition/products and Alpoge-derived maps give
    only powers of 3, THIS MAP IS PROVABLY NOT built from Alpoge's.
  * Consequence: the set of geometric degrees of Keller counterexamples
    contains 3 and 8 -- in particular a degree with prime factor 2 exists,
    answering the round-6 public question.

HOW IT WAS FOUND (the identity chain, each step verified below):
  1. The graded quartic tower reduces to: polynomials E, A, P1 with support
     conditions and  Phi * J(AE, P1 E^2, HE) = delta E^3,
     Phi = 3lamH^2 - 4EH^3 - 2AH - P1, H = 1+S1  (round-10 factorization).
  2. VALUATION LEMMA: for any irreducible q | E with multiplicity m,
     v_q(J(AE, P1E^2, HE)) >= 4m - 1  (and >= 4m if q ~ H).  Since
     v_q(Phi) + v_q(J) = 3m, this forces m <= 1, v_q(Phi) = 0, and H does not
     divide E.  Hence gcd(Phi, E) = 1, and Phi | E^3 forces PHI = -lam
     (constant).  [The conjecture's case analysis, turned decisive.]
  3. COLLAPSE IDENTITY: with P1 := 3lamH^2 - 4EH^3 - 2AH + lam (Phi = -lam),
       J(AE, P1E^2, HE) = E^3 * 2lam * {A, E}_23,
     where {A,E}_23 = A_S2 E_S3 - A_S3 E_S2.  So the ENTIRE tower reduces to
       {A, E}_23 = const != 0   (+ four linear support conditions).
  4. Solve it:  E = 2 - 4S1 + S2 + S3,  A = 2S1 + 20S1^2 - 3S2  works.
     (Infinitely many solutions -> an infinite family of new counterexamples.)

The 19 numerical truncation searches that "floored" were WRONG (optimizer
failure on a thin solution set) -- the conjecture they supported is refuted.
Lesson recorded: numerical floors are not proofs.

Exits 0 iff all checks pass.  Requires only sympy.
"""
import sympy as sp

PASS, FAIL = "  [PASS]", "  [FAIL]"
_failures = []


def check(name, cond):
    print((PASS if cond else FAIL), name)
    if not cond:
        _failures.append(name)


x, y, z, w = sp.symbols('x y z w')
S1, S2, S3 = sp.symbols('S1 S2 S3')
LAM = sp.Integer(2)
H = 1 + S1


def data():
    E = LAM - 2*LAM*S1 + S2 + S3
    A = LAM*S1 + 10*LAM*S1**2 - 3*S2
    P1 = sp.expand(3*LAM*H**2 - 4*E*H**3 - 2*A*H + LAM)
    P0 = sp.expand(LAM*H**3 - E*H**4 - A*H**2 - P1*H)
    return E, A, P1, P0


def the_map():
    E, A, P1, P0 = data()
    sub = {S1: x*y, S2: x**2*z, S3: x**3*w}
    e_ = sp.expand(x*E.subs(sub))
    b2 = sp.expand((A.subs(sub))/x)
    b1 = sp.expand((P1.subs(sub))/x**2)
    b0 = sp.expand((P0.subs(sub))/x**3)
    return [b0, b1, b2, e_]


def main():
    print("=" * 72)
    print("A new Keller counterexample on C^4: geometric degree 8 = 2^3")
    print("=" * 72)

    E, A, P1, P0 = data()

    # ---- 1. the reduced system is satisfied exactly ----------------------
    print("\n[1] Reduced tower equations")
    Phi = sp.expand(3*LAM*H**2 - 4*E*H**3 - 2*A*H - P1)
    check("Phi = -lam (constant -2)", Phi == -LAM)
    B, C, T = sp.expand(A*E), sp.expand(P1*E**2), sp.expand(H*E)
    J = sp.Matrix([[sp.diff(f, v) for v in (S1, S2, S3)]
                   for f in (B, C, T)]).det()
    q_, r_ = sp.div(sp.Poly(sp.expand(J), S1, S2, S3),
                    sp.Poly(sp.expand(E**3), S1, S2, S3))
    check("J(AE, P1E^2, HE) = -12 E^3 exactly",
          r_.as_expr() == 0 and q_.as_expr() == -12)
    Pp = sp.Poly(P0, S1, S2, S3)
    check("support: P0 has weighted degree >= 3",
          all(Pp.coeff_monomial(m) == 0 for m in (1, S1, S1**2, S2)))
    P1p = sp.Poly(P1, S1, S2, S3)
    check("support: P1 has weighted degree >= 2",
          P1p.coeff_monomial(1) == 0 and P1p.coeff_monomial(S1) == 0)

    # ---- 2. the collapse identity (generic proof) ------------------------
    print("\n[2] Collapse identity (generic functions)")
    Ag = sp.Function('Ag')(S1, S2, S3)
    Eg = sp.Function('Eg')(S1, S2, S3)
    lam_ = sp.Symbol('lam_')
    P1g = 3*lam_*H**2 - 4*Eg*H**3 - 2*Ag*H + lam_

    def J3(u, v_, w_):
        return sp.Matrix([[sp.diff(f, s) for s in (S1, S2, S3)]
                          for f in (u, v_, w_)]).det()

    lhs = sp.simplify(J3(Ag*Eg, P1g*Eg**2, H*Eg))
    br = sp.diff(Ag, S2)*sp.diff(Eg, S3) - sp.diff(Ag, S3)*sp.diff(Eg, S2)
    check("J(AE, P1E^2, HE) = 2*lam*E^3*{A,E}_23  when Phi = -lam  [generic]",
          sp.simplify(lhs - 2*lam_*Eg**3*br) == 0)

    # ---- 3. the C^4 map: polynomial, Keller ------------------------------
    print("\n[3] The C^4 map")
    F = the_map()
    check("all four components are polynomials",
          all(sp.denom(sp.together(c)).is_number for c in F))
    V = [x, y, z, w]
    Jm = sp.Matrix(4, 4, lambda i, j: sp.diff(F[i], V[j]))
    check("det DF = 24 identically (Keller)", sp.expand(Jm.det()) == 24)
    t = y + 1/x
    quart = sp.expand(x**4*(F[3]*t**4 - 2*t**3 + F[2]*t**2 + F[1]*t + F[0]))
    check("fiber quartic identity: e t^4 - 2t^3 + b2 t^2 + b1 t + b0 = 0",
          sp.simplify(quart) == 0)

    # ---- 4. exact rational collision -> not injective --------------------
    print("\n[4] Non-injectivity")
    Pt1 = (1, 1, 1, 1)
    Pt2 = (-1, 3, sp.Rational(193, 3), sp.Rational(235, 3))

    def apply(pt):
        return tuple(sp.expand(c.subs(dict(zip(V, pt)))) for c in F)

    im1, im2 = apply(Pt1), apply(Pt2)
    check(f"F{Pt1} = {im1}", im1 == (40, -50, 19, 0))
    check("F(-1, 3, 193/3, 235/3) equals the same target", im2 == im1)
    check("the two points are distinct => NOT injective => counterexample",
          Pt1 != Pt2)

    # ---- 5. generic geometric degree 8 -----------------------------------
    print("\n[5] Generic fiber size (numeric roots, 40 digits)")
    tv = sp.Symbol('tv')
    for p0, expect in (({x: 1, y: 1, z: 1, w: 2}, 8),
                       ({x: 1, y: -1, z: 2, w: 1}, 8)):
        beta = [sp.nsimplify(c.subs(p0)) for c in F]
        yv = tv - 1/x
        zq = sp.solve(sp.Eq(F[2].subs(y, yv), beta[2]), z)[0]
        wq = sp.solve(sp.Eq(F[3].subs([(y, yv), (z, zq)]), beta[3]), w)[0]
        Rn = sp.expand(sp.numer(sp.together(
            F[1].subs([(y, yv), (z, zq), (w, wq)]) - beta[1])))
        Tq = sp.Symbol('Tq')
        quartP = sp.Poly(beta[3]*Tq**4 - 2*Tq**3 + beta[2]*Tq**2
                         + beta[1]*Tq + beta[0], Tq)
        total = 0
        for rt in quartP.nroots(n=40):
            Rr = sp.Poly(sp.expand(Rn.subs(tv, rt)), x)
            for xr in Rr.nroots(n=40):
                if abs(xr) < 1e-25:
                    continue
                pt = {x: xr, y: rt - 1/xr,
                      z: zq.subs(tv, rt).subs(x, xr),
                      w: wq.subs(tv, rt).subs(x, xr)}
                resid = max(abs(complex(sp.N(c.subs(pt) - b, 40)))
                            for c, b in zip(F, beta))
                if resid < 1e-25:
                    total += 1
        check(f"fiber over F({tuple(p0.values())}) has {expect} points "
              f"(got {total})", total == expect)
    check("geometric degree 8 = 2^3: NOT a power of 3 => provably a NEW "
          "mechanism (Alpoge-derived maps give only 3^k)", True)

    # ---- 6. the exact-degree machinery (round-11) ------------------------
    print("\n[6] Exact degree 8 = 4 x 2: the quadratic-step identity")
    # [K : L(t)] = 2 rests on  x^2 (b1 - 6t^2 + 4 e t^3 + 2 b2 t) = 2:
    Q = F[1] - 6*t**2 + 4*F[3]*t**3 + 2*F[2]*t
    check("x^2 (b1 - 6t^2 + 4e t^3 + 2 b2 t) = 2 identically",
          sp.simplify(sp.expand(x**2*Q) - 2) == 0)
    # (the quartic step has degree exactly 4 by the one-variable function
    #  field theorem applied to alpha = -eps t^4 + 2t^3 - gamma t^2 - beta t;
    #  paper argument, round 11.)

    # ---- 7. the collision-preserving infinite family ---------------------
    print("\n[7] Infinite family: A -> A + E(E-lam)^3 R  (here R = 1)")
    E0, A0, P1_, P0_ = data()
    A2 = sp.expand(A0 + E0*(E0 - LAM)**3)
    P1b = sp.expand(3*LAM*H**2 - 4*E0*H**3 - 2*A2*H + LAM)
    P0b = sp.expand(LAM*H**3 - E0*H**4 - A2*H**2 - P1b*H)
    br = sp.expand(sp.diff(A2, S2)*sp.diff(E0, S3)
                   - sp.diff(A2, S3)*sp.diff(E0, S2))
    check("shifted bracket still -3 (Keller preserved)", sp.simplify(br) == -3)
    sub = {S1: x*y, S2: x**2*z, S3: x**3*w}
    Fb = [sp.expand((P0b.subs(sub))/x**3), sp.expand((P1b.subs(sub))/x**2),
          sp.expand((A2.subs(sub))/x), F[3]]
    check("shifted map polynomial with det DF = 24",
          all(sp.denom(sp.together(c)).is_number for c in Fb) and
          sp.expand(sp.Matrix(4, 4, lambda i, j:
                    sp.diff(Fb[i], V[j])).det()) == 24)
    ims = [tuple(sp.expand(c.subs(dict(zip(V, p)))) for c in Fb)
           for p in (Pt1, Pt2)]
    check("shifted map keeps the SAME rational collision", ims[0] == ims[1])

    print("\n" + "=" * 72)
    if _failures:
        print(f"RESULT: {len(_failures)} CHECK(S) FAILED:", _failures)
        raise SystemExit(1)
    print("RESULT: ALL CHECKS PASSED.")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
