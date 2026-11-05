# Review record

## Raw revision 3

Date: 2026-11-04.
The [current proof snapshot](../records/RAW_PROOF_v3.md) contains the complete text now shown on Raw.
Its assembled source SHA-256 is
`0c2661067d9b9914376e1ffba936ef3088bea332d1be3bf0c96d423bd8d694a9`.

Four new critical agents checked that exact final text in separate contexts.
Their detailed assignments cover the complete proof.
No reviewer found a blocking gap in its assigned scope.
Each review records its scope and the parts it did not check in detail.
The [final summary](../records/AUDITS/RAW_v3_REVIEW_SUMMARY.md) records the combined result and verification limits.

| Reviewer | Detailed scope | Record |
| --- | --- | --- |
| A | Harmonic correction, full-block coefficients, qualitative localization, circle traces, and collision passage | [Corrector and trace review](../records/AUDITS/RAW_v3_CORRECTORS.md) |
| B | Statement, sampling, occupation, mass semigroups, tightness, continuity, and path-law identification | [Mass and path review](../records/AUDITS/RAW_v3_MASS.md) |
| C | Collision martingales, form normalization, deterministic collision starts, and circle uniqueness | [Collision and target review](../records/AUDITS/RAW_v3_IDENTIFICATION.md) |
| D | Additional check of the probability argument and the exact Aldous criterion | [Probability and citation check](../records/AUDITS/RAW_v3_PROBABILITY.md) |

The final proof includes the microscopic convergence argument and all three supporting appendices.
It does not assume Proposition 3.1 as an external input.
The earlier simplification report had a narrower review scope.
The reviews above concern the final publication text itself.
All reviewers belong to the producing model family.
No human or outside-family audit is recorded.

## Historical source campaign

The source campaign records C0008 as **promoted**.
This is a label from its stated AI review procedure.
It is not a claim of peer review or formal verification.
No human review or outside-family model audit is recorded.

## Required checks in the source campaign

1. A leakage check compared the proof contract and reconstruction brief.
2. A hostile audit checked the proof against the named checklist.
3. A new agent reconstructed the argument without the author proof.
4. A comparator checked both arguments and their input records.
5. The root checked the current checklist and recorded promotion.

These roles used separate contexts within the same model family.
This page does not call them independent external reviews.

## Exact status records

| Claim | Promotion record |
| --- | --- |
| Full theorem: C0008 | [Contract v1 / proof v1](../records/AUDITS/C0008_PROMOTION_v1.md) |
| Correctors: C0005 | [Contract v2 / proof v2](../records/AUDITS/C0005_PROMOTION_v1.md) |
| Positive layers: C0006 | [Contract v2 / proof v3](../records/AUDITS/C0006_PROMOTION_v1.md) |
| Path transfer: C0002 | [Contract v1 / proof v2](../records/AUDITS/C0002_PROMOTION_v1.md) |

The [status ledger](../records/PROVED.md) states the promoted claims.
The [current checklist](../records/AUDIT_CHECKLIST.md) lists 29 checks.
The earlier [C0004 disposition](../records/AUDITS/C0004_DISPOSITION_v1.md) records an incomplete reconstruction and comparison.
That earlier candidate is not a premise of C0008.

## C0008 records

- [Leakage check](../records/AUDITS/C0008_LEAKAGE_v1.md).
- [Hostile audit](../records/AUDITS/C0008_HOSTILE_v1.md).
- [Reconstruction](../records/AUDITS/C0008_RECONSTRUCTION_v2.md).
- [Reconstruction inputs](../records/AUDITS/C0008_RECONSTRUCTION_INPUTS_v1.md).
- [Comparison](../records/AUDITS/C0008_COMPARISON_v1.md).
- [Promotion record](../records/AUDITS/C0008_PROMOTION_v1.md).

## External review priorities

Review the all-order corrector and localization estimates first.
Then check the accelerated excursion errors and the collision-occupation passage.
Next check target normalization and circle uniqueness.
Finally check the sampling lift, uniform mass semigroups, Appendix C, and the initial conditions.

Report the exact file, version, location, and mathematical objection.
The repository has an issue template for proof gaps.

## Export integrity

All proof, contract, and brief files retain their exact source bytes.
Some audit copies replace an absolute private workspace path.
The [export notes](../provenance/) identify those copies.
The [manifest](../downloads/manifest.json) records both source and public SHA-256 hashes.
No source mathematical text was changed during export.
