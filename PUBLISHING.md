# Publish on GitHub

The local repository is ready for publication.
No remote repository was created during preparation.
The request to use the existing GitHub sign-in was declined.

The suggested repository name is inclusion-to-sticky-flow.
The planned owner is KugelschreiberY, based on the workspace Git remote.
Confirm the owner when you sign in.

Use the GitHub CLI:

~~~sh
gh auth login
gh repo create inclusion-to-sticky-flow --public --source . --remote origin --push
gh api --method POST repos/OWNER/inclusion-to-sticky-flow/pages \
  --input - <<'JSON'
{"build_type":"legacy","source":{"branch":"main","path":"/docs"}}
JSON
~~~

Replace OWNER with the account that owns the new repository.
You can also create the repository and enable Pages through the GitHub website.

After creation:

1. Set the actual repository URL in site.json.
2. Set repository_created to true.
3. Build and check the site.
4. Commit the changed files and push them.
5. Check that GitHub Pages reports a successful build.
6. Open the deployed Overview, Digested, and Raw pages.

The normal Pages URL is https://OWNER.github.io/inclusion-to-sticky-flow/.
This is a planned address, not a verified deployment.
