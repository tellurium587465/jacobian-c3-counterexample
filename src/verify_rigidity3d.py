"""
verify_rigidity3d.py -- infinitesimal rigidity of Alpoge's map in its
weighted-degree box.

    python src/verify_rigidity3d.py     (run from src/)

STATEMENT (first-order, box-restricted; every ingredient checked below).
Consider deformations  F + eps*dF  with dF = (df, dg, dh) graded like F and
supported in the same weighted monomial boxes as F itself:
    df: the 13 weight-2 monomials of (s,w)-content <= 4,
    dg: the  9 weight-1 monomials of content <= 3,
    dh: the  3 weight-(-1) monomials of content <= 1.
By Jacobi's formula, 'det D(F + eps dF) = const' to first order means the
nonconstant part of  tr(adj(DF) . D(dF))  vanishes: a linear condition L.
First-order REPARAMETRIZATIONS are  dF = V(F) + DF.W  with V, W graded
polynomial vector fields whose joint divergence  divV(F) + divW  is constant
(that is exactly (d/de) of 'det D(Phi_e o F o Psi_e) = const').

RESULT:  dim ker L = 7  and we exhibit 7 independent gauge directions inside
the box, each verified to lie in ker L.  Since gauge directions always lie in
ker L, this proves  ker L = gauge exactly:

    every first-order Keller-preserving deformation of F inside its weighted
    monomial box is tangent to the reparametrization orbit.

Honest scope: first-order only; box-restricted; says nothing about non-graded
or higher-content deformations, nor about other components of the Keller
variety.

IMPORTANT POST-SCRIPT (round-6 review): this result is correct but UNIVERSAL.
For any Keller map, (DF)^{-1} is polynomial, so every perturbation factors as
dF = DF.X and delta(det) = det * div X: ker L = source reparametrizations
holds automatically for every Keller map and compatible box.  This script is
therefore an implementation check of that identity, not evidence that Alpoge's
map is special.  See docs/degree4-obstruction.md sections 4-5 and
verify_degree4.py section [4].

Exits 0 iff all checks pass.  Requires only sympy.
"""
import sympy as sp
from counterexample import F_map, x, y, z

PASS, FAIL = "  [PASS]", "  [FAIL]"
_failures = []


def check(name, cond):
    print((PASS if cond else FAIL), name)
    if not cond:
        _failures.append(name)


def mono_source(w, cap):
    """weight-w monomials x^i y^j z^k (-i+j+2k = w) with content j+k <= cap."""
    out = []
    for j in range(0, cap + 1):
        for k in range(0, cap + 1 - j):
            i = j + 2*k - w
            if i >= 0:
                out.append(x**i * y**j * z**k)
    return out


def main():
    print("=" * 72)
    print("Infinitesimal rigidity of Alpoge's map in its weighted-degree box")
    print("=" * 72)
    V3 = [x, y, z]
    F = F_map()
    J = sp.Matrix(3, 3, lambda i, j: sp.diff(F[i], V3[j]))
    adjJ = J.adjugate()

    Bf, Bg, Bh = mono_source(2, 4), mono_source(1, 3), mono_source(-1, 1)
    check("box sizes (13, 9, 3)", (len(Bf), len(Bg), len(Bh)) == (13, 9, 3))
    boxsets = [set(sp.Poly(m, x, y, z).monoms()[0] for m in B)
               for B in (Bf, Bg, Bh)]
    check("F itself lies in the box",
          all(set(sp.Poly(F[s], x, y, z).monoms()) <= boxsets[s]
              for s in range(3)))
    basis_dirs = [(0, m) for m in Bf] + [(1, m) for m in Bg] + [(2, m) for m in Bh]

    # ---- Keller linearization L ----------------------------------------
    print("\n[1] Keller linearization")

    def Ddet_of(slot, mono):
        dF = [sp.Integer(0)]*3
        dF[slot] = mono
        return sp.expand(sum(adjJ[j, i]*sp.diff(dF[i], V3[j])
                             for i in range(3) for j in range(3)))

    exprs = [Ddet_of(s, m) for (s, m) in basis_dirs]
    monoms = set()
    for e in exprs:
        monoms |= set(sp.Poly(e, x, y, z).monoms())
    monoms.discard((0, 0, 0))
    monoms = sorted(monoms)
    L = sp.zeros(len(monoms), len(basis_dirs))
    for cix, e in enumerate(exprs):
        P = sp.Poly(e, x, y, z)
        for rix, mm in enumerate(monoms):
            L[rix, cix] = P.coeff_monomial(mm)
    kerdim = len(basis_dirs) - L.rank()
    check(f"dim ker L = 7  (got {kerdim})", kerdim == 7)

    # ---- gauge directions ----------------------------------------------
    print("\n[2] Gauge directions (graded fields, separately-constant divergences)")
    Fa, Fb, Fc = F
    A_, B_, C_ = sp.symbols('A_ B_ C_')
    Vmono = ([(0, A_), (0, B_**2), (0, A_*B_*C_)] +
             [(1, B_), (1, A_*C_), (1, B_**2*C_)] +
             [(2, C_), (2, B_*C_**2), (2, A_*C_**3)])
    gauge_all = []
    for slot, vm in Vmono:
        comp = sp.expand(vm.subs({A_: Fa, B_: Fb, C_: Fc}))
        v = [sp.Integer(0)]*3
        v[slot] = comp
        dv = sp.diff(vm, [A_, B_, C_][slot])
        gauge_all.append((v, sp.expand(dv.subs({A_: Fa, B_: Fb, C_: Fc}))))
    Wmonos = ([(0, m) for m in mono_source(-1, 3)] +
              [(1, m) for m in mono_source(1, 3)] +
              [(2, m) for m in mono_source(2, 3)])
    for slot, m in Wmonos:
        Wv = sp.Matrix([0, 0, 0])
        Wv[slot] = m
        dFv = J*Wv
        gauge_all.append(([sp.expand(dFv[i]) for i in range(3)],
                          sp.expand(sp.diff(m, V3[slot]))))

    # gauge_all entries were appended V-candidates first, then W-candidates
    n_V = len(Vmono)
    slot_monoms = [set(), set(), set()]
    div_monoms = set()
    for vec, dv in gauge_all:
        for s_ in range(3):
            if vec[s_] != 0:
                slot_monoms[s_] |= set(sp.Poly(vec[s_], x, y, z).monoms())
        if dv != 0:
            div_monoms |= set(sp.Poly(dv, x, y, z).monoms())
    div_monoms.discard((0, 0, 0))
    coords_in, coords_out = [], []
    for s_ in range(3):
        for mm in sorted(slot_monoms[s_]):
            (coords_in if mm in boxsets[s_] else coords_out).append((s_, mm))
    div_coords = sorted(div_monoms)

    def vecof(vec, coords):
        return [sp.Poly(vec[s_], x, y, z).coeff_monomial(mm)
                if vec[s_] != 0 else 0 for s_, mm in coords]

    def divof(dv, coords):
        if dv == 0:
            return [0]*len(coords)
        P = sp.Poly(dv, x, y, z)
        return [P.coeff_monomial(mm) for mm in coords]

    Min = sp.Matrix([vecof(v, coords_in) for (v, _) in gauge_all]).T
    # SEPARATE divergence constraints (GPT round-5 repair): a genuine
    # one-parameter automorphism family forces div V = const and div W = const
    # individually, not just their sum.  V-candidates fill div-block 1,
    # W-candidates div-block 2.
    zeros_div = [0]*len(div_coords)
    Mout_rows = []
    for ix, (v, dv) in enumerate(gauge_all):
        dvec = divof(dv, div_coords)
        blockV = dvec if ix < n_V else zeros_div
        blockW = dvec if ix >= n_V else zeros_div
        Mout_rows.append(vecof(v, coords_out) + blockV + blockW)
    Mout = sp.Matrix(Mout_rows).T
    ker_out = Mout.nullspace()
    Gin = (sp.Matrix.hstack(*[Min*k for k in ker_out])
           if ker_out else sp.zeros(len(coords_in), 0))
    gdim = Gin.rank()
    check(f"dim(gauge ∩ box) = 7 under SEPARATE div-const constraints (got {gdim})",
          gdim == 7)

    # each gauge direction lies in ker L (verified directly on the map level)
    sane = True
    for kv in ker_out:
        vec3 = [sp.Integer(0)]*3
        for cand_ix, coef in enumerate(kv):
            if coef != 0:
                for s_ in range(3):
                    vec3[s_] += coef*gauge_all[cand_ix][0][s_]
        dd = sp.expand(sum(adjJ[j, i]*sp.diff(vec3[i], V3[j])
                           for i in range(3) for j in range(3)))
        if sp.expand(dd - dd.subs({x: 0, y: 0, z: 0})) != 0:
            sane = False
    check("every gauge-in-box direction satisfies the linearized Keller condition",
          sane)

    print("\n[3] Conclusion")
    check("ker L = gauge  =>  F is INFINITESIMALLY RIGID in its weighted box",
          kerdim == gdim == 7 and sane)

    print("\n" + "=" * 72)
    if _failures:
        print(f"RESULT: {len(_failures)} CHECK(S) FAILED:", _failures)
        raise SystemExit(1)
    print("RESULT: ALL CHECKS PASSED.")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
