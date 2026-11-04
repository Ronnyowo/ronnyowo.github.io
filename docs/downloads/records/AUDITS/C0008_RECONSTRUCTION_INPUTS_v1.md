# C0008 independent reconstruction: actual inputs v1

Date: 2026-09-05. Role: proof- and audit-blind independent reconstructor.

This is the actual-exposure manifest for the argument first frozen in `AUDITS/C0008_RECONSTRUCTION_v1.md` and represented with corrected literal LaTeX delimiters in `AUDITS/C0008_RECONSTRUCTION_v2.md`. Both were written once. Version 1 remains unchanged. Version 2 changes only literal math delimiters and math/text boundaries in two display annotations; it does not change the mathematical argument. The operative readable reconstruction is version 2. Its inherited heading names the target contract version, C0008 v1.

Status of both representations: **self-audited independent reconstruction relative to the exact promoted dependency statements**. Neither has a fresh comparison, hostile-audit, verifier-backed, or promoted status assigned by this reconstructor.

## 1. Frozen output bindings

| Output | SHA-256 |
| --- | --- |
| `AUDITS/C0008_RECONSTRUCTION_v1.md` — preserved first write, with some lost inline delimiters | `4e28fc51438791d6bb1cc970801e0dc9b435fd16f99ceb0c2a0fdbc7fcf119ad` |
| `AUDITS/C0008_RECONSTRUCTION_v2.md` — literal rendering repair, same argument | `88e53846cc7f218de25bbf4a25bbae1d4fad1805960ee8fe3119027b96686608` |

## 2. Permitted local mathematical inputs actually read

All six files below were hashed in one `shasum -a 256` command before any contents were read. Every computed hash matched the assigning root's exact hash. Contents were then read in two `cat` commands. Both the C0008 contract and brief repeat the frozen statement and administrative dependency bindings; that repeated content was actually exposed.

| File | Verified SHA-256 | Use |
| --- | --- | --- |
| `STATEMENT.md` | `ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97` | Exact target and scope |
| `CANDIDATES/C0008_full_mass_convergence/CONTRACT_v1.md` | `56bde5e0c1f439c43bf600aa9f0783b4f7da9ba8c6648e05072373af92b040cd` | Exact submitted contract and allowed dependencies |
| `CANDIDATES/C0008_full_mass_convergence/BRIEF_v1.md` | `ec0c06433d0303df9a8c0120373103beed8b0f53687011f2b4b5834bf5c139f4` | Accepted proof-blind brief containing the exact contract |
| `CANDIDATES/C0002_resolvent_path_transfer/CONTRACT_v1.md` | `d42cb0e8db6e9667f77d45f7e4d54994179e48b206fb343af6e50eaf67057c6b` | Promoted all-state resolvent-to-path transfer statement |
| `CANDIDATES/C0005_harmonic_correctors/CONTRACT_v2.md` | `0a0130d01e482dbe546a19248b1ca67180aa373643dace7a87abc5cff8eb8cec` | Promoted line corrector, trace, covariance, and excursion statement |
| `CANDIDATES/C0006_uniform_thin_layers/CONTRACT_v2.md` | `805ea9a15da4e350f0af208075932c45473a8f499a89f77f050c6c916c4891b9` | Promoted conditional positive thin-layer occupation statement |

The three dependencies were treated as exact promoted premises solely because the assigning root explicitly authorized these versions despite their immutable creation-time candidate headers.

The proof hashes and promotion-record hashes repeated in the permitted C0008 contract and brief were seen as administrative text. None of those referenced files was opened, hashed, searched, or used as an additional mathematical premise. The permitted contract's mention of the existing route was seen; no route file or route argument was opened.

## 3. Directly consulted primary literature

The single literature-search query was:

> Howitt Warren Consistent families of Brownian motions stochastic flows kernels martingale problem uniqueness theta k l

It sought the standard named continuum theorem, not the solution, proof, counterexample, or open status of the exact campaign target.

In the same web call, the two exact background reference pages from the frozen statement were opened: [Le Jan--Raimond](https://arxiv.org/abs/math/0211387) and [Le Jan--Lemaire](https://arxiv.org/abs/math/0307106). The search exposed the Howitt--Warren arXiv result and the incidental snippets in Section 4. Three primary PDFs were then downloaded directly into new reconstructor-owned temporary paths and converted using `pdftotext -layout`:

| Primary PDF URL | Local path | PDF SHA-256 |
| --- | --- | --- |
| `https://arxiv.org/pdf/math/0211387` | `/tmp/c0008_reconstruct_ljr.pdf` | `8438ae6c2e782857b756f43f71fe8577291cb49fcb31ba4e87dd2b177b23be38` |
| `https://arxiv.org/pdf/math/0307106` | `/tmp/c0008_reconstruct_ljl.pdf` | `0a6c000584332b03dc0ad54f225623435bbbdb873d7dc838c42629ccd6abefdb` |
| `https://arxiv.org/pdf/math/0611292` | `/tmp/c0008_reconstruct_hw.pdf` | `dde4f02ef55c655b9c42715004fdc0b62c359f12601b3a468159be845353140c` |

| Extracted text | SHA-256 |
| --- | --- |
| `/tmp/c0008_reconstruct_ljr.txt` | `c047256f1b1395aacb2d93b0a4cc67468531d1965ce2380ddd3d4193f26e51f4` |
| `/tmp/c0008_reconstruct_ljl.txt` | `8b477247d5f7091640444bd479057fad196d1637bf8e75452caad2f2ef8f5fc3` |
| `/tmp/c0008_reconstruct_hw.txt` | `fdd9af0c30468c7aeda202975425ec890dba08602bc2a2e7de4464532b3cb28b` |

Actual text read operations:

- The whole LR text was requested with `cat`. The tool response shared an aggregate output budget with a search of the other texts and was truncated by the wrapper. LR lines 320--425 were later read explicitly. Exposed material includes the partition recursion, target form construction, Theorem 3.3, Proposition 3.4, their surrounding explanations/proofs, and bibliography. The argument uses the target form identification, strong Feller property, compatibility, and mass-kernel construction from the cited results.
- An `rg -n` search over HW and LL used the patterns `Theorem`, `Proposition`, `theta`, `θ`, `Beta`, and `Dirichlet`. The aggregate returned output was truncated. Its displayed lines and snippets were seen, including the HW closing discussion of LR forms.
- HW lines 190--435 and 1740--1810 were then read explicitly. They cover the martingale-problem definitions, consistency, parameter conventions, Theorem 2.1, the start of its exit analysis, Theorem 8.1 with its proof, and the final LR comments. The reconstruction uses Definition 2.1 and Theorem 2.1. It does not treat the final comments as a proved identification theorem; its own Section 2 supplies the calculation.
- Another `rg -n` search of LL used `Theorem`, `Proposition`, `Dirichlet`, `Beta`, `beta`, and `alpha`; all returned hits were exposed.
- LL lines 510--632 were read explicitly. This exposed text remnants of figures and Section 3.2, including Propositions 6--7 and the Brownian time convention. No Beta-flow convergence proof was read or used.
- The six PDF/text artifacts were hashed after extraction. No visual PDF page was opened.

References appearing in the papers' bibliographies or discussions were incidentally seen to the extent these read ranges or search hits displayed them. No further reference was opened. No literature source beyond these three primary papers is a mathematical premise.

## 4. Incidental search-result exposure

The one HW query returned additional titles, URLs, and snippets. The following were actually exposed. Except for the primary HW result, these were not opened, downloaded, or used as premises:

- [Howitt--Warren arXiv abstract](https://arxiv.org/abs/math/0611292).
- [Howitt--Warren published PDF at Warwick](https://wrap.warwick.ac.uk/id/eprint/37376/1/WRAP_warren_euclid.aop.1248182138.pdf); the tool displayed a substantial excerpt of the introduction and start of Section 2.
- [Warwick record of the Howitt--Warren paper](https://wrap.warwick.ac.uk/id/eprint/37376/).
- [CiteSeerX copy of the Howitt--Warren paper](https://citeseerx.ist.psu.edu/document?doi=762afa192716c8d99c4bd0d9095713e76b3872bd&repid=rep1&type=pdf).
- [KPZ equation limit of sticky Brownian motion, ScienceDirect abstract](https://www.sciencedirect.com/science/article/abs/pii/S0022123624002970).
- [ResearchGate record of the Howitt--Warren paper](https://www.researchgate.net/publication/2132901_Consistent_families_of_Brownian_motions_and_stochastic_flows_of_kernels_ArXiv_mathPR0611292).
- [The Bethe ansatz for sticky Brownian motions, DOI result](https://doi.org/10.1016/j.spa.2023.04.015).
- [ResearchGate: The Brownian web, the Brownian net, and their universality](https://www.researchgate.net/publication/277723289_The_Brownian_web_the_Brownian_net_and_their_universality).
- [Jon Warren's Warwick page](https://warwick.ac.uk/fac/sci/statistics/staff/academic-research/warren/).
- [Dialnet record of the Howitt--Warren paper](https://dialnet.unirioja.es/servlet/articulo?codigo=3034724).
- [AMS: Stochastic flows in the Brownian web and net](https://bookstore.ams.org/MEMO/227/1065).
- [Stochastic-process citation page hosted at Hebrew University](https://math.huji.ac.il/~ohadfeld/Tsirelson/Research/stochpr/cit_co.html).
- [Stochastic flows in the Brownian web and net, arXiv](https://arxiv.org/abs/1011.3895).
- [The Bethe ansatz for sticky Brownian motions, ScienceDirect full-article result](https://www.sciencedirect.com/science/article/pii/S0304414923000832).
- [Warwick author bibliography](https://wrap.warwick.ac.uk/view/author_id/8173.type.html).
- [ResearchGate: KPZ equation limit of sticky Brownian motion](https://www.researchgate.net/publication/370338412_KPZ_EQUATION_LIMIT_OF_STICKY_BROWNIAN_MOTION).
- [Dynamics for the Brownian web and the erosion flow, arXiv](https://arxiv.org/abs/math/0702542).
- [Edwards--Wilkinson fluctuations in the Howitt--Warren flows, arXiv](https://arxiv.org/abs/1412.3911).
- [Wikipedia: Stochastic analysis on manifolds](https://en.wikipedia.org/wiki/Stochastic_analysis_on_manifolds).
- [Wikipedia: Mouvement brownien](https://fr.wikipedia.org/wiki/Mouvement_brownien).
- [Wikipedia: Itô isometry](https://en.wikipedia.org/wiki/It%C3%B4_isometry).
- [Wikipedia: Martingale (probability theory)](https://en.wikipedia.org/wiki/Martingale_%28probability_theory%29).
- [Wikipedia: Rough path](https://en.wikipedia.org/wiki/Rough_path).
- [Wikipedia: Wiener process](https://en.wikipedia.org/wiki/Wiener_process).

The LR/LL pages opened in the same call are separately recorded in Section 3. No assertion of primary-source verification rests on incidental secondary snippets.

## 5. Communications and administrative exposure

The reconstructor began with the root's independent-reconstruction assignment, the user-supplied rigor and renderer-safe-LaTeX instructions, and generic workspace/tool instructions. The assignment supplied the six exact paths and hashes, promotion authorization for three dependency versions, the requirement of a complete fresh argument, and the prohibitions on candidate/audit exposure, subagents, and mathematical programs. No candidate argument was included.

Two subsequent root messages arrived after the first argument write. They were administrative:

1. A request for status at the next natural write boundary, asking whether a complete argument was in preparation or an exact remaining gap had appeared, explicitly retaining the same input boundary and supplying no author/audit content.
2. Literal feedback that the root had begun reading this reconstructor's own first write and saw missing inline backslashes, with examples from its opening paragraph. The root instructed preservation of v1, allowed a v2 containing only literal delimiter repairs, and prohibited changing the mathematical argument in response.

The outbound root status message reported that the complete self-audited argument had been first-written and that the manifest/integrity checks were in progress. No mathematical advice, author proof, or audit evaluation was requested from the root or another agent. The second inbound message concerned only text already written by this reconstructor. Neither message supplied a new mathematical premise or strategy hint.

Progress comments described the reconstructor's own hash verification, local estimates and transfer work, computed normalization, sampling cancellation, and literal formatting repair.

No subagent was spawned. No author or auditor was contacted for mathematical input. No candidate proof, dependency proof, author manifest, existing audit, checklist, reconstruction by another party, registry, failed/proved list, route file, or other campaign file was read. Paths merely mentioned in permitted inputs were not followed.

## 6. Administrative operations on the reconstructor's own outputs

Existence checks confirmed that the requested v1 argument and v1 manifest paths did not exist before writing. The argument was composed and added once with `apply_patch`.

The first write was read by `sed -n '1,90p'` and an `rg -n` parentheses search to inspect serialization. Unescaped JavaScript string literals had removed some inline backslashes; display delimiters survived. The original file was not modified.

A Python text-only repair read the reconstructor's own v1, protected existing math spans, and restored an explicitly enumerated set of missing inline delimiters. It also repaired math/text boundaries in two display annotations. The composed result was written once to `/tmp/c0008_reconstruction_v2_composed.md`. A second text-only check confirmed balanced delimiters and braces in all 288 math segments. Those checked bytes were written to v2 using exclusive file creation. These were administrative text transformations only. No mathematical computation, simulation, theorem prover, numerical check, or symbolic-algebra program was run.

Both argument files were hashed. A first attempted manifest tool invocation failed with a JavaScript syntax error before execution because its raw template literal contained Markdown backticks; it wrote nothing and exposed no new input. This manifest was then composed for first writing with corrected serialization. Subsequent output hashes or integrity checks for delivery are administrative, not mathematical inputs.

