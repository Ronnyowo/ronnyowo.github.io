# Raw revision 3: corrector and trace review

Date: 2026-11-04.
Role: new critical agent A, with a separate context.
The agent read the complete final manuscript.
Its detailed review covers Appendix A and Sections 2–3.

Reviewed content/raw.md SHA-256:
`0c2661067d9b9914376e1ffba936ef3088bea332d1be3bf0c96d423bd8d694a9`.

Verdict: pass within the stated scope.
No mathematical gap was found in the assigned arguments.
No repair was required.
This is a same-family AI review, not a human or outside-family audit.
The [complete revision](../RAW_PROOF_v3.md) is preserved as a new record.

## Detailed checks

### Absorption and harmonic correction

In A.4–A.5, the identity \(IV\ge4\) off the stable set gives the absorption bound.
The near-set occupation bound gives absolute convergence of the correction integral.
The bounded semigroup identity for the correction gives \(QH_f=0\).
The argument does not apply a bounded-function domain assertion to the unbounded function \(H_f\).

### Perturbed excursions

In A.6, the independent-event count has the stated geometric tail.
The visited-support bound controls the complete excursion, including its returning jump.
These bounds justify the calculation with unbounded boundary data.
The Neumann condition follows from \(4ndc_n\le1/2\).
The two inverse identities have the correct operator order.
The trace expansion is proved before it is used in A.7.

### Full-block coefficients

In A.7, the finite-cycle labelled weights satisfy detailed balance.
Their leading terms are \(d(m-1)!\) for a full stack and \(d^2(|A|-1)!(m-|A|-1)!\) for two stacks.
Their ratio gives the stated factorial coefficient.
Weighted symmetry of \(M\) justifies the second equality in (A.19).
Each split orientation is counted once.
No binomial factor is missing.

### Qualitative localization

In A.8, the gradient change across a chamber face gives the block decomposition (A.20).
The signed \(B\)-row has the stated finite support.
The split block merges almost surely.
The later full-stack center meetings also occur almost surely.
The total coupling radius is therefore finite almost surely.
There are finitely many local initial types, which gives the uniform tail (A.22).

The optional-sampling argument uses the bounded harmonic difference \(\Delta\).
It needs no finite mean coupling time.
The common-filtration clock construction preserves both marginal generators.
The local factorization of \(BW\) follows from the vanishing residual of each unaffected full block.
It does not use the estimate that the coupling replaces.

### Covariances

The unsplit types in A.8 include the coordinate shifts used in A.9.
They give the corrected increments needed for (A.27).
The perturbed-excursion error is bounded by a second moment on \(\{J\ge1\}\).
This gives the uniform \(O(d)\) estimate in (A.28).
The jump-moment bound gives absolute convergence of the covariance series.

### Circle comparison and time acceleration

In Section 2.4, both excursion counts reach the stated threshold before the line-circle coupling fails.
The polynomial tail factors are controlled because \(m\le L/2\), and hence \((m+1)^p\le C_pL^p\).
This gives the factors in (I.4.1), (I.4.2), and (I.4.5).
After acceleration, \(qr^m\to0\) and \(qd^2/L\to0\).
Additive constants in the test cancel from every increment.

The absorption and lost-time estimates include the initial absorption interval.
They count complete excursions initiated before the horizon, including those that return later.
The inverse-clock convention in (I.3.6) agrees with the returning state.
The nested-chart estimate includes exit overshoots.
The argument makes no stopping-time assertion about \(A(\tau)\) in a trace filtration.

### Collision passage

The positive-layer bound transfers to trace time without a trace-filtration stopping-time assumption.
The qualitative modulus suffices: fix \(\varepsilon>0\), let \(N\to\infty\), then let \(\varepsilon\downarrow0\).
The layer bound controls equality-indicator mismatch in (II.7), and then the complete weak-order cell.
The good-radius construction gives convergent exit times.
Bounded stopped values and drift integrals justify the conditional martingale passage.

## Dependency check and limit of this review

No circular dependence was found.
In particular, A.8 does not use microscopic convergence or continuum uniqueness.
The agent read Sections 4–5 and Appendices B–C for compatibility.
It did not derive all their proofs or check all their external references.
The other final reviews cover those assigned parts.
This record does not claim that one agent verified the full manuscript independently.
