# Promoted results

Current revision: P-005.

## C0002 — abstract uniform-resolvent path transfer

Status: promoted. Exact version: CANDIDATES/C0002_resolvent_path_transfer/PROOF_v2.md, with CONTRACT_v1.md and accepted BRIEF_v1.md. No promoted campaign dependencies.

For a finite-state Markov chain projected into a compact metric space, uniform convergence of all positive resolvents on continuous tests to those of a supplied continuous-path Feller process, together with uniformly vanishing projected jumps, implies convergence of the full projected path law from every converging deterministic initial projection. The projection need not itself be Markov. The uniform microscopic resolvent hypothesis is an assumption, not an established SIP result.

Proof SHA256: dc06b8b7e052bc994905afaa3b7fe168d7cde233dfa52e5e0355f5458c809a06. Contract SHA256: d42cb0e8db6e9667f77d45f7e4d54994179e48b206fb343af6e50eaf67057c6b.

Passing records: AUDITS/C0002_LEAKAGE_v1.md; AUDITS/C0002_HOSTILE_v1.md; AUDITS/C0002_RECONSTRUCTION_v1.md and C0002_RECONSTRUCTION_INPUTS_v1.md; AUDITS/C0002_COMPARISON_v1.md; AUDITS/C0002_SUPPLEMENT_AC003_v1.md. Baseline hostile coverage AC-001 and AC-002 plus fresh supplemental coverage of all AC-003 additions equaled the checklist current at its historical promotion, AC-003. Exact promotion decision and hashes: AUDITS/C0002_PROMOTION_v1.md.

Outside-family audit has not run: no eligible different-family model or human verifier is available in this environment. This result is not independently audited. It does not complete STATEMENT-v1, identify the SIP limit, or remove the all-order microscopic identification gap.

## C0006 — uniform conditional positive-layer occupation

Status: promoted. Exact version: CANDIDATES/C0006_uniform_thin_layers/CONTRACT_v2.md / PROOF_v3.md, accepted BRIEF_v2.md. No promoted campaign dependencies.

For the exact finite labelled inclusion generator \(q(R_n+d^{-1}I_n)\) on a cycle of length \(L\), every allowed state, law, and pair of bounded stopping times has the conditional positive-layer estimate
\[
\mathbb E\left[\int_\tau^\sigma B_k(Z_s)\,ds\mid\mathcal F_\tau\right]
\le\binom n2\left[\frac{2k\delta}{L+1/d}+\frac{Lk}{q}\right],
\qquad 0\le\tau\le\sigma\le\tau+\delta.
\]
The exact contract quantifies over all integers \(L\ge3,n\ge2,1\le k<L/2\), all positive \(q,d\), deterministic \(\delta\ge0\), and arbitrary initial distributions. Equality distances are excluded from \(B_k\).

Contract SHA256: 805ea9a15da4e350f0af208075932c45473a8f499a89f77f050c6c916c4891b9. Proof SHA256: 9a4e9936a55b8e4179c3c964eb297236ac06d008425bb64f9e48eb4856dc4186.

Passing records: AUDITS/C0006_LEAKAGE_v2.md; C0006_HOSTILE_v2.md; C0006_RECONSTRUCTION_v2.md and its INPUTS-v2; C0006_COMPARISON_v2.md. Full exact inventory, mechanism comparison, current AC-005 coverage and promotion decision: AUDITS/C0006_PROMOTION_v1.md.

Outside-family audit has not run because no eligible verifier is available. This is not independently audited. It removes the unproved uniform positive-layer estimate from the microscopic convergence argument; it does not by itself establish microscopic convergence, identify the full mass limit, or complete STATEMENT-v1.

## C0005 — canonical harmonic corrections and actual trace estimates

Status: promoted. Exact version: CANDIDATES/C0005_harmonic_correctors/CONTRACT_v2.md / PROOF_v2.md, accepted BRIEF_v2.md. No promoted campaign dependencies.

All six exact contract conclusions and the one-label convention are promoted: pure absorption and leading trace bounds; the canonical chamber-affine correction and harmonicity; every labelled split coefficient with quantitative separated-block localization; corrected coordinate covariances; the actual perturbed trace expansion with bounded remainder; and all specified duration, event-count, displacement and jump-moment estimates. The count includes an independent jump causing return. The theorem is uniform in every position, partition and test covered by the contract, at each arbitrary fixed particle order.

Contract SHA256: 0a0130d01e482dbe546a19248b1ca67180aa373643dace7a87abc5cff8eb8cec. Proof SHA256: 68a9fec530428b3fd61e9f3bef1564e3ad3bcbd905d0cf0b51801a58bd6fc5ef.

Passing records: AUDITS/C0005_LEAKAGE_v2.md; C0005_HOSTILE_v2.md; C0005_RECONSTRUCTION_v2.md and its INPUTS-v2; C0005_COMPARISON_v2.md. The exact inventory, mechanism mapping, current AC-005 coverage, provenance qualification and promotion decision are in AUDITS/C0005_PROMOTION_v1.md.

Outside-family audit has not run because no eligible verifier is available. This result is not independently audited. It removes the canonical corrector and trace-estimate dependency but does not itself prove microscopic circle convergence or the full mass theorem. The unsuccessful C0004 v1 cadence is not changed by this promotion.

## C0008 — exact full mass convergence in the critical regime

Status: promoted. Exact version: CANDIDATES/C0008_full_mass_convergence/CONTRACT_v1.md / PROOF_v1.md, accepted BRIEF_v1.md. This proves the complete unchanged finite-stack assertion in STATEMENT-v1. Its only promoted campaign dependencies are the exact C0002, C0005 and C0006 versions above.

For every parameter sequence and deterministic initial sequence specified in STATEMENT-v1,
\[
\operatorname{Law}_{\eta_N^0}(\mu_N(\cdot))
\Longrightarrow Q_{\mu_0}
\quad\text{in }D([0,\infty),\mathcal P(\mathbb T))
\]
with the weak state topology and Skorokhod \(J_1\) path topology. The target is the exact common sticky-flow mass law fixed by the partition forms, and has continuous paths. All fixed finite stack bounds, vanishing normalized masses, coincident limiting positions and prescribed nonstationary starts are included.

Contract SHA256: 56bde5e0c1f439c43bf600aa9f0783b4f7da9ba8c6648e05072373af92b040cd. Proof SHA256: 8d97fd0abba1232e8befd553489dd88a5239dbbdb962a8472e7e050dc9408868. Frozen statement SHA256: ca925b943f2dc5573b840512e12ebd5f38fbdb15df7a6b02c3dd72f7ac698a97.

Passing records: AUDITS/C0008_LEAKAGE_v1.md; C0008_HOSTILE_v1.md; complete C0008_RECONSTRUCTION_v2.md with RECONSTRUCTION_INPUTS_v1.md; C0008_COMPARISON_v1.md. Root's exact inventory, current AC-005 coverage, mechanism and premise-scope checks, and promotion decision are in AUDITS/C0008_PROMOTION_v1.md. The earlier reconstruction v1 is preserved as a literal-formatting version; no mathematical change was made in v2. Every required check applies to this same full candidate version.

The proof derives actual all-order microscopic path convergence and the full-state mass resolvent hypothesis before applying C0002. It is not a conditional microscopic-limit reduction, fixed-order endpoint, equilibrium result, or Mosco proof.

**Outside-family audit has not run because no eligible verifier is available. The earned status is promoted, not independently audited.** Highest-priority external checks: C0005 all-order localization; C0008 accelerated excursion and collision-occupation passage; exact target normalization and every-point uniqueness; full mass resolvents and C0002; target continuity and initial quantifiers. No broader initial-data or full-line theorem is separately promoted.

Each future entry must identify the exact immutable version, status, claim contract, proof/certificate, promoted dependencies, all passing audit records, checklist coverage, and outside-family audit status. Remove any retracted claim from the active promoted list while preserving its retraction record elsewhere.
