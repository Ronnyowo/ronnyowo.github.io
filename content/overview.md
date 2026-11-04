# Overview

This project records an AI-written proof of convergence from the inclusion process to a sticky Brownian mass flow.
The setting is the one-dimensional torus.
The initial state has a fixed finite number of stacks.

<div class="notice"><strong>AI proof record.</strong> The source campaign labels the result “promoted” after its AI review procedure. No human review or outside-family model audit is recorded.</div>

The small inclusion parameter is \(d_N\).
The number of particles is \(N\).
The cycle has \(L_N\) sites.
The scaling is
\[
\frac{N}{L_N}\longrightarrow\rho\in(0,\infty),
\qquad Nd_N\longrightarrow\Theta\in(0,\infty).
\]
With time acceleration \(N^2/d_N\), the claimed limit concerns the full mass measure
\[
\mu_N(t)=\frac1N\sum_x\eta_N(t,x)\delta_{x/L_N}.
\]
The target is the mass process associated with the Le Jan–Raimond sticky flow on the circle.
The proof addresses Skorokhod \(J_1\) convergence, with a continuous limit.
The [exact statement](records/STATEMENT.md) gives all initial conditions and the full target definition.

<div class="reader-grid">
<div><h2><a href="digested/">Digested</a></h2><p>Read the theorem, the proof plan, and the main new steps. This is a guide, not a paper draft.</p></div>
<div><h2><a href="raw/">Raw</a></h2><p>Read the main AI proof and its three supporting proofs. Download the source records.</p></div>
<div><h2><a href="review/">Review</a></h2><p>Check the review status, version hashes, audit records, and priorities for external review.</p></div>
</div>

## Scope

The theorem permits vanishing normalized stack masses.
Distinct initial stacks can have the same limiting position.
The initial occupied sites must be separated by at least two lattice steps.
The result concerns the torus.
No full-line theorem is claimed.

## Work planned

The current release preserves the AI proof and supplies a reading guide.
A paper draft and a full human mathematical review are later tasks.
Reports of precise gaps are welcome.
See the [review guide](review/).

## Project record

Simon Gabriel proposed the problem and directed the proof campaign.
Codex produced the proof text and the AI review records.
These roles do not imply human verification of the argument.

The three-section reading structure follows the
[transverse-instability site](https://transverse-instability.github.io/).
