"""
shadow.py -- the hyperbolic C*-shadow of Alpoge's map, and the shadow principle.

Alpoge's map F is equivariant for the hyperbolic C* action
    t . (x,y,z) = (t^-1 x, t y, t^2 z)     (source weights (-1,1,2))
    t . (a,b,c) = (t^2 a, t b, t^-1 c)     (target weights (2,1,-1)).
Source invariant ring: C[s,w], s = xy, w = x^2 z.
Target invariant ring: C[s',w'], s' = b c, w' = a c^2.

Writing  f = x^-2 Pf(s,w),  g = x^-1 Pg(s,w),  h = x Ph(s,w)  (equivariance),
F induces the polynomial "shadow" map of the plane

    phi(s,w) = ( Pg*Ph , Pf*Ph^2 ).

SHADOW PRINCIPLE (verified for generic Pf,Pg,Ph in verify_n2.py):
  (1) det DF depends only on (s,w) and equals the bracket expression
          D = -2 Pf {Pg,Ph} + Pg {Pf,Ph} + Ph {Pf,Pg},
      where {A,B} = A_s B_w - A_w B_s.
  (2) det J_phi = - Ph^2 * D.
  (3) If F is Keller (D = const != 0), phi is etale exactly off {Ph = 0},
      and the curve {Ph = 0} is contracted to the origin
      (h = 0 => (bc, ac^2) = (0,0)).

For Alpoge's map:
    Pf = (s+1)(3s^3 + s^2 w + 4s^2 + 2sw + w)
    Pg = 9s^3 + 3s^2 w + 12 s^2 + 6 s w + s + 3 w
    Ph = 2 - 3s - w
    D  = -2,   det J_phi = 2 (3s + w - 2)^2.
The shadow is generically 3-to-1 and inherits explicit rational triple
collisions, e.g. (-4/3,3), (-2,9), (1/3,-1/2) |-> (-1,-1).

Why this matters for n = 2 (honest framing): the shadow shows exactly how the
degree-3 mechanism "almost" fits in the plane -- at the cost of the factor
Ph^2 in the Jacobian, concentrated on one contracted line.  It is NOT a plane
Keller map (det J_phi is not constant), consistent with the plane Jacobian
Conjecture remaining open.  The corollary below makes the obstruction precise.

COROLLARY (no free lunch): the shadow of a hyperbolic Keller map is itself
Keller iff Ph is a nonzero constant c0; then h = c0 x and, on each slice
x = const, (f,g) restricts to a plane Keller family -- i.e. the construction
could only produce a plane counterexample from data that already contains one.
The weight-2 variable z is what allows Ph to be nonconstant in dimension 3.
"""
import sympy as sp

s, w = sp.symbols('s w')
x, y, z = sp.symbols('x y z')


def bracket(A, B):
    return sp.expand(sp.diff(A, s)*sp.diff(B, w) - sp.diff(A, w)*sp.diff(B, s))


def shadow_data():
    """(Pf, Pg, Ph) of Alpoge's map, computed from scratch."""
    u = 1 + x*y
    f = sp.expand(u**3*z + y**2*u*(4 + 3*x*y))
    g = sp.expand(y + 3*x*u**2*z + 3*x*y**2*(4 + 3*x*y))
    h = sp.expand(2*x - 3*x**2*y - x**3*z)

    def to_sw(poly):
        out = 0
        for (i, j, k), cf in sp.Poly(poly, x, y, z).terms():
            assert -i + j + 2*k == 0, "not weight-0"
            out += cf * s**j * w**k
        return sp.expand(out)

    Pf = to_sw(sp.expand(x**2 * f))
    Pg = to_sw(sp.expand(x * g))
    Ph = to_sw(sp.expand(sp.cancel(h / x)))
    return Pf, Pg, Ph


def shadow_map():
    """The plane shadow phi(s,w) = (Pg*Ph, Pf*Ph^2)."""
    Pf, Pg, Ph = shadow_data()
    return sp.expand(Pg*Ph), sp.expand(Pf*Ph**2)


def bracket_D(Pf, Pg, Ph):
    """D = -2 Pf {Pg,Ph} + Pg {Pf,Ph} + Ph {Pf,Pg}  (= det DF)."""
    return sp.expand(-2*Pf*bracket(Pg, Ph) + Pg*bracket(Pf, Ph) + Ph*bracket(Pf, Pg))
