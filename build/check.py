"""Check the public export and all local site links."""
import hashlib
import json
import re
import zipfile
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"


class Page(HTMLParser):
    def __init__(self, text):
        super().__init__()
        self.links = []
        self.ids = set()
        self.feed(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.add(attrs["id"])
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])


def main():
    count = 0
    manifest = json.loads((ROOT / "records/manifest.json").read_text())
    for entry in manifest["files"]:
        path = ROOT / entry["path"]
        content = path.read_bytes()
        assert hashlib.sha256(content).hexdigest() == entry["public_sha256"], path
        assert (DOCS / "downloads" / entry["path"]).read_bytes() == content, path
        if "/PROOF_" in entry["path"] or "/CONTRACT_" in entry["path"] or "/BRIEF_" in entry["path"] or entry["path"] == "records/STATEMENT.md":
            assert entry["source_sha256"] == entry["public_sha256"], path
    pages = {p.resolve(): Page(p.read_text()) for p in DOCS.rglob("*.html")}
    historical = (DOCS / "records/AUDITS/C0008_RECONSTRUCTION_v1.html").read_text()
    assert 'id="primary-references-consulted"' in historical, "The historical record was truncated."
    assert "For (0&lt;" in historical, "A source inequality was not escaped."
    for path, page in pages.items():
        text = path.read_text()
        assert "MATHPLACEHOLDER" not in text, path
        assert "/Users/" not in text and "file://" not in text, path
        for href in page.links:
            parsed = urlsplit(href)
            if parsed.scheme or parsed.netloc:
                continue
            target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
            if target.is_dir():
                target = target / "index.html"
            assert target.is_relative_to(DOCS.resolve()), (path, href)
            assert target.is_file(), (path, href)
            if parsed.fragment and target in pages:
                assert unquote(parsed.fragment) in pages[target].ids, (path, href)
            count += 1
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or path.suffix in {".zip", ".pyc"}:
            continue
        if path.suffix in {".md", ".html", ".json", ".yml", ".css"}:
            text = path.read_text()
            assert not re.search(r"/Users/|gh[pousr]_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}", text), path
    with zipfile.ZipFile(DOCS / "downloads/proof-records.zip") as archive:
        for name in archive.namelist():
            assert archive.read(name) == (ROOT / name).read_bytes(), name
    print(f"Passed: {len(manifest['files'])} record hashes, {len(pages)} pages, {count} local links, and ZIP contents.")


if __name__ == "__main__":
    main()
