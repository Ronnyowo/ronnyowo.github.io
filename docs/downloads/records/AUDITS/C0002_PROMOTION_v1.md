# C0002 promotion record — v1

Status: promoted. Root decision after all version-bound checks passed; no mathematical edit made to any candidate or audit.

Exact input tuple:

| Input | SHA256 |
|---|---|
| STATEMENT.md v1 | ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97 |
| C0002 CONTRACT_v1.md | d42cb0e8db6e9667f77d45f7e4d54994179e48b206fb343af6e50eaf67057c6b |
| C0002 PROOF_v2.md | dc06b8b7e052bc994905afaa3b7fe168d7cde233dfa52e5e0355f5458c809a06 |
| C0002 BRIEF_v1.md | ec44f79e9849a71bc2cad4d75978ffdde78b8748c83bbeb5e991d4529a92b192 |
| C0002 RECONSTRUCTION_v1.md | 28a6115917c3c793a923dcd34c168f8c17d28fdf1ec23083979c1bd688c624d8 |
| C0002 RECONSTRUCTION_INPUTS_v1.md | 39fccaa850ba5593aaa475bddd2e3150c39f7a13c8a8d2c02b519ba279a6de75 |
| C0002 HOSTILE_v1.md | 279bf8dce9cb0dcd8b6c31b4c3ccaf24c0abb586b2e88432168f7422e08b1255 |
| C0002 COMPARISON_v1.md | 8515fc1b675393c5faaaece1a07716d74877482890be3bb250d4eb1aedbc9374 |
| C0002 SUPPLEMENT_AC003_v1.md | 28efbd1861cb264daca85bf9bf65c98ef5d0a0a8ba29e37d35ba789f88d75368 |

The leakage record AUDITS/C0002_LEAKAGE_v1.md passes the exact contract/brief/proof tuple above. The fresh hostile auditor passed against the exact AC-002 digest 20e1958f0c9d28179fa45fcf6aa0a55954538058d220f72c728e624e2b652188, preserved in CHECKLIST_AC002_CANONICAL.md. The proof-blind reconstruction and fresh comparison passed with recorded input manifests; the accepted brief names only the resolvent definition, and the comparator checked both tightness derivations as well as the common identification mechanism. A fresh supplemental auditor passed every AC-003 addition against CHECKLIST_AC003.md, digest ad7ebab088ea9c241ae4803d4c6687782df10f9c2653980be1150a20a9dc5db5. Its item content equals the current AC-003, global digest f33383b960e9e50f2759ec5550c2d3b00e1359d47c9fba5da1d1b3e5b8f6efdc. Root revalidated these exact digests before promotion. There are no uncovered checklist additions.

Thus the exact candidate has completed the full internal cadence and is recorded in PROVED.md P-002. Its status in this decision is promoted; candidate-era labels in frozen source files describe their creation state and are not edited.

No different-family model or human verifier is available. No cross-family audit has run. For future external review, check first (1) the general-metric stopping-time tightness and J_1 continuity step, (2) passage of microscopic resolvent martingales without projected Markovianity, and (3) conditional Laplace identification of the whole path law.

The contract is conditional. Its SIP uniform-resolvent hypothesis remains unproved, and STATEMENT-v1 remains candidate. No campaign completion is recorded. No result is transmitted into the currently unmatured routes' pinned W2 bundles.
