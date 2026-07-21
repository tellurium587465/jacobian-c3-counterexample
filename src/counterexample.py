"""
counterexample.py
=================

Alpoge's (July 2026) polynomial counterexample to the Jacobian Conjecture in
dimension 3, plus the fiber structure used throughout this repo.

With  u = 1 + x*y  the map  F : C^3 -> C^3  is

    f = u^3 * z + y^2 * u * (4 + 3*x*y)
    g = y + 3*x * u^2 * z + 3*x * y^2 * (4 + 3*x*y)
    h = 2*x - 3*x^2*y - x^3*z

Everything here is exact symbolic algebra (sympy).

Fiber structure (the "cubic t-model")
-------------------------------------
The structural description below is the *publicly documented* one (see the
references in README / docs/mechanism.md); it is reproduced and machine-checked
here, and used to generate the collision families.  The clean fiber variable is

    t = y + 1/x          (for x != 0),

which, over a target (a, b, c), is a root of the cubic

    P(T) = c*T^3 - 2*T^2 + b*T - 2*a ,      with   P'(t) = 2/x .

Given a *simple* root t of P, the preimage is reconstructed by
    r = P'(t),   x = 2/r,   y = t - r/2,   z = 5/4 r^2 - 3/2 t r - c/8 r^3 .
Its discriminant is  Disc_T(P) = -4*A,  where
    A = 27*a^2*c^2 - 18*a*b*c + 16*a + b^3*c - b^2 ,
so the genuine branch locus (where two sheets meet) is exactly  A = 0.

Eliminating y and z instead gives the depressed "x-eliminant"
    Q(x) = A*x^3 + (4 - 3*b*c)*x - 2*c    (no x^2 term),
whose roots are the x-coordinates of the finite preimages.  WARNING: projecting
to x can identify two distinct sheets that share an x-value, so Q's extra
discriminant factor is a projection artifact, not a real collision of sheets.
The t-model is the globally correct description.
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
a, b, c = sp.symbols('a b c')      # coordinates on the target C^3
T = sp.symbols('T')                # fiber-cubic variable


def F_map():
    """Return [f, g, h], expanded."""
    u = 1 + x * y
    f = u**3 * z + y**2 * u * (4 + 3 * x * y)
    g = y + 3 * x * u**2 * z + 3 * x * y**2 * (4 + 3 * x * y)
    h = 2 * x - 3 * x**2 * y - x**3 * z
    return [sp.expand(f), sp.expand(g), sp.expand(h)]


def jacobian_det():
    F = F_map()
    J = sp.Matrix(3, 3, lambda i, j: sp.diff(F[i], [x, y, z][j]))
    return sp.expand(J.det())


def apply(F, pt):
    """Evaluate F at pt=(x0,y0,z0)."""
    return tuple(sp.expand(Fi.subs({x: pt[0], y: pt[1], z: pt[2]})) for Fi in F)


# --- the cubic t-model -----------------------------------------------------

def A_coeff(av, bv, cv):
    return 27*av**2*cv**2 - 18*av*bv*cv + 16*av + bv**3*cv - bv**2


def fiber_cubic_P(av, bv, cv):
    """P(T) = c T^3 - 2 T^2 + b T - 2 a, whose roots t give the finite preimages."""
    return cv*T**3 - 2*T**2 + bv*T - 2*av


def x_eliminant_Q(av, bv, cv):
    """Depressed cubic Q(x) = A x^3 + (4-3bc) x - 2c (roots = x-coords of preimages)."""
    return A_coeff(av, bv, cv)*x**3 + (4 - 3*bv*cv)*x - 2*cv


def reconstruct(av, bv, cv, tv):
    """Full preimage (x,y,z) from a simple root t of P (requires P'(t) != 0)."""
    r = (3*cv*tv**2 - 4*tv + bv)              # = P'(t) = 2/x
    xv = 2/r
    yv = tv - r/2
    zv = sp.Rational(5, 4)*r**2 - sp.Rational(3, 2)*tv*r - cv/8*r**3
    return (sp.nsimplify(xv), sp.nsimplify(yv), sp.nsimplify(zv))


def fiber(av, bv, cv):
    """The full set-theoretic fiber F^{-1}(a,b,c) over the rationals/complexes.

    Uses the t-model for x!=0 sheets and the explicit x=0 sheet (only c=0)."""
    av, bv, cv = sp.nsimplify(av), sp.nsimplify(bv), sp.nsimplify(cv)
    pts = []
    P = fiber_cubic_P(av, bv, cv)
    for tv in sp.roots(sp.Poly(P, T), multiple=True):
        r = 3*cv*tv**2 - 4*tv + bv
        if sp.simplify(r) == 0:
            continue                          # sheet escaped to infinity (P'(t)=0)
        pts.append(reconstruct(av, bv, cv, tv))
    if cv == 0:                               # extra x=0 sheet: F(0,y,z)=(z+4y^2, y, 0)
        pts.append((sp.Integer(0), bv, av - 4*bv**2))
    # de-duplicate exactly
    uniq = []
    for p in pts:
        if p not in uniq:
            uniq.append(p)
    return uniq
