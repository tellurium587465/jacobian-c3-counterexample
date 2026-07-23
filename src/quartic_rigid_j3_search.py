"""
quartic_rigid_j3_search.py -- the rigid case Phi = -E^3/lam^2 of the
factorization identity: (B,C,T) is then a C^3 KELLER TRIPLE with C determined
by (E,A).  (Numerics, clearly labeled.)

RESULTS OF RECORD (2026-07-23; 8 random starts x 300 damped GN iterations,
all nonconstant coefficients of J(B,C,T) + support residuals + a nonzero-
constant barrier):

    (dE,dA)   unknowns  equations  best residual
    (2,4)        11        173        3.2
    (3,5)        19        513        2.9      [consistent with box sweeps]
    (4,6)        30       1136        3.1      [NEW territory: dE >= 4]
    (4,8)        48       1346        3.0
    (5,7)        43       2127        2.9
    (5,9)        65       2442        3.0
    (6,8)        60       3571        5.6

ALL FLOOR AT O(1): the rigid j=3 route (the last structured door within
computational reach) also yields no polynomial solution.  Combined with the
12-pattern general sweeps, the exact divisibility obstruction Phi | E^3, and
the existing order-6 formal jets, this supports:

CONJECTURE (polynomial non-realizability of the graded quartic tower).
There are no polynomials E, A, P1 in C[S1,S2,S3] satisfying the support
conditions and  Phi * J(AE, P1 E^2, HE) = delta E^3  with delta != 0.
Equivalently: geometric degree 4 is not realizable by the (-1,1,2,3)-graded
marked-quartic mechanism.  (Open: a proof via the divisibility obstruction's
case analysis; and non-graded / other-weight constructions.)
"""
import numpy as np
import sys, time

LAM = 2.0

def monos_upto(cap):
    out = []
    for m in range(cap+1):
        for l in range(m//3+1):
            for k in range((m-3*l)//2+1):
                out.append((m-3*l-2*k, k, l))
    return out

def run(dE, dA, ntrials=8, seed=0, iters=300, tol=1e-11):
    capJ = dA + 7*dE - 5 + 2
    cap = capJ
    M = monos_upto(cap)
    idx = {mo: i for i, mo in enumerate(M)}
    N = len(M)
    degv = np.array([mo[0]+2*mo[1]+3*mo[2] for mo in M])

    I, J_, K = [], [], []
    for i1, m1 in enumerate(M):
        d1 = degv[i1]
        for i2 in range(i1, N):
            if d1 + degv[i2] > cap:
                continue
            m2 = M[i2]
            mo = (m1[0]+m2[0], m1[1]+m2[1], m1[2]+m2[2])
            I.append(i1); J_.append(i2); K.append(idx[mo])
    I = np.array(I); J_ = np.array(J_); K = np.array(K)
    DIAG = (I == J_)

    def pmul(u, w):
        prod = u[I]*w[J_] + np.where(DIAG, 0.0, u[J_]*w[I])
        out = np.zeros(N)
        np.add.at(out, K, prod)
        return out

    DIrows = []
    for var in range(3):
        src, dst, cf = [], [], []
        for i, mo in enumerate(M):
            if mo[var] > 0:
                mo2 = tuple(x-(1 if t == var else 0) for t, x in enumerate(mo))
                src.append(i); dst.append(idx[mo2]); cf.append(mo[var])
        DIrows.append((np.array(src), np.array(dst), np.array(cf)))

    def pdiff(u, var):
        s, d, c = DIrows[var]
        out = np.zeros(N)
        np.add.at(out, d, u[s]*c)
        return out

    Hv = np.zeros(N); Hv[idx[(0,0,0)]] = 1.0; Hv[idx[(1,0,0)]] = 1.0
    H2 = pmul(Hv, Hv); H3 = pmul(H2, Hv)

    layoutA = [mo for mo in M if 1 <= mo[0]+2*mo[1]+3*mo[2] <= dA
               and mo != (1, 0, 0)]
    layoutE = [mo for mo in M if 2 <= mo[0]+2*mo[1]+3*mo[2] <= dE]
    NV = len(layoutA) + len(layoutE)
    eqsel = np.where((degv >= 1) & (degv <= capJ))[0]

    def resid(v):
        A = np.zeros(N); E = np.zeros(N)
        for mo, val in zip(layoutA, v[:len(layoutA)]):
            A[idx[mo]] = val
        for mo, val in zip(layoutE, v[len(layoutA):]):
            E[idx[mo]] = val
        A[idx[(1,0,0)]] = -5*LAM
        E[idx[(0,0,0)]] = LAM
        E[idx[(1,0,0)]] = 4*LAM
        E2 = pmul(E, E); E3 = pmul(E2, E)
        P1 = 3*LAM*H2 - 4*pmul(E, H3) - 2*pmul(A, Hv) + E3/(LAM**2)
        # support residuals on P1 (deg >= 2): constant and S1-coeff must vanish
        sup = np.array([P1[idx[(0,0,0)]], P1[idx[(1,0,0)]]])
        B = pmul(A, E); C = pmul(P1, E2); T = pmul(Hv, E)
        D1 = [pdiff(B, i) for i in range(3)]
        D2 = [pdiff(C, i) for i in range(3)]
        D3 = [pdiff(T, i) for i in range(3)]
        det = (pmul(pmul(D1[0], D2[1]), D3[2]) + pmul(pmul(D1[1], D2[2]), D3[0])
               + pmul(pmul(D1[2], D2[0]), D3[1]) - pmul(pmul(D1[0], D2[2]), D3[1])
               - pmul(pmul(D1[2], D2[1]), D3[0]) - pmul(pmul(D1[1], D2[0]), D3[2]))
        # J(B,C,T) must be a NONZERO constant: kill nonconstant part; barrier on 0
        const = det[idx[(0,0,0)]]
        rr = np.concatenate([det[eqsel], sup, [1.0/(abs(const)+1e-9) * 1e-3]])
        return rr

    rng = np.random.default_rng(seed)
    best = (np.inf, None, 0.0)
    for trial in range(ntrials):
        v = rng.normal(0, 0.4, NV)
        r = resid(v); rn = np.linalg.norm(r)
        mu = 1e-3
        Jm = None; sinceJ = 999
        for it in range(iters):
            if sinceJ >= 6 or Jm is None:
                Jm = np.zeros((len(r), NV))
                h = 1e-7
                for i2 in range(NV):
                    v2 = v.copy(); v2[i2] += h
                    Jm[:, i2] = (resid(v2) - r)/h
                sinceJ = 0
            Am = Jm.T@Jm + mu*np.eye(NV)
            try:
                step = np.linalg.solve(Am, -Jm.T@r)
            except np.linalg.LinAlgError:
                mu *= 10; continue
            v2 = v + step
            r2 = resid(v2); rn2 = np.linalg.norm(r2)
            if rn2 < rn:
                v, r, rn = v2, r2, rn2
                mu = max(mu/2.5, 1e-14); sinceJ += 1
                if rn < tol:
                    break
            else:
                mu *= 8; sinceJ = 999
                if mu > 1e12:
                    break
        if rn < best[0]:
            best = (rn, v.copy(), 0.0)
        if best[0] < tol:
            break
    return best[0], NV, len(eqsel)

if __name__ == '__main__':
    for (dE, dA) in eval(sys.argv[1]):
        t0 = time.time()
        rn, nv, ne = run(dE, dA)
        print(f"rigid j=3, dE={dE}, dA={dA}: {nv} unknowns, {ne} eqs, "
              f"best residual {rn:.3e}  ({time.time()-t0:.0f}s)", flush=True)
