"""Select mathematical source records for the reading site."""
from pathlib import Path


def is_public_record(path):
    parts = Path(path).parts
    return parts[0] == "CANDIDATES" or parts == ("STATEMENT.md",) or parts == ("RAW_PROOF_v3.md",)
