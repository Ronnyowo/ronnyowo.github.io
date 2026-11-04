# Digested

This guide explains the current AI proof.
It does not replace the exact statement or the source proofs.
The paper draft is planned for a later stage.

## 1. The theorem

Let \(\mathbb T=\mathbb R/\mathbb Z\).
The microscopic system has \(N\) particles on the cycle \(\mathbb Z/L_N\mathbb Z\).
Its accelerated generator is
\[
\mathcal L_NF(\eta)=\frac{N^2}{d_N}
\sum_x\sum_{y=x\pm1}\eta_x(d_N+\eta_y)
\bigl[F(\eta-\delta_x+\delta_y)-F(\eta)\bigr].
\]
Assume
\[
N/L_N\to\rho>0,\qquad Nd_N\to\Theta>0,
\qquad \alpha=\Theta/\rho.
\]
Fix any integer \(k\ge1\).
Take deterministic initial configurations with at most \(k\) occupied sites.
Distinct occupied sites must have circular lattice distance at least two.
Assume that their empirical mass measures converge weakly to \(\mu_0\).

The claimed conclusion is
\[
\operatorname{Law}(\mu_N(\cdot))
\Longrightarrow Q_{\mu_0}
\quad\text{in }D([0,\infty),\mathcal P(\mathbb T)).
\]
The state topology is weak convergence of measures.
The path topology is Skorokhod \(J_1\).
The target law has continuous paths.

Read the [exact statement](../records/STATEMENT.md) for the target forms and every quantifier.

## 2. The limit

The limit is the mass process associated with the Le Jan–Raimond Brownian sticky flow.
It is a circle version of a Howitt–Warren process in the uniform characteristic-measure case.
The mass evolves by
\[
\mu_t(A)=\int_{\mathbb T}K_{0,t}(x,A)\,\mu_0(dx).
\]
All initial mass uses the same random kernel flow.
A single sampled trajectory is Brownian motion.
Finite samples have sticky interactions at collisions.
The full family of split coefficients specifies the target.
Pairwise stickiness alone does not specify that family.

The one-point generator is \(\rho^2\partial_{xx}\).
After the time change that gives variance rate one, the characteristic measure is
\[
\nu(dq)=\frac{\alpha}{2}\,dq,\qquad 0\le q\le1.
\]
This normalization is derived in Part III.5 of the [main proof](../raw/full-mass/).

The continuum mass process is already in the literature.
See Le Jan–Raimond, Proposition 3.4(b), and Le Jan–Lemaire, Proposition 7.
The references appear below.

## 3. The proof dependencies

The full theorem is C0008.
It uses three auxiliary results.
The auxiliary results do not depend on each other.

| Record | What it supplies | Read |
| --- | --- | --- |
| C0005 | Harmonic corrections, split coefficients, trace estimates, and covariance bounds | [Correctors](../raw/correctors/) |
| C0006 | A conditional occupation bound for small positive pair distances | [Positive layers](../raw/positive-layers/) |
| C0002 | Transfer from uniform resolvents to full path convergence | [Path transfer](../raw/path-transfer/) |
| C0008 | The complete argument using those three results | [Full mass proof](../raw/full-mass/) |

## 4. The microscopic problem

First fix an auxiliary particle number \(n\).
Keep the acceleration \(N^2/d_N\).
Let \(N\) tend to infinity while \(n\) stays fixed.
Repeat the argument for every finite \(n\).

The proof uses a reference chain \(Q\).
This chain makes one independent jump, then lets pure inclusion relax.
Its number of stacks cannot increase.
This fact gives a bound on its total occupation of near-collision states.

For a continuous test \(f\) that is affine in each coordinate-order chamber, define
\[
H_f=f+\psi_f,\qquad
\psi_f(z)=\mathbb E_z\int_0^\infty Qf(Y_s)\,ds.
\]
The occupation bound makes \(\psi_f\) bounded.
The construction gives \(QH_f=0\).
Thus a small correction to the test cancels the large leading boundary drift.
See [C0005, Sections 1–2](../raw/correctors/).

## 5. The part that survives the scaling

The actual auxiliary trace generator has the expansion
\[
T_d=Q+dB+O(d^2).
\]
The proof supplies a uniform remainder bound for the corrected tests.
Since \(QH_f=0\), the first surviving action is \(dBH_f\).
The scaling gives
\[
\frac{N^2d_N}{L_N}\to\rho^2\alpha,
\qquad
\frac{N^2d_N^2}{L_N}\to0.
\]
The first term therefore remains in the limit.
The remainder tends to zero.

For every collision block \(B\), and every nonempty proper subset \(A\subset B\), the oriented split coefficient is
\[
\rho^2\alpha
\frac{(|A|-1)!(|B\setminus A|-1)!}{(|B|-1)!}.
\]
Detailed balance gives the complete-stack calculation.
Quantitative localization extends it to separated blocks.
The proof also controls corrected coordinate covariances.
See [C0005, Sections 3–6](../raw/correctors/).

## 6. Passing collisions to the limit

Path convergence alone does not give convergence of equality indicators.
The proof bounds time at small positive separations.
It retains time at exact equality.

An explicit pair Poisson equation gives the conditional occupation estimate in C0006.
Factorial averaging extends it to every fixed auxiliary order.
This estimate and the corrector bounds identify every collision stratum.
The proof also removes the trace clock and controls the deleted excursions.
See [C0008, Parts I–II](../raw/full-mass/).

Part III identifies the exact sticky target.
It checks the form boundary coefficients, every deterministic starting point, and circle localization.
It uses the continuum uniqueness theorem of Howitt and Warren.
The form defines the target; the convergence proof does not use Mosco convergence.

## 7. Recovering the full mass law

Uniform sampling without replacement gives an exact semigroup intertwining.
It connects the full inclusion process to every fixed auxiliary order.
For a degree-\(n\) mass polynomial, replacement of the sampling law has error at most
\[
\frac{n(n-1)}{N}\|f\|_\infty.
\]
Compactness gives uniform auxiliary semigroup convergence over starting tuples.
The sampling identity gives uniform convergence for mass polynomials.
Stone–Weierstrass then gives every continuous mass test.

The resulting resolvent estimate is
\[
\sup_{\eta\in\Omega_N}
\left|
\mathcal R_{N,\lambda}(G\circ\Phi_N)(\eta)
-(\mathsf R_\lambda G)(\Phi_N(\eta))
\right|\to0.
\]
This holds for every \(\lambda>0\) and every \(G\in C(\mathcal P(\mathbb T))\).
The supremum is over the entire microscopic state space.
It is proved in C0008, equation (IV.2.9).

The target mass process has a fourth-moment continuity bound.
Each microscopic jump moves the empirical measure by at most \(1/(NL_N)\) in Wasserstein distance.
These facts verify the remaining hypotheses of C0002.
The path-transfer theorem then gives the full mass path law.
See [C0008, Part IV](../raw/full-mass/).

## 8. Relation to Kim–Landim

Kim–Landim use microscopic excursion estimates, trace control, uniform resolvents, tightness, and identification.
Their boundary argument uses a positive probability of reaching a configuration with fewer stacks.
Their Theorem 1.9 concerns projected condensate positions.
The supplied manuscript assumes \(d_NN^3\log N\to0\).

Our scaling does not satisfy that assumption.
The first-order splitting effect must be retained.
The new proof also recovers the full mass law from every fixed auxiliary order.
The main additional work is the all-order collision calculation and its localization.
The final resolvent-to-path transfer has the same general role.

The Kim–Landim manuscript was supplied privately for the campaign.
It is not redistributed here.

## 9. Review order

Review the proof in this order:

1. C0005: correction construction and separated-block localization.
2. C0008, Parts I–II: accelerated excursion errors and collision occupation.
3. C0008, Part III: normalization and uniqueness from every starting point.
4. C0008, Part IV.2, and C0002: full-state resolvents and path transfer.
5. C0008, Parts IV.3–IV.4: continuity and the initial-data quantifiers.

The source campaign records these results as promoted.
No outside-family audit is recorded.
See the [review records](../review/).

## References

- Le Jan and Raimond, [Sticky flows on the circle](https://arxiv.org/abs/math/0211387). Theorem 3.3 and Proposition 3.4.
- Le Jan and Lemaire, [Products of Beta matrices and sticky flows](https://arxiv.org/abs/math/0307106). Propositions 6–7.
- Howitt and Warren, [Consistent families of Brownian motions and stochastic flows of kernels](https://arxiv.org/abs/math/0611292). Definition 2.1, Theorem 2.1, and Proposition 8.1.
- Schertzer, Sun and Swart, [Stochastic flows in the Brownian web and net](https://arxiv.org/abs/1011.3895). Sections 2.2–2.3.
