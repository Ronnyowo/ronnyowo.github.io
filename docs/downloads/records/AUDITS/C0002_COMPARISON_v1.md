# C0002 comparison audit — v1

**Verdict: PASS, bound exclusively to the versions and SHA-256 hashes below.**

The independent reconstruction proves CONTRACT-v1 completely and implements the mechanism specified by BRIEF-v1. Its stopping-time argument differs from the author's cutoff construction, but the accepted brief specifies only the resolvent definition, stopping-time tightness, and path-law identification. Both derivations use that mechanism. The reconstruction adds no hypothesis or campaign dependency and leaves no required path-law step conditional. This verdict follows from the checks below, not from similarity of the final conclusions.

This is a comparison verdict on an auxiliary candidate. It neither promotes C0002 nor certifies STATEMENT-v1, a leakage audit, a hostile audit, or any system-specific resolvent estimate. No other audit was read.

## Exact input and exposure manifest

All relative paths in this document are relative to the exact workspace root:

`[private workspace]`

| Key | Exact source | Version and role | Bytes | SHA-256 |
| --- | --- | --- | ---: | --- |
| S | `STATEMENT.md` | Frozen statement v1; campaign boundary | 6511 | `ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97` |
| C | `CANDIDATES/C0002_resolvent_path_transfer/CONTRACT_v1.md` | Exact auxiliary claim contract v1 | 2121 | `d42cb0e8db6e9667f77d45f7e4d54994179e48b206fb343af6e50eaf67057c6b` |
| B | `CANDIDATES/C0002_resolvent_path_transfer/BRIEF_v1.md` | Accepted reconstruction brief v1 | 351 | `ec44f79e9849a71bc2cad4d75978ffdde78b8748c83bbeb5e991d4529a92b192` |
| P | `CANDIDATES/C0002_resolvent_path_transfer/PROOF_v2.md` | Candidate author proof v2 | 7368 | `dc06b8b7e052bc994905afaa3b7fe168d7cde233dfa52e5e0355f5458c809a06` |
| A | `CANDIDATES/C0002_resolvent_path_transfer/AUTHOR_INPUTS_v1.md` | Author exposure manifest v1 | 1970 | `a322ca4a495d06567b9e6e0e4aa317fc411d6a1af630dc970354f05078147973` |
| V | `CANDIDATES/C0002_resolvent_path_transfer/VERSION_NOTE_v2.md` | Binding of P-v2 to C-v1, B-v1, A-v1 | 548 | `9d8681bf0fc841aac101a5afc0108101441e83621d6220738d6c6b111647dede` |
| R | `AUDITS/C0002_RECONSTRUCTION_v1.md` | Independent reconstruction v1 | 15297 | `28a6115917c3c793a923dcd34c168f8c17d28fdf1ec23083979c1bd688c624d8` |
| I | `AUDITS/C0002_RECONSTRUCTION_INPUTS_v1.md` | Reconstruction exposure manifest v1 | 4187 | `39fccaa850ba5593aaa475bddd2e3150c39f7a13c8a8d2c02b519ba279a6de75` |

References such as R:118–120 designate one-based source lines in the exact hashed file. All eight files were read in full and hashed. C, B, P, and R were additionally read with line numbers. All eight hashes and byte counts were rechecked immediately before exclusive creation of this report.

Promoted dependencies: **none**.

The comparator's complete source exposure was the eight files above; the fresh-comparator dispatch and its allowlist; general system/developer instructions and tool descriptions; the user's rigorous-mathematics and renderer-safe-LaTeX instructions; workspace/environment metadata; tool results from reading and hashing the same eight files; and this comparator's own analysis and output-generation checks. No inherited campaign conversation was used as mathematical input. No directory listing, workspace search, other candidate, author proof v1, hostile/leakage audit, search transcript, registry, or other audit was consulted. No web page or embedded literature link was opened. No subagent was spawned and no cross-agent mathematical input was received. The final response returns the result to the assigning parent.

A reports exposure to Kim–Landim source and bibliographic searches; those are author-exposure facts reported by A, not sources consulted or premises adopted here. I's three source hashes agree exactly with S, C, and B, and I's recorded reconstruction hash agrees with R. Those consistencies have been verified. This comparison cannot independently reconstruct an agent's undisplayed access history; the statements about that history in A and I remain the respective agents' declarations.

A describes the initial v1 freeze. V explicitly binds the current P-v2 to unchanged C-v1 and B-v1 while retaining A-v1. The v1/v2 naming is therefore not an unresolved contract-version mismatch. The assertion that the v1-to-v2 edit was exclusively typographic was not independently diff-checked, because P-v1 was outside the allowlist; the present verdict evaluates P-v2 itself.

## Complete claim, hypothesis, object, and output mapping

| Contract obligation or quantified object | Candidate evidence | Reconstruction evidence and check |
| --- | --- | --- |
| Arbitrary compact metric space \(E\), with its specified metric \(d\) (C:6) | P:13, 35, 37 | R:15 adopts the exact contract; R:139–162 uses a finite metric net and compact containment, with no linear structure or extra geometry. Compact metric spaces are Polish, as required for the probability compactness tools. |
| Conservative, strongly continuous Feller semigroup \(P_t\) on \(C(E)\) (C:6) | P:6, 15, 67 | R:25–42 uses contraction and strong continuity; R:200 uses continuity of resolvent functions; R:271 and 287 use strong continuity and the Feller property. No stronger time regularity or generator-core hypothesis is introduced. |
| Specified continuous-path Markov law \(Q_x\) for every \(x\in E\) (C:6) | P:69 | R:287–289 compares the recursion with this same Markov law. Its continuous-path property is used when identifying laws from coordinate distributions. Existence of this law is a contract assumption, not an additional lemma. |
| Every positive integer \(N\), arbitrary finite \(S_N\), microscopic chain \(Z_N\), generator \(A_N\), and semigroup \(T_N\) (C:8) | P:6–8, 27, 41–45 | R:44–49, 84–97, 166–170, 192–223. No irreducibility, reversibility, stationarity, invariant law, common state space, or uniform rate bound is used. Finite-state nonexplosion and bounded finite-horizon Dynkin martingales are sufficient. |
| Arbitrary map \(\pi_N:S_N\to E\), and exactly \(X_N=\pi_N(Z_N)\) (C:8) | P:6, 35, 46–50 | R:15–21, 53–61, 231. No injectivity, Markov property of the projection, or microscopic reconstruction from \(X_N\) is assumed. A map from a finite discrete space is measurable, and its image of a finite-state chain is cadlag. |
| Positive-discount continuum and microscopic resolvent definitions for every positive parameter (C:6, 8) | P:6–8, 15, 60–67 | R:25–49, 194–208, 256–278. The sign in \(A_NR_\lambda^N=\lambda R_\lambda^N-I\) agrees with the contract; all integrations use \(e^{-\lambda t}\). |
| For every \(\lambda>0\) and every \(g\in C(E)\), uniform microscopic resolvent approximation (C:10–11) | P:6, 15–19, 41–46 | R:63–78 and 200–208. Parameters and finitely many functions are fixed before taking \(N\to\infty\). Using \(g^2\) introduces no assumption because \(g^2\in C(E)\). Real-valued tests suffice; complex tests, if desired, split into real and imaginary parts. |
| Supremum over every state of \(S_N\), without a restricted good set (C:11, 16) | P:22–35 | R:59–78, 122–159. All error bounds are full-state supremum bounds, so they apply even after arbitrary bounded stopping times and under any microscopic initial distribution. No typical-state or equilibrium substitution occurs. |
| Maximum projected jump along positive-rate transitions tends to zero, with empty-set value zero (C:12) | P:37 | R:166–186 defines exactly that maximum, explicitly includes the empty case, and proves the continuous-limit consequence. Omitting \(z=w\) has no effect, since a diagonal pair has projected distance zero and is not an off-diagonal transition. |
| Every deterministic initial sequence \(z_N\in S_N\) with \(\pi_N(z_N)\to x\) (C:14) | P:41, 69 | R:17–21 and 188. The estimates are uniform in initial states, and evaluation at time zero identifies \(X(0)=x\). No distributional regularity or additional convergence rate is used. |
| Tightness at stopping times, not merely fixed-time control (C:14; B:7) | P:22–35 | R:84–162 proves the stronger condition for any two microscopic stopping times \(\tau\leq\sigma\leq\tau+\delta\), with \(\tau\leq T\), uniformly in the initial state. The finite-net probability bound explicitly gives metric increments. |
| Every finite horizon and the whole half-line (C:14) | P:35, 37, 69 | R:84, 162, 186, 291–298. \(T\) is arbitrary; compact containment and the stopping-time bound give the local half-line Aldous criterion. No large-time estimate beyond boundedness and exponentially discounted integration is required. |
| Tightness in the Skorokhod \(J_1\) topology and limits supported on continuous paths (C:6, 14) | P:35–37 | R:162–188 gives tightness and the deterministic time-change jump inequality. This addresses the stated topology, rather than only a weaker path or occupation-measure topology. |
| Unique identification of the specified full path law (C:14; B:7) | P:41–69 | R:192–298 passes resolvent martingale identities with past-cylinder multipliers, inverts the resulting Laplace transforms, recursively identifies all finite-dimensional laws, and then identifies the continuous path law. |
| No projected Markov assumption (C:14) | P:35, 46–50 | R:84–97 uses microscopic optional stopping; R:218–240 removes microscopic approximants by a uniform error before passage to the projected path limit. The limiting transition recursion is proved, not assumed. |
| No uniform-in-time microscopic semigroup-convergence hypothesis (C:16) | P:6–35, 41–69 | R:25–162, 192–298 uses only the stated resolvent convergence. Strong continuity of the fixed target semigroup is not a microscopic semigroup-convergence assumption. |
| No promoted campaign dependency (C:4, 18; B:5) | P:4, 71 | R:13, 302–313 and I. All substantive auxiliary estimates are supplied in R. |
| Auxiliary claim only; no establishment of SIP resolvent hypotheses or STATEMENT-v1 (C:3, 16) | P:71 | R:3, 311–313. The frozen microscopic scaling, all finite-stack initial conditions, target sticky-flow conventions, and full mass-process conclusion in S remain outside this lemma's proved assertions. |

The last row is a scope boundary, not a defect in C0002. Both C and B request the abstract transfer lemma. Neither P nor R presents that lemma as a proof of the campaign's microscopic assumptions, changes S to fit the lemma, or asserts the continuum conventions in S have been checked here.

## Mathematical verification of the reconstruction

### 1. Resolvent estimates and generator identities

R:25–49 is valid. Contraction gives the resolvent norm bounds. For any fixed small \(h>0\), the approximation-of-identity error is bounded by
\[
\sup_{0\leq t\leq h}\|P_tg-g\|_\infty
+2\|g\|_\infty e^{-rh}.
\]
First choose \(h\) by strong continuity, then send \(r\to\infty\). This proves R:(1) without a rate assumption. Finite-state semigroup differentiation gives
\[
\int_0^\infty e^{-rt}A_NT_N(t)b\,dt
=\left[e^{-rt}T_N(t)b\right]_{0}^{\infty}
+rR_r^Nb
=rR_r^Nb-b.
\]
For fixed \(r\), multiplying the contract's resolvent error by \(r\) still gives an error tending to zero. This proves R:(3) and R:(4). Since \(\|F_N\|_\infty\leq M\) and \(\|H_N\|_\infty\leq M^2\), R:(2) yields the constants \(2rM\) and \(2rM^2\) in R:(5).

### 2. Optional stopping and the precise tightness estimate

At R:84–97, both stopping times are bounded by \(T+1\). For a fixed finite chain and bounded \(V\), the stopped Dynkin martingale is integrable and has bounded magnitude on that horizon, using the finite number \(\|A_NV\|_\infty\). Optional stopping after multiplication by bounded \(\mathcal F_\tau^N\)-measurable \(B\) proves R:(6). There is no uniform-in-\(N\) optional-stopping assertion here; the uniform bounds are introduced afterward using R:(5).

Replacing \(G^2\) by \(H_N\) at its two endpoint evaluations costs at most \(2b_N\). The integral costs \(2rM^2\delta\). Replacing the two occurrences of \(G\) in the increment multiplied by \(G_\tau\) costs \(2Ma_N\), and its integral costs \(2rM^2\delta\). Therefore
\[
\mathbb E[(G_\sigma-G_\tau)^2]
\leq 2b_N+4Ma_N+6rM^2\delta,
\]
exactly as R:(9) states. Signed real test functions cause no problem: absolute values and \(|G_\tau|\leq M\) justify each bound.

The limit order at R:124–135 is essential and correct: first take the uniform stopping-time and initial-state suprema; then \(\limsup_N\); then \(\delta\downarrow0\) at fixed \(r\); finally \(r\to\infty\). No interchange requires a convergence rate, and no parameter is silently chosen as a function of \(N\).

For R:139–159, if \(d(y,y')>\varepsilon\) and \(d(y,e_i)<\varepsilon/4\), then
\[
d(y',e_i)-d(y,e_i)
\geq d(y,y')-2d(y,e_i)>\varepsilon/2.
\]
This proves the finite-net implication. The union bound and the second-moment bound give R:(11), with its constant \(4/\varepsilon^2\). All \(g_i\) are bounded continuous because \(E\) is compact.

The version of Aldous' sufficient criterion permitted by C:18 requires compact containment and vanishing probabilities of increments across stopping times a vanishing distance apart, on every bounded horizon. R:(11) gives precisely these hypotheses, in a filtration containing the projected filtration. Compact containment is automatic. Thus the criterion's use at R:162 is justified. The local half-line form is covered by the same finite-horizon conditions. Finitely many initial indices do not spoil tightness: each individual law is a probability on a Polish space and is tight; finitely many associated compact sets may be combined. The criterion is an expressly permitted background theorem, not a new campaign dependency. P:35 supplies the bibliographic citation to D. Aldous, “Stopping Times and Tightness,” Annals of Probability 6 (1978), 335–340, DOI 10.1214/aop/1176995579; this audit does not claim to have inspected that external text.

### 3. Continuity of every possible limit

R:166–170 correctly bounds every actual projected jump by \(j_N\). For each finite chain only finitely many jumps occur on bounded intervals almost surely. Self-transitions or microscopic jumps preserving the projected state give size zero.

Under the time changes at R:172–182, taking a left limit in the uniform metric bound is legitimate because both paths have left limits and an increasing continuous bijection maps approach from the left to approach from the left. The triangle inequality gives R:(12). Sending \(N\to\infty\) forces every jump of the limiting path to vanish. This argument uses \(J_1\) time changes and would not follow from finite-dimensional convergence alone.

For a local half-line limit, every finite time lies below an endpoint of continuity of its cadlag path. Applying the finite-interval inequality at such endpoints removes jumps throughout the half-line; right continuity handles time zero. Skorokhod representation is available because the state and Skorokhod spaces are Polish. The usual time-change argument plus uniform continuity of a continuous limit proves uniform convergence on compact intervals, as R:188 states. Evaluation at zero then gives the exact initial point \(x\).

### 4. Passage of the microscopic martingales to projected paths

For fixed \(\lambda\) and \(g\), R:(13) follows directly from full-state resolvent approximation and the finite-state identity already checked. Every cylinder multiplier \(B_N\) in R:212–218 is measurable at the microscopic time \(s\). Hence the Dynkin identity R:(14) is valid without any projected Markov property.

The replacement error consists of two endpoint errors \(\epsilon_N\) and the integrated drift error \(\lambda(t-s)\epsilon_N\), multiplied by \(\prod_i\|h_i\|_\infty\). This gives R:(15) exactly. It removes every occurrence of a microscopic function that need not factor through \(\pi_N\). After that replacement the expression is a bounded function of the projected path. At continuous limiting paths it is continuous for \(J_1\) convergence, including the integral. Bounded convergence on a Skorokhod coupling therefore proves R:(16).

This works for the same arbitrary subsequential limiting law and every fixed choice of tests and parameters. It does not extract a different subsequence for different \(g\) or \(\lambda\), or assume a common almost-sure event for an uncountable set of martingales. The conclusions needed later are numerical expectation identities, for which individual validity for every test is sufficient.

### 5. Laplace inversion and full-law uniqueness

At R:246–256, \(v\) and \(k\) are bounded continuous, and R:(16) yields the displayed integral equation. Thus the ordinary differentiation and integration by parts used to reach R:(17) are justified. Its terminal term vanishes because \(v\) is bounded and \(\lambda>0\). Boundedness also justifies the exponentially weighted Fubini interchange.

For fixed \(B,s,g\), the function \(q\) at R:269 is independent of \(\lambda\). The argument proves that its Laplace transform is zero for every positive \(\lambda\). Its continuity follows from path continuity for the first term and norm continuity of \(r\mapsto P_rg\) for the second. Norm continuity at every time follows from strong continuity and the contraction semigroup property.

The substitution \(a=e^{-r}\) at \(\lambda=n+1\) gives exactly the weight \(a^n\,da\). The bounded density defines a finite signed measure annihilating all polynomials. Stone–Weierstrass, followed by uniqueness of a finite Borel measure from its continuous integrals, makes that measure zero. On \((0,1)\), continuity then makes the density zero pointwise; equivalently \(q(r)=0\) for every finite \(r\geq0\). This verifies the precise uniqueness assertion used in R:(18).

To see explicitly why this identifies more than one-time marginals, order distinct times \(0\leq t_1<\cdots<t_m\). Apply R:(18) with \(s=t_{m-1}\), \(r=t_m-t_{m-1}\), \(g=h_m\), and \(B=\prod_{i<m}h_i(X(t_i))\). This replaces the last two factors by
\[
h_{m-1}(X(t_{m-1}))
(P_{t_m-t_{m-1}}h_m)(X(t_{m-1})).
\]
Their product is a continuous test function by the Feller property, so repeat. The last expectation is fixed by the initial point \(x\) and \(P_t\). Repeated times are handled by multiplying their test functions first. The identical recursion holds under \(Q_x\). Product tests determine laws on \(E^m\) by Stone–Weierstrass; all finite-dimensional distributions therefore agree. The limiting and target laws are supported on continuous paths, whose Borel sigma-field is generated by the rational-time coordinates. This proves equality of their full path laws. Tightness and uniqueness of every subsequential limit yield whole-sequence convergence, as claimed at R:291–298.

The reconstruction's direct cylinder/FDD argument is complete. It does not need the author's intermediate extension to all bounded variables in the natural filtration; proving the displayed recursion supplies the same required path-law identification obligation directly.

## Mechanism comparison and dependency audit

B:7 requires the exact contract, stopping-time tightness, and path-law identification. B:9 gives the sole mechanism hint: “Use the resolvent definition in the contract.” B:11 expressly supplies no other hints. In particular, B does not freeze the author's choice of cutoff functions, supermartingales, or a particular formula for exit probabilities.

| Logical step | P-v2 | R-v1 | Comparison |
| --- | --- | --- | --- |
| Obtain bounded microscopic generator test functions from the given resolvent | P:6–8 | R:25–78 and 192–210 | Same resolvent identity and full-state approximation. |
| Turn resolvent information into stopping-time tightness | P:13–35 uses cutoff functions, positive discounted supermartingales, optional stopping, and the microscopic strong Markov property | R:51–162 approximates a function and its square, applies bounded microscopic optional stopping, and controls metric increments with a finite net | Different valid derivations within the specified resolvent mechanism; both prove the required stopping-time bridge without a new premise. |
| Obtain continuous limits from microscopic jump sizes | P:37 | R:166–188 | Same deterministic \(J_1\) jump argument, expanded in R. |
| Pass resolvent Dynkin identities to limit laws | P:41–50 | R:192–240 | Same argument; R writes the microscopic-to-projected replacement error explicitly. |
| Identify the transition semigroup and full path law from resolvent identities | P:52–69 | R:246–298 | Same positive-discount Laplace mechanism. R uses continuous cylinders and FDD recursion directly; P states conditional expectations in the natural filtration. Both establish the full required law. |

The different tightness derivation does not conceal an unproved analogue of the author's exit step. For comparison, the author's step itself checks out: positivity gives \((A_N-\lambda)h_{N,i}=-\lambda g_i\circ\pi_N\leq0\); its chosen initial state has \(h_{N,i}\leq a\); any attained exit has \(h_{N,i}\geq1-a\). Bounded optional stopping consequently gives
\[
(1-a)e^{-\lambda\delta}\mathbb P_z(\tau\leq\delta)
\leq h_{N,i}(z)\leq a.
\]
Finite-state nonexplosion ensures the relevant exit is attained, and the stated order of limits gives the uniform exit estimate. Conditioning on a microscopic stopping time gives its stopping-time form. R instead proves R:(11) directly for two stopping times; it does not invoke the author's estimate, assume the desired tightness, or replace the requirement by deterministic-time convergence. No disputed step was supplied to this isolated comparator, and no unavailable audit was used to infer one. Every substantive step appearing in the candidate's route has nevertheless been checked or matched to a fully proved reconstruction step above.

Both proofs use only the ordinary background permitted by C:18: finite-state chain calculus; bounded Dynkin martingales and optional stopping; compactness and Stone–Weierstrass; Aldous tightness; Prokhorov and Skorokhod representation; and elementary \(J_1\) properties. The reconstruction proves the particular Laplace uniqueness argument itself. Bounded convergence, finite/exponentially weighted Fubini, and elementary facts about continuous-test determination of finite measures are basic measure-theoretic operations used explicitly, not additional unproved campaign results. The author's use of the microscopic strong Markov property is permitted but is not needed by the reconstruction's optional-stopping estimate. The author's monotone-class formulation can be replaced, as R does, by the proved continuous-product recursion. Neither change adds a dependency or weakens the conclusion.

No generator-domain theorem, Mosco convergence, microscopic uniform semigroup convergence, equilibrium convergence, SIP estimate, finite-tag theorem, sticky-flow convention check, or result from another candidate is used. There is no dependency inflation or claim of resolving S by this transfer lemma alone.

## Nonblocking source notation observation

At R:258 and R:265, the source prints a comma before `dr` rather than the conventional LaTeX spacing command before the differential. The preceding integral equation, the stated integration variable, the limits, and the subsequent change of variables make the intended integrals in \(r\) unambiguous. The derivation above verifies those integrals directly. This is a typography issue, not a missing estimate, a changed claim, or a mathematical gap. No source was edited, and this verdict remains bound to the exact R-v1 bytes.

## Final version-bound determination and output integrity

**PASS for the exact tuple S-v1, C-v1, B-v1, P-v2, A-v1, V-v2, R-v1, I-v1 listed above.** The reconstruction covers every contract hypothesis, every quantified initial sequence, all finite horizons, stopping-time tightness, continuous subsequential limits, and unique identification of the full law in the specified \(J_1\) topology. Its argument implements the accepted resolvent brief without additional hypotheses or promoted dependencies. There is no substantive claim or mechanism mismatch and no missing mathematical step identified by this comparison.

This report was checked in memory for paired renderer-safe LaTeX delimiters and balanced mathematical braces, then written once with exclusive-create semantics and read-only file mode. No input file was modified and no preexisting output was overwritten. The output SHA-256 is reported by the creation tool and completion message, avoiding a self-referential hash. Any change to a hashed input requires a new version-bound comparison; this report does not advance campaign or dependency status.
