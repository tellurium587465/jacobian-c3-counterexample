"""
verify.py  --  self-contained, exact verification of every claim in this repo.

    python src/verify.py

Exits 0 iff all checks pass.  Requires only sympy.  All arithmetic is exact.
"""
import sympy as sp
from counterexample import (
    F_map, jacobian_det, apply, A_coeff, fiber_cubic_P, x_eliminant_Q,
    reconstruct, fiber, x, y, z, a, b, c, T,
)
from collisions import family, collisions_general

PASS, FAIL = "  [PASS]", "  [FAIL]"
_failures = []


def check(name, cond):
    print((PASS if cond else FAIL), name)
    if not cond:
        _failures.append(name)


def main():
    F = F_map()
    print("=" * 72)
    print("Alpoge (July 2026) counterexample to the Jacobian Conjecture, dim 3")
    print("=" * 72)
    print("f =", F[0]); print("g =", F[1]); print("h =", F[2])

    # 1. Keller property ---------------------------------------------------
    print("\n[1] Keller property")
    check("det(DF) = -2 (nonzero constant)", jacobian_det() == -2)

    # 2. Alpoge's triple collision -> not injective ------------------------
    print("\n[2] Alpoge's triple collision -> not injective")
    P = [(0, 0, sp.Rational(-1, 4)),
         (1, sp.Rational(-3, 2), sp.Rational(13, 2)),
         (-1, sp.Rational(3, 2), sp.Rational(13, 2))]
    imgs = [apply(F, p) for p in P]
    check("three distinct points all map to (-1/4,0,0)",
          len(set(P)) == 3 and imgs[0] == imgs[1] == imgs[2] == (sp.Rational(-1, 4), 0, 0))
    check("=> genuine counterexample (Keller + non-injective)",
          jacobian_det() == -2 and imgs[0] == imgs[1] == imgs[2])

    # 3. Geometric degree 3 ------------------------------------------------
    print("\n[3] Geometric degree = 3")
    import random
    random.seed(0)
    sizes = []
    for _ in range(3):
        t = (sp.Rational(random.randint(-9, 9), random.randint(1, 5)),
             sp.Rational(random.randint(-9, 9), random.randint(1, 5)),
             sp.Rational(random.randint(1, 9), random.randint(1, 5)))
        sizes.append(len(sp.solve([F[0]-t[0], F[1]-t[1], F[2]-t[2]], [x, y, z], dict=True)))
    check(f"random fibers all have 3 points (sizes={sizes})", all(s == 3 for s in sizes))

    # 4. Cubic t-model -----------------------------------------------------
    print("\n[4] Cubic t-model  P(T)=cT^3-2T^2+bT-2a,  t=y+1/x")
    tt = y + 1/x
    Psub = fiber_cubic_P(F[0], F[1], F[2])          # a,b,c := f,g,h
    check("t = y+1/x is a root of P (identically)", sp.simplify(Psub.subs(T, tt)) == 0)
    check("P'(t) = 2/x", sp.simplify(sp.diff(Psub, T).subs(T, tt) - 2/x) == 0)
    Pgen = fiber_cubic_P(a, b, c)
    check("Disc_T(P) = -4A", sp.expand(sp.discriminant(Pgen, T) + 4*A_coeff(a, b, c)) == 0)
    # reconstruction round-trips on a target with rational t-roots
    a0, b0, c0 = sp.Integer(0), sp.Rational(8, 9), sp.Integer(1)
    troots = sp.roots(sp.Poly(fiber_cubic_P(a0, b0, c0), T), multiple=True)
    rec_ok = all(apply(F, reconstruct(a0, b0, c0, tv)) == (a0, b0, c0) for tv in troots)
    check("reconstruct(t) round-trips to the target", rec_ok)

    # 5. x-eliminant and its projection artifact ---------------------------
    print("\n[5] x-eliminant Q(x)=A x^3+(4-3bc)x-2c and the x-projection artifact")
    zc = sp.solve(sp.Eq(F[2], c), z)[0]
    f2 = sp.expand(sp.numer(sp.together(F[0].subs(z, zc) - a)))
    g2 = sp.expand(sp.numer(sp.together(F[1].subs(z, zc) - b)))
    _, rem = sp.div(sp.Poly(f2, y), sp.Poly(g2, y), y)
    ysol = sp.solve(sp.Eq(rem.as_expr(), 0), y)[0]
    res = sp.expand(sp.numer(sp.together(g2.subs(y, ysol))))
    check("eliminating y,z gives res = -9 c x * Q(x)",
          sp.expand(res - (-9*c*x)*sp.expand(x_eliminant_Q(a, b, c))) == 0)
    check("Q has no x^2 term (=> sum of x-coords = 0 when 3 finite sheets)",
          sp.Poly(sp.expand(x_eliminant_Q(a, b, c)), x).coeff_monomial(x**2) == 0)
    # artifact: at (0,8/9,1) the fiber has 3 distinct points but only 2 x-values
    fb = fiber(a0, b0, c0)
    xs = [p[0] for p in fb]
    check("(0,8/9,1): 3 distinct preimages but x=9/4 is shared (Q double root)",
          len(fb) == 3 and len(set(xs)) == 2 and xs.count(sp.Rational(9, 4)) == 2)
    check("=> the genuine branch locus is A=0 (Disc P), not the extra Q-factor",
          A_coeff(a0, b0, c0) != 0)  # A!=0 here yet Q has a double root -> artifact

    # 6. x=0 sheet only when c=0 ------------------------------------------
    print("\n[6] x=0 preimages occur only when c=0")
    check("Q(0) = -2c (so x=0 possible iff c=0; h(x=0)=0 forces c=0)",
          sp.expand(x_eliminant_Q(a, b, c).subs(x, 0)) == -2*c)
    check("Alpoge's (0,0,-1/4) is the c=0 extra sheet, recovered by fiber()",
          (0, 0, sp.Rational(-1, 4)) in fiber(sp.Rational(-1, 4), 0, 0))

    # 7. weighted-homogeneous grading -------------------------------------
    print("\n[7] Weighted grading deg(x,y,z)=(-1,1,2) -> deg(f,g,h)=(2,1,-1)")
    lam = sp.symbols('lam', positive=True)
    def wdeg(expr, k):
        return sp.expand(expr.subs({x: x*lam**-1, y: y*lam, z: z*lam**2}) - lam**k*expr) == 0
    check("f homogeneous of weighted degree 2", wdeg(F[0], 2))
    check("g homogeneous of weighted degree 1", wdeg(F[1], 1))
    check("h homogeneous of weighted degree -1", wdeg(F[2], -1))

    # 8. rational triple-collision families -------------------------------
    print("\n[8] Explicit rational triple-collisions (infinitely many)")
    fam = family()
    fam_ok = len(fam) >= 50 and all(
        len(set(hit["preimages"])) == 3 and all(apply(F, Pt) == tuple(hit["target"])
                                                for Pt in hit["preimages"])
        for hit in fam)
    check(f"square-free a=0 family: {len(fam)} targets, all verified", fam_ok)
    gen = collisions_general()
    gen_ok = len(gen) >= 12 and all(
        len(set(hit["preimages"])) == 3 and all(apply(F, Pt) == tuple(hit["target"])
                                                for Pt in hit["preimages"])
        for hit in gen)
    check(f"general a!=0 scan: {len(gen)} targets, all verified", gen_ok)

    # 9. suspension to all n>=3 -------------------------------------------
    print("\n[9] Suspension F x id gives counterexamples in all n>=3")
    w = sp.symbols('w')
    F4 = F + [w]
    J4 = sp.Matrix(4, 4, lambda i, j: sp.diff(F4[i], [x, y, z, w][j]))
    check("det(F x id_C) = -2", sp.expand(J4.det()) == -2)
    q4 = [tuple(sp.expand(Fi.subs({x: p[0], y: p[1], z: p[2], w: 7})) for Fi in F4) for p in P]
    check("F x id still non-injective", q4[0] == q4[1] == q4[2])

    print("\n" + "=" * 72)
    if _failures:
        print(f"RESULT: {len(_failures)} CHECK(S) FAILED:", _failures)
        raise SystemExit(1)
    print("RESULT: ALL CHECKS PASSED.")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
