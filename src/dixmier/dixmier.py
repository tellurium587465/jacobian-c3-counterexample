"""
dixmier.py -- from Alpoge's Keller map to:
  (1) an explicit non-injective SYMPLECTIC unimodular polynomial map of C^6
      (counterexample to the symplectic/unimodular Jacobian conjecture, dim 6), and
  (2) an explicit endomorphism of the Weyl algebra A_3(C) that is injective but
      NOT an automorphism -- a counterexample to the DIXMIER CONJECTURE (1968)
      for A_3, hence for all A_n with n >= 3.

Construction
------------
Let F = (f,g,h) be Alpoge's map (det DF = -2) and
    G := ((DF)^T)^{-1}  --  a POLYNOMIAL 3x3 matrix (adjugate over the unit -2).

* Cotangent lift:  Fhat(q,p) = ( F(q), G(q) p )  on C^6 = T*C^3.
  Then (verified exactly):  det D(Fhat) = 1;  (D Fhat)^T Omega (D Fhat) = Omega
  (Fhat preserves the standard symplectic form); and Fhat inherits explicit
  rational 3-point collisions from F.

* Weyl endomorphism:  A_3 = C<q1,q2,q3,p1,p2,p3 | [p_i,q_j]=delta_ij, ...>.
  Define on generators:
      phi(q_i) = f_i(q),        phi(p_j) = sum_k G[j,k](q) p_k .
  The defining relations are preserved:
      [phi(q_i), phi(q_j)] = 0                    (inside commutative C[q]);
      [phi(p_j), phi(q_i)] = v_j(f_i) = delta_ij  where v_j = sum_k G[j,k] d_k;
      [phi(p_i), phi(p_j)] = 0  because the vector fields v_j are F-related to
      the coordinate fields d/da_j (v_j(f_i) = delta_ij with DF invertible
      everywhere), and F-relatedness + etaleness forces [v_i,v_j] = 0.
  All these are COMMUTATIVE polynomial identities (everything is of order <= 1),
  verified exactly in verify_dixmier.py; by the universal property of A_3
  (generators and relations) phi is a well-defined unital endomorphism.

Why phi is not an automorphism (self-contained proof)
-----------------------------------------------------
* phi is injective: A_3 is simple in characteristic 0 and phi(1) = 1.
* LEMMA:  Centralizer_{A_3}( C[f,g,h] ) = C[q1,q2,q3].
  Proof.  C[q] is commutative and contains C[f,g,h], giving one inclusion.
  Conversely let T have order m >= 1 in the order filtration (degree in p) with
  principal symbol sigma_m (homogeneous of degree m in p).  [T, f_i] = 0 forces
  the order-(m-1) symbol {sigma_m, f_i} = -sum_k (d sigma_m/d p_k)(d f_i/d q_k)
  to vanish for i = 1,2,3, i.e. (DF)^T grad_p sigma_m = 0.  Since det DF = -2 is
  a unit, grad_p sigma_m = 0, and Euler's identity (char 0, m >= 1) gives
  sigma_m = 0 -- contradiction.  So T has order 0: T in C[q].                []
* If phi were surjective (= an automorphism, given injectivity), automorphisms
  carry centralizers to centralizers:
      Centralizer(phi(C[q])) = phi(Centralizer(C[q])) = phi(C[q]),
  using Centralizer(C[q]) = C[q] (the Lemma with F = id).  Hence
  C[f,g,h] = Centralizer(C[f,g,h]) = C[q].  In particular q1 = W(f,g,h) for
  some polynomial W; evaluating at the collision points (0,0,-1/4),
  (1,-3/2,13/2), (-1,3/2,13/2) -- where F takes a single common value -- the
  right side is constant while q1 takes the values 0, 1, -1.  Contradiction. []

Consequences
------------
* The DIXMIER CONJECTURE is FALSE for A_3, and (tensoring with the identity on
  A_{n-3}, same proof with F x id) for every A_n, n >= 3.
* A_3 is NOT co-Hopfian: phi embeds A_3 properly into itself.
* The Poisson analogue fails in dimension 6: Fhat^* is a bracket-preserving,
  injective, non-surjective endomorphism of the standard Poisson algebra.
* With Zheglov's theorem that every endomorphism of A_1 is an automorphism
  (arXiv:2410.06959), the status map becomes:
      A_1: Dixmier TRUE.   A_2: OPEN.   A_n (n >= 3): FALSE.
  -- exactly parallel to the Jacobian Conjecture itself (n=1 trivial, n=2 open,
  n >= 3 false).
"""
import sympy as sp

x, y, z = sp.symbols('x y z')
p1, p2, p3 = sp.symbols('p1 p2 p3')
Q = [x, y, z]
PV = [p1, p2, p3]


def F_map():
    u = 1 + x*y
    f = sp.expand(u**3*z + y**2*u*(4 + 3*x*y))
    g = sp.expand(y + 3*x*u**2*z + 3*x*y**2*(4 + 3*x*y))
    h = sp.expand(2*x - 3*x**2*y - x**3*z)
    return [f, g, h]


def jac(F):
    return sp.Matrix(3, 3, lambda i, j: sp.diff(F[i], Q[j]))


def G_matrix(F=None):
    """G = ((DF)^T)^{-1}: polynomial because det DF = -2 is a unit."""
    J = jac(F or F_map())
    Gm = (J.T).adjugate() / (J.T).det()
    return sp.Matrix(3, 3, lambda i, j: sp.expand(sp.cancel(Gm[i, j])))


def cotangent_lift():
    """Fhat = (F(q), G(q)p): the six components as polynomials on C^6."""
    F = F_map()
    Gm = G_matrix(F)
    P = Gm * sp.Matrix(PV)
    return F + [sp.expand(P[i]) for i in range(3)]


def collision_C6():
    """Three distinct rational points of C^6 with the same Fhat-image."""
    F = F_map()
    Gm = G_matrix(F)
    J = jac(F)
    pts = [(0, 0, sp.Rational(-1, 4)),
           (1, sp.Rational(-3, 2), sp.Rational(13, 2)),
           (-1, sp.Rational(3, 2), sp.Rational(13, 2))]
    # choose p = (1,0,0) at the first point; transport P* = G(q1)p back
    Pstar = Gm.subs({x: 0, y: 0, z: sp.Rational(-1, 4)}) * sp.Matrix([1, 0, 0])
    Pstar = sp.Matrix([sp.nsimplify(sp.simplify(c)) for c in Pstar])
    out = []
    for pt in pts:
        Jt = (J.T).subs({x: pt[0], y: pt[1], z: pt[2]})
        pv = Jt * Pstar                      # p = (DF)^T P*  at this point
        out.append(tuple(list(pt) + [sp.nsimplify(c) for c in pv]))
    return out


def phi_p_formulas():
    """The explicit images phi(p_j) = sum_k G[j,k](q) p_k, printed as strings."""
    Gm = G_matrix()
    return [sp.expand(sum(Gm[j, k]*PV[k] for k in range(3))) for j in range(3)]
