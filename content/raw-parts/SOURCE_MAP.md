# Source map for Raw revision 3

Date: 2026-11-04.
This revision gives the complete theorem and proof on the Raw page.
It replaces the earlier editorial text with the shorter arguments listed below.
The theorem and its initial-state hypotheses are unchanged.
The fixed campaign proof and audit records remain unchanged.

## Mathematical sources

| Public part | Source and change |
| --- | --- |
| Section 1 | The statement in records/STATEMENT.md. Only the abstract and revision note changed. |
| Sections 2–4 | C0008 proof v1. Section 2 transfers trace tightness through the clock. Section 3 uses the qualitative localization bound. The stopped martingale and target-identification proofs remain complete. |
| Section 5 | Uniform semigroup convergence, the shared sampling lemma, and Theorem C.1 give mass-path convergence directly. |
| Appendix A | C0005 proof v2, with a finite-type coupling in place of the power-rate localization argument. The construction, perturbation expansion, and full-block coefficient proof remain. |
| Appendix B | One general sampling lemma replaces the repeated algebra. The conditional occupation estimate has the original constants. Its full Poisson and optional-sampling proof is included. |
| Appendix C | A direct semigroup path-transfer theorem replaces the resolvent theorem. Its proof includes tightness, continuity, and identification. |

The C0005, C0006, and C0008 source files are under records/CANDIDATES/.
The old C0002 resolvent result remains a historical source record.
The revised proof does not need it.
The [manifest](../../records/manifest.json) records the fixed file hashes.

## Scope

Proposition 3.1 is proved in Sections 2–4.
It is not an assumed microscopic convergence result.
Appendix A proves the retained harmonic-correction estimates.
Appendix B proves the positive-layer bound used to pass equality indicators.
Section 4 proves the target identification, including deterministic collision starts.
Thus the published proof includes the inputs that the earlier simplification report retained as premises.

## Version and review record

The full revision is preserved in records/RAW_PROOF_v3.md.
The separate critical reviews and their exact source hash are linked from content/review.md.
These reviews concern the final assembled text.
The reviewers use separate contexts within the producing model family.
No human or outside-family audit is claimed.

The build assembles content/raw.md from the five mathematical part files.
The webpage template, stylesheet, navigation, and hosting configuration are unchanged.

## Public display

The review page and audit exports are omitted from the public build.
The review records remain in the repository.
The Raw revision note has no review link.
Only this display note changed; the mathematical proof is unchanged.
