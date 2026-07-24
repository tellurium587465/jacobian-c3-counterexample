"""
local_models.py -- session 6 seed: Reidemeister-Schreier local models
for the source-side H1 constraint (round-17 ranked move 3).

For a capable cusp with full nonabelian local monodromy, compute the
first homology of the index-5 cover of the local knot-group complement
(= the local piece of the affine source near the escaping cusp), both
unbranched and with the section-meridian disk filled ("affine model").

Method: pure exponent arithmetic.  G = <u, v | u^m = v^n> (torus-knot
cusp), rho: G -> S5 with image D5 (resp. F20), subgroup
H = rho^{-1}(Stab(v0)) of index 5 where v0 = the meridian's fixed
point (the section sheet).  Schreier generators on the 5 cosets with a
v-transversal tree; abelianize the relator conjugates; Smith normal
form.  The affine model adds the rewritten meridian row (the section
crosses E, so its meridian lift bounds a disk in the affine chart).

RESULTS (machine-verified below):
  * D5 at a (2,5)-cusp : H1(unbranched) = Z^3,  affine model = Z^2.
  * F20 at a (4,5)-cusp: H1(unbranched) = Z^4,  affine model = Z^3.

INTERPRETATION.  Every active cusp contributes local rank 2 (D5) resp.
3 (F20) to the homology of the affine source cover.  Globally
H1(C^2 \ Etilde) = Z (irreducible curve complement, round 17), so the
global relations must collapse ~ 2*(4s) = 8s (resp. 12s) local ranks to
a single Z: the quantitative content of the "special position"
requirement.  The next step of the program is the global
Zariski-van Kampen / Fox computation with the monochromatic-section
constraint imposed, to decide whether this collapse is possible at all.
"""
from sympy.combinatorics import Permutation
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def local_model(m, n, pu, pv, mu_word, name):
    """H1 of the index-5 local cover for G = <u,v | u^m = v^n>."""
    perms = {'u': pu, 'v': pv}
    mu = Permutation([], size=5)
    for (letter, e) in mu_word:
        mu = mu * perms[letter]**e
    fix = [i for i in range(5) if mu(i) == i]
    assert len(fix) == 1, (name, "meridian must fix exactly one sheet")
    v0 = fix[0]
    cols = {}
    for i in range(5):
        for letter in 'uv':
            cols[(i, letter)] = len(cols)
    order = [(v0 + k) % 5 for k in range(5)]
    tree = [(order[k], 'v') for k in range(4)]

    def rewrite(word, start):
        row = [0] * len(cols)
        st = start
        for (letter, e) in word:
            p = perms[letter]
            for _ in range(abs(e)):
                if e > 0:
                    row[cols[(st, letter)]] += 1
                    st = p(st)
                else:
                    st = (p**-1)(st)
                    row[cols[(st, letter)]] -= 1
        return row, st

    rows = []
    for (i, letter) in tree:
        r = [0] * len(cols)
        r[cols[(i, letter)]] = 1
        rows.append(r)
    relator = [('u', m), ('v', -n)]
    for i in range(5):
        r, st = rewrite(relator, i)
        assert st == i
        rows.append(r)

    def h1(extra=()):
        M = Matrix(rows + list(extra))
        S = smith_normal_form(M, domain=ZZ)
        diag = [S[i, i] for i in range(min(S.shape))]
        nz = [abs(d) for d in diag if d != 0]
        return len(cols) - len(nz), [d for d in nz if d > 1]

    rk_u, tor_u = h1()
    r_mu, st = rewrite(mu_word, v0)
    assert st == v0
    rk_a, tor_a = h1(extra=(r_mu,))
    print(f"  {name}: H1(unbranched) = Z^{rk_u}{tor_u or ''}  |  "
          f"affine model = Z^{rk_a}{tor_a or ''}")
    return rk_u, tor_u, rk_a, tor_a


def main():
    c5 = Permutation([1, 2, 3, 4, 0])
    refl = Permutation([0, 4, 3, 2, 1])
    four = Permutation([0, 2, 4, 1, 3])

    print("=== Local RS models at active cusps (index-5 subgroup H1) ===")
    r1 = local_model(2, 5, refl, c5, [('u', 1), ('v', -2)],
                     "D5  @ (2,5)-cusp")
    assert (r1[0], r1[2]) == (3, 2) and not r1[1] and not r1[3]
    r2 = local_model(4, 5, four, c5, [('u', 1), ('v', -1)],
                     "F20 @ (4,5)-cusp")
    assert (r2[0], r2[2]) == (4, 3) and not r2[1] and not r2[3]
    print("  => each active cusp adds local rank 2 (D5) / 3 (F20);")
    print("     global H1 = Z demands collapsing ~8s (D5) / 12s (F20)")
    print("     ranks -- the quantitative 'special position' burden.")


if __name__ == '__main__':
    main()
