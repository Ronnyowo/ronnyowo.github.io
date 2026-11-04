# C0008 leakage check — v1

Verdict: **PASS**.

Role: fresh LEAKAGE CHECK. Scope: protocol only. This verdict is bound jointly to the exact three versions and SHA-256 values in the complete actual input manifest below. It does not verify the proof, promote any mathematical assertion, or advance mathematical status.

## Complete actual input manifest

Working directory: `[private workspace]`.

The only local files opened as inputs were these three files, all relative to that directory:

| Actual input | Verified SHA-256 |
| --- | --- |
| `CANDIDATES/C0008_full_mass_convergence/CONTRACT_v1.md` | `56bde5e0c1f439c43bf600aa9f0783b4f7da9ba8c6648e05072373af92b040cd` |
| `CANDIDATES/C0008_full_mass_convergence/PROOF_v1.md` | `8d97fd0abba1232e8befd553489dd88a5239dbbdb962a8472e7e050dc9408868` |
| `CANDIDATES/C0008_full_mass_convergence/BRIEF_v1.md` | `ec0c06433d0303df9a8c0120373103beed8b0f53687011f2b4b5834bf5c139f4` |

All three hashes were checked against the assignment before the first content read and checked again before this report was written. The contents of all three files were inspected. An initially truncated proof display was supplemented by a complete later display of its omitted middle section.

The non-file inputs were the assigning root's role, exact-path, hash, leakage-rule, and output instructions, together with the inherited session instructions and tool descriptions. No other local file, named dependency, audit, author manifest, registry, source mentioned by the documents, or external source was opened. No search, subagent, or mathematical program was used. Commands performed only administrative hashing, text reads/comparison, and exclusive creation of this report. Output from those commands added no other document input.

## Rule applied

The brief may contain the exact claim contract and at most three one-sentence strategy hints. Any hints may name definitions or promoted results, but may not contain unpromoted intermediate claims, ordered derivations, equations or calculations, witness values, case splits, or proof paraphrases. The exact claim contract itself is the expressly permitted payload.

## Evidence

1. The body enclosed by the unique `--- BEGIN EXACT CONTRACT ---` and `--- END EXACT CONTRACT ---` delimiters in `BRIEF_v1.md` is exactly 8,828 bytes. Administrative byte comparison established that it equals the entire hash-verified `CONTRACT_v1.md` byte for byte, including its final newline. These are brief lines 7–129, corresponding to contract lines 1–123.

2. The complete text preceding the opening delimiter is the brief title, a blank line, and the following status paragraph, followed by a blank line:

   > Status: candidate. The material below is the exact claim contract. There are zero strategy hints and no proof content in this brief.

   There is no text after the closing delimiter and its newline. Thus there are exactly zero strategy hints and no additional mathematical assertion or argument outside the permitted exact-contract payload.

3. The contract payload specifies the microscopic system, initial quantifiers, continuum target, exact conclusion, method restrictions, and permitted dependencies. Its dependency table names the three exact contracts represented as promoted in the assignment, with administrative hashes and scope restrictions. Those names and bindings are part of the supplied contract; they add no intermediate derivation from the candidate proof. Their promotion status was not independently investigated in this protocol-only role.

4. Comparison with `PROOF_v1.md` shows that its candidate arguments in Parts I–IV are not supplied as hints or added brief text. In particular, the brief does not supply the proof's absorption and excursion estimates, local correction calculations, equality-indicator replacement argument, integration-by-parts derivation, parameter completion, factorial-intertwining calculation, or fourth-moment continuity argument. Any shared target equations or target assertions occur within the byte-identical permitted contract, not as additional proof content.

The exhaustive decomposition in items 1–2 proves compliance: the brief consists solely of the exact contract plus administrative framing, with zero hints. No prohibited proof material is added.

## Version and status boundary

This PASS applies only to the exact hash-bound triple listed above. Any change to any of those files requires a new version-specific leakage check. The verdict certifies brief admissibility under the assigned leakage rule only; it is not a mathematical correctness verdict, independent reconstruction, comparison result, promotion, or campaign-completion finding.

This report was created once using exclusive creation, with read-only file permissions. It must be preserved; any correction belongs in a new version.
