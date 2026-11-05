# From inclusion to sticky Brownian mass flow

This repository records an AI-written proof for public review.
It also contains a reading guide and the AI audit records.
A paper draft will be written in a later stage.

**Status:** the source campaign records the main result as **promoted**.
This label means that the proof passed the stated AI review procedure.
It does not mean peer review.
No audit by a human or a model outside the producing model family is recorded.

## Read the material

The reading site has three sections.

- **Overview:** the result and contributor.
- **Digested:** empty until a digested account is written.
- **Raw:** the exact theorem, full AI proof, and three supporting appendices.

The site follows the reading structure of
[the transverse-instability project](https://transverse-instability.github.io/).
The HTML template and stylesheet come from that site.
The title, links, and mathematical content are specific to this project.

Start with [the AI-written account](content/raw.md).
The exact theorem is in [STATEMENT.md](records/STATEMENT.md).
The current reading version is [Raw revision 3](records/RAW_PROOF_v3.md).
The earlier campaign proof is [C0008, proof v1](records/CANDIDATES/C0008_full_mass_convergence/PROOF_v1.md).
The source status is in [PROVED.md](records/PROVED.md).

## Result

The system has \(N\) particles on a cycle of length \(L_N\).
The small inclusion parameter is \(d_N\).
Assume
\[
N/L_N\to\rho\in(0,\infty),\qquad Nd_N\to\Theta\in(0,\infty).
\]
Use time acceleration \(N^2/d_N\).
For each fixed finite bound on the initial stack count, the proof claims convergence of the full mass process.
The initial occupied sites must have circular lattice distance at least two.
The initial mass measures must converge weakly.

The target is the mass process associated with the Le Jan–Raimond sticky flow on the circle.
The parameter is \(\alpha=\Theta/\rho\).
The one-point generator is \(\rho^2\partial_{xx}\).
The path topology is Skorokhod \(J_1\) on \(D([0,\infty),\mathcal P(\mathbb T))\).
The limit has continuous paths.
See the exact statement for every hypothesis and the full target definition.

## Proof files

| ID | Role | Exact version |
| --- | --- | --- |
| C0008 | Full mass convergence | Contract v1; proof v1 |
| C0005 | Harmonic correctors and trace estimates | Contract v2; proof v2 |
| C0006 | Conditional positive-layer occupation | Contract v2; proof v3 |
| C0002 | Uniform-resolvent path transfer | Contract v1; proof v2 |

The three auxiliary results have no campaign dependencies.
The campaign proof uses all three.
Raw revision 3 uses the shared sampling lemma and a direct semigroup transfer.
It retains the complete microscopic convergence proof.
Its version and final critical reviews are listed in [the review record](content/review.md).
The source files retain their creation-time labels.
The later promotion records state their review status.

## Build and check

Python 3.9 or later is required.

~~~sh
python3 -m venv .venv
.venv/bin/python -m pip install -r requirements.txt
.venv/bin/python build/build.py
.venv/bin/python build/check.py
.venv/bin/python -m http.server 8000 --directory docs
~~~

Open http://localhost:8000/.
The static site is generated in docs/.
The checked-in site can run without Python.
MathJax 3.2.2 loads from jsDelivr to render the mathematics.

## Publish

The GitHub repository is [inclusion-to-sticky-flow/inclusion-to-sticky-flow.github.io](https://github.com/inclusion-to-sticky-flow/inclusion-to-sticky-flow.github.io).
Use [PUBLISHING.md](PUBLISHING.md) to update the repository and enable GitHub Pages.
GitHub Pages uses GitHub Actions. The publishing workflow builds main and publishes the docs folder after its checks pass.
No site URL is claimed until deployment is complete.

## Edit

Edit content/raw-parts/ for the Raw proof.
The build assembles content/raw.md from these sections.
Keep content/digested.md empty until a digested account is written.
Edit content/overview.md for the overview.
Edit assets/style.css for the layout.
Then build the site and commit the source and generated files.

Do not overwrite a proof or audit record.
Add a new version for a mathematical change.
State the exact claim, its dependencies, and its review status.
Use [CONTRIBUTING.md](CONTRIBUTING.md) to report a possible gap.

See [PROVENANCE.md](PROVENANCE.md) for source hashes and the limited path redactions.
See [LICENSE.md](LICENSE.md) for the current license status.
