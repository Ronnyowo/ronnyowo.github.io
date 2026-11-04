# C0005 comparison — v2

**Version-bound verdict: PASS. Mathematical status: self-audited comparison only.**

This verdict applies exclusively to the seven input byte versions in the manifest below. The reconstruction proves the exact auxiliary theorem in CONTRACT_v2.md and reproduces the candidate's canonical correction, perturbed trace, factorial boundary calculation, and harmonic localization mechanism. I found no missing contract conclusion, changed hypothesis, unproved campaign premise, or replacement of a disputed stage by an assumed result.

This is not a promotion, an outside-family audit, a verdict on any other candidate or version, or a proof of STATEMENT.md. No outside-family verification is asserted.

## 1. Scope, definitions, and quantifiers

The contract is an auxiliary theorem on the line lattice. STATEMENT.md is the frozen full probability-measure-valued path-law target, with its specified finite-stack initial conditions, parameter limits, continuum semigroups, and Skorokhod topology. Neither the candidate nor reconstruction claims to obtain that convergence from this auxiliary result. The parameters and continuum constructions in STATEMENT.md are therefore not silently used as premises or replaced by this comparison.

The following identifications were checked against the contract, candidate proof, and reconstruction.

| Contract object or hypothesis | Exact identification and coverage |
|---|---|
| Arbitrary fixed integer \(n\ge2\), state space \(E_n=\mathbb Z^n\), labelled coordinates | Both proofs use the labelled line chain. No ordering quotient, unlabeled replacement, or fixed upper bound on \(n\) is introduced. |
| \(R\), \(I\), and their time normalization | Each label has two independent rate-one directions under \(R\); an interaction direction has rate equal to the population at its neighboring destination. The reconstruction's proposal constructions preserve these rates. |
| \(S_n\), entrance including time zero, \(P\), \(U\) | Both use the absence of adjacent distinct occupied sites, actual first entrance, absorption expectation, and the potential killed at that entrance. \(U\) is zero on \(S_n\); linear-growth absorption data are justified by displacement bounds. |
| \(Q=(RP)|_{S_n}\), \(B=(RURP)|_{S_n}\), \(Y\), \(K\), and the near set | These are the same operators, chain, occupied-site count, and distance-two set. Neither proof substitutes an alternative harmonic extension or effective generator. |
| \(c_n=n(n-1)/4\), \(a_n=4n^2(n-1)\), \(d_n=(8nc_n)^{-1}\) | Reconstruction §§1, 3, and 4 establish the displayed constants and use exactly the interval \(0<d\le d_n\). |
| Chamber-affine \(f\), including constants, and the global sum-norm Lipschitz bound \(D\ge0\) | Reconstruction §§2–3 and 7–8 use continuity across all chamber walls and coordinate slopes bounded by \(D\). They do not impose symmetry, homogeneity without an intercept, or boundedness of \(f\). |
| Canonical \(\psi_f\) and \(H_f=f+\psi_f\) | The reconstruction uses the prescribed infinite-time \(Qf\) potential, proves absolute integrability, and obtains harmonicity from its Markov identity. No unspecified choice among harmonic functions is used. |
| Every partition, distinct integer centers, and every oriented proper nonempty subset | Reconstruction §§7–8 retain the labels and all subsets separately. Singleton block sums are empty. |
| Real \(R_*\ge16\), separation at least \(16R_*\), and directional derivatives | The estimates are proved on local boxes with these separations. The derivative is the stated right derivative in the vector with entries minus one and plus one within the block. No finite-separation identity is asserted beyond the full-block case. |
| \(P_d,U_d,\tau_d,R^0,T_d\), and \(T_0=Q\) | Reconstruction §4 uses absorption for \(I+dR\), the zero-boundary restriction \(R^0\), and the trace of \(R+d^{-1}I\) in its \(S_n\)-time. All resolvent orders and boundary restrictions agree. |
| \(H_i\) and \(\Gamma_d^{ij}\) | Reconstruction §§5 and 9 use the same coordinate correctors and off-diagonal covariance sums. Both the global and separated estimates cover every pair of labels. |
| Initiating step \(w=z+\epsilon e_i\), count \(J\), and all excursion conventions | Reconstruction §4 counts independent events up to and including one causing entrance. If \(w\in S_n\), the duration and count are zero. The initiating step is included in displacement but excluded from \(J\), exactly as required. |
| Every real \(p\ge1\), every \(t\ge0\), all initial tuples where required | Geometric tails supply real-order event moments; exponential duration tails apply to arbitrary initial tuples, not only initiating-step states. The displacement estimate for \(Y\) covers all \(t\ge0\). |
| Constants depending only on \(n\), or \(n,p\), simultaneously | The estimates involve only bounded rates, \(c_n,a_n\), at most \(n\) groups, and fixed box ratios. Constants from group dimensions at most \(n\) can be replaced by their finite maximum. There is no dependence on absolute positions, actual separations, partition, subset, or \(f\) beyond \(D\). |
| The complete \(n=1\) convention | Candidate §8 and reconstruction §10 verify all stipulated operators, zero potentials, covariance two, duration/count zero, and displacement and jump-moment bounds separately. |

The full contract appears verbatim in BRIEF_v2.md; an administrative literal-text check confirmed this. Its sole additional hint is: “The absorption extension, killed potential, and coordinate-order chambers are the named definitions.” It supplies no extra mathematical premise.

## 2. Mathematical verification of all required outputs

### Contract item 1: absorption, trace geometry, occupation, and displacement

Candidate §1 and reconstruction §§1–2 use the same occupancy-square function. Pairing the two directed jumps along an occupied edge gives
\[
IV=4\sum_x\eta_x\eta_{x+1}
 \ge4\mathbf{1}_{S_n^c},
\qquad n\le V\le n^2.
\]
Stopped Dynkin and monotone convergence give almost-sure absorption and the exact bound \(c_n\). The support of a pure interaction path is contained in its initial occupied set, so a label remains within \(n-1\) sites. This also proves finiteness of the stated unbounded absorption data.

An initiating independent step can connect only the source, its neighbor, and a previously occupied site two steps away. Pure absorption then moves any label at most two sites. The proposal rate is \(2n\), and self-return proposals do not contribute to off-diagonal rates.

For a distance-two pair of total mass \(m\), the middle population is a bounded martingale with upward and downward rates \(k(m-k)\). Each inward proposal starts it at one, so its chance to absorb at \(m\) is \(1/m\); there are \(m\) such proposals. This proves the rate-one middle merger. No proposal-absorption move increases \(K\). Consequently
\[
QK\le-\mathbf{1}_{C_n^{\mathrm{near}}}.
\]
The first occupation bound follows from \(1\le K\le n\). For the second, Tonelli and the conditional first-moment bound give
\[
\mathbb E_z A^2
 =2\mathbb E_z\int_0^\infty
 \mathbf{1}_{C_n^{\mathrm{near}}}(Y_s)\,
 \mathbb E_{Y_s}A\,ds
 \le2(n-1)^2,
\quad
A=\int_0^\infty\mathbf{1}_{C_n^{\mathrm{near}}}(Y_s)\,ds.
\]
The identity is valid by first using finite time integrals and then monotone convergence.

Outside the near set, whole stacks translate in either direction at rate one. Thus the coordinate drift is zero there and uniformly bounded everywhere. Coordinate jumps have size at most two, and their quadratic-variation rate is at most \(8n\). The square-martingale maximal bound and the estimate on \(A^2\) give exactly the required \(C_n(t+1)\) displacement estimate. These arguments require neither label-deletion consistency nor stationary initial data.

### Contract item 2: canonical harmonic corrections and every basic identity

Candidate §2 and reconstruction §3 both establish
\[
|Qf|\le4n^2D\,\mathbf{1}_{C_n^{\mathrm{near}}}.
\]
The occupation bound therefore proves absolute integrability of the canonical potential and \(\|\psi_f\|_\infty\le a_nD\). Its Markov identity, differentiated for the bounded operator \(Q\) on bounded functions, gives \(Q\psi_f=-Qf\). This proves \(QH_f=0\) pointwise without asserting an unbounded-function semigroup domain.

Linearity and equivariance follow by applying the permitted transformations to the absolutely integrable potential. On the full-stack class, the trace stays a full stack and \(f\) restricts to an affine function, so the correction vanishes there.

For the total coordinate sum \(s(z)=\sum_i z_i\), directed-edge pairing gives \(Is=Rs=0\). The pure path has bounded displacement, which justifies absorption stopping and \(Ps=s\). Therefore all functions \(b+as\) have zero correction and zero \(B\)-action.

Finally the reconstruction proves on all \(E_n\)
\[
|PH_f-f|\le\bigl(n(n-1)+a_n\bigr)D.
\]
Taking \(R\), whose bounded-function norm is at most \(4n\), bounds \(RPH_f\). Applying the killed potential and the outer \(R\), with its argument zero on \(S_n\), bounds \(BH_f\). These establish the two global bounds simultaneously.

### Contract items 5 and 6: actual excursions before resolvent manipulations

Candidate §3 and reconstruction §4 prove perturbed absorption before using a killed inverse. With
\[
q=2nc_nd\le\frac14,
\]
the probability of an independent alarm before pure interaction absorption is at most \(q\), from every starting tuple. Restarting after each alarm, including an entrance-causing alarm, gives \(\mathbb P(J\ge j)\le q^j\). The inclusive terminal convention is necessary for the later zero-alarm endpoint coupling and is respected in both proofs.

Summing the expected lengths of reached segments gives
\[
\sup_x\mathbb E_x\tau_d\le \frac{c_n}{1-q}\le2c_n.
\]
Applying this uniform bound conditionally at intervals \(4c_n\) gives an exponential duration tail and hence every real-order duration moment. The event-count tail gives both the uniform \((1+J)^p\) moment and its \(O(d)\) part on \(J\ge1\).

The visited-site proof of displacement is valid even when occupied components join: the initial set together with independent arrivals has at most \(n+1+J\) sites, and any label's nearest-neighbor path between its initial and later positions is contained in that set. Its length is at most \(n+J\). Without the initiating step, the corresponding bound is \(n-1+J\).

The uniformly decaying killed semigroups give bounded inverse potentials. Since \(d\|UR^0\|\le1/2\), the stated inverse is norm convergent, and both proofs obtain
\[
U_d=(\operatorname{Id}-dUR^0)^{-1}U,
\qquad
U_d-U=dU_dR^0U.
\]
These give precisely the stated \(2c_n\) and \(8nc_n^2d\) bounds, with the operator order required by the contract.

Stopped Dynkin applied to \(Pb\) yields the absorption difference and, after applying \(R\), the exact expansion
\[
P_db-Pb=dU_dRPb,
\]
\[
T_db=Qb+dBb+
 d^2(RU_dR^0URPb)|_{S_n}.
\]
For \(H_f\), the bounded residual and the arbitrary-start displacement/event moments justify uniform integrability of the stopped terminal values. Thus the identities are proved for the actual unbounded corrector, not just for bounded truncations without a justified limit. The remainder bounds then give both required \(T_dH_f\) estimates.

The trace has \(2n\) independent proposals per unit of time spent in \(S_n\), with endpoint law \(P_d\). This proves its generator and rate bound. The construction also rules out finite exhaustion of trace time: successive attempt holding times in \(S_n\) are exponential with rate \(2n\), while excursions return almost surely. Their accumulated \(S_n\)-time diverges. Thus the conservativity statement refers to the actual trace on all trace times.

The endpoint bound
\[
|H_f(y)-H_f(z)|
 \le Dn(n+J)+2a_nD
\]
and the proposal representation prove every required trace jump moment. The case \(d=0\) follows from the finite \(Q\)-jump displacement bound. No assertion here is restricted to integer \(p\).

### Contract item 3: exact factorial identity and separated localization

The exact full-stack calculation is candidate §4 and reconstruction §7. Both derive, rather than assume, the labelled reversible weights
\[
\nu_d(z)=\prod_{x:\eta_x(z)>0}(d)_{\eta_x(z)}.
\]
For a specified label moving from population \(a\) to neighboring population \(b\), the weight ratio is \((d+b)/(d+a-1)\), exactly the forward/reverse rate ratio.

The candidate proves trace symmetry by a finite-cycle block-matrix elimination and checks locality of the compared coefficients. The reconstruction proves that same trace symmetry directly on the line by reversing killed transition paths. This is legitimate: rates are bounded, the killed Green kernel has finite row sums by the absorption bound, and nonnegative sums may be interchanged. Both calculations use the already proved actual small-\(d\) trace expansion.

Comparing the same first nonzero powers of \(d\) yields weighted symmetry between two-stack label subsets and
\[
B(\mathbf 0,u)=\kappa_A Q(u,\mathbf 0)
\]
for a two-stack \(u\) with left subset \(A\). No factor for unlabeled occupancy states is inserted.

Boundedness of the correction and the exact stack translations at gaps at least three imply that the two-stack correction is constant as a function of the gap for every integer gap at least two. The reconstruction multiplies the two-stack harmonic equations by \(\kappa_A\); weighted symmetry cancels every transition between different label subsets. The remaining merger terms are exactly the finite row of \(B\) from a full stack. Full-stack destination increments cancel by reflection symmetry. The result is the contract's derivative sum, with every oriented subset included once. This is the same weighted boundary identity as the candidate's finite equation \(Ma=2c\), expressed without first subtracting the common-translation affine term.

The localization stage is candidate §5 and reconstruction §§6 and 8. Both construct the block chamber-affine decomposition from chamber-wall gradient differences. They compare the global corrector with the sum of the separate canonical block correctors, obtain a bounded locally harmonic difference, and control that difference on the finite set of boundary values read by \(B\).

The reconstruction supplies a stronger internal coalescence estimate than the two-substack estimate used by the candidate. Its derivation was checked. For the occupied span \(W\) of an isolated group, while \(W>0\), upward span jumps have size one and total rate two. The total downward rate multiplied by its span decrement is at least two. For two occupied sites at gap two the single middle merger decreases span by two, so it is not counted twice. For at least three sites the extreme merger events are distinct. Consequently, for \(s>0\),
\[
Qe^{-sW}\ge4(\cosh s-1)e^{-sW}.
\]
The stopped discounted submartingale gives
\[
\mathbb E_y e^{-\lambda\sigma}\ge e^{-sW(y)},
\qquad \lambda=4(\cosh s-1),
\]
and hence the stated \(C W(y)t^{-1/2}\) coalescence tail. This is a proved strengthening of the same merger stage, not a new assumed dependency or a bypass of localization.

The bounded harmonic gradient estimate follows by coupling one differing center coordinate until meeting. Its difference has generator \(2\Delta\); the meeting tail is \(O(t^{-1/2})\), while the chance of exiting the larger box before time \(t\) is \(O(t/R^2)\). Choosing \(t=R\) gives the required \(O(R^{-1/2})\) gradient bound.

Starting all labels within two sites of the reference block centers gives initial span at most four in each group. The reconstruction's stopped product-chain comparison, with \(t=R_*^{1/4}\), yields
\[
C_nD\left[
 t^{-1/2}+\frac{t+1}{R_*^2}
 +R_*^{-1/2}(1+\sqrt t)
\right]\le C_nD R_*^{-1/8}.
\]
The groups stay distinct inside the specified boxes because their centers are separated by \(16R_*\). Exit endpoints remain inside the region where the decomposition and boundedness hold. The displacement estimate justifies both the exit probability and the expected telescoping length.

Every boundary value read by the row \(RURP\) at the separated reference tuple lies within two sites of its original group center. The two independent steps in this row cannot violate that fact. Subtracting the constant reference value and using the bounded operator factors gives the \(R_*^{-1/8}\) error. Finally the inner \(R\)-action of each uninvolved full group is zero by its own canonical harmonicity; this proves the blockwise \(B\)-sum rather than assuming additivity. Applying the exact full-block calculation proves item 3 in full.

### Contract item 4: covariance sums, perturbation, and separated values

Candidate §6 and reconstruction §§5 and 9 establish the same assertions. The trace second-moment bound and \(|ab|\le(a^2+b^2)/2\) prove absolute convergence and the global covariance bound.

Couple perturbed and pure excursions using the same pure interaction path until an independent alarm. With the inclusive convention for \(J\), their endpoints agree on \(J=0\). On \(J\ge1\), the pure corrected-coordinate increments are bounded and the perturbed ones are at most \(C_n(1+J)\). The event-moment estimate therefore bounds the expectation of the product difference by \(C_nd\), uniformly in the initiating step and labels. Summing the \(2n\) proposals proves the claimed global \(O(d)\) covariance perturbation.

For separated full groups, the local restriction of each bounded coordinate correction is harmonic for independent rate-one stack walks. Its one-step gradient is \(O(R_*^{-1/2})\). Each corrected-coordinate increment is therefore
\[
H_i(z+\epsilon\mathbf{1}_B)-H_i(z)
 =\epsilon\mathbf{1}_{\{i\in B\}}+O_n(R_*^{-1/2}).
\]
These are all the \(Q\)-transitions at the reference tuple, each at rate one. Their products sum to \(2\mathbf{1}_{\{z_i=z_j\}}\) plus the stated error. Adding the already proved perturbation gives the bound for every allowed \(d>0\).

### One label and degenerate tests

Reconstruction §10 checks the full separate convention: \(S_1=\mathbb Z\), no interactions, identity absorption extensions, zero potentials, \(Q=T_d=R\), \(B=0\), and \(H_f=f\) for affine \(f\). The two unit-rate coordinate jumps give covariance two, square maximal displacement at most \(8t\), and trace moment rate at most \(2D^p\). The near set and split sums are empty, and all excursions have zero duration and count. Additive constants and \(D=0\) are also covered in every dimension.

## 3. Mechanism, dependency, and correctness verdict

The reconstruction does not merely prove an alternative sufficient theorem. It reconstructs the prescribed canonical potential itself, proves the exact \(B\)-coefficient with the same labelled reversible boundary identity, and estimates the same global-minus-block corrector on the precise finite row read by \(B\). It also proves the actual perturbed excursion expansion and the covariance estimates, rather than assuming any of them from a different candidate.

Two presentation differences were examined explicitly above: direct line trace symmetry versus finite-cycle matrix symmetry, and a span-based group coalescence estimate versus the candidate's two-substack killed-gap estimate. Both are internally proved implementations of the same respective stages. Neither alters the claim, target objects, coefficient normalization, canonical correction, localization mechanism, or dependency list.

There are no promoted campaign dependencies. The candidate's author manifest discloses extraction from another candidate; the current proof rederives the assertions rather than invoking that candidate as a theorem. I did not read that source or accept its conclusions. The reconstruction does not import it.

Both arguments use ordinary bounded-rate Markov-chain construction, strong Markov and stopped Dynkin identities, square-martingale estimates, bounded or uniformly integrable stopping, monotone convergence, and bounded-operator inverses. Their needed finiteness, boundedness, and limiting hypotheses are supplied by the displayed rate, occupation, and excursion estimates. No specialized literature premise was used.

Accordingly, the exact v2 reconstruction-to-candidate/contract comparison is **PASS**. This mathematical comparison remains self-audited only and carries no outside-family audit assertion.

## 4. Complete actual-input manifest

All paths below are relative to the assigned workspace:

`[private workspace]`

| File actually read | Verified SHA256 |
|---|---|
| STATEMENT.md | ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97 |
| CANDIDATES/C0005_harmonic_correctors/CONTRACT_v2.md | 0a0130d01e482dbe546a19248b1ca67180aa373643dace7a87abc5cff8eb8cec |
| CANDIDATES/C0005_harmonic_correctors/PROOF_v2.md | 68a9fec530428b3fd61e9f3bef1564e3ad3bcbd905d0cf0b51801a58bd6fc5ef |
| CANDIDATES/C0005_harmonic_correctors/BRIEF_v2.md | 35a10be2298890820aeeb7ab72d47e3a0602f9ea7907cbd20666648353ed4e5b |
| CANDIDATES/C0005_harmonic_correctors/AUTHOR_INPUTS_v2.md | 5920bb21d0520d0e0407b58140b31c193c866138e8da9a90e665306f4a2014af |
| AUDITS/C0005_RECONSTRUCTION_v2.md | 8defb3caadc36081286f874eb9ce8d1adade2368341317b0fea1b9ff1e956e95 |
| AUDITS/C0005_RECONSTRUCTION_INPUTS_v2.md | c6f5cb3231ea0ed7c3722af4e0d3c955bb96fb080b50bafd8abca7413c57f875 |

All seven initial hashes matched the expected assignment hashes. The files were read using a concatenated text read and subsequent complete/chunked reads confined to these same paths. Some large tool output was truncated; subsequent permitted reads supplied the missing portions. A line-count command inspected only these seven files. A text-only check reread the contract and brief to verify exact embedding, and performed an existence-only check that the new comparison output did not already exist.

The remaining received context consisted of the fresh comparator assignment, its seven expected hashes and isolation requirements, the user-provided rigor and LaTeX instructions and workspace information, and operational system/developer instructions. No mathematical defense, verifier result, or other mathematical message was requested or received from the parent after assignment. Progress messages sent outward reported this comparator's own checks.

Paths, hashes, titles, and provenance statements named inside the two permitted input manifests were seen only as their text. None of those referenced files, scripts, earlier versions, other candidates, audits, checklists, registries, search records, or defense files was opened. The manifests' historical exposure assertions were not independently verified against unallowlisted sources and are not treated as mathematical premises.

No external source, web page, literature document, or external URL was opened or consulted. The literature URLs within STATEMENT.md were merely read as part of that file and supplied no premise for this auxiliary comparison. No mathematical program, numerical enumeration, simulation, symbolic computation, or subagent was used.

The comparison file was authored as a new file. Before creation, in-memory administrative checks verified paired inline/display math delimiters and balanced unescaped braces in mathematical segments. Any final read or hash check of this report concerns only this comparator's own authored output. The seven allowed input hashes are checked again after creation; any mismatch would prevent reporting completion. Existing files are preserved. The report's own final SHA256 is returned externally, avoiding a self-referential digest.

