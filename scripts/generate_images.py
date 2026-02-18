"""
Generate formula images for NFT assets.
White background, mathtext rendering (no LaTeX install required).
Output: build/images/{token_id}.png
"""

import json
import os
import sys

# Use non-interactive backend so no display is needed (e.g. on servers)
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Project root = parent of 'scripts'
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONFIG_PATH = os.path.join(ROOT, "config.json")
FORMULAS_DATA_DIR = os.path.join(ROOT, "formulas", "data")
BUILD_IMAGES_DIR = os.path.join(ROOT, "build", "images")


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def load_all_formulas():
    formulas = []
    # Per subject: use formulas_*.json from database export if present, else math.json / physics.json / statistics.json
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


def ensure_formula_math_mode(formula: str) -> str:
    """Ensure formula is in math mode for matplotlib (e.g. $ ... $)."""
    s = formula.strip()
    if not s.startswith("$"):
        s = "$" + s
    if not s.endswith("$"):
        s = s + "$"
    return s


def render_formula_to_file(
    formula_text: str,
    output_path: str,
    width_px: int,
    height_px: int,
    dpi: int,
    bg_hex: str,
    formula_name: str = "",
):
    """Render a single formula to a PNG file: name on top, formula below. White (or custom) background."""
    formula_text = ensure_formula_math_mode(formula_text)
    width_in = width_px / dpi
    height_in = height_px / dpi

    fig, ax = plt.subplots(figsize=(width_in, height_in), facecolor=f"#{bg_hex}")
    ax.set_facecolor(f"#{bg_hex}")
    ax.axis("off")
    # Font sizes: name smaller than formula, both scale with canvas
    fontsize_formula = max(24, min(120, width_px // 25))
    fontsize_name = max(14, min(48, width_px // 50))

    if formula_name:
        # Name/title at top (y=0.72), formula centered below (y=0.5)
        ax.text(0.5, 0.72, formula_name, fontsize=fontsize_name, ha="center", va="center", transform=ax.transAxes)
    ax.text(0.5, 0.5, formula_text, fontsize=fontsize_formula, ha="center", va="center", transform=ax.transAxes)
    plt.tight_layout(pad=0)
    fig.savefig(
        output_path,
        dpi=dpi,
        facecolor=fig.get_facecolor(),
        edgecolor="none",
        bbox_inches="tight",
        pad_inches=0.2,
    )
    plt.close(fig)


def main():
    os.makedirs(BUILD_IMAGES_DIR, exist_ok=True)
    config = load_config()
    img_cfg = config.get("image", {})
    width = int(img_cfg.get("width", 3000))
    height = int(img_cfg.get("height", 3000))
    dpi = int(img_cfg.get("dpi", 150))
    bg = (img_cfg.get("background_color") or "ffffff").replace("#", "")

    formulas = load_all_formulas()
    if not formulas:
        print("No formulas found in formulas/data/*.json", file=sys.stderr)
        sys.exit(1)

    for i, item in enumerate(formulas, start=1):
        formula = item.get("formula", "")
        if not formula:
            continue
        name = item.get("name", "")
        out_path = os.path.join(BUILD_IMAGES_DIR, f"{i}.png")
        try:
            render_formula_to_file(formula, out_path, width, height, dpi, bg, formula_name=name)
            print(f"  {i}.png  <- {name or '?'}")
        except Exception as e:
            print(f"  ERROR {i}: {item.get('name', '?')} -> {e}", file=sys.stderr)

    print(f"\nDone. {len(formulas)} images in {BUILD_IMAGES_DIR}")


if __name__ == "__main__":
    main()
