from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def discover_scripts() -> list[Path]:
    scripts: list[Path] = []
    for base in [ROOT / "app" / "agents", ROOT / "tests"]:
        if base.exists():
            scripts.extend(sorted(base.rglob("check_*.py")))
    return scripts


def main() -> None:
    scripts = discover_scripts()
    if not scripts:
        print("No check scripts found.")
        sys.exit(1)

    env = os.environ.copy()
    env.setdefault("LLM_MODE", "mock")
    failed: list[str] = []

    for script in scripts:
        rel = script.relative_to(ROOT)
        module = ".".join(rel.with_suffix("").parts)
        print(f"\n--- {rel} ---")
        result = subprocess.run([sys.executable, "-m", module], cwd=ROOT, env=env)
        if result.returncode != 0:
            failed.append(str(rel))

    if failed:
        print("\nFailed:")
        for path in failed:
            print(f"  - {path}")
        sys.exit(1)
    print("\nAll check scripts passed.")


if __name__ == "__main__":
    main()
