"""Build the reading site. Keep the source records unchanged."""
import html
import hashlib
import json
import os
import re
import shutil
import zipfile
from pathlib import Path

import markdown
from assemble_raw import assemble

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CONFIG = json.loads((ROOT / "site.json").read_text())
STYLE_VERSION = hashlib.sha256((ROOT / "assets/style.css").read_bytes()).hexdigest()[:12]
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
    # The reference uses h2 for the site title and h3 for section headings.
    body = re.sub(r"<(/?)h([1-6])\b", lambda m: "<" + m[1] + "h" + str(min(6, max(3, int(m[2]) + 1))), body)
    return body, toc


def write_page(output, title, source, active="", download=None, record=False, provenance=False, literal_text=False):
    body, toc = render(source, output, provenance, literal_html=(record or literal_text))
    link = lambda p: relative(p, output)
    nav = '<span class="sep">·</span>'.join(
        '<a href="{}"{}>{}</a>'.format(link(path), ' class="current" aria-current="page"' if active == name else "", name)
        for name, path in [("Overview", "index.html"), ("Digested", "digested/index.html"), ("Raw", "raw/index.html")]
    )
    notice = ""
    if record:
        notice = ('<p class="ai-note"><strong>Fixed source record.</strong> '
                  'Creation-time labels remain unchanged. See the '
                  f'<a href="{link("review/index.html")}">review record</a> for later status. '
                  'No human or outside-family model audit is recorded.</p>')
    actions = ""
    if download:
        actions = (f'<hr><p><a href="{link(download)}" download>Markdown</a> · '
                   '<a href="#" onclick="window.print(); return false">Print / save PDF</a></p>')
    contents = '<details><summary>Contents</summary>' + toc + "</details>" if len(source) > 5000 and "<li>" in toc and output != "raw/index.html" else ""
    if output == "raw/index.html":
        body = re.sub(
            r'(<p><strong>Theorem 1 \(full mass path convergence\)\.</strong>.*?)(?=<p>The limit)',
            r'<div class="theorem thm thm-plain" id="theorem-1">\1</div>\n',
            body, flags=re.S,
        )
    page = (ROOT / "build/template.html").read_text()
    replacements = {
        "@@STYLESHEET@@": link("assets/style.css") + "?v=" + STYLE_VERSION,
        "@@TITLE@@": html.escape(title + " · " + CONFIG["short_title"]),
        "@@HEADING@@": html.escape(CONFIG["title"]),
        "@@MENU@@": nav,
        "@@CONTENT@@": notice + contents + body + actions,
    }
    for key, value in replacements.items():
        page = page.replace(key, value)
    destination = DOCS / output
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(page, encoding="utf-8")


def main():
    assemble()
    DOCS.mkdir(exist_ok=True)
    (DOCS / ".nojekyll").write_text("")
    (DOCS / "assets").mkdir(exist_ok=True)
    shutil.copyfile(ROOT / "assets/style.css", DOCS / "assets/style.css")
    for name in ["overview", "digested", "raw", "review"]:
        output = "index.html" if name == "overview" else name + "/index.html"
        write_page(output, name.title(), (ROOT / f"content/{name}.md").read_text(), name.title(), literal_text=(name == "raw"))
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
