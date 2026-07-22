"""
quartic_search.py -- REPRODUCIBLE NUMERIC EVIDENCE (not part of the exact suite).

Least-squares search for a Keller structure on the marked-quartic tower with
the weight-2 marking r = 2t/x (the "second door" of docs/degree4-obstruction.md
section 6).  The pole conditions force kap = lam = 2 (verified exactly in
verify_degree4.py section [5]); this script then searches the 24-parameter
polynomial ansatz for  det M = c * Pe^5  with c != 0 (enforced via the
auxiliary unknown mu: residuals mu*ratio - 1).

Outcome (seed 5, 80 starts): residual floor ~1.0 -- no Keller structure; the
only numeric solutions have det = 0 identically (degenerate maps).  Requires
numpy + scipy.  Runtime a few minutes.
"""
import numpy as np
import sympy as sp
from scipy.optimize import least_squares

S1, S2, S3 = sp.symbols('S1 S2 S3')
pn = ['e111', 'ez1', 'ew', 'ew1', 'c_y2', 'c_z', 'c_y3', 'c_yz',
      'c_w', 'c_y4', 'c_y2z', 'c_yw',
      'e4', 'e5', 'ez2', 'ew2', 'ezz', 'ezw', 'eww',
      'c_y5', 'c_y3z', 'c_y2w', 'c_zz', 'c_zw']
ps = sp.symbols(pn)
(e111, ez1, ew, ew1, c_y2, c_z, c_y3, c_yz, c_w, c_y4, c_y2z, c_yw,
 e4, e5, ez2, ew2, ezz, ezw, eww, c_y5, c_y3z, c_y2w, c_zz, c_zw) = ps

Pe = (2 - 3*S1 + (4 - c_y2/3)*S1**2 + e111*S1**3 + e4*S1**4 + e5*S1**5
      + (-c_z/3 + ez1*S1 + ez2*S1**2)*S2 + (ew + ew1*S1 + ew2*S1**2)*S3
      + ezz*S2**2 + ezw*S2*S3 + eww*S3**2)
P2 = (S1 + c_y2*S1**2 + c_z*S2 + c_y3*S1**3 + c_yz*S1*S2 + c_w*S3
      + c_y4*S1**4 + c_y2z*S1**2*S2 + c_yw*S1*S3
      + c_y5*S1**5 + c_y3z*S1**3*S2 + c_y2w*S1**2*S3 + c_zz*S2**2 + c_zw*S2*S3)
t1 = S1 + 1
r1 = 2*(S1 + 1)
P1 = r1 + 6*t1**2 - 2*P2*t1 - 4*Pe*t1**3
P0 = 3*Pe*t1**4 - 4*t1**3 + P2*t1**2 - r1*t1

T = [P2*Pe, P1*Pe**2, P0*Pe**3]
Vs = [S1, S2, S3]
Ment = [[sp.diff(T[i], Vs[j]) for j in range(3)] for i in range(3)]
args = Vs + list(ps)
fM = [[sp.lambdify(args, Ment[i][j], 'numpy') for j in range(3)] for i in range(3)]
fPe = sp.lambdify(args, Pe, 'numpy')

rng = np.random.default_rng(5)
NPTS = 70
pts = rng.uniform(-0.8, 0.8, size=(NPTS, 3))

def ratio(params, p):
    a = list(p) + list(params)
    M = np.array([[fM[i][j](*a) for j in range(3)] for i in range(3)])
    pe = fPe(*a)
    return np.linalg.det(M) / pe**5

def resid(u):
    params, mu = u[:24], u[24]
    vals = np.array([ratio(params, p) for p in pts])
    return mu*vals - 1.0

best = None
for trial in range(80):
    x0 = np.append(rng.normal(0, 2, size=24), rng.normal(0, 2))
    try:
        r = least_squares(resid, x0, method='lm', max_nfev=4000)
    except Exception:
        continue
    cost = float(np.sqrt(2*r.cost))
    if best is None or cost < best[0]:
        best = (cost, r.x.copy())
    if cost < 1e-10:
        break

print(f"best residual norm over trials: {best[0]:.3e}")
print("best params:")
for name, v in zip(pn + ['mu'], best[1]):
    print(f"   {name} = {v:.10f}")
if best[0] < 1e-8:
    print("\n*** CANDIDATE SOLUTION FOUND -- rationalize and verify exactly ***")
    vals = np.array([ratio(best[1][:24], p) for p in pts])
    print("constant value ~", vals.mean())
else:
    print("\nNo solution found numerically (residual floor above tolerance).")
