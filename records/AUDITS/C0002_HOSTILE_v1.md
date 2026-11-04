# C0002 hostile audit — v1

Verdict: **PASS** for the exact auxiliary pair **CONTRACT_v1.md / PROOF_v2.md**, subject to the hypotheses stated in that contract. No blocking mathematical defect was found. This is an audit result only: it neither promotes C0002 nor proves or promotes STATEMENT-v1.

Auditor: isolated agent `/root/c0002_hostile_v1`. Audit date: 2026-09-05 UTC. No subagents. Promoted campaign dependencies: none. This artifact is created once and must not be edited; any later audit belongs in a new version.

## Exact input manifest and isolation

The only distinct campaign-file contents read were the following four complete inputs, relative to the authorized workspace. The final pinning check uses the subsequently authorized byte-identical AC-002 snapshot described below. SHA-256 hashes are hashes of raw bytes, not normalized text.

| Input | Version/revision | SHA-256 |
|---|---|---|
| STATEMENT.md | v1 | ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97 |
| CANDIDATES/C0002_resolvent_path_transfer/CONTRACT_v1.md | v1 | d42cb0e8db6e9667f77d45f7e4d54994179e48b206fb343af6e50eaf67057c6b |
| CANDIDATES/C0002_resolvent_path_transfer/PROOF_v2.md | v2 | dc06b8b7e052bc994905afaa3b7fe168d7cde233dfa52e5e0355f5458c809a06 |
| AUDIT_CHECKLIST.md | AC-002, including AC-001; bytes read at audit start | 20e1958f0c9d28179fa45fcf6aa0a55954538058d220f72c728e624e2b652188 |
| AUDITS/CHECKLIST_AC002_CANONICAL.md | Authorized stable replacement path; byte-identical AC-002 | 20e1958f0c9d28179fa45fcf6aa0a55954538058d220f72c728e624e2b652188 |

Workspace: `[private workspace]`.

Administrative path substitution: after the mathematical analysis, an input-stability check hashed the global AUDIT_CHECKLIST.md again. Its digest had changed to f33383b960e9e50f2759ec5550c2d3b00e1359d47c9fba5da1d1b3e5b8f6efdc; the check stopped before creating this artifact. Only that later-file digest, not any later checklist text, was exposed. An administrative parent message then authorized AUDITS/CHECKLIST_AC002_CANONICAL.md solely as a byte-identical replacement for the original AC-002 input and stated that a separate fresh supplemental audit would handle additions. The canonical snapshot hash was independently verified against the original input hash. No later checklist content was read or used as mathematics. This administrative message supplied no mathematical defense.

No other campaign files, briefs, earlier audits, registry, search discussion, reconstruction, or author defense were read. Ambient system/developer/user instructions and the audit assignment were available. The assignment specified the input allowlist and subjects to test, but supplied no mathematical finding or defense. External exposure was restricted to ordinary Aldous tightness background and is itemized below. No campaign target or candidate solution was searched publicly.

The claim audited is precisely convergence of the full projected path law for every deterministic sequence of microscopic initial states whose projections converge. The continuous target realization, compact metric state space, uniform resolvent approximation over every microscopic state for every positive discount and continuous test function, and vanishing projected transition sizes are hypotheses. None is established here for the microscopic system in STATEMENT-v1.

## Mathematical checks

### 1. Quantifiers, constants, and exit bound

For each fixed positive discount \(\lambda\) and \(g\in C(E)\), finite-state resolvent calculus gives
\[
A_N R_\lambda^N(g\circ\pi_N)
=\lambda R_\lambda^N(g\circ\pi_N)-g\circ\pi_N.
\]
There is no missing factor of \(\lambda\) in the proof: when
\(h_{N,i}=\lambda R_\lambda^N(g_i\circ\pi_N)\), its discounted drift is
\[
-\lambda e^{-\lambda t}g_i(X_N(t)).
\]
Positivity of the transition semigroup gives \(h_{N,i}\geq 0\), so the discounted process is a nonnegative supermartingale.

For each \(\varepsilon>0\), compactness yields a finite cover by the required balls. A suitable cutoff is
\[
g_i(y)=\min\!\left(1,\max\!\left(0,\frac{4d(y,x_i)}{\varepsilon}-1\right)\right).
\]
This construction is valid in an arbitrary metric space, including when a level set is empty. Strong continuity and the contraction bound imply
\[
\|\lambda R_\lambda g_i-g_i\|_\infty\longrightarrow0.
\]
For a prescribed \(a\in(0,1/4)\), first choose one sufficiently large \(\lambda\) for the finite family, with this error at most \(a/2\). Then choose one sufficiently large \(N\), with the microscopic approximation error after multiplication by \(\lambda\) at most \(a/2\). Thus the proof's bound (2) follows using precisely the contract's quantifiers. No uniformity over an infinite family of cutoffs or over \(\lambda\) is presumed.

For a start \(z\), choose a cover center with \(d(\pi_N(z),x_i)<\varepsilon/8\). The starting cutoff is zero, hence \(h_{N,i}(z)\leq a\). At the first exit from the open \(\varepsilon\)-ball about \(\pi_N(z)\), the distance to that center is at least \(7\varepsilon/8\); thus \(g_i=1\) and \(h_{N,i}\geq1-a\). A finite-state continuous-time chain with a finite generator is nonexplosive. Its exit time is a microscopic stopping time, and an exit before a finite horizon is attained. Optional stopping at the bounded time \(\tau\wedge\delta\) therefore yields exactly
\[
(1-a)e^{-\lambda\delta}\mathbb P_z(\tau\leq\delta)
\leq h_{N,i}(z)\leq a.
\]

The order of limits is essential and is handled correctly. For each fixed \(a\), \(\lambda\) and the lower bound on \(N\) are fixed before \(\delta\downarrow0\). Consequently
\[
\lim_{\delta\downarrow0}\limsup_{N\to\infty}
\sup_{z\in S_N}
\mathbb P_z\!\left(\sup_{t\leq\delta}d(X_N(t),X_N(0))
\geq\varepsilon\right)
\leq\frac{a}{1-a}.
\]
Letting \(a\downarrow0\) proves (4). No rate of resolvent convergence is used. Empty exit sets and chains without transitions cause no difficulty.

### 2. Microscopic stopping times and general compact metric tightness

Write the supremum probability in (4), before taking limits, as \(p_N(\delta,\varepsilon)\). The strong Markov property of \(Z_N\) gives, for every bounded stopping time \(\sigma\) in its filtration,
\[
\mathbb P\!\left(
\sup_{0\leq u\leq\delta}d(X_N(\sigma+u),X_N(\sigma))
\geq\varepsilon\ \middle|\ \mathcal F_\sigma^{Z_N}
\right)
\leq p_N(\delta,\varepsilon).
\]
This inequality follows by conditioning on the full microscopic state \(Z_N(\sigma)\). It does not condition only on the projection and does not assert projected Markovianity. It is uniform in the initial state and in \(\sigma\), and implies the usual Aldous condition for all deterministic offsets in \([0,\delta]\), including offsets varying with \(N\). Projected-filtration stopping times are also microscopic-filtration stopping times.

Compact containment is automatic because every path takes values in the fixed compact space \(E\). The invoked stopping-time criterion applies to general compact metric spaces: these are Polish, and marginal tightness is automatic. Independently checked ordinary background is Aldous, *Weak convergence and the general theory of processes*, July 1981 draft, Section 4, conditions (4.2)–(4.3), Theorem 4.4 and the paragraph immediately following it, printed pages 25–26. That paragraph explicitly extends the criterion with marginal tightness to Polish state spaces. [Aldous manuscript](https://www.stat.berkeley.edu/~aldous/Papers/weak-gtp.pdf).

This supplies a direct metric-space justification of the proof's application; a claim that separate coordinate tightness automatically gives joint \(J_1\) tightness is not needed. The cited 1978 article is correctly identified bibliographically, but its full theorem text was not retrieved in this audit; the theorem statement was checked in the author's above manuscript instead. [Aldous bibliography](https://www.stat.berkeley.edu/~pitman/aldbib/bydate.html).

The stopping-time bound holds on every finite horizon, and the chains are defined beyond that horizon, so terminal-time offsets present no obstruction. The local Skorokhod tightness conclusion on \([0,\infty)\) follows from tightness on all finite horizons.

### 3. Vanishing jumps and continuous limits

Let \(q_N\) be the supremum in contract hypothesis 2. Almost surely each projected jump on every finite horizon has size at most \(q_N\), because microscopic jumps use positive off-diagonal rates and simultaneous transitions have probability zero. Finiteness of the state space prevents explosion.

The deterministic \(J_1\) assertion used in the proof is correct. If \(y_N\to y\) and the time changes give uniform error \(e_N\to0\), then at every interior jump time \(t\) of \(y\),
\[
d(y(t),y(t-))
\leq 2e_N+
d\bigl(y_N(\gamma_N(t)),y_N(\gamma_N(t)-)\bigr)
\leq2e_N+\sup_r d(y_N(r),y_N(r-)).
\]
The left-limit estimate follows by approaching \(t\) from below in the uniform bound; increasing continuous time changes preserve the corresponding left limits. Thus a positive limit jump would require positive approximating jumps. One can work on a horizon beyond the proposed jump whose endpoint is a continuity point, so no endpoint assumption is hidden. Since \(q_N\to0\), every subsequential limit is continuous. This argument is specific to \(J_1\) and does not import an invalid continuous-limit assertion from a weaker topology.

### 4. Passing the resolvent martingales

For fixed \(\lambda,g\), put \(f_N=R_\lambda^N(g\circ\pi_N)\) and \(f=R_\lambda g\). Positivity/contraction gives
\[
\|f_N\|_\infty\leq\frac{\|g\|_\infty}{\lambda},
\qquad
\|\lambda f_N-g\circ\pi_N\|_\infty\leq2\|g\|_\infty.
\]
Accordingly, the absolute value of (5) on \([0,T]\) is bounded by
\[
\frac{2\|g\|_\infty}{\lambda}+2T\|g\|_\infty.
\]
These uniform deterministic bounds justify the required expectation limits.

The target resolvent \(f\) is continuous by the Feller property. Along a Skorokhod representation of a convergent subsequence with continuous limit, paths converge uniformly on compact time intervals. Uniform approximation of \(f_N\) by \(f\circ\pi_N\), uniform continuity of \(f,g\), and the preceding bounds therefore give convergence of both evaluation and integrated terms in (5). For each bounded continuous cylinder function of times at or before \(s\), the microscopic martingale identity passes to the limit. The cylinder algebra generates the natural path filtration: on continuous paths, coordinates on a countable dense set, together with approximation to any endpoint, generate all earlier coordinates. The monotone-class extension consequently proves (6) in that filtration.

Convergence at time zero gives \(X_0=x\). No density or core assertion for a smooth generator domain is being silently used; every positive resolvent parameter and every member of \(C(E)\) is available directly. Individual martingale identities can be obtained separately for each test; the argument does not require an intersection over uncountably many probability-one events.

### 5. Conditional Laplace identity and uniqueness of the full law

Discounting (6) is justified by integration by parts with its bounded-on-finite-horizons martingale. Given deterministic \(s\) and finite \(v\), conditional expectation gives the displayed identity before (7). The terminal term is bounded by \(e^{-\lambda v}\|f\|_\infty\). The tail of the discounted integral is bounded by \(e^{-\lambda v}\|g\|_\infty/\lambda\). Thus passage to \(v=\infty\) in conditional expectation is valid and proves (7).

For any bounded real \(\mathcal F_s^X\)-measurable \(H\), the function
\[
b(u)=\mathbb E[Hg(X_{s+u})]
-\mathbb E[H(P_u g)(X_s)]
\]
is bounded and continuous. Path continuity and bounded convergence prove the first continuity assertion; strong continuity of the contraction semigroup proves the second. Conditional identity (7) gives zero Laplace transform for every \(\lambda>0\), with Fubini justified by boundedness.

The proof's elementary uniqueness step is valid. For every integer \(m\geq1\),
\[
0=\int_0^\infty e^{-mu}b(u)\,du
=\int_0^1 v^{m-1}b(-\log v)\,dv.
\]
Assign any value at \(v=0\). These identities annihilate every polynomial against a finite signed measure on \([0,1]\). Polynomial density forces that measure to be zero. Changing variables then gives \(b=0\) almost everywhere in \(u\), and continuity gives \(b(u)=0\) for every \(u\geq0\).

Since this holds for every bounded \(H\), it identifies the conditional transitions on continuous tests. Continuous functions determine probability measures on compact metric \(E\). More explicitly, iteration against products of continuous coordinate tests gives all target finite-dimensional distributions, and Stone–Weierstrass on each finite product \(E^m\) determines the corresponding joint measures. Continuous path laws are determined by their finite-dimensional distributions on a countable dense time set. Hence the limit law is \(Q_x\). This verifies full path-law identification rather than only unconditional one-time marginals.

The original arbitrary deterministic initial sequence was retained throughout. Every convergent subsequence has the same limit law, so tightness gives the asserted convergence for the whole sequence.

## AC-002 item-by-item record

Every row below records a test or a precise limitation of applicability. It does not discharge or edit any campaign checklist item.

| Item | Result in this audit | Evidence or precise inapplicability |
|---|---|---|
| AC-001-01 | Inapplicable to SIP constants; abstract normalization checked | The auxiliary contract contains no \(d_N,\rho,\alpha\). The factors of \(\lambda\) and the discount sign are verified in check 1. No SIP acceleration or target-form normalization is derived. |
| AC-001-02 | Pass within auxiliary scope | Checks 2–5 prove the full \(E\)-valued path-law conclusion stated in the contract. The proof explicitly declines to establish the SIP resolvent premise or STATEMENT-v1. |
| AC-001-03 | Inapplicable as an SIP initial-state verification; no abstract exclusion | There is no mass, stack-count, or separation condition in C0002. Every deterministic initial sequence with converging projection is retained. This does not certify that the SIP resolvent premise holds for any specified initial class. |
| AC-001-04 | Inapplicable | No deletion consistency or physical-tag construction occurs. The sole Markov argument is for the full finite chain \(Z_N\), as checked in 2. |
| AC-001-05 | Inapplicable | No collision occupation or discontinuous collision indicator is passed to a path-law limit. Exit events are bounded before taking limits; their indicators are not assumed continuous under weak convergence. |
| AC-001-06 | Inapplicable as target-construction verification | The full semigroup \(P_t\) is an input. Check 5 identifies all its conditional transitions; no replacement by pair stickiness occurs. The sticky-flow semigroup in STATEMENT-v1 is not independently constructed here. |
| AC-001-07 | Inapplicable | The cutoffs are ordinary distance cutoffs on \(E\), and resolvents are already defined operators. No intersecting collision-stratum corrector is assumed or constructed. |
| AC-001-08 | Pass | Uniform approximation over all microscopic states is an explicit hypothesis, used without restricting to equilibrium or integrated estimates. Check 1 yields uniform point-start exit control; check 2 preserves it after stopping. |
| AC-001-09 | Pass within auxiliary scope | Every \(g\in C(E)\) and \(\lambda>0\) is available; check 5 establishes uniqueness through resolvent martingales and Laplace transforms. No unproved smooth core is invoked. |
| AC-001-10 | Pass | Check 2 proves stopping-time control and compact containment in general compact metric \(E\); check 3 proves continuous subsequential limits from the exact jump hypothesis. |
| AC-001-11 | Pass | Check 5 tests the Laplace identity against arbitrary past-measurable bounded \(H\), identifies conditional transitions, and then all finite-dimensional distributions and path laws. |
| AC-001-12 | Inapplicable to particle/flow conversions; abstract identity checked | No ordered/labelled particle or kernel-flow conversion is made. The limit is identified with the same input semigroup \(P_t\) and initial point \(x\). |
| AC-001-13 | Pass with explicit hypothesis boundary | The microscopic uniform-resolvent premise is not proved, hidden, or labeled a campaign result. The only non-elementary tightness input is permitted ordinary background, independently checked as documented. There are no promoted campaign dependencies. |
| AC-001-14 | Pass for this audit and proof method | No exact campaign/candidate solution was searched. External lookups concerned only Aldous tightness. The proof uses exit estimates, martingales, and path-law compactness; no Mosco convergence is used. |
| AC-001-15 | Pass for this auditor's input boundary | Only the four permitted logical campaign inputs were read, with the documented byte-identical checklist snapshot substitution. No earlier audit, live-route finding, reconstruction, or author defense entered this audit. The complete ordinary-background exposure is recorded below. This does not certify other agents' histories. |
| AC-001-16 | Pass for this artifact's status boundary | The exact pair and all allowed inputs are pinned by hashes. This audit supplies one PASS only, without promotion, and relies on no promoted or retracted campaign premise. Other protocol gates were not inspected and are not certified here. |
| AC-002-17 | Inapplicable | No almost-sure spatial identity is integrated against a random atomic measure. Identities involving \(X_s\) are deterministic semigroup identities evaluated at a random state, or conditional identities proved by bounded expectations. All discounted Fubini steps have deterministic integrable bounds. |
| AC-002-18 | Pass where applicable | Limit paths are proved continuous in check 3. Countable coordinates and continuity justify filtration/path-law generation in checks 4–5. The proof makes no transition from an unspecified modification to indistinguishability and needs no uncountable intersection of exceptional sets. |

## Ordinary literature and exact external exposure

The permitted Aldous criterion is the only mathematical literature input checked. The sticky-flow references in STATEMENT-v1 were not consulted, because their constructions are not premises used in proving this abstract conditional lemma.

1. Open attempt: `https://doi.org/10.1214/aop/1176995579`. The web tool reported a non-retryable safe-open failure and returned no article text.
2. Web query, exactly: `"Stopping Times and Tightness" "1176995579"`, without a domain restriction. The result excerpts exposed the following URLs. None of these pages was separately opened, and none is relied on for a mathematical theorem:
   - [Mendeley catalogue](https://www.mendeley.com/catalogue/5860f961-a703-3ae3-ac3e-fe5b85deac44/)
   - [MaRDI item](https://portal.mardi4nfdi.de/wiki/Item%3AQ1251416)
   - [Utah bibliography PDF](https://ftp.math.utah.edu/pub/tex/bib/annprobab1970.pdf)
   - [Annals volume 49 issue 6 PDF](https://imstat.org/publications/aop/aop_49_6/aop_49_6.pdf)
   - [CiteSeer bibliography PDF](https://citeseerx.ist.psu.edu/document?doi=ee498c3d4bdd9c31474557be36bc56449f0e0803&repid=rep1&type=pdf)
   - [PubMed 42317399](https://pubmed.ncbi.nlm.nih.gov/42317399/)
   - [Springer article](https://link.springer.com/article/10.1007/s13398-026-01883-9)
   - [Annals volume 48 issue 1 PDF](https://www.imstat.org/publications/aop/aop_48_1/aop_48_1.pdf)
   - [Kinetic and Related Models DOI](https://doi.org/10.3934%2Fkrm.2022018)
   - [PMC13272274](https://pmc.ncbi.nlm.nih.gov/articles/PMC13272274/)
   - [Sydney preprint PDF](https://www.maths.usyd.edu.au/u/pubs/publist/preprints/2024/brzezniak-1.pdf)
   - [CPAA 2020100](https://www.aimsciences.org/article/doi/10.3934/cpaa.2020100)
   - [Statistical Science volume 37 issue 4 PDF](https://www.imstat.org/publications/sts/sts_37_4/sts_37_4.pdf)
   - [CPAA 2020241](https://www.aimsciences.org/article/doi/10.3934/cpaa.2020241)
   - [PubMed 33527236](https://pubmed.ncbi.nlm.nih.gov/33527236/)
   - [AIMS CAM 2026010](https://aimspress.com/article/doi/10.3934/cam.2026010)
   - [OUCI entry](https://ouci.dntb.gov.ua/works/7WA11Q5l/)
   - [CPAA 2020100 HTML variant](https://www.aimsciences.org/article/doi/10.3934/cpaa.2020100?viewType=HTML)
3. Web query, exactly: `"Stopping Times and Tightness" Aldous`, restricted to `projecteuclid.org` and `stat.berkeley.edu`. Returned result excerpts exposed:
   - [Aldous 1981 manuscript](https://www.stat.berkeley.edu/~aldous/Papers/weak-gtp.pdf)
   - [Bibliography by subject, HTML](https://www.stat.berkeley.edu/users/pitman/aldbib/bysubjecta.html)
   - [Bibliography by date, PDF](https://www.stat.berkeley.edu/users/pitman/aldbib/bydate.pdf)
   - [Aldous interview PDF](https://www.stat.berkeley.edu/~aldous/Misc/statsci_interview.pdf)
   - [Bibliography by date, HTML](https://www.stat.berkeley.edu/~pitman/aldbib/bydate.html)
   - [Bibliography by subject, PDF](https://www.stat.berkeley.edu/users/pitman/aldbib/bysubjecta.pdf)
   The bibliography excerpts confirmed the 1978 title, journal volume, and pages. The interview and unrelated bibliography entries were incidental exposure, not premises.
4. In the same web call, opened [Project Euclid article URL](https://projecteuclid.org/journals/annals-of-probability/volume-6/issue-2/Stopping-Times-and-Tightness/10.1214/aop/1176995579.full). The tool returned an empty one-line page, with no theorem text.
5. Opened the Aldous 1981 manuscript URL through the web tool. It reported a 148-page PDF but supplied no extracted lines. Requested web screenshots at zero-based pages 29 and 30; both failed and exposed no page image.
6. Downloaded the same manuscript by `curl -L` to the exact temporary file listed below. `pdftotext` on physical page 1 and physical pages 25–32 produced only page-break characters; no textual contents of pages 27–32 were exposed. Rendered and visually inspected physical pages 1, 25, and 26 only. Page 1 identifies David J. Aldous and the July 1981 incomplete monograph draft; pages 25–26 contain the tightness condition, Theorem 4.4, and the explicit Polish-space extension used above. No other page was rendered or read.

Exact external artifact hashes:

| Artifact | Bytes | SHA-256 |
|---|---:|---|
| /tmp/C0002_Aldous_weak_gtp_hostile_v1.pdf | 5794620 | c8aafdb6f6b6e66ff432996e38fba7c99554e9bd2659697f8122b420c6334b1a |
| /tmp/C0002_Aldous_page1_hostile_v1.png | 20300 | 44901316c495c7571a3c8498a82aa24659491a71317c85f1da18f38922bcc678 |
| /tmp/C0002_Aldous_page25_hostile_v1.png | 76756 | eb024a5af947c4b5323fffab04ebcb82bc2793ee0b7972337eddaff09f93ae97 |
| /tmp/C0002_Aldous_page26_hostile_v1.png | 76238 | e4780ee094c9bebb81ba0ddb0a308d74587d3e1ca4178c1cb07b74cab6878b4a |

Web search excerpts and failed web responses were transient tool outputs; no raw response files were saved, so no content hashes are claimed for them. The exact queries, requested URLs, resulting exposed URLs, and extent of consultation above are the external-exposure record.

## Version-bound decision

**PASS: C0002 CONTRACT-v1 / PROOF-v2, with no promoted campaign dependencies.** The proof establishes the contracted abstract path-transfer implication. The metric-space tightness invocation has been checked against ordinary primary-author background; all other critical steps are verified above. There are no blocking findings and no requested proof revision.

The uniform microscopic resolvent premise remains an assumption. Verification of that premise for SIP, verification of the concrete sticky-flow target, and all remaining promotion/campaign checks remain outside this audit. This file does not authorize any promotion.
