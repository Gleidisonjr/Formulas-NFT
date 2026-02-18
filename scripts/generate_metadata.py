"""
Generate OpenSea-compliant metadata JSON for each token.
Output: build/metadata/{token_id}.json
Uses config.json for collection name, description, and base URLs.
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT, "config.json")
FORMULAS_DATA_DIR = os.path.join(ROOT, "formulas", "data")
BUILD_METADATA_DIR = os.path.join(ROOT, "build", "metadata")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_all_formulas():
    formulas = []
    pairs = (
        ("formulas_math.json", "math.json"),
        ("formulas_physics.json", "physics.json"),
        ("formulas_statistics.json", "statistics.json"),
    )
    for primary, fallback in pairs:
        for name in (primary, fallback):
            path = os.path.join(FORMULAS_DATA_DIR, name)
            if os.path.isfile(path):
                with open(path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                formulas.extend(data)
                break
    return formulas


def build_opensea_metadata(token_id: int, item: dict, config: dict) -> dict:
    """Build one token's metadata following OpenSea/ERC-721 standard."""
    image_base = (config.get("image_base_url") or "").rstrip("/")
    meta_base = (config.get("metadata_base_url") or "").rstrip("/")
    external_url = (config.get("external_url") or "").rstrip("/")

    image_url = f"{image_base}/{token_id}.png" if image_base else f"{token_id}.png"
    # Optional: point external_url to the token (if your site supports it)
    ext = f"{external_url}/{token_id}" if external_url else ""

    return {
        "name": item.get("name", f"Formula #{token_id}"),
        "description": item.get("description", ""),
        "image": image_url,
        "external_url": ext or None,
        "background_color": (config.get("image", {}).get("background_color") or "ffffff").replace("#", ""),
        "attributes": [
            {"trait_type": "Category", "value": item.get("category", "Math")},
            {"trait_type": "Difficulty", "value": int(item.get("difficulty", 1))},
            {"trait_type": "Subject", "value": _subject_from_category(item.get("category", ""))},
        ],
    }


def _subject_from_category(category: str) -> str:
    """Map category to broader subject (Math, Physics, Statistics)."""
    cat = (category or "").lower()
    if any(x in cat for x in ("algebra", "calculus", "geometry", "number")):
        return "Math"
    if any(x in cat for x in ("mechanics", "thermo", "electro", "quantum", "relativity")):
        return "Physics"
    if any(x in cat for x in ("descriptive", "probability", "regression", "inference")):
        return "Statistics"
    return "Math"


def main():
    os.makedirs(BUILD_METADATA_DIR, exist_ok=True)
    config = load_config()
    formulas = load_all_formulas()
    if not formulas:
        print("No formulas found in formulas/data/*.json", file=sys.stderr)
        sys.exit(1)

    for i, item in enumerate(formulas, start=1):
        meta = build_opensea_metadata(i, item, config)
        # Remove keys with None/empty for cleaner JSON
        meta = {k: v for k, v in meta.items() if v is not None and v != ""}
        out_path = os.path.join(BUILD_METADATA_DIR, f"{i}.json")
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2, ensure_ascii=False)
        print(f"  {i}.json  <- {item.get('name', '?')}")

    print(f"\nDone. {len(formulas)} metadata files in {BUILD_METADATA_DIR}")


if __name__ == "__main__":
    main()
