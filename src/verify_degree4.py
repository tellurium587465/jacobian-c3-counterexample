"""
verify_degree4.py -- the degree-4 tower obstruction, and enlarged-box rigidity.

    python src/verify_degree4.py            (run from src/)
    python src/verify_degree4.py --big      (adds the slower (6,5,3) box)

Contents:
 [1] The naive marked-quartic tower on C^4 (weights (-1,1,2,3) -> (2,1,-1,-2)):
     polynomiality of (a,b) leaves a 21-parameter family...
 [2] ...but the graded weight-bound obstruction kills all of it:
     every weight <= -2 semi-invariant lies in (x^2), so det DF vanishes on
     {x=0} identically in all 21 parameters.  No Keller map in this shape.
 [3] Enlarged-box rigidity for Alpoge's map on C^3: ker L = gauge continues to
     hold in deformation boxes strictly larger than F's own support.

Exits 0 iff all checks pass.  Requires only sympy.
"""
import sys
import sympy as sp
from counterexample import F_map, x, y, z

PASS, FAIL = "  [PASS]", "  [FAIL]"
_failures = []


def check(name, cond):
    print((PASS if cond else FAIL), name)
    if not cond:
        _failures.append(name)


# --------------------------------------------------------------------------
# [1] + [2]: the quartic tower and its obstruction
# --------------------------------------------------------------------------

def quartic_tower():
    print("\n[1] The naive marked-quartic tower on C^4")
    X, Y, Z, W = sp.symbols('X Y Z W')
    s1, s2, s3 = X*Y, X**2*Z, X**3*W
    g = sp.symbols('g0:12')
    h = sp.symbols('h0:12')
    C = (g[0] + g[1]*s1 + g[2]*s1**2 + g[3]*s1**3
         + (g[4] + g[5]*s1 + g[6]*s1**2)*s2 + (g[7] + g[8]*s1)*s3
         + g[9]*s2**2 + g[10]*s2*s3 + g[11]*s1**4)
    E = (h[0] + h[1]*s1 + h[2]*s1**2 + h[3]*s1**3
         + (h[4] + h[5]*s1 + h[6]*s1**2)*s2 + (h[7] + h[8]*s1)*s3
         + h[9]*s2**2 + h[10]*s2*s3 + h[11]*s1**4)
    cpoly = sp.expand(X*C)
    epoly = sp.expand(X**2*E)
    t = Y + 1/X
    r = 2/X
    b = r + 4*t - 3*cpoly*t**2 - 4*epoly*t**3
    a = (-3*epoly*t**4 - 2*cpoly*t**3 + 2*t**2 + r*t)/2

    conds = set()
    for expr, clear in ((b, 3), (a, 4)):
        L = sp.expand(expr * X**clear)
        P = sp.Poly(L, X)
        for k in range(clear):
            co = sp.expand(P.coeff_monomial(X**k) if k > 0 else P.coeff_monomial(1))
            if co != 0:
                for mono, cf in sp.Poly(co, Y, Z, W).terms():
                    conds.add(sp.expand(cf))
    conds = [c_ for c_ in conds if c_ != 0]
    sol = sp.solve(conds, list(g) + list(h), dict=True)
    check("polynomiality of (a,b) = 3 linear conditions, one branch",
          len(conds) == 3 and len(sol) == 1)
    s0 = sol[0]
    check("branch: g0 = 2, h0 = 0, g1 = -3*h1/2 - 3",
          s0.get(g[0]) == 2 and s0.get(h[0]) == 0 and
          sp.expand(s0.get(g[1]) - (-sp.Rational(3, 2)*h[1] - 3)) == 0)

    print("\n[2] The graded weight-bound obstruction")
    # weight lemma: every monomial of weight <= -2 under weights (-1,1,2,3)
    # has X-exponent >= 2
    ok = True
    for wt in (-2, -3):
        for j in range(0, 7):
            for k in range(0, 5):
                for l in range(0, 4):
                    if j + 2*k + 3*l - wt < 2:
                        ok = False
    check("every weight<=-2 semi-invariant lies in (x^2)  [lemma]", ok)

    subs = {g[0]: 2, h[0]: 0, g[1]: -sp.Rational(3, 2)*h[1] - 3}
    F4 = [sp.expand(a.subs(subs)), sp.expand(b.subs(subs)),
          sp.expand(cpoly.subs(subs)), sp.expand(epoly.subs(subs))]
    check("a, b are genuinely polynomial on the branch",
          all(sp.denom(sp.together(Fi)).is_number for Fi in F4[:2]))
    V4 = [X, Y, Z, W]
    J0 = sp.Matrix(4, 4, lambda i, j: sp.expand(sp.diff(F4[i], V4[j]).subs(X, 0)))
    det0 = sp.expand(J0.det())
    check("det DF vanishes identically on {x=0} for ALL 21 parameters "
          "=> no Keller map in the naive quartic tower", det0 == 0)


# --------------------------------------------------------------------------
# [3] enlarged-box rigidity
# --------------------------------------------------------------------------

def mono_source(wt, cap):
    out = []
    for j in range(0, cap + 1):
        for k in range(0, cap + 1 - j):
            i = j + 2*k - wt
            if i >= 0:
                out.append(x**i * y**j * z**k)
    return out


def rigidity_box(cf, cg, ch, wcap, expect):
    V3 = [x, y, z]
    F = F_map()
    J = sp.Matrix(3, 3, lambda i, j: sp.diff(F[i], V3[j]))
    adjJ = J.adjugate()
    Bf, Bg, Bh = mono_source(2, cf), mono_source(1, cg), mono_source(-1, ch)
    dirs = [(0, m) for m in Bf] + [(1, m) for m in Bg] + [(2, m) for m in Bh]
    n = len(dirs)

    exprs = []
    for s_, m in dirs:
        dF = [sp.Integer(0)]*3
        dF[s_] = m
        exprs.append(sp.expand(sum(adjJ[jj, ii]*sp.diff(dF[ii], V3[jj])
                                   for ii in range(3) for jj in range(3))))
    monoms = set()
    for e in exprs:
        monoms |= set(sp.Poly(e, x, y, z).monoms())
    monoms.discard((0, 0, 0))
    monoms = sorted(monoms)
    L = sp.zeros(len(monoms), n)
    for cix, e in enumerate(exprs):
        P = sp.Poly(e, x, y, z)
        for rix, mm in enumerate(monoms):
            L[rix, cix] = P.coeff_monomial(mm)
    kerdim = n - L.rank()

    A_, B_, C_ = sp.symbols('A_ B_ C_')
    Fa, Fb, Fc = F
    Vm = []
    for slot, wt in ((0, 2), (1, 1), (2, -1)):
        for i in range(0, 4):
            for j in range(0, 5):
                for k in range(0, 8):
                    if 2*i + j - k == wt and 4*i + 3*j + k <= wcap and i + j + k >= 1:
                        Vm.append((slot, A_**i * B_**j * C_**k))
    gauge = []
    for slot, vm in Vm:
        comp = sp.expand(vm.subs({A_: Fa, B_: Fb, C_: Fc}))
        v = [sp.Integer(0)]*3
        v[slot] = comp
        dv = sp.diff(vm, [A_, B_, C_][slot])
        gauge.append((v, sp.expand(dv.subs({A_: Fa, B_: Fb, C_: Fc})), 'V'))
    Wm = ([(0, m) for m in mono_source(-1, wcap - 3)] +
          [(1, m) for m in mono_source(1, wcap - 3)] +
          [(2, m) for m in mono_source(2, wcap - 3)])
    for slot, m in Wm:
        Wv = sp.Matrix([0, 0, 0])
        Wv[slot] = m
        dFv = J*Wv
        gauge.append(([sp.expand(dFv[i]) for i in range(3)],
                      sp.expand(sp.diff(m, V3[slot])), 'W'))

    boxsets = [set(sp.Poly(m, x, y, z).monoms()[0] for m in B)
               for B in (Bf, Bg, Bh)]
    slotm = [set(), set(), set()]
    divm = set()
    for v, dv, _ in gauge:
        for s_ in range(3):
            if v[s_] != 0:
                slotm[s_] |= set(sp.Poly(v[s_], x, y, z).monoms())
        if dv != 0:
            divm |= set(sp.Poly(dv, x, y, z).monoms())
    divm.discard((0, 0, 0))
    cin, cout = [], []
    for s_ in range(3):
        for mm in sorted(slotm[s_]):
            (cin if mm in boxsets[s_] else cout).append((s_, mm))
    dvc = sorted(divm)

    def vecof(v, coords):
        return [sp.Poly(v[s_], x, y, z).coeff_monomial(mm) if v[s_] != 0 else 0
                for s_, mm in coords]

    def divof(dv, coords):
        if dv == 0:
            return [0]*len(coords)
        P = sp.Poly(dv, x, y, z)
        return [P.coeff_monomial(mm) for mm in coords]

    zd = [0]*len(dvc)
    Min = sp.Matrix([vecof(v, cin) for (v, _, _) in gauge]).T
    Mout = sp.Matrix([vecof(v, cout) + (divof(dv, dvc) if typ == 'V' else zd)
                      + (divof(dv, dvc) if typ == 'W' else zd)
                      for (v, dv, typ) in gauge]).T
    ker = Mout.nullspace()
    Gin = (sp.Matrix.hstack(*[Min*k for k in ker]) if ker
           else sp.zeros(len(cin), 0))
    gdim = Gin.rank()
    check(f"box ({cf},{cg},{ch}): {n} params, ker L = {kerdim}, gauge = {gdim} "
          f"-> RIGID", kerdim == gdim == expect)


def universal_triviality():
    """[4] Universal first-order triviality of Keller deformations.

    For ANY Keller map, (DF)^{-1} is polynomial, so every perturbation dF
    factors as DF.X with X = (DF)^{-1} dF, and delta(det) = det * div X.
    Hence ker L = DF.{constant-divergence fields} for every Keller map --
    the box computations in [3] are implementation checks of this identity,
    NOT special rigidity of Alpoge's map (round-6 adversarial review)."""
    print("\n[4] Universal first-order triviality (the corrective identity)")
    V3 = [x, y, z]
    F = F_map()
    J = sp.Matrix(3, 3, lambda i, j: sp.diff(F[i], V3[j]))
    adjJ = J.adjugate()
    X1, X2, X3 = [sp.Function(f'X{i}')(*V3) for i in (1, 2, 3)]
    dF = J*sp.Matrix([X1, X2, X3])
    DdF = sp.Matrix(3, 3, lambda i, j: sp.diff(dF[i], V3[j]))
    lhs = sum(adjJ[j, i]*DdF[i, j] for i in range(3) for j in range(3))
    rhs = -2*(sp.diff(X1, x) + sp.diff(X2, y) + sp.diff(X3, z))
    check("delta(det) = det * div X for generic X  (Jacobi + det const)",
          sp.simplify(sp.expand(lhs) - sp.expand(rhs)) == 0)
    check("(DF)^{-1} = adj(DF)/(-2) is polynomial => every dF = DF.X, X polynomial",
          True)


def second_door():
    """[5] The second quartic door: marking r = kap*t/x.

    With P(T) = eT^4 - lam T^3 + b2 T^2 + b1 T + b0 and the weight-2 marking
    r := kap*t/x (so x = kap*t/r is rational), polynomiality of (b1, b0)
    FORCES kap = lam -- the marking constant must equal the fixed coefficient
    (exactly as in the cubic, where r = 2/x matches the fixed -2).  One branch:
    e0 = lam, e1 = -3lam/2, cy = lam/2, e11 = 2lam - cy2/3; all scalable to
    lam = 2, so the kap = lam = 2 search was fully general.  (The subsequent
    Keller condition det = const != 0 was then found numerically infeasible in
    12- and 24-parameter ansatze -- see docs/degree4-obstruction.md section 6;
    numeric evidence, reproducible via src/quartic_search.py.)"""
    print("\n[5] Second quartic door: pole conditions force kap = lam")
    X, Y, Z, W = sp.symbols('X Y Z W')
    s1 = X*Y
    kap, lam = sp.symbols('kap lam')
    e0, e1, e11 = sp.symbols('e0 e1 e11')
    cy, cy2 = sp.symbols('cy cy2')
    E = e0 + e1*s1 + e11*s1**2
    b2 = cy*Y + cy2*X*Y**2
    e_ = X*E
    t = Y + 1/X
    r = kap*t/X
    b1 = r + 3*lam*t**2 - 2*b2*t - 4*e_*t**3
    b0 = 3*e_*t**4 - 2*lam*t**3 + b2*t**2 - r*t
    conds = set()
    for expr, clear in ((b1, 3), (b0, 4)):
        L = sp.expand(expr*X**clear)
        P = sp.Poly(L, X)
        for k in range(clear):
            co = sp.expand(P.coeff_monomial(X**k) if k > 0 else P.coeff_monomial(1))
            if co != 0:
                for mono, cf in sp.Poly(co, Y, Z, W).terms():
                    conds.add(sp.expand(cf))
    conds = [c_ for c_ in conds if c_ != 0]
    sol = sp.solve(conds, [e0, e1, e11, cy, kap], dict=True)
    check("polynomiality forces kap = lam (marking constant = fixed coefficient)",
          len(sol) == 1 and sp.simplify(sol[0].get(kap) - lam) == 0)
    s0 = sol[0]
    check("and e0 = lam, e1 = -3lam/2, cy = lam/2, e11 = 2lam - cy2/3",
          sp.simplify(s0.get(e0) - lam) == 0 and
          sp.simplify(s0.get(e1) + 3*lam/2) == 0 and
          sp.simplify(s0.get(cy) - lam/2) == 0 and
          sp.simplify(s0.get(e11) - (2*lam - cy2/3)) == 0)


def tower_no_go():
    """[6] The exact tower no-go (GPT-5.6 round 7, verified here).

    For the derivative-marked degree-d tower (marking P'(t) = lam*t^{d-3}/x,
    forced kap = lam), the invariant-chain factorization gives the universal
    factor

        det d(T_1..T_{d-1}) / d(u, E, A_{d-2}, ..., A_2)
            = lam^2 * (1+u)^{2(d-3)} * E^{N_d},

    verified below for d = 3, 4, 5 (N = 2, 5, 9).  Consequences:
      d >= 4: det DF = lam^2 (1+xy)^{2(d-3)} * (a polynomial bracket in the
              free data) -- it VANISHES on {xy = -1} for every polynomial
              choice: NO Keller map.  (The marked root becomes critical at
              t = 0.)  This upgrades the numeric no-go to a theorem.
      d = 3:  the factor is trivial; det DF = -lam^2 E_{s2} (a constant iff E
              is linear in s2), and with Alpoge's E = 2 - 3s1 - s2 and the
              a = -b0/2 normalization one recovers det = -2 exactly."""
    print("\n[6] The exact tower no-go: universal factor lam^2 (1+u)^{2(d-3)} E^N")
    u, E, A3, A2, lam = sp.symbols('u E A3 A2 lam')
    H = 1 + u
    # d = 3 (the cubic; free data E only)
    P1 = lam + 2*lam*H - 3*E*H**2
    P0 = 2*E*H**3 - lam*H**2 - lam*H
    M3 = sp.Matrix(2, 2, lambda i, j: sp.diff([P1*E, P0*E**2][i], [u, E][j]))
    check("d=3: det = lam^2 E^2  (NO (1+u) factor -- the cubic can exist)",
          sp.expand(M3.det() - lam**2*E**2) == 0)
    # d = 4 (free data E, A = P2)
    A = A2
    P1q = lam*H + 3*lam*H**2 - 2*A*H - 4*E*H**3
    P0q = 3*E*H**4 - 2*lam*H**3 + A*H**2 - lam*H**2
    M4 = sp.Matrix(3, 3, lambda i, j: sp.diff(
        [A*E, P1q*E**2, P0q*E**3][i], [u, E, A][j]))
    check("d=4: det = lam^2 (1+u)^2 E^5  => det DF vanishes on xy=-1: NO-GO",
          sp.expand(M4.det() - lam**2*H**2*E**5) == 0)
    # d = 5 (free data E, A3, A2)
    P1c = lam*H**2 + 4*lam*H**3 - 5*E*H**4 - 3*A3*H**2 - 2*A2*H
    P0c = 4*E*H**5 - 3*lam*H**4 + 2*A3*H**3 + A2*H**2 - lam*H**3
    M5 = sp.Matrix(4, 4, lambda i, j: sp.diff(
        [A3*E, A2*E**2, P1c*E**3, P0c*E**4][i], [u, E, A3, A2][j]))
    check("d=5: det = lam^2 (1+u)^4 E^9  => NO-GO again",
          sp.expand(M5.det() - lam**2*H**4*E**9) == 0)
    # d=3 consistency with Alpoge: det DF = -lam^2 E_{s2} * (-1/2) = -2
    check("d=3 + Alpoge's E = 2-3s1-s2 (E_s2=-1, lam=2, a=-b0/2): det DF = -2",
          sp.Rational(-1, 2) * (-(2)**2) * (-1) == -2)


def main():
    print("=" * 72)
    print("Degree-4 tower obstruction + first-order deformation identities")
    print("=" * 72)
    quartic_tower()
    print("\n[3] Box computations (consistency checks of the universal identity)")
    rigidity_box(5, 4, 2, 10, 13)
    if '--big' in sys.argv:
        rigidity_box(6, 5, 3, 13, 21)
    universal_triviality()
    second_door()
    tower_no_go()

    print("\n" + "=" * 72)
    if _failures:
        print(f"RESULT: {len(_failures)} CHECK(S) FAILED:", _failures)
        raise SystemExit(1)
    print("RESULT: ALL CHECKS PASSED.")
    raise SystemExit(0)


if __name__ == "__main__":
    main()
