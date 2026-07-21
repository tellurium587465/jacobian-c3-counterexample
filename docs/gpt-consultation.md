# GPT-5.6 adversarial consultation

This project was carried out by **Claude (Opus 4.8)** and deliberately stress-tested
by **GPT-5.6** acting as an *adversarial reviewer*. The dialogue materially changed
the results: it caught two real errors, corrected an over-claim of novelty, and
supplied a cleaner construction. This file records what happened, honestly.

## What Claude proposed
* Independent symbolic verification of Alpoge's map: `det(DF) = -2`; the three-point
  collision over `(-1/4,0,0)`; generic fiber size 3.
* A "resolvent cubic" `Q(x) = A x^3 + (4-3bc)x - 2c` for the `x`-coordinates, with
  `A = 27a^2c^2 - 18abc + 16a + b^3c - b^2`, plus rational formulas `y(x)`, `z(x)`.
* An 8-parameter deformation that stays Keller — found to collapse to the original
  under diagonal scaling.
* 24 new rational triple-collisions via a discriminant-square condition.

## What GPT-5.6 corrected (all re-verified by Claude in `verify.py`)
1. **Use `t = y + 1/x`, not `x`.** The globally valid fiber model is
   `P(T) = c T^3 - 2 T^2 + b T - 2a`, with `P'(t) = 2/x`, `Disc_T(P) = -4A`, and an
   explicit reconstruction from each simple root. Claude verified `P(t)=0`,
   `P'(t)=2/x`, and `Disc=-4A` symbolically.
2. **The `y(x)` formula is only *generically* valid.** Its denominator can hit `0/0`;
   then one `x`-root carries two preimages. GPT's witness `(a,b,c)=(0,8/9,1)`,
   `x=9/4` (a double root of `Q`) was confirmed: the fiber has **three distinct
   points**, two sharing `x = 9/4`, while `A ≠ 0`. Hence the squared factor of
   `disc_x Q` is a **projection artifact**; the true branch locus is `A = 0`.
3. **"`x1+x2+x3 = 0` on every fiber" needs a qualifier** — it holds when there are
   three *finite* sheets; at `A = 0` a sheet escapes to infinity and `Q` drops
   degree. Adopted.
4. **Terminology.** "resolvent cubic" has a specific classical meaning; use
   "fiber cubic / x-eliminant". Adopted.
5. **Novelty, honestly.** GPT's literature check (corroborated by Claude fetching the
   *Secret Blogging Seminar* post) showed the cubic reduction, generic degree 3, the
   discriminant `A`, and the weighted grading were **already public** within a day of
   the announcement. So this repo does **not** claim the mechanism; it verifies,
   caveats, and extends it. The over-claim was removed from the README and docs.
6. **A cleaner infinite family.** GPT supplied the square-condition-free
   parametrization `P(T) = (2/(p+q)) T(T-p)(T-q) ⇒ (a,b,c) = (0, 2pq/(p+q),
   2/(p+q))`. Claude verified it and made it the primary generator
   (`collisions.py:family`), producing 308 targets in the default box.
7. **`n = 2`.** GPT gave the sharp safe framing now in `mechanism.md` §6
   (`d>=3` for any plane counterexample; the Moskowicz 2024 preprint cited as a
   preprint claim, not settled).

## Takeaway
The adversarial pass improved correctness (fixed a false global formula and a
mis-stated invariant), improved honesty (removed a novelty over-claim), and improved
the mathematics (a cleaner family). Every adopted claim is machine-checked in
`src/verify.py` — Claude took nothing on GPT's word, and GPT took nothing on Claude's.

*Raw prompt and reply are omitted for length; the substantive content is captured
above and encoded as executable checks.*
