"""
collisions.py
=============

Explicit *rational triple-collisions* of Alpoge's map: distinct rational points
P1, P2, P3 in Q^3 with F(P1) = F(P2) = F(P3).  Alpoge published exactly one (over
(-1/4, 0, 0)); here is a clean two-parameter rational family, plus a scan.

The construction (a square-condition-free family)
-------------------------------------------------
Over (a,b,c) the finite preimages are the roots t of  P(T) = c T^3 - 2 T^2 + b T - 2a
(the cubic t-model, see counterexample.py).  Prescribe the three roots directly:
choose rationals p, q with  p q (p-q)(p+q) != 0  and set

    P(T) = (2/(p+q)) * T * (T - p) * (T - q).

Matching coefficients forces the target to be

    (a, b, c) = ( 0,  2pq/(p+q),  2/(p+q) ),

with NO discriminant-square side condition (P is split by construction).  The
three preimages come from reconstruct(.) at t in {0, p, q}.  (This family and the
underlying t-model are due to the public analysis / the GPT-5.6 collaboration
documented in docs/gpt-consultation.md; the verification here is ours.)
"""
import sympy as sp
from counterexample import F_map, apply, reconstruct, fiber_cubic_P, T


def collision_pq(p, q):
    """The rational triple-collision for parameters (p, q).  Returns dict or None."""
    p, q = sp.Rational(p), sp.Rational(q)
    if p*q*(p - q)*(p + q) == 0:
        return None
    a0 = sp.Integer(0)
    b0 = 2*p*q/(p + q)
    c0 = sp.Rational(2)/(p + q)
    pts = [reconstruct(a0, b0, c0, tau) for tau in (sp.Integer(0), p, q)]
    if len(set(pts)) < 3:
        return None
    F = F_map()
    if all(apply(F, P) == (a0, b0, c0) for P in pts):
        return {"pq": (p, q), "target": (a0, b0, c0), "preimages": pts}
    return None


def family(pmax=6, qmax=6):
    """Members of the square-free family over a small (p,q) box (de-duplicated)."""
    seen, out = set(), []
    for pn in range(-pmax, pmax + 1):
        for pd in (1, 2, 3):
            for qn in range(-qmax, qmax + 1):
                for qd in (1, 2, 3):
                    hit = collision_pq(sp.Rational(pn, pd), sp.Rational(qn, qd))
                    if hit and tuple(hit["target"]) not in seen:
                        seen.add(tuple(hit["target"]))
                        out.append(hit)
    return out


# ---- a second, independent generator (general targets, not just a=0) -------

def collisions_general(rmax=4, smax=4, cnums=range(1, 7), cdens=(1, 2, 3, 4)):
    """Scan targets whose x-eliminant has three rational roots {r,s,-(r+s)}.

    This reaches collisions with a != 0 (complementary to the a=0 family)."""
    from counterexample import x_eliminant_Q, x
    seen, out = set(), []
    for r in range(1, rmax + 1):
        for s in range(1, smax + 1):
            r_, s_ = sp.Integer(r), sp.Integer(s)
            x1, x2, x3 = r_, s_, -(r_ + s_)
            if len({x1, x2, x3}) < 3:
                continue
            e2 = x1*x2 + x1*x3 + x2*x3
            e3 = x1*x2*x3
            for cn in cnums:
                for cd in cdens:
                    cv = sp.Rational(cn, cd)
                    if e3 == 0:
                        continue
                    A = 2*cv/e3
                    bv = (4 - A*e2)/(3*cv)
                    aa = sp.symbols('aa')
                    quad = (27*aa**2*cv**2 - 18*aa*bv*cv + 16*aa
                            + bv**3*cv - bv**2 - A)
                    for ar in sp.solve(sp.Eq(quad, 0), aa):
                        if not ar.is_rational:
                            continue
                        tgt = (sp.Rational(ar), bv, cv)
                        if tgt in seen:
                            continue
                        fb = fiber(*tgt)
                        rat = [P for P in fb if all(v.is_rational for v in P)]
                        if len(rat) >= 3:
                            seen.add(tgt)
                            F = F_map()
                            if all(apply(F, P) == tgt for P in rat[:3]):
                                out.append({"target": tgt, "preimages": rat[:3]})
    return out


# import fiber lazily to avoid a cycle at module import time
from counterexample import fiber  # noqa: E402


if __name__ == "__main__":
    fam = family()
    print(f"[square-free a=0 family]  {len(fam)} distinct targets, e.g.:")
    for hit in fam[:6]:
        p, q = hit["pq"]
        print(f"  (p,q)=({p},{q}) -> target {tuple(hit['target'])}")
        for P in hit["preimages"]:
            print(f"       {P}")
    gen = collisions_general()
    print(f"\n[general a!=0 scan]  {len(gen)} distinct targets, e.g.:")
    for hit in gen[:4]:
        print(f"  target {tuple(hit['target'])}")
        for P in hit["preimages"]:
            print(f"       {P}")
