"""Assemble the exact statement and full proof for the Raw page."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PARTS = ROOT / "content/raw-parts"


def assemble():
    statement = (PARTS / "statement.md").read_text()
    main = (PARTS / "main-proof.md").read_text()
    argument, references = main.split("## 6. References and standard results", 1)
    sections = [statement, argument]
    sections.extend((PARTS / name).read_text() for name in
                    ("correctors.md", "occupation.md", "path-transfer.md"))
    sections.append("## References and standard results\n" + references)
    sections.append(
        "## Source versions\n\n"
        "This editorial version is a **candidate**. "
        "It presents the recorded proof and its three supporting results in one document. "
        "It has not undergone a separate mathematical audit. "
        "The [source map](https://github.com/inclusion-to-sticky-flow/"
        "inclusion-to-sticky-flow.github.io/blob/main/content/raw-parts/SOURCE_MAP.md) "
        "identifies the fixed source versions.\n"
    )
    (ROOT / "content/raw.md").write_text("\n\n".join(s.strip() for s in sections) + "\n")


if __name__ == "__main__":
    assemble()
