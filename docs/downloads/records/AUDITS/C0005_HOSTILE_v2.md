# C0005 hostile audit — canonical v2

**Verdict: PASS, restricted to the exact auxiliary theorem in the input contract and proof identified below.** All six conclusions and the one-label convention withstand this audit. No counterexample or theorem-strength missing lemma was identified. This is an audit verdict, not promotion, a proof-blind reconstruction, validation of another candidate, or a proof of STATEMENT-v1.

The mathematical status of this report's supplementary calculations is at most **self-audited**. They are checks of the supplied argument, not separately promoted dependencies. This report invokes no campaign dependency and no literature premise.

## 1. Complete input manifest and exposure record

Workspace: `[private workspace]`.

| Authorized input | Pinned version | Verified SHA-256 |
|---|---|---|
| `STATEMENT.md` | v1 | `ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97` |
| `CANDIDATES/C0005_harmonic_correctors/CONTRACT_v2.md` | v2 | `0a0130d01e482dbe546a19248b1ca67180aa373643dace7a87abc5cff8eb8cec` |
| `CANDIDATES/C0005_harmonic_correctors/PROOF_v2.md` | v2 | `68a9fec530428b3fd61e9f3bef1564e3ad3bcbd905d0cf0b51801a58bd6fc5ef` |
| `AUDITS/CHECKLIST_AC005.md` | AC-005, including AC-001 through AC-005 | `d328652a06ff5ef7fa9ae64a70011a3060b32e80cc23b0afbce4cf1fca97c170` |

All four hashes matched before the mathematical audit. The complete contents of these four files were read; the proof was reread in two bounded text ranges after the first combined tool display was truncated. No other campaign file, inventory, old version, provenance file, author manifest, leakage report, audit, reconstruction, route, registry, FAILED/PROVED record, or author defense was read. Mentions of other files inside the authorized proof and checklist were encountered only as part of those authorized inputs; none was followed or used as a premise.

No web or literature search, external source, mathematical program, simulation, inline calculation program, or subagent was used. Tools performed text reads, SHA-256 checks, and creation/freezing of this report. In particular, the target references mentioned in STATEMENT-v1 were not consulted or used: target identification and convergence are expressly outside this auxiliary contract.

The audit instruction supplies the role and access restrictions; the four entries above are the complete mathematical input manifest. There are **no promoted dependencies**.

## 2. Scope of the verdict

The contract concerns the labelled chains on the line lattice with generators \(I\), \(R\), their absorption operators, the leading trace \(Q\), the perturbed trace \(T_d\), and the canonical correctors of chamber-affine functions. It claims uniform statements for every fixed order \(n\), every lattice tuple allowed by the relevant conclusion, every partition and oriented label subset, every allowed test function, and every stated separation and perturbation parameter.

It does **not** claim the mass-process path-law convergence in STATEMENT-v1, a torus corrector, limiting collision occupation, a determining martingale core, target uniqueness, deletion consistency, or microscopic-to-continuum clock transfer. The checks below distinguish these unclaimed conclusions from checks actually discharged for C0005. In particular, no full-mass checklist item is silently passed because the auxiliary theorem passes.

## 3. Conclusion 1: pure absorption, trace, occupation, and displacement — PASS

**Absorption from every state.** For an occupied edge with endpoint populations \(a,b\), the two directed occupation jumps have equal rate \(ab\), and their changes of \(V=\sum_x\eta_x^2\) sum to four. Thus
\[
IV=4\sum_{\{x,x+1\}}\eta_x\eta_{x+1}
\ge 4\mathbf{1}_{S_n^c},
\qquad n\le V\le n^2.
\]
The stopped Dynkin inequality therefore gives the stated \(c_n=n(n-1)/4\), uniformly in every initial tuple and every initial separation. Letting the deterministic stop increase proves almost sure absorption and the potential norm bound. Interaction creates no new occupied site, so a label stays in one initially occupied connected interval, which has at most \(n\) sites. This also justifies the finite absorption expectation for linear growth data. The absorption kernel is a probability kernel, giving the claimed contraction.

**Leading trace and jump range.** There are \(2n\) independent initiating attempts. A single attempt from \(S_n\) affects a component contained in at most three consecutive sites. The absorbed endpoint consequently moves each label by at most two. Self-return attempts contribute zero, so \(Q\) is conservative with off-diagonal rate at most \(2n\).

**Stack count and near-set rate.** An affected two-site component absorbs to a full stack; a three-site component absorbs to a full stack or its two endpoints. Neither increases the original stack count. At a distance-two pair of masses \(a,b\), the inward attempt rate is \(a+b\). Immediately after an attempt the intervening population is one, including the case where a singleton source is emptied. That population is a bounded interaction martingale and ends at zero or \(a+b\). Its chance to end as the full intervening stack is \(1/(a+b)\). Hence this particular merger has rate one, establishing the inequality for \(QK\), without an assumption on other distance-two pairs.

**Infinite-horizon occupation.** Boundedness of \(K\) and its lower bound one give \(\sup_z\mathbb E_z A\le n-1\). Tonelli and the Markov property give
\[
\mathbb E_z A^2
=2\mathbb E_z\int_0^\infty
\mathbf{1}_{C_n^{\mathrm{near}}}(Y_s)\mathbb E_{Y_s}A\,ds
\le2(n-1)^2.
\]
The finite-time diagonal has zero Lebesgue measure; monotone convergence justifies the infinite-time identity without assuming its conclusion. These are uniform statewise bounds. At any almost surely finite stopping time, the same bounds apply conditionally to the subsequent occupation by the strong Markov property. No equilibrium estimate is being upgraded to a pointwise estimate.

**Displacement.** Away from the near set a stack of size \(a\) shifts in a specified direction at effective rate \(a(1/a)=1\). Thus the coordinate drift vanishes there, its absolute value elsewhere is at most \(4n\), and its bracket density is at most \(8n\). The compensated coordinate martingale has square maximal expectation at most \(32nt\). Bounding the integrated drift by \(4nA\), then summing the coordinate bounds, yields the stated \(C_n(t+1)\). Bounded jump rates and jump sizes justify the localization removal. The argument applies uniformly over all starting states of the trace.

## 4. Conclusion 2: canonical correctors and their identities — PASS

**Support and integrability of the residual.** Off the near set, centered stack translations stay in a common closed chamber; affine increments cancel. A trace jump has sum distance at most \(2n\), giving
\[
|Qf|\le4n^2D\mathbf{1}_{C_n^{\mathrm{near}}}.
\]
The occupation bound therefore proves absolute integrability of the defining potential and the exact stated bound \(\|\psi_f\|_\infty\le4n^2(n-1)D=a_nD\).

**Harmonicity.** The potential identity is applied to the bounded function \(Qf\) and the bounded potential \(\psi_f\). Since \(Q\) is a bounded operator on bounded functions, differentiation at zero is justified in that space and gives \(Q\psi_f=-Qf\). The remaining evaluation of \(Qf\) is a finite endpoint sum. No unbounded semigroup-domain assertion is needed for \(QH_f=0\).

**Linearity and covariance under the specified maps.** Absolute convergence permits linearity inside the defining integral. Coordinate permutations and common integer translations intertwine the clocks, absorption, and trace kernels. Their compositions also preserve the class of chamber-affine functions. This proves the precise identity \(H_{f\circ g}=H_f\circ g\). A full stack remains a full stack under \(Q\), and the diagonal restriction of \(f\) is affine, proving zero correction on every full stack.

**Symmetric affine functions.** For \(g=\sum_i x_i\), both \(Rg=0\) and \(Ig=0\). The pure interaction path is bounded relative to its initial coordinates, so stopped martingale convergence gives \(Pg=g\). Hence \(Qg=0\), \(\psi_g=0\), and \(Bg=0\). This applies to the specified additive constants and multiples, without incorrectly asserting that each physical coordinate is separately an interaction martingale.

**Uniform residuals on the full lattice.** Absorption moves each label at most \(n-1\). For neighboring lattice tuples, the Lipschitz estimate and the bounded correction give the proof's bound
\[
|PH_f(x+\epsilon e_i)-PH_f(x)|
\le D\bigl(2n(n-1)+1+2a_n\bigr).
\]
Summing the \(2n\) independent increments bounds \(RPH_f\) on all of \(E_n\). Applying \(R\) and \(U\) gives the stated uniform bound on \(BH_f\). Intercepts of \(f\) do not enter these constants.

## 5. Conclusions 5 and 6: actual excursions and exact expansion — PASS

These conclusions were checked before the coefficient calculation, as in the proof; the later use of the expansion is therefore not circular.

**Exact terminal-event convention.** With \(q=2nc_nd\le1/4\), the probability that a rate-\(2nd\) independent clock rings before pure absorption is at most \(2nd\mathbb E\tau\le q\). Restarting after each independent event, unless it has entered \(S_n\), proves \(\mathbb P(J\ge j)\le q^j\). The event causing entrance is counted before deciding whether to restart. The proof thus applies to the exact interval \((0,\tau_d]\), not a count that discards the terminal jump. An already stable initiating-step state has duration and count zero. The same restart argument works from arbitrary initial tuples.

**Duration moments.** Each reached stage has conditional mean duration at most \(c_n\); the chance to reach stage \(j\) is at most \(q^j\). Summation yields \(\sup_x\mathbb E_x\tau_d\le c_n/(1-q)\le2c_n\), establishing almost sure absorption before any inverse is used. Conditional Markov bounds at successive times \(4c_n\) give \(\sup_x\mathbb P_x(\tau_d>4c_n k)\le2^{-k}\). Tail integration proves every stated real-order duration moment, uniformly in the initial tuple and in the allowed interval of \(d\).

**Pathwise displacement, including merging components.** The union of initially occupied sites, the initiating destination, and the destinations newly occupied by the \(J\) further independent events has at most \(n+1+J\) sites. Every label trajectory lies in the connected component of this union containing its initial site. A finite connected subset of the line has diameter at most its cardinality minus one. This proves \(n+J\) without assuming that initially distinct components remain distinct. From arbitrary initial tuples without an initiating event the corresponding bound is \(n-1+J\), which is the bound needed for unbounded boundary data.

**Count moments and endpoint moments.** For every real \(p\ge1\),
\[
\mathbb E\bigl[(1+J)^p\mathbf{1}_{\{J\ge1\}}\bigr]
\le q\sum_{j\ge1}(1+j)^p4^{1-j}
\le C_{n,p}d.
\]
The series is finite; adding the event \(J=0\) gives the other count moment. The endpoint bound
\[
|H_f(y)-H_f(z)|\le Dn(n+J)+2a_nD
\]
and the \(2n\) initiating choices give every trace jump moment, including noninteger orders and \(d=0\). The case \(D=0\) also satisfies the bound because the corrected function is constant.

**Killed inverse.** The already constructed bounded potential \(U_d\) solves its killed equation by conditioning on the first jump. Pure stopped Dynkin gives \(U(-I^0w)=w\) for bounded zero-boundary \(w\). Consequently
\[
U_d=U+dUR^0U_d,
\qquad \|dUR^0\|\le4ndc_n\le\tfrac12.
\]
This proves the actual norm-convergent inverse, \(\|U_d\|\le2c_n\), and \(\|U_d-U\|\le8nc_n^2d\). Its series also gives the correctly ordered identity \(U_d-U=dU_dR^0U\).

**Absorption and trace identities.** For bounded boundary data, stopped Dynkin for \(Pb\) yields \(P_db-Pb=dU_dRPb\), with zero difference on the boundary. For \(H_f\), the uniformly bounded residual, the neighboring-increment bound, and the integrable maximal displacement controlled by \(J\) justify removal of both time and spatial stops. In particular the terminal values are uniformly integrable from each fixed initial tuple. Applying \(R\) and the resolvent identity gives precisely
\[
T_db=Qb+dBb+d^2(RU_dR^0URPb)|_{S_n}.
\]
The zero extensions and the order of all operators agree with the contract. The proof's remainder norms follow from multiplying the displayed bounded-operator norms; using \(RPH_f\) in place of \(RPb\) gives the stated \(D d^2\) estimate. Harmonicity then gives both estimates for \(T_dH_f\).

**Actual trace clock.** On \(S_n\), the chain \(R+d^{-1}I\) initiates attempts at rate \(2n\); its off-set absorption law is \(P_d\). Every excursion is finite. The successive trace holding times at the attempt level are exponential with rate \(2n\), so their sum diverges almost surely. Thus the trace is defined for every trace time and has the claimed conservative generator and rate bound. This proves the auxiliary trace assertion; it makes no claim about a rescaled limiting clock.

## 6. Conclusion 3: labelled coefficients and quantitative localization — PASS

**Reduction and the two-stack boundary equation.** Gradients in adjacent chambers differ only in the two exchanged coordinates, by a multiple of their difference vector. Their coordinate sums therefore coincide. Subtracting the resulting symmetric affine function makes the test translation invariant and zero on full stacks, without changing its correction or its \(B\)-action. For a fixed oriented left subset \(A\), the gap at values at least three is a walk with rate two in each direction. Harmonicity and the bounded correction imply
\[
H(A,r)=(r-2)c_A+a_A,\qquad r\ge2.
\]
At gap two the inward attempt rate is \(m\), the center merger rate is one, and the nonnegative two-stack kernel \(K\), including self-returns, has row sum at most \(m-1\). Thus \(M=m\operatorname{Id}-K\) is invertible by its explicit convergent series. The two outward effective moves contribute \(2c_A\), yielding exactly \(Ma=2c\).

**Weighted symmetry, rather than exchangeability.** The finite-cycle weight is the product of rising factorials over occupied sites. A specified label's forward/reverse rate ratio is
\[
\frac{d+b}{d+a-1},
\]
equal to the destination/source weight ratio. The finite-matrix Schur complement in the proof preserves this weighted symmetry. Absorption and the convergent expansion on the sufficiently long cycle follow from the same population and restart arguments; they do not require a separate campaign theorem. The coefficients used here involve only one or two independent events and interaction on occupied sites. Their support fits in the displayed fixed local interval, so they agree with the line coefficients and incur no wrap-around term.

**Coefficient comparison and orientation factors.** The weights of full and two-stack tuples start at orders \(d\) and \(d^2\), respectively. Since \(Q\) cannot increase stack count, comparison at order \(d^2\) gives exactly
\[
\kappa_AK(A,A')=\kappa_{A'}K(A',A),
\qquad B(o,s)=\kappa_AQ(s,o).
\]
The only split placements in the full-stack \(B\)-row are \((-1,1)\), \((0,2)\), and \((-2,0)\). Translating their reverse merger rates to a fixed pair shows their sum is \((M\mathbf{1})_A\). Weighted symmetry and the previously established boundary equation consequently give
\[
BH_f(o)=\sum_A\kappa_A(M\mathbf{1})_Aa_A
=\sum_A\kappa_A(Ma)_A
=2\sum_A\kappa_Ac_A.
\]
For the reduced test, the directional derivative in the specified vector is \(2c_A\). Restoring the affine term contributes zero after pairing complementary subsets. Each oriented subset remains separately counted. As a direct order-two check, the inward kernel between two singleton stacks has \(K=0\), hence \(M=2\operatorname{Id}\); this is consistent with the same factor two, without a division by an unlabelled exchange factor. The argument above holds for every order \(m\), rather than relying on this check.

**Construction at intersecting internal chambers.** The block functions in (20) are explicitly defined from chamber gradients. Exchanging the order inside another block changes no gradient coordinate in the given block. Adjacent internal formulas agree on their shared face; successive exchanges of equal coordinates prove agreement on further intersections. Their gradient coordinates have magnitude at most \(D\). Hence they are globally continuous chamber-affine functions with the required Lipschitz bound. This supplies the compatibility used here rather than asserting it as routine.

**Bounded harmonic discrepancy.** In the region of prescribed block order, the decomposition of \(f\) gives the sum of the isolated corrected block functions. The discrepancy \(\delta\) is bounded by the global potential bounds. In the box of radius \(2r_0\), all trace endpoints remain in the radius-\(4r_0\) box, and distinct blocks are still separated because the initial separation is at least \(16r_0\). Each initiating interaction component belongs to a single block. Thus \(Q\delta=0\) there, with all stopping arguments applied to a bounded function.

**Coarse coupling estimate.** Before box exit, block centers are independent walks with rate one in each direction. Independent-until-meeting coupling makes their difference a rate-two walk in each direction. Stopping that walk at zero or an upper boundary proves the stated survival bound by its coordinate martingale and the function \(x(b-x)\), whose generator is minus four. At time \(r_0\), the probability of exiting the center box from either allowed starting point is at most \(C_n/r_0\), by the square maximal estimate and the starting margin \(r_0/2\). Bounded stopped harmonicity and the union bound over blocks therefore prove (22), uniformly in absolute positions and shifts.

**Internal merger tail.** At gap two, the gap has outward rate two and merger rate at least one; label-subset redistributions preserve that gap. Splitting off rate-one killing and removing further killing bounds the lifetime by the stated boundary-killed walk. Its displayed Laplace transform solves both the interior and boundary equations. Bounded discounted stopping supplies uniqueness, and its limit at zero proves almost sure killing. The elementary inequality comparing \(\mathbf{1}_{\{\zeta>t\}}\) to \(1-e^{-\zeta/t}\) gives (24). No unproved recurrence assertion is needed.

**Stopping margins and exponent.** For the possible single internal split in the \(B\)-row, the proof stops at merger, time \(r_0^{1/2}\), or displacement \(r_0^{3/8}\). The displacement and survival failure probabilities are each at most \(C_nr_0^{-1/4}\). A simultaneous merger and displacement exit is counted as failure. Successful endpoints have center shift at most \(r_0^{3/8}+2\le r_0/2\) for \(r_0\ge16\); all stopped endpoints lie within \(r_0^{3/8}+4<2r_0\). Inserting the successful shift in (22) gives \(r_0^{3/8}/r_0^{1/2}=r_0^{-1/8}\). Thus (25) has the exact claimed rate with safe stopping margins.

**Local row and the surviving first-order action.** Every destination in the signed \(B\)-row moves each label at most two sites and has at most one block split into two substacks at distance two. A second independent event in a different block only leaves two two-site components, each absorbing to a full stack. Negative terms in \(R\) have smaller support. The row has uniformly bounded total variation and zero sum. Applying (25) after subtracting \(\delta(z)\) bounds its action by \(C_nD r_0^{-1/8}\).

The proof also evaluates the action on the block sum: after the first independent event only the affected block is transient; the residual in any other full block is its zero harmonic residual. Independent pure absorption in the separated groups and the killed integral therefore yield the sum of the isolated block \(B\)-actions. This controls the surviving first-order action, rather than assuming that bounded corrections disappear under \(B\). The full-block identity then gives precisely the contract's split sum. Singleton blocks contribute zero. The one-full-block formula is exact without any separation parameter.

## 7. Conclusion 4: covariance bounds — PASS

At a coarse separated tuple, all individual block corrections vanish. Thus the coarse estimate (22) applied to a unit center shift bounds the change of the coordinate correction by \(C_nR_*^{-1/2}\). Every nonzero leading transition shifts one entire block left or right at rate one, giving
\[
H_i(z+\epsilon\mathbf{1}_B)-H_i(z)
=\epsilon\mathbf{1}_{\{i\in B\}}+O(C_nR_*^{-1/2}).
\]
Multiplication and summation give the normalization \(2\mathbf{1}_{\{z_i=z_j\}}\) with error \(C_nR_*^{-1/2}\). At arbitrary states, jumps of each corrected coordinate are bounded by \(2+2a_n\) and the leading total rate is at most \(2n\), giving a uniform bound on \(\Gamma_0\).

For each initiating attempt, the pure excursion can be sampled independently of the extra independent clocks and coupled to the perturbed excursion up to the first such event. It retains its pure marginal even if interruption occurs. With the specified terminal-event count, \(J=0\) implies equality of endpoints; an entrance-causing independent event lies in the complementary event \(J\ge1\). The two products of corrected coordinate increments consequently differ by at most
\[
C_n\bigl((1+J)^2+1\bigr)\mathbf{1}_{\{J\ge1\}}.
\]
The already proved weighted count moment gives the uniform \(C_nd\) covariance difference after summing the \(2n\) attempts. Absolute convergence follows from the second trace jump moment and \(|ab|\le(a^2+b^2)/2\). These estimates establish every displayed bound in conclusion 4, including the joint separation-plus-\(d\) error.

## 8. One-label convention and uniform quantifiers — PASS

For \(n=1\), every tuple is already stable: both potentials and excursion durations vanish, and \(P=P_d=\operatorname{Id}\), \(Q=T_d=R\), \(B=0\). A chamber-affine function is affine, so its correction and centered second difference vanish. The coordinate jumps by plus and minus one at rate one; therefore its bracket density is two, its square maximal displacement is at most \(8t\), and its trace jump moment is \(2|a|^p\le2D^p\). The initiating displacement is one, while \(J=0\). The split sums and near occupation are empty. These facts establish the complete separately stated convention, without substituting \(n=1\) in the undefined expression for \(d_n\) in the \(n\ge2\) setup.

The all-order arguments are finite-dimensional for each arbitrary \(n\). Subblock orders are at most \(n\); taking maxima over these orders leaves constants depending only on \(n\). Every position-dependent step uses bounded occupied-component size, translation-invariant rates, or the explicit separation margin. Every test-dependent estimate uses its gradient bound or its correction bound. Real \(p\ge1\) is handled by convergent tails, and \(d\) ranges over the contract's full interval. No positive lower bound on a block's size beyond being a nonempty set of labels, no fixed partition type, and no additional separation condition are introduced.

## 9. Complete AC-005 checklist disposition

“PASS within scope” means that the identified failure mode was tested for this auxiliary theorem. “NOT CLAIMED” means the corresponding full-mass or target assertion is not established by C0005 and is not discharged by this report.

| Item | Disposition | Evidence and limit |
|---|---|---|
| AC-001-01 | PASS within scope; target scaling NOT CLAIMED | The attempt rate is \(2n\), isolated stack rates are one per direction, the merger rate is one, the split derivative contributes \(2c_A\), and the coordinate bracket is two. The auxiliary \(d\) is not an acceleration parameter. No conversion to \(\rho\) or \(\alpha\) is made. |
| AC-001-02 | Full mass path law NOT CLAIMED | The contract and proof explicitly state the auxiliary line-lattice scope. This audit does not treat it as convergence of the full mass process. |
| AC-001-03 | Frozen initial-condition scope NOT CLAIMED; auxiliary quantifiers PASS | All auxiliary lattice positions, distance-two states, block sizes, partitions, and arbitrary excursion starts are covered. The prescribed finite-stack mass sequences in STATEMENT-v1 are not addressed. |
| AC-001-04 | PASS within scope; deletion consistency NOT CLAIMED | No physical-tag autonomy or deletion identity is used. Coordinate drift is controlled directly and need not vanish near collisions. |
| AC-001-05 | Limiting collision occupation NOT CLAIMED | The occupation estimates concern the actual \(Q\)-chain and follow from \(QK\); no weak-limit passage of indicators is used. |
| AC-001-06 | PASS for all-order coefficients; sticky-flow identification NOT CLAIMED | The finite labelled weight and matrix calculation derives every oriented subset coefficient for arbitrary order. It is not substituted for identification of the continuum target. |
| AC-001-07 | PASS within scope | The canonical potential is defined globally; the block chamber functions are explicitly constructed and agree at intersecting faces. Bounded harmonic discrepancy and the signed \(B\)-row estimate establish localization. |
| AC-001-08 | PASS within scope; convergence from prescribed starts NOT CLAIMED | Absorption, occupation, displacement, and excursion estimates are proved uniformly for each allowed state, without an equilibrium averaging argument. |
| AC-001-09 | Determining continuum test class or core NOT CLAIMED | Only the stated chamber-affine class and its correctors are treated. No core or boundary-identification inference is made. |
| AC-001-10 | Mass-process tightness and continuity NOT CLAIMED | The auxiliary estimates are not an Aldous argument for the mass process and do not establish the requested path topology. |
| AC-001-11 | Full path-law identification NOT CLAIMED | No one-time or moment result is advertised as path-law convergence. |
| AC-001-12 | PASS for labelled line identities; circle/flow target conversion NOT CLAIMED | Oriented subsets remain labelled, and the finite cycle is used only for coefficients whose local support is proved. No ordered-particle, circle-coordinate, or kernel-flow identification is performed. |
| AC-001-13 | PASS within scope | Absorption precedes inversion; the actual expansion precedes coefficient comparison; the killed-walk tail and chamber compatibility are proved explicitly; no external or campaign lemma is substituted for a missing step. |
| AC-001-14 | PASS | No exact-target/open-status search was made, and no Mosco argument is used. |
| AC-001-15 | PASS for this audit's access discipline | Only the four pinned inputs were read. No leakage report, other proof, or reconstruction was consulted. This does not certify the provenance of other stages. |
| AC-001-16 | PASS for status discipline | The verdict is tied to the four verified hashes, relies on no promoted dependencies, and is expressly not promotion or completion of the campaign. |
| AC-002-17 | Random atomic evaluation issue NOT CLAIMED | No identity is integrated against a random atomic measure and no independent-noise evaluation argument is used. |
| AC-002-18 | Modification/indistinguishability issue NOT CLAIMED | No random-field modification is constructed. The paths and stopped identities used here belong to the specified bounded-rate chains. |
| AC-003-19 | Whole-kernel/random-evaluation measurability NOT CLAIMED | No kernel-flow evaluation or noise-sigma-field independence assertion occurs in the auxiliary argument. |
| AC-003-20 | PASS | No mathematical computation or simulation was executed or used as evidence. All calculations in this report are symbolic checks of the displayed proof. |
| AC-003-21 | PASS within scope | The occupation and displacement constants hold uniformly over every trace state, and the strong Markov property gives their conditional versions after finite stopping times. The perturbed duration argument likewise restarts from every microscopic tuple. |
| AC-003-22 | PASS for the coefficient device; sampled-index/generator-class claims NOT CLAIMED | The cycle is explicitly longer than \(6m+10\), and only local line coefficients are compared. No \(L=3\) assertion, sampled-index correction, or all-orders determining generator class is used. |
| AC-004-23 | Thin-layer-to-exact-collision transfer NOT CLAIMED | No positive-layer estimate is used to remove exact occupation, and no such bound is multiplied by a diverging defect. |
| AC-004-24 | PASS within scope | \(n\) and the subblock order \(m\) denote label counts. No \(N\)-dependent acceleration enters the factorial derivation. |
| AC-004-25 | PASS for auxiliary trace and excursion assertions; limiting clock transfer NOT CLAIMED | The trace is defined for all trace times; arbitrary initial tuples have uniform duration moments; initiating excursions have pathwise and weighted rare-event bounds. No transfer to a limiting microscopic path law is asserted. |
| AC-004-26 | PASS | The proof controls both the signed first-order \(B\)-action at rate \(R_*^{-1/8}\) and coordinate brackets at rate \(R_*^{-1/2}\), with an additional \(O(d)\) perturbation bound. |
| AC-004-27 | Deterministic continuum collision starts and wrapping NOT CLAIMED | No \(L^2\) target identity is used pointwise, and no real-line process is wrapped to infer a circle martingale problem. |
| AC-004-28 | Collision-cell accumulation scheme NOT CLAIMED | No such decomposition or sum of cell errors is used. The auxiliary stopping arguments separately handle exits and arbitrary starting states required by their own claims. |
| AC-005-29 | PASS for the exact v2 count | The count includes an entrance-causing independent jump on \((0,\tau_d]\), is zero for zero-duration excursions, has the proved geometric tail, and makes endpoint agreement on \(J=0\) valid in the covariance coupling. |

## 10. Final version-bound determination

**PASS** for `CONTRACT_v2.md` at SHA-256 `0a0130d01e482dbe546a19248b1ca67180aa373643dace7a87abc5cff8eb8cec`, supported by `PROOF_v2.md` at SHA-256 `68a9fec530428b3fd61e9f3bef1564e3ad3bcbd905d0cf0b51801a58bd6fc5ef`, against the frozen statement and complete checklist in the manifest.

No repair or additional theorem-strength premise is supplied as a condition of this verdict. No required auxiliary conclusion was left incomplete. The unrelated full-mass, target, and path-identification checks remain **NOT CLAIMED**, as recorded individually above. This immutable report supplies one hostile-audit record only; further protocol stages and promotion remain separate.
