# Raw revision 3: additional probability and citation check

Date: 2026-11-04.
Role: new critical agent D, with a separate context.
The detailed scope is Section 5, Appendices B–C, and their input interface with Proposition 3.1.

Reviewed content/raw.md SHA-256:
`0c2661067d9b9914376e1ffba936ef3088bea332d1be3bf0c96d423bd8d694a9`.

Verdict: pass within the stated scope.
No mathematical gap was found in the assigned arguments.
No repair was required.
This is a same-family AI review, not a human or outside-family audit.
The [complete revision](../RAW_PROOF_v3.md) is preserved as a new record.

## Checks

Proposition 3.1 covers every convergent sequence of initial points.
Compactness and continuity therefore give the uniform estimate in Lemma 5.1, including time zero.

For each adjacent label pair, the sampling terms that contain exactly one label cancel.
Both population orders use the same \(N^2,d_N,L_N\).
The pair equation satisfies \(\mathcal Hv=b-\beta\), with \(\beta=2k/(L+1/d)\).
Its solution has \(\operatorname{osc}(v)\le Lk/q\).
Conditional optional sampling proves Proposition B.2.

Estimate (C.3) is uniform over bounded microscopic stopping times and deterministic lags \(h\le\delta\).
The reviewer read the page images of [Aldous, *Weak Convergence and the General Theory of Processes*](https://www.stat.berkeley.edu/~aldous/Papers/weak-gtp.pdf).
Condition (4.2), on printed page 25, uses deterministic lags after bounded stopping times.
Theorem (4.4)(ii), on printed page 26, gives tightness when the one-time marginals are tight.
The next paragraph states the extension to Polish state spaces.
Compactness supplies the required marginal tightness here.
Thus the criterion used in Appendix C has the needed form.

Under \(J_1\) convergence, each limit jump is bounded by \(j_N\) plus twice the uniform approximation error.
Equation (C.2) therefore gives continuous limits.
The recursion in (C.4) identifies all finite-dimensional laws.
It does not require the projected process to be Markov.

The initial-state restrictions in Theorem 1 are sufficient.
The Section 5 estimates also apply to every deterministic initial sequence whose empirical measures converge.
The frozen theorem retains its narrower stated scope.

## Scope limit

This review checks the probability argument from Proposition 3.1 and the supplied target semigroup onward.
It does not independently prove Proposition 3.1 or the target construction.
Those arguments have separate assigned reviews.
No source file was changed by this reviewer.
