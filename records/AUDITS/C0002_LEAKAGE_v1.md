# C0002 leakage audit — v1

Verdict: **PASS**, exclusively for the exact input versions and SHA-256 hashes listed below.

Scope: disclosure restrictions on `BRIEF_v1.md`, assessed against `CONTRACT_v1.md` and `PROOF_v2.md`. This is not a mathematical-correctness audit. It neither promotes C0002 nor advances any mathematical claim status.

## Exhaustive input manifest

The checker read only these three workspace files. No other workspace files, external sources, or subagents were consulted. The task's leakage-checking instructions supplied the audit standard; no other conversation history supplied evidence.

| Input | Bytes | SHA-256 |
| --- | ---: | --- |
| `CANDIDATES/C0002_resolvent_path_transfer/CONTRACT_v1.md` | 2121 | `d42cb0e8db6e9667f77d45f7e4d54994179e48b206fb343af6e50eaf67057c6b` |
| `CANDIDATES/C0002_resolvent_path_transfer/BRIEF_v1.md` | 351 | `ec44f79e9849a71bc2cad4d75978ffdde78b8748c83bbeb5e991d4529a92b192` |
| `CANDIDATES/C0002_resolvent_path_transfer/PROOF_v2.md` | 7368 | `dc06b8b7e052bc994905afaa3b7fe168d7cde233dfa52e5e0355f5458c809a06` |

## Evidence and restriction-by-restriction determination

1. **Exact contract only: PASS.** The brief identifies `CANDIDATES/C0002_resolvent_path_transfer/CONTRACT_v1.md` as its exact contract. Its request, “Prove the exact contract, including stopping-time tightness and path-law identification,” restates the contractual obligations to prove stopping-time tightness and unique path-law identification. It adds no hypothesis, conclusion, or auxiliary assertion. Its candidate status and declaration of no promoted campaign dependencies agree with the contract.
2. **At most three one-sentence hints: PASS.** There is exactly one hint: “Strategy hint 1: Use the resolvent definition in the contract.” It is one sentence and refers to a definition expressly contained in the contract. “No other hints are supplied” provides no mathematical guidance.
3. **Permitted hint content: PASS.** The single hint names the contract's resolvent definition. It names no unpromoted result and asserts no intermediate mathematical claim.
4. **Forbidden disclosure: PASS.** Exhaustive inspection of the brief finds no intermediate lemma or claim, ordered proof step, case split, calculation, equation, witness, or candidate-proof quotation or paraphrase. Comparison with `PROOF_v2.md` supplies no additional disclosure in the brief: the only substantive hint remains the permitted reference to a contract definition. The shared reference to resolvents does not disclose a candidate-specific proof assertion.

The verdict is version-specific. It applies to no revised brief, contract, or proof unless separately audited.
