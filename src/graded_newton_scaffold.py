"""
graded_newton_scaffold.py -- SCAFFOLD (not yet a result) for the decisive
degree-by-degree exact solve of the Psi-extended quartic tower.

CLEAN PROBLEM STATEMENT (the whole degree-4 tower reduces to this):
  find polynomials E, A, P1 in Q-bar[S1,S2,S3] (weighted deg(S) = (1,2,3))
  and constants lam, delta != 0 with
    support: A(0) = 0;  P1 has weighted degree >= 2;
             P0 := lam*H^3 - E*H^4 - A*H^2 - P1*H  has degree >= 3  (H = 1+S1);
    Keller:  det d(A*E, P1*E^2, P0*E^3)/dS = delta * E^5.
  Any solution yields a graded Keller map of C^4 of geometric degree 4 --
  a NEW counterexample mechanism.  Numerics (src/quartic_psi_search.py) show a
  near-solution curve with det* ~ 0.0859-0.0860 and the stable invariant
  c/lam ~ -0.5424 across independent runs.

STATUS: the naive all-symbolic truncated expansion below exceeds sympy's
practical limits (expression swell in the symbolic-coefficient products).
NEXT IMPLEMENTATION (specified for resumption):
  * per-stage recomputation: at stage m, substitute already-solved numeric
    coefficients, keep ONLY degree-(m+3) coefficients symbolic; truncate at
    cap = m.  Each stage is then linear in the few active symbols.
  * resolve free choices with the numeric solution as guide (rationalize);
    keep lam symbolic if the lam = 2 slice proves inconsistent.
  * alternatively: evaluation-interpolation (sample S-points, solve numeric
    linear systems per stage, reconstruct exact coefficients), or port to
    Singular/Macaulay2 for the polynomial algebra.
Outcomes: solution truncates -> NEW degree-4 counterexample (verify det,
fiber = 4, rational 4-collision); forced infinite tail -> formal-yes/
polynomial-no dichotomy theorem; contradiction -> full closure of the tower.
"""
import sympy as sp
from itertools import product

CAP_EQ = 6          # impose det-equations exactly up to this degree
CAP_DATA = CAP_EQ + 3
lam = sp.Rational(2)     # gauge slice attempt
delta = sp.Symbol('delta')

def monos(m):
    out = []
    for l in range(m // 3 + 1):
        for k in range((m - 3*l) // 2 + 1):
            j = m - 3*l - 2*k
            out.append((j, k, l))
    return out

# ---------- truncated poly: dict (j,k,l) -> coeff ----------
def tadd(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = sp.expand(r.get(k, 0) + v)
        if r[k] == 0:
            del r[k]
    return r

def tscale(a, c):
    return {k: sp.expand(c*v) for k, v in a.items() if sp.expand(c*v) != 0}

def tmul(a, b, cap=CAP_DATA + 4):
    r = {}
    for (j1, k1, l1), v1 in a.items():
        for (j2, k2, l2), v2 in b.items():
            j, k, l = j1 + j2, k1 + k2, l1 + l2
            if j + 2*k + 3*l > cap:
                continue
            key = (j, k, l)
            r[key] = sp.expand(r.get(key, 0) + v1*v2)
    return {k: v for k, v in r.items() if v != 0}

def tdiff(a, i):
    r = {}
    for (j, k, l), v in a.items():
        e = (j, k, l)[i]
        if e > 0:
            key = tuple(x - (1 if idx == i else 0) for idx, x in enumerate((j, k, l)))
            r[key] = sp.expand(r.get(key, 0) + e*v)
    return {k: v for k, v in r.items() if v != 0}

def deg(key):
    return key[0] + 2*key[1] + 3*key[2]

# ---------- data with symbolic coefficients ----------
sym_of = {}
def coeffs(prefix, mindeg):
    d = {}
    for m in range(mindeg, CAP_DATA + 1):
        for mo in monos(m):
            s = sp.Symbol(f"{prefix}_{mo[0]}_{mo[1]}_{mo[2]}")
            d[mo] = s
            sym_of[s] = (prefix, mo)
    return d

E = coeffs('E', 0)
A = coeffs('A', 1)
P1 = coeffs('P', 2)
H = {(0, 0, 0): sp.Integer(1), (1, 0, 0): sp.Integer(1)}
H2 = tmul(H, H); H3 = tmul(H2, H); H4 = tmul(H3, H)

P0 = tadd(tadd(tscale(H3, lam), tscale(tmul(E, H4), -1)),
          tadd(tscale(tmul(A, H2), -1), tscale(tmul(P1, H), -1)))

support_eqs = [P0.get(mo, sp.Integer(0)) for m in range(0, 3) for mo in monos(m)]

T1 = tmul(A, E)
E2 = tmul(E, E)
T2 = tmul(P1, E2)
T3 = tmul(P0, tmul(E2, E))

rows = [[tdiff(T, i) for i in range(3)] for T in (T1, T2, T3)]
def det3(M):
    t = {}
    for perm, sgn in [((0,1,2),1),((1,2,0),1),((2,0,1),1),((0,2,1),-1),((2,1,0),-1),((1,0,2),-1)]:
        p = tmul(tmul(M[0][perm[0]], M[1][perm[1]]), M[2][perm[2]])
        t = tadd(t, tscale(p, sgn))
    return t
print("computing det (truncated)...", flush=True)
D = det3(rows)
E5 = tmul(tmul(E2, E2), E)
R = tadd(D, tscale(E5, -delta))

eqs_by_deg = {}
for key, v in R.items():
    if deg(key) <= CAP_EQ:
        eqs_by_deg.setdefault(deg(key), []).append(v)
print("eq counts by degree:", {m: len(v) for m, v in sorted(eqs_by_deg.items())}, flush=True)

# ---------- staged solve ----------
subs = {}
def apply_subs(e):
    return sp.expand(e.subs(subs))

# stage -1: support equations (linear, low degree data)
pend = [apply_subs(e) for e in support_eqs]
pend = [e for e in pend if e != 0]
unk = sorted({s for e in pend for s in e.free_symbols if s in sym_of}, key=str)
sol = sp.solve(pend, unk, dict=True)
print("support solve branches:", len(sol), flush=True)
subs.update(sol[0])
subs = {k: sp.expand(v.subs(subs)) for k, v in subs.items()}

leftover = []
for m in range(0, CAP_EQ + 1):
    eqs = [apply_subs(e) for e in eqs_by_deg.get(m, [])]
    eqs = [e for e in eqs if e != 0] + [apply_subs(e) for e in leftover]
    eqs = [e for e in eqs if e != 0]
    leftover = []
    if not eqs:
        print(f"deg {m}: satisfied", flush=True)
        continue
    unk = sorted({s for e in eqs for s in e.free_symbols
                  if s in sym_of or s == delta}, key=str)
    print(f"deg {m}: {len(eqs)} eqs, {len(unk)} unknowns", flush=True)
    if not unk:
        print(f"  INCONSISTENT at degree {m}: residual {eqs[:3]}", flush=True)
        raise SystemExit(1)
    sol = sp.solve(eqs, unk, dict=True)
    if not sol:
        print(f"  no solution at degree {m} -> deferring", flush=True)
        leftover = eqs
        continue
    s0 = sol[0]
    subs.update({k: sp.expand(v.subs(subs)) for k, v in s0.items()})
    subs = {k: sp.expand(v.subs(subs)) for k, v in subs.items()}
    solved_names = [str(k) for k in s0][:10]
    print(f"  solved {len(s0)}: {solved_names}{'...' if len(s0)>10 else ''}", flush=True)

# zero remaining free coefficients (greedy truncation) and check all residuals
free_left = [s for s in sym_of if s not in subs]
z = {s: 0 for s in free_left}
print(f"\nzeroing {len(free_left)} free coefficients", flush=True)
bad = []
for m, eqs in sorted(eqs_by_deg.items()):
    for e in eqs:
        r = sp.expand(e.subs(subs).subs(z))
        if r != 0:
            bad.append((m, r))
print("delta =", sp.simplify(sp.expand(subs.get(delta, delta))), flush=True)
if not bad:
    print("\n*** ALL EQUATIONS SATISFIED (within cap) -- CANDIDATE EXACT SOLUTION ***", flush=True)
    for prefix, dd in (('E', E), ('A', A), ('P', P1)):
        print(f"-- {prefix}:", flush=True)
        for mo in sorted(dd, key=deg):
            val = sp.expand(dd[mo].subs(subs).subs(z))
            if val != 0:
                print(f"   S1^{mo[0]} S2^{mo[1]} S3^{mo[2]} : {val}", flush=True)
else:
    print(f"\n{len(bad)} residual equations remain, lowest degrees:", flush=True)
    for m, r in bad[:6]:
        print(f"   deg {m}: {sp.factor(r)}", flush=True)
