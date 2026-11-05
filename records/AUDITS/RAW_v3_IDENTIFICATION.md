# Raw revision 3: collision and target review

Date: 2026-11-04.
Role: new critical agent C, with a separate context.
The agent read the complete final manuscript.
Its detailed review covers Sections 3–4 and their use of the other results.

Reviewed content/raw.md SHA-256:
`0c2661067d9b9914376e1ffba936ef3088bea332d1be3bf0c96d423bd8d694a9`.

Verdict: pass within the stated scope.
No blocking gap was found in Sections 3–4.
No repair was required.
This is a same-family AI review, not a human or outside-family audit.
The [complete revision](../RAW_PROOF_v3.md) is preserved as a new record.

## Collision indicators

The positive-layer bound (II.2) controls the mismatch when discrete coordinates are unequal but their limit coordinates are equal.
When limit coordinates are unequal, the discrete equality indicator is eventually zero.
These two bounds prove (II.7).
For unequal coordinates, uniform path convergence also preserves their strict order eventually.
A finite union over pairs therefore gives the weak-order-cell passage.

## Stopped martingales

The good-radius construction gives convergent stopped paths.
The corrected terminal values and stopped drift integrals are uniformly bounded.
They therefore permit passage of the Dynkin and product martingale identities.
Continuous cylinder tests and the monotone-class theorem give the conditional identities.
The smaller-ball argument permits stopping-time entry.
The positive distances between the nested boundaries prevent exits from accumulating in finite time.
This supports (II.10)–(II.11).

## Form calculation and deterministic starts

Ambient mollification gives the required tangential derivatives on every partition stratum.
Each refined-stratum face gives the stated flux.
Its surface factor \(\sqrt2\) cancels the normal factor \(1/\sqrt2\).
The ratio
\[
\frac{p_\alpha(\sigma)}{p_\alpha(\pi)}
=\alpha\frac{(|A|-1)!(|C|-1)!}{(|A|+|C|-1)!}
\]
gives every oriented splitting coefficient.

The strong Feller property and full support extend the operator identity from almost every point to every deterministic start.
The versioned primary source supplies the required construction: [Le Jan–Raimond, equation (3.6) and Theorem 3.3](https://arxiv.org/pdf/math/0211387v1).

## Parameters and circle uniqueness

The completed parameters satisfy the consistency recurrence at positive indices, on both axes, and at \((0,0)\).
Their drift is zero.
The time change gives the exact bracket and splitting rates required by [Howitt–Warren, Definition 2.1, equations (2.7) and (2.9), and Theorem 2.1](https://arxiv.org/pdf/math/0611292v2).
Proposition 8.1 gives the Feller laws used to form a Borel continuation family.
Stopped real uniqueness and the finite nested-chart construction give circle uniqueness.

## Limit of this review

Proposition 3.1 is proved through the estimates and identification on the final page.
It is not used as an assumed convergence theorem.
The agent checked the compatibility of the remaining sections.
It did not independently derive every estimate in Appendices A–C.
Those estimates have separate assigned reviews.
This record does not claim that one agent verified the full manuscript independently.
