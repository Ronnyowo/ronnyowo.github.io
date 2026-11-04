# Source map for the Raw proof

Status: candidate. This is an editorial presentation of the fixed source proof.
The edit does not create a new promotion record.

| Public section | Fixed source |
| --- | --- |
| Statement and Theorem 1 | records/STATEMENT.md |
| Sections 2–5 | C0008_full_mass_convergence/PROOF_v1.md |
| Appendix A: statement | C0005_harmonic_correctors/CONTRACT_v2.md |
| Appendix A: proof | C0005_harmonic_correctors/PROOF_v2.md |
| Appendix B: statement | C0006_uniform_thin_layers/CONTRACT_v2.md |
| Appendix B: proof | C0006_uniform_thin_layers/PROOF_v3.md |
| Appendix C: statement | C0002_resolvent_path_transfer/CONTRACT_v1.md |
| Appendix C: proof | C0002_resolvent_path_transfer/PROOF_v2.md |

The C0002, C0005, C0006, and C0008 files are under records/CANDIDATES/.
The source hashes are in [the manifest](../../records/manifest.json).
The fixed source status and review records remain in records/.

## Editorial changes

The public statement retains all mathematical hypotheses, quantifiers, target definitions, and conclusions.
The proof retains the mathematical steps and estimates.
Administrative campaign text is omitted.
The three supporting statements and proofs appear on the same page.
The references C0005, C0006, and C0002 become Appendices A, B, and C.
Equation labels in the appendices have distinct prefixes.
Equation labels I–IV in the main proof retain their source numbers.

The line operators are defined before their first use.
In Appendix A, a block subtuple is distinguished from the block's site.
Its covariance coupling specifies an unconditional pure-excursion marginal.
Its martingale bound uses the precise term “predictable quadratic-variation density”.
In Appendix C, a countable uniformly dense class replaces the ambiguous phrase “countable separating class”.
Uniform approximation explains why this class determines probability measures.

These changes clarify the presentation.
The editorial checks do not replace a mathematical audit of the theorem.
No human or outside-family model audit is recorded.

## Editing

Edit the separate Markdown files in this directory.
The build assembles content/raw.md from those parts.
Keep content/digested.md empty until a digested account is written.
