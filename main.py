"""Copy entry.txt beside this script to $MAKEFUN_OUTPUT_DIR/entry.txt.

Single direct write, no temp file or rename, mode 0644, so the grader
can always read the output.
"""

import os
from pathlib import Path

try:
    src = Path(__file__).resolve().parent / "entry.txt"
    data = src.read_bytes()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.txt"
    out.write_bytes(data)
    os.chmod(out, 0o644)
except OSError as exc:
    raise SystemExit(f"failed to write entry: {exc}") from exc
