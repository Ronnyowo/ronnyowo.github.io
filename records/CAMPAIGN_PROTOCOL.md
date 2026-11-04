# Campaign protocol — version 1

This durable file records the user's operative research protocol. STATEMENT.md is the immutable mathematical target. The root must re-read all durable state after context compaction; route and verification agents re-read only authorized bundles. No mathematical work may survive only in conversation.

## Completion and persistence

Only a complete proof or refutation of STATEMENT.md, promoted after the full verification cadence, completes the campaign. Partial results, special cases, finite computations, and reductions to an unproved theorem-strength lemma are insufficient. Continue new rounds and fresh mechanisms when routes fail. Do not call the problem open or search for whether it is open. No time or token budget was requested. The persistent goal remains the original one; goal tooling exposes no resume operation for a blocked goal.

Explicit user stop/pause/cancel immediately overrides persistence: launch nothing new, interrupt live assignments, mark interrupted active routes paused, record unreturned assignments as interrupted with no claim, and preserve partial artifacts as candidate. On pause/stop keep the goal incomplete, record campaign paused, and do not resume without explicit user instruction. On cancel record cancelled and cancel/deactivate the goal if supported. Save transferable process lessons only. Report the maximal established frontiers, exact gaps and statuses, and all route states on such handoff, notwithstanding the reporting gate.

## Literal claim statuses

- candidate: produced but not verifier-backed; failed, partial, inconclusive or protocol-only checks do not advance it.
- self-audited: rechecked only by its own author/context; for building on, counts as candidate.
- verifier-backed: that exact version passed leakage check, hostile audit, proof-blind independent reconstruction, and comparison with recorded inputs.
- promoted: verifier-backed and recorded in PROVED.md.
- independently audited: that exact promoted version was additionally checked by a nonparticipant outside the producing model family, or by a human.
- retracted: mathematical failure discovered in a previously checked version; retained in history but unusable as premise.

Anything built on a premise has at most that premise's status. Never call a mismatched case, global compatibility assertion, or polynomial recurrence routine. External standard theorems may be cited precisely and their hypotheses checked; do not present an unverified campaign lemma as external established background.

If no outside-family verifier is available, do not simulate it with another same-family model. Deliver at promoted status with prominent disclosure and a risk-ordered list for external review. Protocol-only external failure does not retract a promoted claim; substantive mathematical failure does. Recursively retract every dependent version whose contract cites the retracted version, remove affected entries from PROVED.md, and update REGISTRY.md.

## Search families and independence

At most six agents concurrently as requested, subject to the environment's stricter four-total-slot limit (root plus three workers). Use fresh contexts with fork_turns='none'. Independent search, kill checks and verification are distinct roles.

Before opening any family, check FAILED.md and record either “no close prior route” or “closest prior route is X; this differs materially because of ...”. Before assigning search agents to a new family, assign a fresh kill-check agent to test smallest instances and claimed sources. Inability to complete the route is inconclusive. A mismatch, violated hypothesis, circular premise or counterexample is only a candidate obstruction until the full cadence passes.

Begin with substantially different mechanisms. Do not tell most agents the favored approach. Preserve several distinct routes for at least two independent waves unless a verifier-backed obstruction closes one.

A search wave is a batch of search-agent work followed by root synthesis. A fresh independent search context receives only:
1. STATEMENT.md;
2. version-pinned, route-filtered views of baseline AUDIT_CHECKLIST.md, FAILED.md and PROVED.md;
3. later FAILED entries explicitly cited by its novelty check;
4. its own versioned route brief and authorized own-route artifacts.
It must not inspect other live routes, their registry rows, CANDIDATES, AUDITS, search discussion, or inherited conversation. The root supplies exact allowlists and revisions. External mathematical background use must follow the web policy and be recorded in an input manifest.

One independent-wave credit requires a fresh context, distinct brief, and a substantive mathematical deliverable: a proved lemma, explicit construction, counterexample, or exact obstruction plus decisive next test. These author-produced deliverables remain candidate until verified. At most one credit per family per root-synthesized wave; duplicate agents in one batch share the same credit. Kill checks, status messages, verification, and vague optimism earn no credit.

Before two credits, a stall means paused with a distinct remaining independent assignment scheduled. One failure cannot block a family. After two credits and a complete registry row, the root may mark it independently matured. Only matured families may cross-pollinate or combine; shared claims must have source family, exact version, status and dependencies. Hostile auditors remain isolated and reconstructors proof/audit-blind.

Group families by mathematical mechanism AND terminal missing lemma, not terminology. Redirect surplus agents when mechanisms converge. At each wave end update REGISTRY, synthesize consequences without leaking them into unmatured briefs, challenge the favorite, and choose continuations/pauses/redirections.

Registry row fields: family, exact attempted claim, exact gap, smallest known obstruction, decisive next test, independent-wave count, maturity, dependencies, exact evidence links, stall classification, state.
States: active while assigned; paused if viable but deprioritized; blocked after maturity with no mechanism for its exact gap; closed only with a verifier-backed route obstruction.
Every stalled family is classified method failure or evidence against target. If evidence against target, devote effort to complete refutation.
A matured route ending at a theorem-strength missing lemma is blocked, never “one lemma away”. Record blocked/closed routes in FAILED. Reactivate blocked routes only on materially new mechanism/invariant/lemma/source/witness/certificate/scope, with explicit novelty record. Changed mechanism/scope creates a linked new family. Retraction of a closing obstruction returns a closed route to paused.

## Immutable candidates and verification

Freeze each proof, refutation or route-closing obstruction in CANDIDATES as a new immutable version. Mathematical edits always create new versions.
Freeze an exact claim contract: statement, hypotheses, quantifier ranges, object identity, required outputs, and promoted dependencies.
Before audit freeze a reconstruction brief containing the contract and at most three one-sentence strategy hints. Hints may name definitions and promoted results, but may not contain unpromoted intermediate claims, ordered derivations, case splits, calculations/equations, witness values, or paraphrases/quotes from the candidate.

A fresh leakage checker sees candidate, contract and brief, records its complete input manifest, and checks that boundary. If it fails, create a new brief version and repeat.

1. Fresh hostile auditor allowlist: STATEMENT, exact candidate and contract, exact statements of promoted dependencies, and named AUDIT_CHECKLIST revision. No search records, registry commentary or author defense. Explicitly test every edge/failure mode, citation, quantifier and possible circularity.
2. Fresh independent reconstructor with no inherited conversation sees only STATEMENT, accepted brief and contract, and exact promoted-dependency statements. No candidate/audit/registry/FAILED/search artifacts. It writes a complete independent argument with dependencies, not a verdict on a proof it never saw.
3. Fresh comparator sees STATEMENT, contract, promoted-dependency statements, candidate, reconstruction, and both input manifests. Check reconstruction correctness and map all hypotheses, objects, dependencies, conclusions, required outputs and mechanism. A reconstruction changing scope/mechanism/dependencies or bypassing a disputed step becomes its own new candidate; it does not validate the old candidate.

Store every record in AUDITS naming exact inputs. Every failed check sticks to its exact version; never checker-shop with an unchanged/cosmetic version. Repair creates a new candidate and repeats cadence.
Before promotion compare hostile checklist revision with current checklist. Fresh hostile supplemental audits must cover every newly added item. Only all passes yield verifier-backed; recording in PROVED yields promoted.
Apply the same rigor to route-closing obstructions and refutations. Seek outside-family nonparticipant audit before final delivery when available.

## Reporting and evidence

User reporting gate: only unsolicited reports of promoted exact proof/refutation, a promoted lemma removing a named dependency, a verifier-backed minimal route-closing obstruction, or a promoted stronger/simpler theorem. Ordinary route updates and restructuring belong in files. Higher-priority desktop instructions additionally require brief commentary at tool-work start and during long work; keep such notices minimal and do not inflate mathematical progress.

Only write mathematical programs when essential for a named finite question. No inline-stdin computations. Each run has a source file, route ID, timeout, log, output path under EVIDENCE, and registry link. Preserve exact small witnesses/certificates and then prove their implications. No finite computation proves an unbounded theorem.

Public web use is restricted to ordinary mathematical background and standard named theorems. Do not search for a solution of this exact target or benchmark, or merely whether it is open. Log exact sources and theorem hypotheses. Local Kim–Landim manuscript may be copied into authorized route bundles as the user-provided reference.

All user-facing mathematics uses standard renderer-safe LaTeX with balanced \(...\) and \[...\]. Project macros belong only in fenced latex source.

