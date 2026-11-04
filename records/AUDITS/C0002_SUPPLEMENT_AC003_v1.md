# C0002 supplemental hostile audit — AC-003 — v1

Verdict: **PASS for supplemental mathematical coverage of AC-003-19 through AC-003-22**, bound exactly to C0002 CONTRACT-v1 and PROOF-v2 and the input hashes below. This is not a promotion, does not replace the baseline hostile audit or proof-blind reconstruction, and does not prove STATEMENT-v1.

Auditor: fresh isolated supplemental auditor `/root/c0002_supplement_v1`.
Promoted dependencies supplied or used: none.
Scope: the four added checklist items in the pinned AC-003 snapshot, with applicability assessed against this abstract path-transfer contract.

## Input manifest and isolation

The following are the complete mathematical inputs read. SHA-256 hashes identify the exact bytes reviewed.

| Input | Version | SHA-256 |
|---|---|---|
| `STATEMENT.md` | Frozen statement v1 | `ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97` |
| `CANDIDATES/C0002_resolvent_path_transfer/CONTRACT_v1.md` | C0002 contract v1 | `d42cb0e8db6e9667f77d45f7e4d54994179e48b206fb343af6e50eaf67057c6b` |
| `CANDIDATES/C0002_resolvent_path_transfer/PROOF_v2.md` | C0002 proof v2 | `dc06b8b7e052bc994905afaa3b7fe168d7cde233dfa52e5e0355f5458c809a06` |
| `AUDITS/CHECKLIST_AC003.md` | AC-003 snapshot | `ad7ebab088ea9c241ae4803d4c6687782df10f9c2653980be1150a20a9dc5db5` |

No earlier audit, reconstruction, brief, author defense, route deliverable, protocol record, or other mathematical file was opened. The source-route labels printed inside the allowed checklist were read as labels only; the files they name were not consulted. No web search or external literature was used. No subagent was used. Shell operations consisted of reading the allowed files, recording their line numbers and hashes, obtaining the working directory, and exclusively creating this audit; these operations supply provenance, not computational mathematical evidence.

All line references below refer to these exact input bytes. `CONTRACT` and `PROOF` abbreviate the two candidate paths in the manifest.

## Applicability and decisions

| Item | Precise applicability | Decision |
|---|---|---|
| AC-003-19 | No random kernel is evaluated at a random atom. The nearby measurability issue for deterministic semigroup functions evaluated at random states is checked below. | PASS; specified failure mode not triggered. |
| AC-003-20 | No finite numerical or symbolic machine computation is submitted or used as mathematical evidence by this proof. | PASS; specified evidence failure mode not triggered. |
| AC-003-21 | No collision-occupation estimate is asserted. The full-state uniformity and conditional optional-stopping mechanism are directly relevant to the exit estimate, and are checked explicitly below. | PASS for the applicable mechanism. |
| AC-003-22 | Circle-edge multiplicities and sampled-index diagonals are absent from this abstract contract. The distinction between an exact identity and a law-determining test family is relevant to the resolvent identification argument. | PASS for the applicable determining-family component; the two discrete-model components are not triggered. |

### AC-003-19: random evaluation and measurability

Evidence: CONTRACT lines 6–12; PROOF lines 13–22 and 52–69.

The objects evaluated at random states are deterministic continuous functions, including \(g_i\), \(R_\lambda g\), and \(P_u g\). Their compositions with measurable random variables are measurable. In particular, \(R_\lambda g\in C(E)\): the defining integral is a uniform limit of finite-time integrals of the strongly continuous \(C(E)\)-valued map \(t\mapsto e^{-\lambda t}P_tg\). The uniform tail bound is \(e^{-\lambda T}\|g\|_\infty/\lambda\).

For completeness, the map \((u,y)\mapsto(P_ug)(y)\) is jointly continuous. If \(u_n\to u\) and \(y_n\to y\), then
\[
|(P_{u_n}g)(y_n)-(P_ug)(y)|
\le \|P_{u_n}g-P_ug\|_\infty
   +|(P_ug)(y_n)-(P_ug)(y)|\longrightarrow0.
\]
Strong continuity and the contraction semigroup property supply the first limit; the Feller property supplies the second. Thus evaluating this deterministic function at \(X_s\), and integrating in \(u\), requires no independence or exceptional-set convention for a random kernel.

The index of a covering center can be chosen as the first index satisfying \(d(\pi_N(z),x_i)<\epsilon/8\). This is a deterministic function on the finite set \(S_N\), hence is measurable at a stopping time. It is not a random spatial evaluation of an evaluation-measurable random kernel.

The proof's conditional-expectation equalities are used for each fixed \(s,u,g\), with bounded measurable multipliers. It does not assert a spatially simultaneous identity by integrating pointwise almost-sure identities against a random atomic measure. The random-kernel construction in STATEMENT-v1 is neither imported as a proved dependency nor established by C0002. Therefore this supplemental PASS does not certify that construction's separate measurability requirements.

### AC-003-20: computational evidence provenance

Evidence: the entire PROOF, lines 1–71.

The proof uses finite-state resolvent and martingale identities derived analytically, compactness, and a Laplace-transform argument. A finite state space is not a finite computation: no enumerated output, checked finite parameter range, computer algebra result, program, or experiment is asserted to support a mathematical step. In particular, PROOF line 8 is the general resolvent identity, not a reported computed table.

There is consequently no computation for which source, timeout, execution log, and output must be supplied by this candidate. No rerun was performed. This decision concerns only C0002 PROOF-v2; it neither reconstructs nor absolves any protocol incident referenced by the checklist's source labels.

### AC-003-21: uniformity and conditional optional stopping

Evidence: CONTRACT lines 10–16; PROOF lines 13–35, with the finite-state identity in lines 6–9.

The adversarial issue is whether an estimate valid at a prescribed deterministic start can fail after the microscopic process reaches another state. Here the hypothesis explicitly takes the supremum over every state in \(S_N\). After fixing \(\epsilon>0\) and \(a\in(0,1/4)\), the finite covering and uniform resolvent approximation produce a common \(\lambda\) and a common threshold \(N_0\), independent of the starting state, such that
\[
0\le h_{N,i}\le1,
\qquad
\|h_{N,i}-g_i\circ\pi_N\|_\infty\le a
\quad(N\ge N_0)
\]
for every covering index \(i\). The upper bound follows directly from \(0\le g_i\le1\), conservation, and the definition \(h_{N,i}=\lambda R_\lambda^N(g_i\circ\pi_N)\).

The conditional version can be written explicitly. Let \(\mathcal F_t^N\) be the microscopic filtration, let \(\sigma\) be a bounded stopping time, and select the measurable index \(I\) with
\[
d(X_N(\sigma),x_I)<\epsilon/8.
\]
Define the shifted first exit and its bounded truncation by
\[
\tau_\sigma=\inf\{r\ge0:d(X_N(\sigma+r),X_N(\sigma))\ge\epsilon\},
\qquad \theta=\tau_\sigma\wedge\delta.
\]
The strong Markov property of the full chain, followed by bounded optional stopping of the discounted Dynkin martingale, gives
\[
\mathbb E\left[
 e^{-\lambda\theta}h_{N,I}(Z_N(\sigma+\theta))
 +\lambda\int_0^\theta e^{-\lambda r}g_I(X_N(\sigma+r))\,dr
 \;\middle|\;\mathcal F_\sigma^N\right]
 =h_{N,I}(Z_N(\sigma))\le a.
\]
This can equivalently be proved for each of the finitely many possible values of \(I\), then multiplied by the corresponding \(\mathcal F_\sigma^N\)-measurable indicator and summed. All terms are bounded on the stopped interval. There is no optional-stopping integrability gap.

On \(\{\tau_\sigma\le\delta\}\), the distance from the selected center is at least \(7\epsilon/8\), so \(h_{N,I}(Z_N(\sigma+\tau_\sigma))\ge1-a\). Dropping the nonnegative integral and bounding the discount yields the almost-sure conditional estimate
\[
\mathbb P(\tau_\sigma\le\delta\mid\mathcal F_\sigma^N)
\le \frac{a e^{\lambda\delta}}{1-a}.
\]
The same optional-stopping identity also gives the conditional integrated cutoff bound
\[
\lambda\mathbb E\left[
 \int_0^\theta e^{-\lambda r}g_I(X_N(\sigma+r))\,dr
 \;\middle|\;\mathcal F_\sigma^N\right]\le a.
\]
This latter display makes the conditional integrated form explicit; it is not an estimate of any SIP collision occupation.

The constants and threshold are uniform over every microscopic state, every bounded \(\sigma\), and every initial law. The first-exit event bounds every projected increment with offset at most \(\delta\). First taking the large-\(N\) limit superior, then \(\delta\downarrow0\), and then \(a\downarrow0\), gives exactly the claimed uniform stopping-time modulus. No Markov property of the projection is required: every use of the strong Markov property is at \(Z_N\). Thus the conditional extension in PROOF line 35 is justified rather than inferred from deterministic starts alone.

### AC-003-22: discrete corrections and a determining class

Evidence: CONTRACT lines 6–16; PROOF lines 6–9 and 41–71.

The contract has no discrete torus length, nearest-neighbor edge sum, sampled physical index, particle polynomial, or diagonal-subtraction formula. Its input is an arbitrary finite-state generator and a supplied full-state resolvent convergence hypothesis. Neither a finite-circle multiplicity nor a sampled-index correction enters its argument. Checking those model identities would require inputs outside this audit and is not licensed by a PASS here.

The analogous law-determination issue is applicable. The identity
\[
A_N R_\lambda^N(g\circ\pi_N)
=\lambda R_\lambda^N(g\circ\pi_N)-g\circ\pi_N
\]
alone would not identify a limit. The proof additionally uses its martingale consequence for every \(\lambda>0\) and every \(g\in C(E)\), with all continuous finite-coordinate multipliers from the past. Its passage to a limiting martingale has a uniform bound on a horizon \(T\): the absolute value is at most
\[
\frac{2\|g\|_\infty}{\lambda}+2T\|g\|_\infty.
\]
Uniform resolvent approximation and convergence to continuous paths therefore justify convergence of the multiplied expectations. The usual monotone-class extension yields the natural-filtration martingale claimed in PROOF lines 46–50.

The proof then verifies determination, rather than merely naming the class. For fixed \(s\), bounded \(\mathcal F_s^X\)-measurable \(H\), and \(g\in C(E)\), define
\[
b(u)=\mathbb E[H g(X_{s+u})]-\mathbb E[H(P_ug)(X_s)].
\]
It is bounded and continuous, by continuity of the limiting paths and strong continuity of the semigroup. The discounted martingale identity gives
\[
\int_0^\infty e^{-\lambda u}b(u)\,du=0
\qquad(\lambda>0).
\]
Taking \(\lambda=m\in\{1,2,\ldots\}\) and substituting \(v=e^{-u}\) gives
\[
\int_0^1 v^{m-1}b(-\log v)\,dv=0.
\]
The value of the bounded integrand at \(v=0\) can be assigned arbitrarily. Polynomial density implies that its finite signed measure is zero, hence \(b\) is zero almost everywhere on \([0,\infty)\). Continuity gives \(b(u)=0\) for every \(u\). Varying \(H\) proves the conditional transition identity for every fixed time pair and every continuous test function.

Continuous test functions determine probability measures on compact metric \(E\); one may use a countable uniformly dense subset of \(C(E)\) to make the conditional-measure identification simultaneous when needed. Repeated conditioning determines all finite-dimensional laws, and continuous paths are determined by their values on a fixed countable dense time set. Thus this is a determining resolvent-martingale class, not a finite collection of exact author identities. No assertion about an SIP all-orders generator class is supplied or implied.

## Disposition

No failure was found among AC-003-19 through AC-003-22 for the exact candidate and checklist bytes in the manifest. The applicable conditional stopping argument and law-determining argument pass the explicit checks above. The nonapplicable model-specific and computation-specific components remain outside C0002's mathematical content.

This record provides supplemental coverage only. It does not discharge the checklist globally, alter any status, promote C0002, establish its microscopic hypothesis for SIP, verify the continuum construction in STATEMENT-v1, or prove the frozen convergence claim. PROOF line 71 expressly retains the missing SIP resolvent hypothesis.

Output: `AUDITS/C0002_SUPPLEMENT_AC003_v1.md`, created with exclusive-create semantics. Any correction must be a new version; this file is not to be overwritten. Its own SHA-256 is reported separately because embedding a file's own cryptographic hash would not be a stable manifest convention.
