# Raw revision 3: mass and path review

Date: 2026-11-04.
Role: new critical agent B, with a separate context.
The agent read the complete final manuscript.
Its detailed review covers the statement, Appendix B, Appendix C, Section 5, and the initial-state quantifiers.

Reviewed content/raw.md SHA-256:
`0c2661067d9b9914376e1ffba936ef3088bea332d1be3bf0c96d423bd8d694a9`.

Verdict: pass within the stated scope.
No blocking gap was found in the assigned arguments.
No repair was required.
This is a same-family AI review, not a human or outside-family audit.
The [complete revision](../RAW_PROOF_v3.md) is preserved as a new record.

## Sampling

The cancellation in Lemma B.1 holds for every \(1\le m\le a\).
It uses symmetry and an average over all samples.
It does not require a fixed set of labels to be Markov.
The argument includes \(L=3\).

## Occupation bound

The pair generator, edge conductances, Poisson equation sign, and bound \(\operatorname{osc}(v)\le Lk/q\) are correct.
The flux construction is cyclic and the even averaging preserves its equation.
Conditional optional sampling applies because the state space and stopping horizons are finite.
It gives Proposition B.2 with its exact stated constants.

## Mass semigroups

Compactness and point-start path convergence give Lemma 5.1, including sequences with \(t_N\to0\).
The two sampling errors have the stated constants.
Polynomial density then gives uniform convergence for every continuous mass test.
Both population orders use the same time acceleration.

## Path transfer

Equation (C.3), a finite set of separating tests, and compactness give the metric stopping-time bound.
The projected-jump bound excludes discontinuous \(J_1\) limits.
Microscopic conditioning gives the finite-dimensional recursion.
No projected Markov property is used.
The path-transfer argument does not require target path continuity as an extra assumption.

## Initial states and scope limit

Section 5 uses only convergence of the initial empirical measures.
It therefore covers all initial states in Theorem 1, including vanishing normalized masses and coincident limiting positions.

This review uses Proposition 3.1 and the stated conservative, strongly continuous Feller target semigroup as inputs.
The harmonic correction, collision passage, form calculation, and continuum uniqueness have separate assigned reviews.

## Citation verification limit

This agent did not verify the precise wording or page numbers of the cited Aldous PDF.
The web tool could not extract its scanned text, and a download was not completed.
The separate [probability and citation check](RAW_v3_PROBABILITY.md) checked the relevant page images and the exact criterion.
No source file was changed by this reviewer.
