# C0006 exact version-bound comparison — version 2

Mathematical status: self-audited.

Verdict: PASS.

This verdict compares CONTRACT_v2.md, PROOF_v3.md, BRIEF_v2.md, and AUTHOR_INPUTS_v2.md in CANDIDATES/C0006_uniform_thin_layers with AUDITS/C0006_RECONSTRUCTION_v2.md and AUDITS/C0006_RECONSTRUCTION_INPUTS_v2.md, against STATEMENT.md version 1. It applies only to the exact SHA-256 hashes recorded below. All seven observed hashes matched the supplied allowlist before substantive reading.

Both arguments prove the full finite-system contract. The reconstruction also implements the author's operative mechanism: the same two-particle Poisson potential, the same exact average over all unordered label pairs, cancellation of the additional-label interaction terms, and conditional bounded stopping. Sections 4–5 below establish equivalence of the actual potentials and generator identities; agreement of the final inequality alone is not the basis of this verdict. The brief prescribes no strategy and supplies no hints. There is no missing premise, altered parameter range, changed conclusion, or bypass of the nonautonomous-label issue in the compared arguments.

This report concerns the finite lemma only. It does not establish the full convergence statement, promote a campaign result, or constitute an outside-family audit. No outside-family verification was performed in this comparison. This file is an immutable first write; a changed comparison requires a new versioned file.

## 1. Exact claim and scope

For the definitions of the cycle, labelled generator, filtration, and pair count in CONTRACT-v2, the required conclusion is
\[
\mathbb E\left[\int_\tau^\sigma B_k(Z_s)\,ds
\;\middle|\;\mathcal F_\tau\right]
\le \binom n2\left[
\frac{2k\delta}{L+1/d}+\frac{Lk}{q}
\right]
\quad\text{almost surely}.
\]
The author proves this in Section 4 after an averaged generator identity in (3.7). The reconstruction proves it in Section 4 after its generator identity (4). Both use arbitrary initial distributions, which include all deterministic starting states.

STATEMENT-v1 concerns an accelerated mass-valued process, a scaling limit, its prescribed initial configurations, tightness, and a uniquely specified continuum law. None of those convergence assertions is a premise here. CONTRACT-v2 explicitly isolates a finite lemma with no relation between its particle number and its rate parameter. The two proofs maintain that distinction: neither assumes the campaign target or any finite-stack convergence theorem. Neither claims that this lemma alone settles any required path-law output of STATEMENT-v1. The continuum references listed in that statement were not consulted or used in this comparison.

## 2. Complete hypothesis, object, and quantifier mapping

In this table, “author” means PROOF-v3 and “reconstruction” means RECONSTRUCTION-v2.

| Contract item | Author realization | Reconstruction realization and check |
| --- | --- | --- |
| Every integer \(L\ge3\); cycle \(\mathbb T_L=\mathbb Z/(L\mathbb Z)\) | Opening fixed-parameter declaration and Sections 1–3 use the contract's cycle. | Opening claim reproduces it. Both use modular addition throughout. |
| Circular distance from the residue representative \(r\in\{0,\ldots,L-1\}\) | Retained contract notation; Section 2 uses its nonzero layer. | Opening claim repeats \(\min\{r,L-r\}\). Reflection and coordinate differences give the same distance. |
| Every integer \(n\ge2\) and every labelled state \(z\in\mathbb T_L^n\) | Section 3 derives identities at every labelled state for arbitrary \(n\). | Opening claim and Section 2 do the same. \(\binom n2\) is positive, so every normalization used is legitimate. |
| Coordinate updates \(z+\varepsilon e_i\), with \(\varepsilon\in\{-1,1\}\) | Retained definitions; direct two-particle enumeration and occupation projection preserve them. | Opening claim reproduces updates and both generators exactly. |
| Every real \(q>0\) and \(d>0\), without a relation to \(n\) | Same \(q,d\) in the two-particle and full generators; common edge factor \(q/d\) in Section 3. | Sets \(a=d^{-1}\), keeps \(q\), and divides the aggregate potential by \(2q\). No limiting or scaling argument occurs. |
| \(G_n=q(R_n+d^{-1}I_n)\), all destination labels counted separately | Occupation rate \((q/d)\eta_x(d+\eta_y)\) in (3.1), derived from the full labelled sum. | Groups the full interaction sum by unordered adjacent label pairs, explicitly including coincident other labels. |
| Both directions counted once, also on the three-site cycle | Section 1 lists the exact three-site difference rates; Section 3 counts three undirected and six directed edges. | Uses that \(1\) and \(-1\) are distinct and that each adjacent ordered label pair selects exactly one direction. |
| Every integer \(k\) with \(1\le k<L/2\) | Section 2 counts exactly \(2k\) distinct nonzero layer sites. | Section 1 counts the same disjoint residue sets. No even-cycle antipode is included. |
| \(B_k\) sums over all unordered distinct indices and excludes equality | Its pair indicator \(b\) in (2.1) vanishes at zero; (3.6)–(3.7) sum all pairs. | Its pair indicator \(\chi\) vanishes at zero; opening definition and aggregate identity use all pairs. |
| Every deterministic initial state and every initial distribution | Final paragraph and finite-state martingale construction impose no starting-law restriction. | Starts with an arbitrary probability distribution; Section 3 explicitly preserves this freedom. |
| Completed right-continuous natural filtration | Section 4 uses the usual augmentation and conditional martingale identity. | Section 3 supplies the augmentation argument from deterministic raw-filtration identities and right continuity. |
| Every deterministic real \(\delta\ge0\) | Used only through \(\sigma-\tau\le\delta\) and a nonnegative centering constant. | Same use; explicitly includes \(\delta=0\). No positive lower bound on \(\delta\) is needed. |
| Every bounded nonnegative pair of stopping times \(\tau\le\sigma\le\tau+\delta\) almost surely | Section 4 chooses a deterministic common bound and approximates both from above by dyadic stopping times. | Section 3 writes those approximations and their finite-grid martingale sum explicitly. Neither assumes independence of stopping times. |
| Conditional expectation given \(\mathcal F_\tau\), with an almost-sure bound | Equation (4.1), followed by the conditional identity for \(B_k\). | Equation (7), followed by the same conditional identity. No unconditional estimate substitutes for it. |
| Exactly the two displayed constants | \(\beta=2k/(L+1/d)\), and \(\operatorname{osc}(V)\le Lk/q\), followed by multiplication by \(\binom n2\). | \(c=2k/(L+a)\), and \(\operatorname{osc}(V)\le\binom n2 Lk/q\), with \(a=d^{-1}\). These are identical constants. |
| Uniformity, no equilibrium, separation, or selected-label autonomy | All identities are pointwise. Section 3 expressly rejects autonomous fixed-label projection. | All identities are pointwise. Third-label increments cancel in the full sum rather than being discarded. |
| Complete proof, no promoted or unproved candidate dependency | Pair equation, factorial identity, and stopped martingale argument are derived internally. | Cyclic construction, aggregate cancellation, augmentation, and bounded stopping are derived internally. |

The author's auxiliary quantifiers are also accounted for. Its occupation space \(\Omega_a\), for every integer population size \(a\ge1\), is the image of the labelled space under the occupation map. Its identity (3.3) is asserted for every real function on \(\Omega_2\); the coefficient derivation covers that full class, as checked in Section 5 below. Only the even difference potential is subsequently used. The reconstruction introduces no occupation-space premise: its all-pair sum realizes the same sampling operation directly. The symbol \(a\) in the reconstruction is the positive real number \(d^{-1}\), not the author's auxiliary population index, and the author's edge coefficients \(a_r\) have a third, explicitly defined role.

## 3. Correctness of the complete reconstructed proof

Write \(C=\binom n2\), \(a=d^{-1}\), and \(c=2k/(L+a)\). The reconstruction sets
\[
b(r)=\chi(r)-c-\frac{ac}{2}\jmath(r),
\qquad
\jmath(r)=\mathbf 1_{\{r=1\text{ or }r=-1\}}.
\]
The layer has cardinality \(2k\), and \(\sum_r\jmath(r)=2\). Hence the claimed zero sum is exactly \(2k-(L+a)c=0\). Its absolute-sum estimate follows from
\[
\sum_r|b(r)|\le\sum_r\chi(r)+Lc+\frac{ac}{2}\sum_r\jmath(r)
=2k+(L+a)c=4k.
\]
This includes the possibility that the nonzero forcing at a nearest neighbor changes sign; the argument does not assume its sign.

For its cumulative sums \(u_j\), subtracting their ordinary mean produces slopes \(s_j\) summing to zero. Thus their primitive is periodic. At residues \(1,\ldots,L-1\), the Laplacian is \(s_{r+1}-s_r=b_r\). At zero it is \(s_1-s_L=b_0\), because \(u_L=0\). These check every residue, including the wraparound equation. The bound \(|s_j|\le4k\) follows from the range of the cumulative sums. Every two cycle vertices admit a path of at most \(\lfloor L/2\rfloor\le L/2\) edges, so the primitive's oscillation is at most \(2Lk\). Reflection averaging preserves the equation, evenness of the forcing, and the oscillation upper bound. Therefore its even \(h\) is fully constructed, with
\[
\Delta h=b,\qquad \operatorname{osc}(h)\le2Lk.
\]
At zero, \(\jmath(0)=\chi(0)=0\). Evenness gives \(2[h(1)-h(0)]=-c\), and consequently
\[
\Delta h(r)+a[h(0)-h(1)]\jmath(r)=\chi(r)-c.
\]
There is no circular use of the pair equation in obtaining this relation.

For \(H(z)=\sum_{i<j}h(z_j-z_i)\), the independent part contributes twice the pair Laplacian: each pair has two coordinate moves increasing its difference and two decreasing it. For an adjacent unordered pair \(\{i,j\}\), the two interaction moves onto one another give \(2[h(0)-h(1)]\) from that pair. For each third label \(\ell\), the remaining changes are
\[
h(z_j-z_\ell)-h(z_i-z_\ell)
\quad\text{and}\quad
h(z_i-z_\ell)-h(z_j-z_\ell),
\]
whose sum is zero. Evenness justifies the orientation of each pair summand. The grouping respects the original multiplicity when several labels coincide, since each summand of \(I_n\) is indexed by a particular ordered pair. This verifies all contributions, not only configurations with distinct sites. It yields
\[
G_nH=2q(B_k-Cc),
\qquad
G_nV_R=B_k-Cc,
\qquad V_R=H/(2q).
\]
Bounding each pair summand separately gives \(\operatorname{osc}(V_R)\le CLk/q\).

The total rate bound \(q[2n+a n(n-1)]\) is valid because each ordered pair contributes to at most one direction on a cycle of size at least three. The stated Poisson-clock construction is therefore well-defined and nonexplosive. Conditioning on its finite clock count gives the displayed matrix exponential and the deterministic generator identity. The resulting martingale is bounded on every fixed finite horizon and right-continuous. For the usual augmentation, an event measurable at time \(s\) is measurable up to null events at each raw time \(s+h\). Multiplying the deterministic martingale identity at \(s+h\) by its indicator and sending \(h\downarrow0\) proves the asserted extension.

For the upper dyadic approximations, \(\tau_r\le\sigma_r\) and both decrease to their originals. The identity
\[
\{\tau_r\le t\}=\{\tau\le 2^{-r}\lfloor2^rt\rfloor\}
\]
shows both that they are stopping times and that \(\mathcal F_\tau\subseteq\mathcal F_{\tau_r}\). In the finite telescoping sum, the event \(A\cap\{\tau_r\le t_j<\sigma_r\}\) belongs to \(\mathcal F_{t_j}\). Thus each increment has zero expectation after multiplication by its indicator. Boundedness on a deterministic interval containing every approximation permits dominated convergence. This proves the conditional stopped generator identity for all the specified stopping times and every initial law.

Finally, \(c\ge0\), \(\mathbb E[\sigma-\tau\mid\mathcal F_\tau]\le\delta\), and the pointwise oscillation bound give exactly the contract. If \(\delta=0\), the time interval has zero length almost surely; the same inequality holds. No gap in the reconstructed argument is filled by an unproved assertion from the author.

## 4. The pair constructions give the same potential

The author's pair operator \(\mathcal H\) in (1.1) has independent rates \(2q\) in each cyclic direction and additional inward rate \(2q/d\) from each of \(1,-1\). Its conductance identity (1.3) is correct: at zero the incident edge coefficient cancels the vertex weight, at each neighbor the inward edge coefficient is \(1+1/d\), and all remaining ratios are one. The two edges incident to zero are distinct also for \(L=3\).

Its forcing \(g_r=m_r(\chi(r)-c)\) has zero total and positive part summing to \(2k(1-c)\le2k\). The cumulative-current range is thus at most \(k/q\). Subtracting the weighted mean enforces periodicity of the potential increments; the edge coefficients are at least one. This proves its Poisson equation and \(Lk/q\) oscillation bound with the stated constants. Reflection averaging is legitimate because both the operator and forcing commute with reflection.

Let \(v_A\) be that final even author potential, and define \(v_R=h/(2q)\) from the reconstruction. The reconstructed equation gives
\[
\mathcal H v_R
=\Delta h+a[h(0)-h(1)]\jmath
=\chi-c
=\mathcal H v_A.
\]
Both constructions have value zero at residue zero, including after reflection averaging. Their difference is harmonic for \(\mathcal H\). At a point attaining its maximum, every summand in the generator applied to the difference is nonpositive. The two nearest-neighbor summands have strictly positive rates, so a zero sum forces both neighbors also to attain the maximum. Propagating around the connected cycle makes the difference constant. Its value at zero makes that constant zero. Hence
\[
v_R=v_A\quad\text{at every residue}.
\]
This establishes equality of the actual pair potential, not merely equality of its forcing or its bound. The two finite constructions are algebraic ways to construct the same normalized function.

The author's observable is the pair average
\[
V_A(z)=C^{-1}\sum_{i<j}v_A(z_j-z_i).
\]
The reconstruction's observable therefore satisfies the exact identity
\[
V_R=C V_A.
\]
Consequently its generator equation, oscillation estimate, and stopped martingale are respectively the author's equations multiplied by \(C\). There is no change of clock or parameter hidden in the different normalization.

## 5. Averaging, dependencies, and the mechanism test

BRIEF-v2 states “No strategy hints are supplied” and reproduces CONTRACT-v2, including its neutral required-output paragraph. Thus it contains no additional advertised intermediate assertion to prove. The author manifest reports a pre-audit change of that paragraph; this comparison uses the supplied canonical contract, not any unallowlisted prior contract. No prior-version content or prior verdict was consulted.

The author's full factorial identity is nevertheless an actual ingredient of its written argument and has been checked. For an undirected edge, the independent polynomial terms are
\[
d(v-u)(\partial_u-\partial_v)J,
\]
and combining the two interaction terms gives \((v-u)^2\partial_u\partial_vJ\). The coefficients at \(u^rv^s\) of the two shifted monomials are respectively
\[
(r+1)(d+s-1),\qquad(s+1)(d+r-1),
\]
while the unshifted coefficient is \(-d(r+s)-2rs\). This confirms (3.5), including the positive sign of the \(du\partial_v\) contribution. If \(s=0\), the first shift is absent; if \(r=0\), the second is absent. When an actual departure count in the generating polynomial is zero, its rate vanishes; no negative power needs to be assigned a probabilistic meaning.

Reindexing the first shifted term by \(\ell=\xi+\delta_x-\delta_y\) yields coefficient \(\ell_x(d+\ell_y)\) and test value \(f(\ell-\delta_x+\delta_y)\), with exactly the restriction \(\ell_x\ge1\). The other term gives its reverse counterpart. The diagonal supplies the negative terms for those rates. Summation over every \(\xi\in\Omega_2\) is a finite sum and makes this valid for every real \(f\) on that space, not just the particular potential. Summing the distinct cycle edges and using the common factor \(q/d\) gives (3.3) exactly. No specialized self-duality theorem is presumed.

The reconstruction does not reproduce that general polynomial calculation. It realizes its needed application as the identical finite sampling operation: for each occupation \(\xi\), the number of unordered index pairs with that occupation is
\[
W_\xi(\eta(z))=\prod_x\binom{\eta_x(z)}{\xi_x}.
\]
Partitioning the sum over index pairs according to these occupations therefore identifies its observable divided by \(C\) with \(D_{n,2}f_{v_R}\). Section 2 of the reconstruction evaluates the full generator of this observable, explicitly cancels every third-label term, and obtains exactly the application of (3.3) used in the author's (3.7). Section 4 of this report proves that the potential in this application is the same function as the author's.

The direct cancellation and the coefficient calculation are two descriptions of the same aggregate averaging step. Both pair each interaction from one label to an adjacent destination label with its reverse, and both remove the resulting effects on other pair summands. The reconstruction does not replace that step by a selected-label autonomy assertion, an equilibrium estimate, a different bound, or a new mathematical premise. It proves the operative aggregate identity pointwise with all additional-label terms present. The author's stronger general-function identity is fully derived in the author proof and checked above; it is not a separate required output of the contract or brief. Its unused extra generality is not a missing conclusion of the reconstruction.

Accordingly the mechanism test passes. This is not an unrelated alternate proof of the same numerical inequality: the potentials are equal, the aggregate sampling observables are equal after the explicit factor \(C\), and the generator and conditional martingale identities coincide after that factor. No changed claim, changed dependency, or disputed generator contribution is being excused by the existence of another argument. Had the reconstruction discarded the third-label terms, used an autonomous fixed pair, or changed the effective \(q\), this correspondence would fail; the displayed equalities rule out each of those possibilities here.

The complete mathematical dependency list is finite cyclic summation and its oscillation bound, finite polynomial coefficient extraction and reindexing in the author proof, exact aggregate generator cancellation in the reconstruction, finite-state transition-matrix differentiation, filtration augmentation, and bounded stopping-time approximation. The substantive uses are proved in the supplied arguments and checked above. There are no promoted dependencies and no literature dependencies. The exposure paths listed inside the author manifest describe provenance; their mathematical assertions were not imported as premises or independently certified by this report.

## 6. Complete actual-input and operation manifest

The following are the only source files actually opened or hashed by this comparator. Paths are relative to the supplied workspace. Every hash below was computed locally before the first substantive read and matched the assignment.

| Actual source input | Verified SHA-256 |
| --- | --- |
| STATEMENT.md | ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97 |
| CANDIDATES/C0006_uniform_thin_layers/CONTRACT_v2.md | 805ea9a15da4e350f0af208075932c45473a8f499a89f77f050c6c916c4891b9 |
| CANDIDATES/C0006_uniform_thin_layers/PROOF_v3.md | 9a4e9936a55b8e4179c3c964eb297236ac06d008425bb64f9e48eb4856dc4186 |
| CANDIDATES/C0006_uniform_thin_layers/BRIEF_v2.md | 48c8eb60d02da1a0a186d5d040a48e3c8b12bfd7fda553352feb29e9f1848086 |
| CANDIDATES/C0006_uniform_thin_layers/AUTHOR_INPUTS_v2.md | 502f46c6cf2b3ebe1df16574e164f3283f1041322678e47f89de3e200e3ea4f9 |
| AUDITS/C0006_RECONSTRUCTION_v2.md | 2825af0de39851170c391f4bdacb8cfa1029e880e58414ddc4d69a1160faa07d |
| AUDITS/C0006_RECONSTRUCTION_INPUTS_v2.md | 899683f7dde4729bebff46d6a1bd2f36fa629a4f584da1c0da7574a7a8d30396 |

The complete additional exposure was the parent assignment specifying this exact allowlist and its hashes, the comparator role and verdict requirements, the assertion that there are no promoted dependencies, the required output path, and the requirements to check mathematical correctness, exact quantifiers, mechanisms, dependency changes, and actual exposure. The general session instructions, user mathematical-rigor and LaTeX instructions, workspace context, available tool descriptions, and installed-skill catalog were visible. No parent defense or additional mathematical argument was requested or received. Two outgoing progress messages reported the comparison's own findings. No other agent supplied mathematical material.

The first administrative shell call returned the workspace path and all seven hashes. An independent batch of cat reads requested all seven authorized inputs. Its combined displayed output was truncated; the brief and author manifest were therefore reread separately in full, and the proof was reread in the two ranges 1–180 and 180–340, covering it completely with overlap. The statement, contract, reconstruction, and reconstruction manifest were visible in full in the original batch. No referenced path or literature URL inside any input was followed. No directory inventory, other audit, registry, FAILED or PROVED record, prior version, other candidate, route, search transcript, or unallowlisted source was opened.

A nonexistence test for AUDITS/C0006_COMPARISON_v2.md succeeded before this add-file write. It was an administrative existence check, not a source read. The report was written as literal patch text. Its final hash is returned separately to the parent to avoid a self-referential hash. Any verification of this new output's hash or text is administrative output verification only. No existing file was overwritten. No mathematical program, simulation, symbolic solver, inline-stdin mathematical calculation, web lookup, or subagent was used. All mathematical comparisons and the finite maximum-principle argument above were reasoned directly.

## 7. Exact verdict boundary

PASS means that the complete reconstruction proves CONTRACT-v2, the author proof proves that same contract, every required quantifier and constant agrees, and their operative pair-potential and aggregate-generator mechanism agrees as demonstrated above. It does not attach this verdict to an earlier version, another candidate, an exposure path that was not read, or the full target in STATEMENT-v1. There is no unresolved mathematical or mechanism discrepancy within this exact compared tuple.
