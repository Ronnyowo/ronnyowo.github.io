# C0002 reconstruction input and exposure record — v1

Role: fresh proof-blind independent reconstructor for C0002. Artifact: `AUDITS/C0002_RECONSTRUCTION_v1.md`. This record accompanies an independent mathematical argument, not a verdict on an author proof.

## Exact mathematical inputs

| Source | Version / role | SHA-256 |
| --- | --- | --- |
| `STATEMENT.md` | Frozen statement v1; campaign scope only | `ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97` |
| `CANDIDATES/C0002_resolvent_path_transfer/CONTRACT_v1.md` | Exact auxiliary contract v1 | `d42cb0e8db6e9667f77d45f7e4d54994179e48b206fb343af6e50eaf67057c6b` |
| `CANDIDATES/C0002_resolvent_path_transfer/BRIEF_v1.md` | Accepted reconstruction brief v1, as identified by the task dispatch | `ec44f79e9849a71bc2cad4d75978ffdde78b8748c83bbeb5e991d4529a92b192` |

Promoted dependencies: none.

All three allowlisted files were read in full in one command. Their hashes were obtained in a subsequent command naming exactly those files. No other mathematical source was opened or read. In particular, no literature links embedded in STATEMENT-v1 were opened; its sticky-flow conventions were not independently checked in this auxiliary reconstruction.

## Complete exposure declaration

The reconstructor was exposed to:

- The task dispatch specifying the allowlist, output paths, reconstruction role, the absence of promoted dependencies, and the prohibitions on candidate proofs, other audit records, cross-agent communication, and subagents.
- General system/developer tool and workflow instructions, the user-provided rigorous-mathematics and renderer-safe-LaTeX instructions, and workspace/environment metadata. No earlier campaign conversation was used as mathematical input.
- Exactly the full contents of the three source files listed above.
- Tool results for reading and SHA-256 hashing those same three files.
- Its own independently developed argument, its generated output content, and the generation/check results for these two output files.

The reconstructor did not read any candidate `PROOF` file, audit file, author manifest, version notes, registry, `FAILED` record, search transcript, or other workspace source. It did not inspect directory listings, search the workspace, browse the web, or consult an external reference. It did not spawn a subagent, send or receive cross-agent mathematical messages, or use a promoted campaign lemma. The eventual completion response necessarily returns the artifact paths to the assigning parent; there was no interim cross-agent communication.

The brief supplied only the hint to use the resolvent definition. No author-specific proof structure was supplied. The argument based on approximating a test function and its square, the stopping-time estimate, and the Laplace-transform identification were reconstructed independently.

## Ordinary background and limits

The argument uses only the ordinary background permitted by the contract: finite-state Markov-chain calculus and bounded optional stopping; compactness and Stone–Weierstrass; the Aldous tightness criterion; Prokhorov and Skorokhod representation; and elementary properties of the Skorokhod topology. It proves the particular Laplace uniqueness assertion directly. Bounded convergence and Fubini interchange are elementary measure-theoretic inputs used explicitly.

No microscopic hypothesis for SIP is asserted to have been established. This document does not certify STATEMENT-v1, promote C0002, compare the reconstruction with a candidate proof, or report any verdict on an unseen proof.

## Output integrity

The reconstruction content was checked in memory for paired renderer-safe LaTeX delimiters and balanced mathematical braces before creation. Both output files were created with exclusive-create semantics and read-only file mode; no preexisting output was overwritten, and no post-creation content edits were made.

SHA-256 of `AUDITS/C0002_RECONSTRUCTION_v1.md`: `28a6115917c3c793a923dcd34c168f8c17d28fdf1ec23083979c1bd688c624d8`.

The SHA-256 of this input record is reported by the creation tool and in the completion response, avoiding a self-referential hash field.
