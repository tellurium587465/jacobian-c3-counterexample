"""
image_census.py -- the exact image of Alpoge's map, and the complete fiber census.

THEOREM (fiber census; every claim machine-checked in verify_image.py).
Let F be Alpoge's counterexample, A the fiber-cubic discriminant coefficient
(Disc_T P = -4A), and let

    Z := V( 3bc - 4 ,  27ac^2 - 4 )  subset  C^3   (a closed curve).

Then for every target v = (a,b,c) in C^3:

    |F^{-1}(v)| = 3   if A(v) != 0,
    |F^{-1}(v)| = 1   if A(v) == 0 and v not in Z,
    |F^{-1}(v)| = 0   iff v in Z.

In particular  F(C^3) = C^3 \\ Z  exactly: the image misses precisely one
explicit closed rational curve (isomorphic to C*, parametrized by
c |-> (4/(27c^2), 4/(3c), c)).

PROOF SKETCH (assembled from verified pieces).
 * c != 0: the finite preimages correspond to the SIMPLE roots of the fiber
   cubic P(T) = cT^3 - 2T^2 + bT - 2a (the t-model; P'(t) = 2/x kills multiple
   roots).  A cubic over C either has a simple root or is a perfect cube
   c(T - t0)^3.  Matching coefficients, the perfect-cube case happens exactly
   when t0 = 2/(3c), b = 3c t0^2 = 4/(3c), a = c t0^3 / 2 = 4/(27c^2) -- i.e.
   exactly on Z.  Off Z: 3 simple roots if A != 0, else (double+simple) 1.
 * c == 0: the x = 0 sheet F(0, y, z) = (z + 4y^2, y, 0) provides the explicit
   section (a,b,0) = F(0, b, a - 4b^2), so the fiber is never empty; the
   quadratic P contributes 2 more simple roots iff A(a,b,0) = 16a - b^2 != 0.
   (Note 3bc - 4 = -4 != 0 on c = 0, so Z is disjoint from this plane and Z is
   genuinely closed: 3bc = 4 forces c != 0 on all of V.)

STRUCTURAL REMARKS (verified where computational).
 * Z is a single orbit of the hyperbolic C* action on the target (weights
   (2,1,-1)): the orbit through (4/27, 4/3, 1).  Under the target invariants
   (B, C) = (bc, ac^2) it is the single point (4/3, 4/27), which lies on the
   shadow discriminant curve Delta = 0.
 * Z sits inside the branch surface {A = 0}.
 * Since Z has codimension 2, C^3 \\ Z is SIMPLY CONNECTED.  So F is a
   surjective etale 3:1 map onto a simply connected space -- which would be
   impossible for a proper (covering) map.  This gives a conceptual, one-line
   reason the nonproperness over {A = 0} is forced: sheets MUST escape to
   infinity somewhere, or F would be a nontrivial cover of a simply connected
   space.
"""
import sympy as sp
from counterexample import (F_map, apply, fiber, fiber_cubic_P, A_coeff,
                            x, y, z, a, b, c, T)

# the missing curve, as an ideal and as a parametrization
Z_IDEAL = (3*b*c - 4, 27*a*c**2 - 4)


def Z_point(cv):
    """The point of Z over c = cv (cv != 0)."""
    cv = sp.nsimplify(cv)
    return (sp.Rational(4, 27)/cv**2, sp.Rational(4, 3)/cv, cv)


def census(av, bv, cv):
    """Return (predicted fiber size, actual fiber points) for a rational target."""
    av, bv, cv = sp.nsimplify(av), sp.nsimplify(bv), sp.nsimplify(cv)
    on_Z = (3*bv*cv - 4 == 0) and (27*av*cv**2 - 4 == 0)
    Aval = A_coeff(av, bv, cv)
    pred = 0 if on_Z else (3 if Aval != 0 else 1)
    return pred, fiber(av, bv, cv)
