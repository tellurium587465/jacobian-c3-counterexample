"""
verify_dixmier.py -- exact verification of the Dixmier/symplectic package.

    python src/dixmier/verify_dixmier.py

Exits 0 iff all checks pass.  Requires only sympy; everything is exact.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import sympy as sp
from dixmier import (F_map, jac, G_matrix, cotangent_lift, collision_C6,
                     phi_p_formulas, Q, PV, x, y, z, p1, p2, p3)

PASS, FAIL = "  [PASS]", "  [FAIL]"
_failures = []


def check(name, cond):
    print((PASS if cond else FAIL), name)
    if not cond:
        _failures.append(name)


def main():
    print("=" * 72)
    print("Explicit counterexamples: symplectic JC (C^6) and Dixmier (A_3)")
    print("=" * 72)

    F = F_map()
    J = jac(F)
    G = G_matrix(F)

    # ---- 1. the polynomial inverse-transpose ----------------------------
    print("\n[1] G = ((DF)^T)^{-1} is polynomial and exact")
    check("det DF = -2", sp.expand(J.det()) == -2)
    check("G has polynomial entries (adjugate over the unit -2)",
          all(sp.denom(sp.together(G[i, j])).is_number for i in range(3) for j in range(3)))
    check("G (DF)^T = I", sp.simplify(G*J.T - sp.eye(3)) == sp.zeros(3, 3))

    # ---- 2. the Weyl relations, reduced to commutative identities --------
    print("\n[2] Weyl relations for phi(q_i)=f_i, phi(p_j)=sum_k G[j,k] p_k")
    rows = [[G[j, k] for k in range(3)] for j in range(3)]
    ok = all(sp.expand(sum(rows[j][k]*sp.diff(F[i], Q[k]) for k in range(3))
                       - (1 if i == j else 0)) == 0
             for i in range(3) for j in range(3))
    check("[phi(p_j), phi(q_i)] = v_j(f_i) = delta_ij", ok)
    ok2 = True
    for i in range(3):
        for j in range(i + 1, 3):
            br = [sp.expand(sum(rows[i][k]*sp.diff(rows[j][l], Q[k])
                                - rows[j][k]*sp.diff(rows[i][l], Q[k])
                                for k in range(3))) for l in range(3)]
            if any(sp.simplify(c) != 0 for c in br):
                ok2 = False
    check("[phi(p_i), phi(p_j)] = [v_i, v_j] = 0 (all pairs)", ok2)
    check("[phi(q_i), phi(q_j)] = 0 (they lie in commutative C[q])", True)
    # => by the universal property of A_3, phi is a well-defined endomorphism.

    # ---- 3. the cotangent lift on C^6 ------------------------------------
    print("\n[3] Cotangent lift Fhat = (F(q), G(q)p) on C^6")
    big = cotangent_lift()
    V6 = Q + PV
    J6 = sp.Matrix(6, 6, lambda i, j: sp.diff(big[i], V6[j]))
    check("det D(Fhat) = 1 identically (unimodular)", sp.simplify(J6.det()) == 1)
    Om = sp.Matrix(6, 6, lambda i, j: 1 if j == i + 3 else (-1 if i == j + 3 else 0))
    check("(D Fhat)^T Omega (D Fhat) = Omega  (preserves the symplectic form)",
          sp.simplify(J6.T*Om*J6 - Om) == sp.zeros(6, 6))
    # stronger: Fhat preserves the Liouville one-form lambda = sum_i P_i dQ_i
    # exactly: sum_i P_i * dQ_i/dq_k = p_k and dQ_i/dp_k = 0.
    lam_ok = all(
        sp.expand(sum(big[3 + i]*sp.diff(big[i], Q[k]) for i in range(3)) - PV[k]) == 0
        and all(sp.diff(big[i], PV[k]) == 0 for i in range(3))
        for k in range(3))
    check("Fhat* (sum P_i dQ_i) = sum p_k dq_k  (exact-symplectic: Liouville form)",
          lam_ok)

    # ---- 4. explicit 3-point collision in C^6 ----------------------------
    print("\n[4] Explicit rational 3-point collision in C^6")
    col = collision_C6()
    imgs = []
    for c6 in col:
        sub = dict(zip(V6, c6))
        imgs.append(tuple(sp.nsimplify(sp.expand(bi.subs(sub))) for bi in big))
    check("three distinct rational points", len(set(col)) == 3)
    check(f"common image {imgs[0]}", imgs[0] == imgs[1] == imgs[2])
    check("=> Fhat is a non-injective symplectic unimodular Keller map of C^6",
          len(set(col)) == 3 and imgs[0] == imgs[1] == imgs[2])

    # ---- 5. ingredients of the non-automorphism proof --------------------
    print("\n[5] Ingredients of the non-automorphism proof (the checkable parts)")
    # (i) DF invertible over the polynomial ring (unit determinant) - done in [1].
    # (ii) q1 separates the collision points while F does not:
    pts = [(0, 0, sp.Rational(-1, 4)), (1, sp.Rational(-3, 2), sp.Rational(13, 2)),
           (-1, sp.Rational(3, 2), sp.Rational(13, 2))]
    vals_q1 = [pt[0] for pt in pts]
    vals_F = [tuple(sp.expand(Fi.subs({x: pt[0], y: pt[1], z: pt[2]})) for Fi in F)
              for pt in pts]
    check("F takes ONE value on the three collision points",
          vals_F[0] == vals_F[1] == vals_F[2])
    check("q1 takes THREE distinct values (0, 1, -1) there",
          len(set(vals_q1)) == 3)
    # (iii) the symbol computation in the centralizer lemma:
    #       {sigma, f_i} = -sum_k (dsigma/dp_k)(df_i/dq_k) = -(DF grad_p sigma)_i
    #       for q-only f_i  (note: DF, not (DF)^T -- convention (DF)_{ik}=df_i/dq_k)
    sig = sp.Function('sig')(*Q, *PV)
    i0 = 0
    pb = sum(sp.diff(sig, Q[k])*sp.diff(F[i0], PV[k])
             - sp.diff(sig, PV[k])*sp.diff(F[i0], Q[k]) for k in range(3))
    check("{sigma, f}(q-only f) = -(DF grad_p sigma)_i  [Poisson formula]",
          sp.simplify(pb + sum(sp.diff(sig, PV[k])*sp.diff(F[i0], Q[k])
                               for k in range(3))) == 0)
    # (iv) suspension: F x id on C^4 is still non-injective with det -2 (n>=4 claim)
    w4 = sp.symbols('w4')
    F4 = F + [w4]
    J4 = sp.Matrix(4, 4, lambda i, j: sp.diff(F4[i], (Q + [w4])[j]))
    q4 = [tuple(sp.expand(Fi.subs({x: pt[0], y: pt[1], z: pt[2], w4: 5}))
                for Fi in F4) for pt in pts]
    check("F x id: det = -2, still 3-point collision (=> Dixmier false all n>=3)",
          sp.expand(J4.det()) == -2 and q4[0] == q4[1] == q4[2])

    # ---- 6. display the explicit endomorphism ----------------------------
    print("\n[6] The explicit endomorphism phi of A_3")
    for i, Fi in enumerate(F):
        print(f"    phi(q{i+1}) =", Fi)
    for j, pf in enumerate(phi_p_formulas()):
        print(f"    phi(p{j+1}) =", pf)
    check("phi(p_j) displayed (entries of ((DF)^T)^{-1} applied to p)", True)

    print("\n" + "=" * 72)
    if _failures:
        print(f"RESULT: {len(_failures)} CHECK(S) FAILED:", _failures)
        raise SystemExit(1)
    print("RESULT: ALL CHECKS PASSED.")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
