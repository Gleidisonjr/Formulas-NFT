"""
Full pipeline: generate all formula images, then all metadata.
Run from project root:  python scripts/batch_build.py
"""

import os
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(ROOT, "scripts")


def run(script_name: str) -> bool:
    path = os.path.join(SCRIPTS_DIR, script_name)
    r = subprocess.run([sys.executable, path], cwd=ROOT)
    return r.returncode == 0


def main():
    print("Math Formula NFT — batch build\n")
    print("1. Generating images...")
    if not run("generate_images.py"):
        sys.exit(1)
    print("\n2. Generating metadata...")
    if not run("generate_metadata.py"):
        sys.exit(1)
    print("\nAll done. Check build/images/ and build/metadata/.")
    print("Next: see docs/DEPLOY_OPENSEA.md to publish on OpenSea.")


if __name__ == "__main__":
    main()
