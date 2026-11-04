"""Build the reading site. Keep the source records unchanged."""
import html
import json
import os
import re
import shutil
import zipfile
from pathlib import Path

import markdown

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CONFIG = json.loads((ROOT / "site.json").read_text())
PROOFS = [
    ("full-mass", "Full mass convergence", "C0008_full_mass_convergence/PROOF_v1.md"),
    ("correctors", "Harmonic correctors", "C0005_harmonic_correctors/PROOF_v2.md"),
    ("positive-layers", "Positive-layer occupation", "C0006_uniform_thin_layers/PROOF_v3.md"),
    ("path-transfer", "Path transfer", "C0002_resolvent_path_transfer/PROOF_v2.md"),
]


def relative(target, output):
    return os.path.relpath(DOCS / target, (DOCS / output).parent).replace(os.sep, "/")


def render(source, output, provenance=False, literal_html=False):
    saved = {}
    # Keep code blocks and code spans out of the math parser.
    pattern = re.compile(r"(?ms)^([~\x60]{3,})[^\n]*\n.*?^\1[ \t]*$|\x60[^\x60\n]+\x60|\\\[.*?\\\]|\\\(.*?\\\)")

    def protect(match):
        value = match.group()
        if not value.startswith(("\\[", "\\(")):
            return value
        key = "MATHPLACEHOLDER" + str(len(saved)) + "END"
        saved[key] = html.escape(value)
        return key

    md = markdown.Markdown(extensions=["extra", "toc"], extension_configs={"toc": {"toc_depth": "2-3"}})
    prepared = pattern.sub(protect, source)
    if literal_html:
        # Source records are text. A bare inequality must not start an HTML tag.
        prepared = prepared.replace("<", "&lt;")
    body = md.convert(prepared)
    toc = md.toc
    for key, value in saved.items():
        body = body.replace(key, value)
        toc = toc.replace(key, value)

    def links(match):
        url = html.unescape(match.group(1))
        if re.match(r"^[a-zA-Z]+:|^#|^//", url):
            return match.group()
        path, sep, fragment = url.partition("#")
        if provenance and path.startswith("records/"):
            path = relative(path, output)
        if path.endswith(".md"):
            path = path[:-3] + ".html"
        if path.endswith("records/manifest.json"):
            path = relative("downloads/manifest.json", output)
        return 'href="' + html.escape(path + sep + fragment, quote=True) + '"'

    body = re.sub(r'href="([^"]+)"', links, body)
    return body, toc


def write_page(output, title, source, active="", download=None, record=False, provenance=False):
    body, toc = render(source, output, provenance, literal_html=record)
    link = lambda p: relative(p, output)
    nav = "".join(
        '<a href="{}"{}>{}</a>'.format(link(path), ' aria-current="page"' if active == name else "", name)
        for name, path in [("Overview", "index.html"), ("Digested", "digested/index.html"), ("Raw", "raw/index.html")]
    )
    notice = ""
    if record:
        notice = ('<div class="notice"><strong>Fixed source record.</strong> '
                  'Creation-time labels remain unchanged. See the '
                  f'<a href="{link("review/index.html")}">review record</a> for later status. '
                  'No human or outside-family model audit is recorded.</div>')
    actions = ""
    if download:
        actions = (f'<div class="actions"><a href="{link(download)}" download>Download Markdown</a>'
                   '<button type="button" onclick="window.print()">Print / save PDF</button></div>')
    contents = '<details><summary>Contents</summary>' + toc + "</details>" if len(source) > 5000 and "<li>" in toc else ""
    repo = (f'<a href="{html.escape(CONFIG["repository_url"])}">GitHub repository</a>'
            if CONFIG["repository_created"] else "Repository upload pending")
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="description" content="An AI proof record and reading guide for inclusion to sticky Brownian mass flow.">
<title>{html.escape(title)} · {html.escape(CONFIG["short_title"])}</title>
<link rel="stylesheet" href="{link("assets/style.css")}">
<script>
window.MathJax = {{tex: {{inlineMath: [['\\\\(', '\\\\)']], displayMath: [['\\\\[', '\\\\]']], tags: 'ams'}},
svg: {{fontCache: 'global'}}, options: {{skipHtmlTags: ['script','noscript','style','textarea','pre','code']}}}};
</script>
<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg-full.js"></script>
</head><body><a class="skip" href="#content">Skip to content</a><main>
<header><p class="eyebrow">AI proof record · Circle · Finite initial stacks</p>
<p class="site-title">{html.escape(CONFIG["title"])}</p>
<nav class="menu" aria-label="Main navigation">{nav}</nav><div class="rule"></div></header>
{notice}{actions}{contents}<article id="content">{body}</article>
<footer><a href="{link("review/index.html")}">Review status</a> ·
<a href="{link("provenance/index.html")}">Source record</a> · {repo}<br>
Proof record: 5 September 2026. Public export: 4 November 2026.</footer>
</main></body></html>
"""
    destination = DOCS / output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(page, encoding="utf-8")


def main():
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("")
    (DOCS / "assets").mkdir(exist_ok=True)
    shutil.copyfile(ROOT / "assets/style.css", DOCS / "assets/style.css")
    for name in ["overview", "digested", "raw", "review"]:
        output = "index.html" if name == "overview" else name + "/index.html"
        write_page(output, name.title(), (ROOT / f"content/{name}.md").read_text(), name.title())
    write_page("provenance/index.html", "Source record", (ROOT / "PROVENANCE.md").read_text(), provenance=True)
    records = sorted((ROOT / "records").rglob("*.md"))
    for path in records:
        rel = path.relative_to(ROOT).as_posix()
        download = "downloads/" + rel
        dest = DOCS / download
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(path, dest)
        text = path.read_text()
        title = text.splitlines()[0].lstrip("# ")
        write_page(rel[:-3] + ".html", title, text, "Raw", download, record=True)
    for slug, title, path in PROOFS:
        rel = "records/CANDIDATES/" + path
        write_page("raw/" + slug + "/index.html", title, (ROOT / rel).read_text(), "Raw",
                   "downloads/" + rel, record=True)
    index = "# Source records\n\nThe current proof versions are listed first.\nOlder versions are retained as history.\nDo not use an older proof in place of the current version.\n\n## Current proofs\n\n"
    for slug, title, path in PROOFS:
        index += f"- [{title}](../raw/{slug}/).\n"
    for category, label in [("", "Statement and protocol"), ("AUDITS", "Audit records"), ("CANDIDATES", "Proof families and version history")]:
        index += "\n## " + label + "\n\n"
        for path in records:
            rel = path.relative_to(ROOT / "records")
            if (category and rel.parts[0] == category) or (not category and len(rel.parts) == 1):
                index += f"- [{rel.as_posix()}]({rel.as_posix()}).\n"
    write_page("records/index.html", "Source records", index, "Raw")
    shutil.copyfile(ROOT / "records/manifest.json", DOCS / "downloads/manifest.json")
    # Store the bytes without compression to keep builds equal across zlib versions.
    with zipfile.ZipFile(DOCS / "downloads/proof-records.zip", "w", compression=zipfile.ZIP_STORED) as archive:
        for path in sorted(records + [ROOT / "records/manifest.json", ROOT / "PROVENANCE.md"]):
            info = zipfile.ZipInfo(path.relative_to(ROOT).as_posix(), (2026, 11, 4, 0, 0, 0))
            info.compress_type = zipfile.ZIP_STORED
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    print(f"Built {len(list(DOCS.rglob('*.html')))} pages and {len(records)} source downloads.")


if __name__ == "__main__":
    main()
