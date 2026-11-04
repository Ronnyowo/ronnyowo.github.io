# C0005 leakage audit — v2

Verdict: **PASS (protocol only)**.

This is a leakage check of the frozen reconstruction brief against its exact claim contract and candidate proof. It is not a mathematical audit, independent reconstruction, promotion, verification of the theorem, or validation of any other candidate. Mathematical status is unchanged.

## Exact inputs and complete exposure

The only local input files opened were the following three files, all under `CANDIDATES/C0005_harmonic_correctors/`:

| Input | Bytes | Lines | SHA256 |
| --- | ---: | ---: | --- |
| `CONTRACT_v2.md` | 8322 | 138 | `0a0130d01e482dbe546a19248b1ca67180aa373643dace7a87abc5cff8eb8cec` |
| `PROOF_v2.md` | 37209 | 340 | `68a9fec530428b3fd61e9f3bef1564e3ad3bcbd905d0cf0b51801a58bd6fc5ef` |
| `BRIEF_v2.md` | 8715 | 148 | `35a10be2298890820aeeb7ab72d47e3a0602f9ea7907cbd20666648353ed4e5b` |

All three hashes match the frozen values in the assignment. The entire contract and brief were exposed. The first combined display truncated part of the proof; the subsequent numbered display exposed all 340 proof lines without truncation. Thus the full candidate proof was available for comparison. It was not supplied as part of the reconstruction brief.

The checker also received the assignment, the user-supplied AGENTS.md instructions, and the tool/environment instructions in the conversation. No other local input, directory inventory, author manifest, old version, earlier audit, route, statement, registry, or external source was opened. Names of other files appearing inside the permitted inputs were read only as text; those files were not followed. No web access, mathematical program, simulation, or subagent was used. Python operations were limited to administrative file reading, hashing, byte comparison, line numbering, and creation of this report.

## Exact-contract inclusion

The opening marker occurs once at brief line 5 and the closing marker occurs once at line 146. Brief lines 7–144 reproduce contract lines 1–138. Extracting the bytes immediately after the opening marker and its separating blank line, and immediately before the newline preceding the closing marker, yields exactly the original 8322 contract bytes, including the contract's final newline. The extracted SHA256 is `0a0130d01e482dbe546a19248b1ca67180aa373643dace7a87abc5cff8eb8cec`; direct byte equality also returned true.

Consequently the embedded claim has no insertion, deletion, modification, or additional material under its exact-contract markers. Its definitions, six numbered required conclusions, and one-label convention are all part of the supplied exact theorem statement. Their presence is not treated as proof leakage.

## Complete material outside the exact claim

Apart from the two marker lines and whitespace, all text outside the exact contract is reproduced below:

```text
# C0005 reconstruction brief — v2

Status: **candidate**. The exact claim contract below is included verbatim. This brief supplies no promoted campaign dependency and makes no verification claim.

Definition-only hint: The absorption extension, killed potential, and coordinate-order chambers are the named definitions.
```

The title and status paragraph are administrative metadata. They give no mathematical argument, result, or instruction for deriving the theorem. The inclusion statement is supported by the byte comparison above. The dependency statement supplies no promoted result.

## Hint check and proof-content comparison

There is exactly one hint, at brief line 148, and it consists of exactly one sentence:

> Definition-only hint: The absorption extension, killed potential, and coordinate-order chambers are the named definitions.

The absorption extension and killed potential are explicitly introduced in contract lines 15–19, reproduced at brief lines 21–25. Coordinate-order chambers occur in the chamber-affine definition at contract line 29, reproduced at brief line 35. The hint merely names this contract vocabulary. It supplies no promoted result and does not assert any additional property of these objects.

The one-sentence hint contains no unpromoted intermediate claim, derivation step or ordering, case split, equation, calculation, or witness value. Comparison against the full proof reveals no quoted or paraphrased proof-specific content in this hint. Shared names of definitions are precisely the permitted overlap. The remaining extra text is exhausted by the administrative material reproduced above, so there is no concealed second hint or appended claim.

## Scope of verdict and sealing

PASS means only that this exact brief contains the exact frozen claim contract and one permissible definition-only sentence, with no prohibited leakage identified under the assigned rule. It does not advance mathematical status.

This report was created at `AUDITS/C0005_LEAKAGE_v2.md` using exclusive file creation, without replacing an existing file, and set to read-only mode 0444. Its content is sealed by the SHA256 returned to the parent task. It is to remain unchanged; any future correction requires a new versioned file.
