# C0008 hostile audit — immutable version 1

Role: fresh HOSTILE AUDITOR. Date: 2026-09-05. Exact candidate: C0008 CONTRACT_v1 plus PROOF_v1, with the hashes below. Checklist: AC-005. This record evaluates the submitted argument relative to the three exact promoted dependency contracts authorized in the assignment. It does not independently re-audit those dependencies, confer campaign promotion, or certify other verification roles.

**Verdict: PASS.** I completed all 29 checklist checks and the dependency, quantifier, object-identity, citation, localization, and circularity checks described below. I found no substantive mathematical failure or unresolved proof obligation in this exact submitted argument, relative to its authorized promoted premises and the ordinary background identified below. This verdict is bound to the exact hashes; it is not transferable to an edited candidate.

## Exact local input manifest and isolation

All seven SHA-256 values were checked with `shasum -a 256` before reading their contents, and all matched the assignment.

| Actual local input | Verified SHA-256 | Role |
| --- | --- | --- |
| STATEMENT.md | ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97 | Frozen target |
| CANDIDATES/C0008_full_mass_convergence/CONTRACT_v1.md | 56bde5e0c1f439c43bf600aa9f0783b4f7da9ba8c6648e05072373af92b040cd | Exact candidate contract |
| CANDIDATES/C0008_full_mass_convergence/PROOF_v1.md | 8d97fd0abba1232e8befd553489dd88a5239dbbdb962a8472e7e050dc9408868 | Entire submitted proof, 833 lines |
| AUDITS/CHECKLIST_AC005.md | d328652a06ff5ef7fa9ae64a70011a3060b32e80cc23b0afbce4cf1fca97c170 | All 29 required checks |
| CANDIDATES/C0002_resolvent_path_transfer/CONTRACT_v1.md | d42cb0e8db6e9667f77d45f7e4d54994179e48b206fb343af6e50eaf67057c6b | Authorized promoted statement only |
| CANDIDATES/C0005_harmonic_correctors/CONTRACT_v2.md | 0a0130d01e482dbe546a19248b1ca67180aa373643dace7a87abc5cff8eb8cec | Authorized promoted statement only |
| CANDIDATES/C0006_uniform_thin_layers/CONTRACT_v2.md | 805ea9a15da4e350f0af208075932c45473a8f499a89f77f050c6c916c4891b9 | Authorized promoted statement only |

These were the only pre-existing local files read. The initial combined read was truncated by the tool; the full proof and checklist were subsequently read in bounded text chunks. Administrative text comparison also verified that the reproduced statement block starts with the byte-exact entire STATEMENT.md and contains only additional whitespace before its closing marker.

The assignment's explicit promotion authorization governs the three dependency versions despite their immutable creation headers. Hashes of dependency proofs and promotion records printed inside the candidate contract were seen only as administrative text. None of those referenced files was opened, and none was an additional mathematical premise. No brief, manifest, other audit, reconstruction, search record, PROVED, FAILED, REGISTRY, author defense, or other local file was read. No author discussion or subagent was used. No mathematical program was run: shell hashing, text reads/counts, byte comparison, output-existence checking, and audit-file writing were administrative operations only. The inherited user instructions and the root's exact audit assignment were the non-file instructions used.

## Primary-source checks and complete external input log

The model-specific background was checked in the named versioned primary papers:

1. [Le Jan–Raimond, Sticky flows on the circle, arXiv:math/0211387v1](https://arxiv.org/pdf/math/0211387v1): Section 2, recurrence (2.5); Section 3, form (3.6), smooth form density, Theorem 3.3; and Proposition 3.4(b) and its polynomial argument. These support the stated partition-form construction, its everywhere strong Feller compatible versions, and the induced Feller mass semigroup. The paper permits the chosen symmetric Brownian one-point semigroup. The candidate's identification of its parameter follows by substituting \(\tau_0=1/(1+\alpha)\) into (2.5).
2. [Howitt–Warren, Consistent families of Brownian motions and stochastic flows of kernels, arXiv:math/0611292v2](https://arxiv.org/pdf/math/0611292v2): Section 2, definitions (2.2)–(2.5), Definition 2.1, consistency (2.7), positivity (2.9), Theorem 2.1; Proposition 8.1. The source requires positivity only when both indices are positive, allows the zero-index terms used here, proves uniqueness from every real point, and supplies Feller continuation laws. Its test space and bracket convention are those used by the candidate after its explicit time change.

The only web search was the ordinary-background query `David Aldous "Stopping Times and Tightness" 1978 pdf`, restricted to `stat.berkeley.edu`, `projecteuclid.org`, and `jstor.org`. No query concerned the target's solution or openness. The citation's bibliographic data agree with the [1978 journal issue contents](https://www.jstor.org/stable/i312955). Aldous's stopping-time criterion is used as the ordinary named background theorem already permitted by the assignment and candidate; the candidate proves its required compact containment and the stronger conditional maximum-increment bound.

For completeness, the following lists every further external response or attempted retrieval, including incidental search results. Only the two model-specific papers above and the ordinary tightness theorem are mathematical premises. Search-result material on other topics was not used.

| External input or attempted input | What was received and used |
| --- | --- |
| https://doi.org/10.1214/aop/1176995579 | Open attempted; tool reported an internal error; no theorem text obtained. |
| https://projecteuclid.org/journals/annals-of-probability/volume-6/issue-2/Stopping-Times-and-Tightness/10.1214/aop/1176995579.full | Open attempted; one-line unusable response; no theorem text used. |
| https://www.jstor.org/stable/2243224 | Open attempted; unusable page response; no theorem text used. |
| https://www.jstor.org/stable/i312955 | Search-result issue contents; checked author, title, year, volume, and pages. |
| https://www.stat.berkeley.edu/~aldous/Papers/weak-gtp.pdf | Search excerpt of Section 4 displayed the ordinary stopping-time condition. Open returned a scanned PDF with no extracted text; screenshots of zero-based pages 25 and 26 were attempted but yielded no inspectable mathematical text in this session. No claim of reading the full source is made. |
| https://www.stat.berkeley.edu/users/pitman/aldbib/bydate.pdf | Incidental search-result bibliography excerpt; no additional premise. |
| https://www.stat.berkeley.edu/~pitman/aldbib/bydate.html | Incidental search-result bibliography excerpt; no additional premise. |
| https://www.stat.berkeley.edu/users/pitman/aldbib/bysubjecta.pdf | Incidental search-result bibliography excerpt; no additional premise. |
| https://www.stat.berkeley.edu/users/pitman/aldbib/bysubjecta.html | Incidental search-result bibliography excerpt; no additional premise. |
| https://www.stat.berkeley.edu/~aldous/Misc/statsci_interview.pdf | Incidental search-result interview excerpt; no additional premise. |
| https://www.jstor.org/stable/44249970 | Incidental search result concerning a prey–predator model; not opened or used. |
| https://www.jstor.org/stable/48586031 | Incidental search result concerning a functional central limit theorem; not opened or used. |

Repeated web opens/finds of the two versioned papers exposed surrounding portions of those same documents, including unrelated model-convergence paragraphs. Those surrounding paragraphs were not used as results about the target. No other external sources were requested. This source log distinguishes retrieved theorem text from unsuccessful retrievals and bibliographic snippets.

## Dependency applications and their hypotheses

For every fixed auxiliary order \(n\), the candidate keeps \(q=N^2\). The parameter assumptions imply
\[
\frac{q}{L^2}\longrightarrow\rho^2,
\qquad \frac{qd}{L}\longrightarrow\alpha\rho^2,
\qquad d\longrightarrow0.
\]
Thus the small-\(d\) restrictions of C0005 hold eventually for each fixed order. Finite initial exceptions do not affect convergence. The one-label conventions are handled separately.

**C0005.** Every common-cut lift of a circle stable tuple is a line stable tuple. The actual corrected test is the line chamber-affine function \(f^{[L]}(u)=Lf(u/L)\), whose Lipschitz constant is exactly the required uniform bound. Additive constants cancel from generator and covariance increments. On the complement of a fixed positive layer, different block positions have separation exceeding \(\varepsilon L\); the choice \(R_*=\varepsilon L/16\) meets the contract's lower threshold eventually and its required separation exactly. The single-block exact clause handles configurations where no separation parameter is available. Uniform drift, covariance, expansion remainder, and jump-moment conclusions are each used with their stated indices and norms. No formula at arbitrary finite block separation is silently assumed.

**C0006.** The auxiliary labelled generator is exactly \(q(R_n+d^{-1}I_n)\), with both neighboring directions once, and has arbitrary positive \(q\) independently of \(n\). The choice \(k=1\) is valid for every \(L\ge3\); the positive macroscopic layer uses \(k_N=\lfloor\varepsilon L\rfloor\), eventually between 1 and \(L/2\). Every invocation is from an allowed deterministic state, distribution, or bounded stopping time. The trace-time estimate is derived by the retained-clock change of variables and a lost-time error; it is not taken as an extra assertion of C0006.

**C0002.** Its state space is the compact metric space \(\mathcal P(\mathbb T)\), its finite microscopic set is exactly \(\Omega_N\), and its map is exactly \(\Phi_N\). Part IV.2 proves the positive-resolvent hypothesis for every continuous mass test, every positive resolvent parameter, and the supremum over the entire microscopic state space. Part IV.3 proves a continuous-path realization of the exact target mass semigroup from every state. Conservativity and the strongly continuous Feller property are those of the constructed target. Each permitted microscopic jump has Wasserstein distance at most \(1/(NL_N)\), tending to zero. C0002's full path-law conclusion, including stopping-time tightness, therefore applies with all its hypotheses verified.

The dependency graph is acyclic: the promoted corrector and layer statements yield fixed-order path tightness and identification; the independently checked continuum characterization identifies those limits; uniform fixed-order semigroups and the algebraic sampling identity yield full-state mass resolvents; the promoted abstract transfer then yields the mass path law. Neither mass convergence nor an unproved microscopic limit is used in the continuum calculation.

## Adversarial mathematical checks

**Excursions and acceleration.** For the pure inclusion chain the displayed calculation of \(I_n\sum_x\eta_x^2\) gives four times the undirected occupied-edge product sum, including on the three-site torus. Its stopped expectation bounds the mean absorption time by \(c_n\). At each independent event, the same bound restarts from the actual state; hence the count of independent events through absorption has tail at most \(r^j\), where \(r=2nc_nd\le1/4\). The terminal independent event is included. Starting inside the stable set gives zero absorption duration and zero excursion count. Inclusion never adds an occupied site, so the visited-support argument bounds each excursion's displacement by its initial support size plus the independent-event count. This also covers initially unstable tuples and a fully visited circle, where geodesic diameter suffices.

The trace-clock bound counts completed durations for every initiation before the horizon, including excursions returning later. Rare-excursion probabilities are multiplied by their actual initiation rate, of order \(q\). The line/circle coupling fails only after enough independent events to reach the cut margin. Weighting the failure by corrected increments and their products gives precisely the drift and bracket errors displayed in I.4. With a fixed macroscopic margin their accelerated error is \(q r^{\lfloor bL-n-2\rfloor}\to0\). The perturbative remainder is \(qd^2/L\to0\); neither rate factor is dropped.

Nested charts produce bounded stopped drifts and bracket densities, including the exit jump. Doob's inequality gives I.5.1. The positive inner/outer chart margin converts this into the displacement and exit bounds I.5.2. I.5.4 restarts the untraced chain at its own stopping time and then at its first stable entrance, so it does not need a questionable stopping-time assertion for the trace clock. Compact containment is automatic. Vanishing original jumps force all resulting Skorokhod limits to be continuous.

**Discontinuous strata and martingales.** Equation II.2 makes only positive layers small. The drift and covariance defects are bounded everywhere in the localized chart and vanish uniformly off that layer; thus their integrated errors vanish by first fixing the layer width, taking the microscopic limit, and then shrinking the width. Under uniform path convergence to a continuous limit, a false microscopic equality at a positive limiting separation eventually disappears. A missed limiting equality is confined to a positive microscopic layer, apart from a vanishing-probability uniform-error event. This proves II.7 in expected time integral. Weak-order-cell discrepancies then reduce to the finite union of these equality discrepancies and eventually stabilized strict orders. Exact collision occupation is preserved.

II.4 supplies actual martingale passage: bounded stopped tests and drifts give uniform integrability; corrected coordinate products have the exact generator decomposition II.9. The radius-monotonicity argument gives deterministic continuity radii for exit times after Fubini, simultaneously for the countable entry times and horizons used. Exit overshoots vanish. Cylinder multipliers and a monotone-class argument supply conditional identities. Dyadic approximation of entry stopping times and nested balls extend the identities to chart localization. A finite basis suffices for the chamber-affine space. These steps establish the entire local determining martingale class and coordinate covariations, rather than just one-time expectations.

**Form, normalization, and every-point uniqueness.** The ambient mollification argument checks convergence of tangential derivatives separately on every partition stratum. Neighboring chamber pieces agree on the equal-coordinate subspace, which gives the needed derivative agreement there; additional coincidences are null in that stratum's independent block coordinates. This proves membership in the specified closed form domain.

For a refinement replacing a block \(B\) by an unordered pair \(\{A,C\}\), direct cancellation of the partition weights gives
\[
\frac{p_\alpha(\sigma)}{p_\alpha(\pi)}
=\alpha\frac{(|A|-1)!(|C|-1)!}{(|B|-1)!}.
\]
The unit-normal factor and the face surface-measure factor cancel in independent block coordinates. Each of the two sides contributes once, producing both oriented splitting derivatives. There is no ambient block-size factor. Higher intersections are null for each individual integration-by-parts face; their own stratum contributions are supplied by the other partition summands. This checks the all-block coefficient, including intersecting strata, without inferring it from a pair calculation.

The bounded Borel generator identity first holds in \(L^2(m_{\alpha,n})\). Strong Feller continuity makes its integrated semigroup right-hand side continuous for positive times, and full support of the reference measure extends the identity to every starting point. Thus no exceptional collision start is omitted. Cutoff coordinates and their products give zero local coordinate drift and bracket rate \(2\rho^2\) on equality.

Dividing physical time by \(2\rho^2\) gives the positive-index coefficients
\[
\theta(k:l)=\frac{\alpha}{2}
\frac{(k-1)!(l-1)!}{(k+l-1)!}.
\]
The stated zero-index values obey the consistency recurrence because the difference of successive harmonic sums is \(1/k\); their oriented tangential derivatives cancel. All hypotheses of the checked real uniqueness theorem therefore hold. Appending Borel Feller continuation laws proves uniqueness of stopped real solutions. Common-cut charts preserve exact equalities, and their finite nested cover has a positive minimum exit displacement. Uniform continuity prevents infinitely many such exits on a finite horizon. Conditional stopped uniqueness therefore glues to uniqueness of the full circle law, without assuming in advance that a proposed limit is Markov.

**Full mass law.** I independently extracted the two-variable generating-function coefficients in IV.2.2. The incoming coefficient of \(W_{k+\delta_x-\delta_y}\) is \((r+1)(d+s-1)\), the reverse coefficient is \((s+1)(d+r-1)\), and the diagonal is \(-d(r+s)-2rs\). Negative occupation indices are absent, so boundary cases cause no negative-index evaluation. Reindexing gives exactly the auxiliary inclusion generator with the same acceleration. The finite matrix-exponential argument proves the semigroup intertwining. This is averaging over uniform samples without replacement, not an autonomy claim for a selected physical label set.

The repeated-index probability is bounded by \(n(n-1)/(2N)\); multiplying by the two-test-value bound yields IV.2.6. Point-start path convergence for every convergent tuple sequence, compactness, and target joint time-space continuity give the uniform fixed-order semigroup bound, including times tending to zero. Sampling bounds then hold uniformly over all full occupation states. The polynomial algebra contains constants, separates probability measures, and is closed under multiplication, so Stone–Weierstrass supplies every continuous mass test. Laplace tails are uniformly bounded, yielding the exact resolvent hypothesis required by C0002.

Finally, the fourth-moment identity IV.3.1 follows by expanding its four factors and using coordinate consistency before deterministic initial integration. The elementary product bound and the one-coordinate Brownian fourth moment give the uniform bound proportional to \((t-s)^2\). Conditioning uses a deterministic transition function evaluated at the current mass state, avoiding random-atom evaluation of spatial almost-sure identities. The dyadic construction uses a countable determining family and every integer horizon on one probability-one event; compactness then supplies an actual continuous measure-valued path. Equality on dense times and right-continuity justify indistinguishability with a càdlàg realization. The hypotheses and conclusion of C0002 therefore concern the full untraced mass law on every finite horizon and on the infinite-horizon Skorokhod space.

## AC-005 dispositions

Every row is discharged for the exact candidate relative to the authorized premises. Protocol rows concern this submission and this auditor's inputs; they do not purport to audit unseen campaign history.

| ID | Disposition and evidence |
| --- | --- |
| AC-001-01 | PASS. The three scaling limits above, the one-label bracket, the all-block face ratio, and the physical-to-unit-bracket time change retain all factors. |
| AC-001-02 | PASS. IV.2.9 and IV.4 apply C0002 to the entire mass-valued process; the trace and fixed-order limits are intermediate steps. |
| AC-001-03 | PASS. All microscopic estimates and the final resolvent supremum allow arbitrary states. Vanishing masses, coalescing limiting positions, lattice-distance-two stacks, and every fixed initial stack count are included. |
| AC-001-04 | PASS. IV.2 proves the factorial averaging intertwining algebraically and bounds replacement-sampling error; no selected-tag autonomy is used. |
| AC-001-05 | PASS. II.7 proves integrated equality-indicator convergence by positive-layer bounds, rather than asserting continuity of collision indicators. |
| AC-001-06 | PASS. The complete chamber-affine test space and every oriented split of every exact block occur in II.3 and III.3–III.6. |
| AC-001-07 | PASS. The global compatible corrector is an exact promoted C0005 premise. Its circle application and integrated replacement include arbitrary entrance states and all equality partitions. |
| AC-001-08 | PASS. The absorption, excursion, corrector, and layer estimates are uniform over all starts. II.12 is prescribed-point path convergence; IV.1 obtains uniformity by compactness from that result. |
| AC-001-09 | PASS. III.2 proves the nonsmooth cutoff tests belong to the specified form closure; III.5 checks the determining real martingale problem. Smooth tests alone are not used for uniqueness. |
| AC-001-10 | PASS. I.5.4 is the original-filtration stopping-time bound, compact containment holds, IV.3 proves continuous target mass paths, and IV.4 verifies C0002. |
| AC-001-11 | PASS. Local martingale uniqueness identifies fixed-order paths. Full-state mass resolvents then invoke a promoted path-transfer theorem with all hypotheses checked. |
| AC-001-12 | PASS. Label symmetrization, occupation quotient, common-cut lifts, the exact partition form, and the common-flow mass polynomial identity are all explicitly matched. |
| AC-001-13 | PASS. The dependency graph described above has no circular step; all remaining model-specific bridge arguments are displayed in this candidate. |
| AC-001-14 | PASS. The form is used for continuum target identification only. No microscopic Mosco limit or target-solution/openness search is used. |
| AC-001-15 | PASS within this audit's scope. The input boundary was respected; no reconstruction, other audit, live-route file, or author defense was read. The external query was restricted to named ordinary background. |
| AC-001-16 | PASS within this audit's scope. Only the exact three expressly promoted contracts are premises. The candidate makes no promotion claim; this audit does not confer campaign completion. |
| AC-002-17 | PASS. IV.3 integrates only deterministic initial measures against Borel transition functions and then conditions via the mass Markov semigroup. |
| AC-002-18 | PASS. IV.3 takes a common event for countably many tests and horizons, constructs continuous paths, and uses right-continuity for indistinguishability. |
| AC-003-19 | PASS. The target continuity argument does not require joint evaluation of an independent random kernel at a random atom. |
| AC-003-20 | PASS within this audit's scope. No mathematical computational output is evidence in the submitted proof or this audit. The symbolic coefficient checks were mathematical arguments, not programs. |
| AC-003-21 | PASS. C0006 supplies the exact uniform conditional estimate. I.3.2 and I.5.4 separately restart from arbitrary original-filtration stopping states. |
| AC-003-22 | PASS. The three-site edge multiplicity is correct; the sampled-index diagonal error is explicitly bounded; the all-orders polynomial argument supplies a determining mass class. |
| AC-004-23 | PASS. II.6 multiplies positive-layer occupation by uniformly bounded defects. II.7 preserves exact collision occupation and never bounds it by a positive layer. |
| AC-004-24 | PASS. The same \(q=N^2\) appears in every auxiliary order and the factorial intertwining; \(n\) stays fixed but arbitrary. |
| AC-004-25 | PASS. I.2–I.5 cover arbitrary initial absorption, the lost clock, complete terminal excursions, rate-weighted rare excursions, and direct original-filtration tightness. |
| AC-004-26 | PASS. The promoted C0005 first-order drift and coordinate-covariance estimates are both applied; I.4 controls the accelerated circle errors and II.6 integrates the remaining defects. |
| AC-004-27 | PASS. III.4 upgrades the operator identity to every point using strong Feller continuity and full support. Common-cut charts preserve circle equality and are glued by stopped uniqueness. |
| AC-004-28 | PASS. The route uses one global corrector per test and integrated bounded errors. Excursion contributions are weighted by actual initiation compensators; there is no uncounted sum over overlapping collision cells. |
| AC-005-29 | PASS. The count includes independent events in the excursion through its returning event; an independent return is counted, while a zero-duration excursion has count zero. Restarting after each counted event gives the geometric tail used in the coupling. |

## Final version-bound conclusion

PROOF_v1 establishes the exact frozen finite-stack conclusion, including the prescribed deterministic initial sequences, all parameter sequences in the statement, the complete mass-valued path law, the stated time normalization, the common-flow target, and continuity of the limit, relative only to the three exact authorized promoted contracts and the ordinary background above. No substantive failure was found to record against this version. The remaining campaign cadence and eligibility of any outside-family verifier are outside this audit's input scope and are not certified here.

This is the first written version of this audit. It is to be preserved unchanged; any subsequent audit or correction must receive a new versioned file.
