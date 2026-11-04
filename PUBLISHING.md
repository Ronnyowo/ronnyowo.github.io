# Publish on GitHub

The user created the public repository:
[inclusion-to-sticky-flow/inclusion-to-sticky-flow.github.io](https://github.com/inclusion-to-sticky-flow/inclusion-to-sticky-flow.github.io).

## Update the site

1. Edit the guide or site code.
2. Run the build and checks described in README.md.
3. Commit the source and generated files.
4. Push the main branch to origin.

Do not overwrite fixed proof or audit records.
Add a new version for a mathematical change.

## Enable GitHub Pages

Open the repository Settings, then Pages.
Select GitHub Actions as the publishing source.
The Publish the reading site workflow builds and checks the site on each push to main.
It publishes the generated docs directory after the checks pass.
The workflow can also be started from the Actions tab.

The site address is https://inclusion-to-sticky-flow.github.io/.
The address serves a new version only after its deployment succeeds.
Check the deployment status in the repository Actions tab.
Then open Overview, Digested, and Raw at the public address.
