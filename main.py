import os
from pathlib import Path

ENTRY = "Four stars. Landed expecting an empire; found eight billion creatures who will not say one word to each other until a plate of small fried things arrives. Would orbit again."

output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
output_dir.mkdir(parents=True, exist_ok=True)
(output_dir / "entry.txt").write_bytes(ENTRY.encode("utf-8"))
