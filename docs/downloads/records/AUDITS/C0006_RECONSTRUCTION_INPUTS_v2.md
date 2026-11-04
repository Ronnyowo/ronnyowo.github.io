# C0006 proof-blind reconstruction inputs and exposure — version 2

Status: complete exposure record for the independently written, self-audited reconstruction in `AUDITS/C0006_RECONSTRUCTION_v2.md`; mathematical comparison and promotion are pending. This record and its companion proof are immutable first writes. Any subsequent mathematical change requires a new versioned file.

## Authorized source files actually read

The reconstructor read exactly the following three source files, in full, in one administrative shell call that first computed their SHA-256 hashes and then concatenated their contents. The observed hashes matched the allowlist supplied in the task.

| Source file | SHA-256 |
| --- | --- |
| `STATEMENT.md` | `ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97` |
| `CANDIDATES/C0006_uniform_thin_layers/CONTRACT_v2.md` | `805ea9a15da4e350f0af208075932c45473a8f499a89f77f050c6c916c4891b9` |
| `CANDIDATES/C0006_uniform_thin_layers/BRIEF_v2.md` | `48c8eb60d02da1a0a186d5d040a48e3c8b12bfd7fda553352feb29e9f1848086` |

The brief reproduces the exact contract and supplies no strategy hints. The statement provides the campaign target and scope, but no campaign assertion is used as a lemma in this reconstruction. Its literature links were neither opened nor used as mathematical premises.

## Other exposure

The reconstructor also received the parent task instructions: the three-file allowlist and their expected hashes, the assertion that the brief passed leakage and that no promoted dependencies exist, the required output filenames, and the requirements for proof blindness, independent completion, versioned preservation, exposure logging, and self-audited status pending comparison. Those instructions contained no candidate proof, proof strategy, or mathematical dependency. General session instructions, the workspace path, and available tool descriptions were visible. No additional mathematical material was supplied by another agent.

No candidate proof, author input, earlier version, prior audit, leakage report, prior reconstruction, other candidate, route, registry, `FAILED` record, `PROVED` record, or unallowlisted referenced file was read. No directory inventory was requested. No web search or literature lookup was made. No subagent was spawned, and no mathematical program, simulation, symbolic check, or inline-stdin calculation was run.

The only filesystem operations before writing the proof were the three authorized hashes and reads, and existence tests for the two intended output filenames. The existence tests returned success, establishing that neither output existed before its first write. The proof was then written as literal patch text, and its SHA-256 hash was computed. This exposure record was likewise written as literal patch text. Hashing the completed outputs for delivery is administrative verification, not an additional mathematical source. Neither file was mathematically edited after being written.

## Mathematical premises and reconstruction

There are no promoted dependencies and no external literature dependencies. The finite cyclic Poisson construction, its oscillation estimate, the cancellation of all third-label terms in the aggregate pair potential, the finite-state martingale argument, the filtration augmentation argument, and the bounded stopping-time identity are proved directly in the companion document. All mathematical reasoning was performed by the reconstructor without mathematical tool calculations.

The output proves the complete quantified conditional inequality in CONTRACT-v2. This statement reports the reconstruction's contents and does not express a verdict on the unseen candidate proof. Its status is self-audited pending comparison.

## Frozen proof output

| Output file | SHA-256 after its first write |
| --- | --- |
| `AUDITS/C0006_RECONSTRUCTION_v2.md` | `2825af0de39851170c391f4bdacb8cfa1029e880e58414ddc4d69a1160faa07d` |

The hash of this exposure record itself is reported separately to the parent after its first write, avoiding a self-referential file hash.
