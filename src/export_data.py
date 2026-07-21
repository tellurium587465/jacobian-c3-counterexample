"""Export verified rational-triple-collision tables (JSON + Markdown)."""
import json
import sympy as sp
from collisions import family, collisions_general
from counterexample import a, b, c


def _rows(hits, with_pq=False):
    rows = []
    for hit in hits:
        row = {"target": [str(v) for v in hit["target"]],
               "preimages": [[str(v) for v in P] for P in hit["preimages"]]}
        if with_pq and "pq" in hit:
            row["pq"] = [str(v) for v in hit["pq"]]
        rows.append(row)
    return rows


def _md(rows, title, note):
    L = [f"# {title}", "", note, "",
         "| # | target (a,b,c) | preimage 1 | preimage 2 | preimage 3 |",
         "|---|---|---|---|---|"]
    for i, r in enumerate(rows, 1):
        t = "(" + ", ".join(r["target"]) + ")"
        ps = ["(" + ", ".join(p) + ")" for p in r["preimages"]]
        L.append(f"| {i} | {t} | {ps[0]} | {ps[1]} | {ps[2]} |")
    return "\n".join(L) + "\n"


if __name__ == "__main__":
    fam = _rows(family(), with_pq=True)
    gen = _rows(collisions_general())

    with open("../data/collisions_family_a0.json", "w") as fh:
        json.dump(fam, fh, indent=2)
    with open("../data/collisions_general.json", "w") as fh:
        json.dump(gen, fh, indent=2)

    with open("../data/collisions_family_a0.md", "w") as fh:
        fh.write(_md(fam[:60],
                     "Square-free rational triple-collision family (a = 0 slice)",
                     "Parametrized by (p,q): target = (0, 2pq/(p+q), 2/(p+q)); preimages "
                     "reconstructed at t in {0,p,q}. All entries verified by src/verify.py. "
                     f"({len(fam)} distinct targets in the default (p,q) box; showing 60.)"))
    with open("../data/collisions_general.md", "w") as fh:
        fh.write(_md(gen,
                     "General rational triple-collisions (a != 0)",
                     "Targets whose x-eliminant splits over Q with roots {r,s,-(r+s)}. "
                     "All entries verified by src/verify.py."))

    # branch-locus summary
    A = 27*a**2*c**2 - 18*a*b*c + 16*a + b**3*c - b**2
    print(f"square-free family: {len(fam)} targets  -> data/collisions_family_a0.*")
    print(f"general scan:      {len(gen)} targets  -> data/collisions_general.*")
    print("\nGenuine branch locus (two sheets meet):  A = 0, where")
    print("  A =", A, " = -Disc_T(P)/4")
    print("The x-projection introduces the spurious extra factor (27ac^2-9bc+8).")
