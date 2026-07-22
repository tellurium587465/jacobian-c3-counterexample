"""
quartic_truncation_search.py -- the polynomial-truncation endgame search.
(Numerics, clearly labeled; float Gauss-Newton with frozen Jacobians.)

QUESTION: does the formal degree-4 Keller structure (see quartic_gn_solver.py)
truncate to an actual POLYNOMIAL solution at some degrees (E<=dE, A<=dA, P1<=dP)?

RESULTS OF RECORD (2026-07-22/23; 8 random starts x 250 damped GN iterations
per pattern; equations imposed through degree min(3*max_deg+4, 26)):

    pattern (dE,dA,dP)   unknowns  equations  best residual
    (2,4,5)                 24        314        4.1e-01
    (3,4,6)                 34        458        1.6e+00
    (3,5,6)                 39        458        2.4e+00
    (2,5,7)                 44        640        1.6e+00
    -- all floor at O(1): NO polynomial solution found in these patterns.
    (4,6,8), (6,6,6), (4,5,7): not completed (compute budget); open.

Combined with the formal solution's slowly-decaying (non-truncating) tail,
the evidence increasingly favors the FORMAL-YES / POLYNOMIAL-NO dichotomy for
the Psi-extended graded quartic tower in this gauge slice (lam=2, delta=11/128).
Open: larger patterns, other gauge slices, and an exactness proof either way.
"""
import numpy as np
import random, sys, time

LAM = 2.0
DELTA = 11.0/128.0

def monos(m):
    out = []
    for l in range(m//3+1):
        for k in range((m-3*l)//2+1):
            out.append((m-3*l-2*k, k, l))
    return out

def deg(mo): return mo[0]+2*mo[1]+3*mo[2]

def tadd(a, b):
    r = dict(a)
    for k, v in b.items():
        r[k] = r.get(k, 0.0)+v
    return r

def tscale(a, c):
    return {k: c*v for k, v in a.items()}

def tmul(a, b, cap):
    r = {}
    for k1, v1 in a.items():
        d1 = deg(k1)
        for k2, v2 in b.items():
            if d1+deg(k2) > cap:
                continue
            key = (k1[0]+k2[0], k1[1]+k2[1], k1[2]+k2[2])
            r[key] = r.get(key, 0.0)+v1*v2
    return r

def tdiff(a, i):
    r = {}
    for k, v in a.items():
        e = k[i]
        if e:
            key = tuple(x-(1 if idx == i else 0) for idx, x in enumerate(k))
            r[key] = r.get(key, 0.0)+e*v
    return r

def run_pattern(dE, dA, dP, meq, cap, ntrials=8, seed=0, iters=250):
    ALLM = {m: monos(m) for m in range(cap+2)}
    H = {(0,0,0): 1.0, (1,0,0): 1.0}
    H2 = tmul(H, H, cap); H3 = tmul(H2, H, cap); H4 = tmul(H3, H, cap)
    layout = []
    for m in range(1, dA+1):
        for mo in ALLM[m]: layout.append(('A', mo))
    for m in range(2, dP+1):
        for mo in ALLM[m]: layout.append(('P', mo))
    for m in range(3, dE+1):
        for mo in ALLM[m]: layout.append(('E', mo))
    NV = len(layout)
    eqmonos = [mo for m in range(0, meq+1) for mo in ALLM[m]]

    def build(v):
        Ad, Pd, Ed = {}, {}, {}
        for (t, mo), val in zip(layout, v):
            {'A': Ad, 'P': Pd, 'E': Ed}[t][mo] = val
        A1 = Ad.get((1,0,0), 0.0); A11 = Ad.get((2,0,0), 0.0); A2 = Ad.get((0,1,0), 0.0)
        P11 = Pd.get((2,0,0), 0.0); P2 = Pd.get((0,1,0), 0.0)
        Ed[(0,0,0)] = LAM
        Ed[(1,0,0)] = -LAM-A1
        Ed[(2,0,0)] = LAM+2*A1-A11-P11
        Ed[(0,1,0)] = -A2-P2
        return Ed, Ad, Pd

    def resid(v):
        E, A, P1 = build(v)
        P0 = tadd(tadd(tscale(H3, LAM), tscale(tmul(E, H4, cap), -1.0)),
                  tadd(tscale(tmul(A, H2, cap), -1.0), tscale(tmul(P1, H, cap), -1.0)))
        E2 = tmul(E, E, cap)
        T1 = tmul(A, E, cap); T2 = tmul(P1, E2, cap)
        T3 = tmul(P0, tmul(E2, E, cap), cap)
        rows = [[tdiff(T, i) for i in range(3)] for T in (T1, T2, T3)]
        det = {}
        for perm, sgn in [((0,1,2),1),((1,2,0),1),((2,0,1),1),
                          ((0,2,1),-1),((2,1,0),-1),((1,0,2),-1)]:
            det = tadd(det, tscale(tmul(tmul(rows[0][perm[0]], rows[1][perm[1]], cap),
                                        rows[2][perm[2]], cap), sgn))
        E5 = tmul(tmul(E2, E2, cap), E, cap)
        return np.array([det.get(mo, 0.0) - DELTA*E5.get(mo, 0.0) for mo in eqmonos])

    rng = np.random.default_rng(seed)
    best = (np.inf, None)
    for trial in range(ntrials):
        v = rng.normal(0, 0.3, NV)
        r = resid(v); rn = np.linalg.norm(r)
        mu = 1e-3
        J = None
        since_J = 999
        for it in range(iters):
            if since_J >= 6 or J is None:
                J = np.zeros((len(r), NV))
                h = 1e-7
                for i in range(NV):
                    v2 = v.copy(); v2[i] += h
                    J[:, i] = (resid(v2) - r)/h
                since_J = 0
            A_ = J.T@J + mu*np.eye(NV)
            step = np.linalg.solve(A_, -J.T@r)
            v2 = v + step
            r2 = resid(v2); rn2 = np.linalg.norm(r2)
            if rn2 < rn:
                v, r, rn = v2, r2, rn2
                mu = max(mu/2.5, 1e-14)
                since_J += 1
                if rn < 1e-11:
                    break
            else:
                mu *= 8
                since_J = 999   # refresh J on failure
                if mu > 1e12:
                    break
        if rn < best[0]:
            best = (rn, v.copy())
        if best[0] < 1e-11:
            break
    return best, NV, len(eqmonos)

if __name__ == '__main__':
    patterns = eval(sys.argv[1]) if len(sys.argv) > 1 else [(6,6,6)]
    for (dE, dA, dP) in patterns:
        top = max(dE, dA, dP)
        meq = min(3*top + 4, 26)
        cap = meq
        t0 = time.time()
        (rn, v), nv, ne = run_pattern(dE, dA, dP, meq, cap)
        print(f"pattern E<={dE} A<={dA} P<={dP}: unknowns {nv}, eqs {ne}, "
              f"best residual {rn:.3e}  ({time.time()-t0:.0f}s)", flush=True)
        if rn < 1e-9:
            np.save(f'endgame_hit_{dE}_{dA}_{dP}.npy', v)
            print("  *** HIT saved ***", flush=True)
