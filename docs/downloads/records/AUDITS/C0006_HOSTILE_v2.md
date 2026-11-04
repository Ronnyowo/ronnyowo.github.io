# C0006 hostile audit — immutable version 2

**Verdict: PASS, bound exclusively to CONTRACT-v2 and PROOF-v3 at the hashes below.**

This verdict concerns the exact finite conditional occupation inequality. It neither proves STATEMENT-v1 nor promotes this lemma or any other mathematical status. No applicable defect or missing mathematical premise was found. The campaign checklist is not edited or globally discharged by this report.

## 1. Exact inputs and complete exposure

The following four files were the only mathematical inputs opened. Their SHA-256 hashes were verified before the audit:

| Input | SHA-256 |
|---|---|
| `STATEMENT.md` | `ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97` |
| `CANDIDATES/C0006_uniform_thin_layers/CONTRACT_v2.md` | `805ea9a15da4e350f0af208075932c45473a8f499a89f77f050c6c916c4891b9` |
| `CANDIDATES/C0006_uniform_thin_layers/PROOF_v3.md` | `9a4e9936a55b8e4179c3c964eb297236ac06d008425bb64f9e48eb4856dc4186` |
| `AUDITS/CHECKLIST_AC005.md` | `d328652a06ff5ef7fa9ae64a70011a3060b32e80cc23b0afbce4cf1fca97c170` |

Additional exposure was limited to the parent assignment, the supplied user/developer instructions and tool descriptions, administrative hash output, and an existence check confirming that this output path did not already exist. The parent assignment stated that leakage had passed; no leakage report or brief was supplied or opened, and that statement is not a mathematical premise. The names and summaries of prior versions, provenance records, routes, and other candidates appearing inside the four allowed files were necessarily visible. None of those other documents was opened, and none of their asserted results was used.

There were no promoted dependencies, author messages or defenses, other audit reports, route documents, reconstructions, registry/FAILED/PROVED files, inventories, or unallowlisted references in the exposure. No subagent was used. No external search, exact-problem/open-status search, literature retrieval, mathematical program, numerical experiment, simulation, or inline stdin computation was performed. Tools were used only to read the four inputs, hash files, check the output path, and write this report. Mathematical checking consisted of the symbolic arguments recorded below. No outside mathematical reference was needed; finite-state Markov conditioning, finite sums, matrix differentiation, and dominated convergence are the elementary background used, with the conditional stopping argument detailed below.

This file is written once. Any subsequent correction must be a separately numbered version.

## 2. The exact assertion audited

For every finite choice
\[
L\ge3,\qquad n\ge2,\qquad q>0,\qquad d>0,
\qquad 1\le k<L/2,
\]
with integer \(L,n,k\), every initial distribution of the specified labelled chain, every deterministic real \(\delta\ge0\), and every pair of bounded nonnegative stopping times with
\[
\tau\le\sigma\le\tau+\delta,
\]
the claim is
\[
\mathbb E\left[\int_\tau^\sigma B_k(Z_s)\,ds
\;\middle|\;\mathcal F_\tau\right]
\le \binom n2\left[
\frac{2k\delta}{L+1/d}+\frac{Lk}{q}\right]
\quad\text{almost surely}.
\]
The proof establishes precisely this assertion. In particular, its \(k\) is a positive-layer width, not the initial-stack-count parameter of STATEMENT-v1. There is no relation imposed between the population \(n\) and the rate \(q\).

## 3. Pair generator, edge multiplicity, and Poisson equation

### 3.1. Difference rates and the small torus

For two labels, increasing the difference \(r=z_2-z_1\) by one can result from either the positive move of label 2 or the negative move of label 1. Decreasing it has the other two independent moves. Consequently both independent difference rates are \(2q\).

At \(r=1\), the two directed jumps that place one label on the other both send the difference to zero, so their additional rates sum to \(2q/d\). The same holds at \(r=-1\), with no interaction at \(r=0\). This proves (1.1), including its factors of two. Since \(L\ge3\), the residues \(1\) and \(-1\) differ. For \(L=3\), their connecting edge is the ordinary edge opposite zero and has no additional collision rate. Thus the proof does not duplicate an interaction at the smallest allowed torus.

With the weights in (1.2), the coefficient of the positive increment in (1.3) is \(2qa_r/m_r\), and the negative-increment coefficient is \(2qa_{r-1}/m_r\). At zero both ratios are one; at each nonzero neighbor of zero precisely its inward ratio is \(1+1/d\). All other ratios are one. These are exactly the rates just derived. This checks (1.2)–(1.3) also when there are only three edges.

### 3.2. Solvability and the exact uniform constant

Because \(k<L/2\), the sets of residues \(1,\ldots,k\) and \(L-k,\ldots,L-1\) are disjoint and nonzero. Thus the layer has exactly \(2k\) residues, including when it occupies all nonzero residues of an odd torus. With
\[
\beta=\frac{2k}{L+1/d},\qquad g_r=m_r(b(r)-\beta),
\]
one has \(0<\beta<1\), and
\[
\sum_r m_r=L+1/d,\qquad
\sum_r m_rb(r)=2k,\qquad
\sum_r g_r=0.
\]
The only positive \(g_r\)'s are the layer values \(1-\beta\). Hence
\[
\sum_r(g_r)^+=2k(1-\beta)\le2k.
\]
The total magnitude of the negative part is the same. In particular the large weight \(m_0=1+1/d\) introduces no unbounded flux estimate: the full signed source has zero sum and total positive mass at most \(2k\).

For the partial sums \(S_r=(2q)^{-1}\sum_{j=0}^r g_j\), the difference of any two values is a signed interval sum. Its magnitude is at most \((2q)^{-1}\sum_r(g_r)^+\le k/q\), which proves (2.3)–(2.4), including the cyclic increment at zero because \(S_{L-1}=0\).

The weighted average \(\overline S\) uses positive weights \(1/a_r\), so it lies between the extremal partial sums. Consequently \(J_r=S_r-\overline S\) satisfies all three conclusions in (2.5): the required divergence, zero weighted circulation, and \(|J_r|\le k/q\). The zero circulation makes the increments
\[
v(r+1)-v(r)=J_r/a_r
\]
periodic. Substitution in (1.3) gives
\[
\mathcal Hv(r)
=\frac{2q}{m_r}(J_r-J_{r-1})
=b(r)-\beta.
\]
This verifies (2.6)–(2.7) without an unproved solvability assertion. Every \(a_r\ge1\), so each increment has magnitude at most \(k/q\); joining two vertices by at most \(L\) edges gives exactly the sufficient bound
\[
\operatorname{osc}(v)\le Lk/q.
\]
There is no factor of two missing in this bound: it bounds the difference between any two values by summing increments along a path.

Reflection commutes with the displayed difference generator and leaves \(b\) invariant. Averaging \(v(r)\) and \(v(-r)\) therefore preserves the Poisson equation and keeps every new value in the old value range. The proof thereafter needs only this equation, evenness, and the oscillation bound; it does not mistakenly require that the original unsymmetrized flux formula remain unchanged. All of Section 2 survives \(d\) or \(q\) arbitrarily close to zero or arbitrarily large, provided they remain positive and finite.

## 4. The averaged identity and its diagonal terms

### 4.1. Occupation rates and sampling

At a source site \(x\), summing the rates of its \(\eta_x\) labels to a neighboring site \(y\) gives
\[
q\eta_x(1+\eta_y/d)=\frac qd\eta_x(d+\eta_y).
\]
This verifies (3.1) and the projection identity. A source with zero occupation contributes no transition, as follows directly from this sum over labels and as explicitly stated in the proof's edge calculation. No test function at a negative occupation is needed.

For a two-particle occupation \(\xi\), the weight
\[
W_\xi(\eta)=\prod_x\binom{\eta_x}{\xi_x}
\]
is exactly the number of unordered pairs of distinct physical indices producing \(\xi\). In particular, a same-site pair is counted by \(\binom{\eta_x}{2}\), not by \(\eta_x^2/2\); at two distinct sites the weight is \(\eta_x\eta_y\). Every unordered index pair contributes to exactly one \(\xi\), proving the normalization \(\sum_\xi W_\xi=\binom n2\). This checks the sampled-index diagonal correction and (3.2).

### 4.2. Edgewise coefficient calculation

For one undirected edge with populations \(A,B\), the two directed increments of \((1+u)^A(1+v)^B\) give, after separating the factors \(d\) and \(AB\),
\[
\mathcal L^{xy}J
=d(v-u)(\partial_u-\partial_v)J
 +(v-u)^2\partial_u\partial_vJ.
\]
The mixed contribution is positive: its two directed terms combine to
\[
AB(v-u)^2(1+u)^{A-1}(1+v)^{B-1}.
\]
Zero departure populations are interpreted through the zero transition or polynomial derivatives, so no negative exponent is required as an independent object. This verifies (3.4).

Expanding the first differential operator gives the two positive shift terms \(dv\partial_u\) and \(du\partial_v\), and the two negative diagonal terms \(-du\partial_u\) and \(-dv\partial_v\). Expanding the second gives \(v^2\partial_u\partial_v\), \(u^2\partial_u\partial_v\), and \(-2uv\partial_u\partial_v\). At coefficient \(u^rv^s\), these are respectively
\[
\begin{aligned}
&(r+1)(d+s-1)W_{\xi+\delta_x-\delta_y},\\
&(s+1)(d+r-1)W_{\xi-\delta_x+\delta_y},\\
&-[d(r+s)+2rs]W_\xi.
\end{aligned}
\]
This is (3.5). If \(s=0\), the first shift is absent; if \(r=0\), the second is absent. Whenever a shift is present its factor \(d+s-1\) or \(d+r-1\) is positive. Thus parameters \(0<d<1\) do not create a negative transition coefficient at a boundary.

For the first shift, setting \(\ell=\xi+\delta_x-\delta_y\) turns its coefficient into \(\ell_x(d+\ell_y)\) and its test into \(f(\ell-\delta_x+\delta_y)\). This substitution is a bijection onto terms with \(\ell_x\ge1\). The reverse shift has the analogous coefficient \(\ell_y(d+\ell_x)\), and the unshifted part supplies exactly the negative terms. Therefore summing against \(f\) proves the claimed edgewise intertwining without dropping boundary terms.

For \(L\ge3\), equality of two unordered edges \(\{x,x+1\}\) and \(\{y,y+1\}\) either gives \(x=y\) or forces \(2=0\) modulo \(L\); the latter is impossible. Hence there are \(L\) distinct undirected edges, whose orientations reproduce all \(2L\) directed edges exactly once. Multiplication by the same \(q/d\) and division by \(\binom n2\) then prove (3.3). The argument uses the same \(q,d\) before and after sampling.

### 4.3. Application to the potential

Evenness of \(v\) makes \(v(z_2-z_1)\) invariant under exchange of its two labels, so it is a well-defined function of the two-particle occupation, including at equality. The sampling interpretation gives (3.6). Applying the just-proved identity and the pair Poisson equation therefore gives, at every labelled state,
\[
G_nV=\binom n2^{-1}B_k-\beta.
\]
This establishes (3.7) for arbitrary configurations, including any number of coincident labels and adjacent occupied sites. No selected pair is asserted to evolve autonomously. The cancellation of interactions with unsampled labels is justified by the edgewise polynomial calculation for the average over every unordered index pair.

Since this average is convex,
\[
\min v\le V(z)\le\max v,
\qquad
\operatorname{osc}(V)\le\operatorname{osc}(v)\le Lk/q.
\]
Thus (3.8) introduces no extra population factor; the sole factor \(\binom n2\) is restored at the final step.

## 5. Conditional stopping argument and uniform quantifiers

For \(L\ge3\), a fixed ordered pair of distinct labels can occupy at most one of the two directed adjacency relations from its source. Summing yields the total-rate bound
\[
2qn+(q/d)n(n-1).
\]
The finite chain is consequently nonexplosive and has right-continuous paths; \(V\) and \(G_nV\) are bounded. The finite matrix semigroup identity gives the deterministic-time martingale
\[
M_t=V(Z_t)-V(Z_0)-\int_0^tG_nV(Z_s)\,ds.
\]
For completeness, the passage to the completed right-continuous natural filtration is valid here: the deterministic-time martingale identities extend to the completion because null sets do not change expectations. If an event belongs to the right-continuous enlargement at time \(s\), it belongs to the completed filtration at every \(u>s\). For \(s<u<t\), multiply the identity for \(M_t-M_u\) by its indicator and let \(u\downarrow s\). Right continuity and boundedness on a deterministic time interval give the identity for \(M_t-M_s\) by dominated convergence. No larger filtration or independent additional information is assumed.

Choose a deterministic bound \(T\) for the two stopping times and set
\[
\tau_j=2^{-j}\lceil2^j\tau\rceil,
\qquad
\sigma_j=2^{-j}\lceil2^j\sigma\rceil.
\]
These are finitely valued stopping times bounded by \(T+1\), satisfy \(\tau_j\le\sigma_j\), decrease to their respective original times, and have \(\mathcal F_\tau\subseteq\mathcal F_{\tau_j}\). For finite grid times, writing the stopped martingale difference as the sum of successive martingale increments multiplied by the events that the increment lies between the two stopping times proves its conditional expectation is zero. In particular,
\[
\mathbb E[H(M_{\sigma_j}-M_{\tau_j})]=0
\]
for every bounded \(\mathcal F_\tau\)-measurable \(H\). The deterministic bound
\[
|M_t|\le2\|V\|_\infty+(T+1)\|G_nV\|_\infty,
\qquad 0\le t\le T+1,
\]
and pathwise right continuity permit dominated convergence. Thus
\[
\mathbb E[M_\sigma-M_\tau\mid\mathcal F_\tau]=0,
\]
which is exactly (4.1). The approximating stopping times need not themselves satisfy the original duration constraint; that constraint is used only after taking the limit. There is no gap from conditioning at \(\tau\) rather than at an approximating time, and no stopping-time independence is used.

Substitution gives the exact conditional equality
\[
\binom n2^{-1}
\mathbb E\left[\int_\tau^\sigma B_k(Z_s)\,ds
\;\middle|\;\mathcal F_\tau\right]
=\beta\mathbb E[\sigma-\tau\mid\mathcal F_\tau]
 +\mathbb E[V(Z_\sigma)-V(Z_\tau)\mid\mathcal F_\tau].
\]
The pointwise inequalities \(\sigma-\tau\le\delta\) and \(V(Z_\sigma)-V(Z_\tau)\le\operatorname{osc}(V)\), together with \(\beta>0\), give precisely the contracted upper bound. Its constants are deterministic and independent of the initial distribution and of the values of the stopping times. The case \(\delta=0\) has \(\sigma=\tau\) almost surely and zero occupation integral. The case \(n=2\) has \(\binom n2=1\), so all normalizations remain defined. No stationarity, separation, absolute continuity, positive mass, or parameter scaling premise occurs anywhere in the argument.

## 6. All 29 checklist items: applicability and audit-local assessment

“Not claimed” below means that the item concerns a mathematical conclusion or construction outside this finite lemma. It is not a claim that the campaign-level obligation has been met.

| Item | Applicability and finding |
|---|---|
| AC-001-01 | Applicable to finite rates and constants: passed. The pair rate is \(2q\), the attraction rate is \(2q/d\), and the denominator is \(L+1/d\). No value of \(\rho\) or \(\alpha\), or conversion to a microscopic acceleration, is asserted. |
| AC-001-02 | Scope check: passed. The output is explicitly a finite auxiliary estimate; full mass path-law convergence is not claimed. |
| AC-001-03 | Applicable to finite-start uniformity: passed for every labelled state and law, with no separation or mass restriction. The initial-stack quantifiers of the full target are not themselves proved by this lemma. |
| AC-001-04 | Applicable: passed by (3.3)–(3.7). Uniform averaging over distinct physical index pairs is proved; fixed physical tags are not treated as autonomous. |
| AC-001-05 | Not claimed. There is no weak convergence step or inference concerning discontinuous indicators from a path limit. |
| AC-001-06 | Not claimed. No continuum pair or higher-order split law is identified. |
| AC-001-07 | Applicable as a check against an assumed compatibility step: passed. The global finite generator identity is proved at every tuple by exact algebra. No stratum-gluing or intersecting-corrector premise is introduced. |
| AC-001-08 | Applicable: passed. The bound is obtained from a pointwise finite Poisson identity and a global deterministic oscillation bound, not from equilibrium or an integrated estimate over starts. |
| AC-001-09 | Not claimed. No continuum core, density assertion, or boundary-determining smooth test class is used. The finite edge identity holds for every real two-particle occupation function. |
| AC-001-10 | Applicable only to the stopping-time estimate requested here: passed in Section 5. Aldous tightness, compact containment, and continuity of limiting mass paths are not claimed. |
| AC-001-11 | Not claimed. No moment convergence or full path-law identification is inferred. |
| AC-001-12 | Applicable to the finite coordinate changes: passed. Labelled occupations, unordered sampling, exchange symmetry, and torus differences are accounted for exactly. Continuum kernel-flow identification is not claimed. |
| AC-001-13 | Applicable: passed. The Poisson solution and averaged identity are constructed and proved within the allowed proof; no unproved candidate or theorem-strength recurrence is used. |
| AC-001-14 | Applicable procedurally: passed. No external search was performed and no Mosco argument is used. |
| AC-001-15 | Applicable procedurally: passed within this audit's exposure. Only the allowed statement, contract, proof, and checklist were read; no route, other audit, reconstruction, or author-defense material was consulted. This does not independently recertify another worker's exposure. |
| AC-001-16 | Applicable procedurally: this report is version-bound and makes no promotion. There is no promoted or unpromoted external mathematical premise. |
| AC-002-17 | Not claimed. No identity is integrated against a random atomic measure and no spatial exceptional-set argument is used. |
| AC-002-18 | Applicable only to finite path regularity in the stopping argument: passed using actual right-continuous chain paths and continuous time integrals. No continuous-modification or continuum indistinguishability assertion is made. |
| AC-003-19 | Not claimed. No random kernel evaluation or independent-noise sigma-field occurs. |
| AC-003-20 | Applicable procedurally: passed. No mathematical computation tool, simulation, numerical experiment, or rerun was used as evidence. Hashing and text/file administration are the only tool-assisted operations. |
| AC-003-21 | Fully applicable: passed. Section 5 verifies the conditional bounded-stopping-time identity and the exact constants uniformly over all microscopic states and initial laws. |
| AC-003-22 | Applicable to finite-circle multiplicity and sampled-index diagonals: passed in Sections 3–4. The proof is an exact finite identity; a determining all-orders generator class is not claimed. |
| AC-004-23 | Applicable to the layer's scope: passed. The source has \(b(0)=0\), and the conclusion bounds positive distances only. It is neither applied to exact equality occupation nor multiplied by an unbounded defect. |
| AC-004-24 | Fully applicable: passed. The particle order is \(n\); the rate parameter \(q\) remains unchanged when sampling two particles. No relation with an acceleration parameter is inserted. |
| AC-004-25 | Not claimed. No trace process, trace clock, absorption estimate, or excursion transfer occurs. |
| AC-004-26 | Not claimed. No decoupling of local harmonic corrections, surviving first-order action, or coordinate brackets is asserted. The interaction cancellation actually needed is proved by the finite averaged identity. |
| AC-004-27 | Not claimed for target generators or real-line wrapping. All identities used are pointwise on the specified finite torus, and its edge cases are checked directly. |
| AC-004-28 | Not claimed. There is no accumulation of cellwise errors, collision-cell decomposition, or entrance-state approximation. |
| AC-005-29 | Not claimed. No extra-jump count, terminal return, geometric-tail bound, or endpoint coupling appears in the proof. |

## 7. Final determination

The refutation attempts addressed rate and edge duplication, the positive-layer exclusion of equality, the Poisson centering and its uniform constant, boundary coefficients with small \(d\), same-site sampling diagonals, dependence on unsampled labels, arbitrary collision configurations, right-continuous filtration completion, adaptive stopping times, and all finite parameter and initial-law quantifiers. The explicit identities above resolve these issues without adding a premise.

**PASS for the exact hashed CONTRACT-v2 / PROOF-v3 pair.** There are no mathematical reservations within that finite claim. The result of this audit alone advances no campaign mathematical status and supplies no assertion of completion of STATEMENT-v1.
