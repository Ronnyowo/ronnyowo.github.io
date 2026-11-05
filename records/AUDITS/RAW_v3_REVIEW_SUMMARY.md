# Raw revision 3: final review summary

Date: 2026-11-04.
Version: Raw revision 3.
Result: four scoped critical reviews completed.
No reviewer reported a blocking mathematical gap in its assigned scope.
The reviews use separate contexts within the producing model family.
No human review, outside-family audit, or formal verification is claimed.
This record does not create a new source-campaign promotion.

## Exact reviewed text

Assembled content/raw.md SHA-256:
`0c2661067d9b9914376e1ffba936ef3088bea332d1be3bf0c96d423bd8d694a9`.

[Preserved proof snapshot](../RAW_PROOF_v3.md) SHA-256:
`b3f3eab86cdacd16a66661f53f0d3d7ac19fc619c72778c86bed63a0ce3b01f0`.

The snapshot is the exact assembled proof, with only the heading `# Raw proof: revision 3` and a blank line prepended.
Each final reviewer checked the same assembled source hash.
The mathematical text was not changed after those reviews.

## Review coverage

| Reviewer | Detailed scope |
| --- | --- |
| A | Appendix A and Sections 2–3: absorption, correction, trace expansion, full-block coefficients, qualitative localization, covariance, accelerated circle comparison, clock transfer, and collision passage. |
| B | Statement, Section 5, and Appendices B–C: sampling, conditional occupation, uniform mass semigroups, path tightness, continuity, law identification, and initial quantifiers. |
| C | Sections 3–4: equality and order cells, stopped martingales, form domain, all-block boundary flux, deterministic collision starts, parameter consistency, and circle uniqueness. |
| D | Additional check of Section 5 and Appendices B–C, including the exact Aldous page images and the Polish-space extension. |

The detailed assignments cover the complete proof.
Each record states the parts that its reviewer did not derive in detail.
Reviewer B did not verify the scanned Aldous citation itself.
Reviewer D checked the relevant page images and confirmed its exact use.
Proposition 3.1 is proved in the manuscript; it is not a hidden convergence premise.
The continuum construction and uniqueness theorems are cited external inputs.

| Reviewer | Record | SHA-256 |
| --- | --- | --- |
| A | [RAW_v3_CORRECTORS.md](RAW_v3_CORRECTORS.md) | `ce50e475a55cd9c8eb21d36e22623683146b7aeb970021a79ec9ee7db8894337` |
| B | [RAW_v3_MASS.md](RAW_v3_MASS.md) | `077d0f7d65a1723c28ebe956c4775f953bf22d35e006a15763b5ce734a9f1447` |
| C | [RAW_v3_IDENTIFICATION.md](RAW_v3_IDENTIFICATION.md) | `61437f89f857c59dea792bd8d19ef5a477972f8e292dd051c7964e433d343643` |
| D | [RAW_v3_PROBABILITY.md](RAW_v3_PROBABILITY.md) | `a029e4c7c99cb535db9d80139aa4dd3df455b8c90e1b84e0389653a986d44a82` |

## Changes from the earlier Raw text

- One general sampling lemma replaces the repeated factorial coefficient calculations.
- Uniform mass semigroup convergence gives path convergence directly through Appendix C.
- Trace tightness transfers through the clock and excursion bounds.
- A finite-type coupling replaces the quantitative localization powers.
- The block factorization used in localization is stated and proved.
- The stopped martingale passage names the three nested chart regions.
- The exact theorem, time scale, target, and finite-stack hypotheses are unchanged.

The source whitespace word count falls from 18,356 to 14,460, a reduction of 21.2 percent.
This count includes mathematical source tokens; it is not a count of prose words alone.
The full corrector construction, full-block coefficient proof, collision passage, and target identification remain.

## Technical checks

The build uses the pinned Markdown 3.7 package from requirements.txt.
The template, stylesheet, navigation, hosting configuration, and build scripts are unchanged.
The theorem text after its section heading is byte-identical to the earlier statement.
All 1,271 mathematical fragments compile with standard LaTeX.
The generated Raw HTML retains those same formula spans in the same order.
The 88 equation tags are unique, every cited equation tag exists, and the math delimiters are balanced.
All 66 earlier fixed records retain their public hashes.
The final site check verifies local links, downloads, all manifest hashes, and ZIP contents.

Visual browser QA was not completed.
The in-app browser could not reach the local preview, and access to Google Chrome was not approved.
This limit concerns display inspection, not the completed mathematical review or source checks.
