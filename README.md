# Math Formula NFT

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![OpenSea](https://img.shields.io/badge/OpenSea-ready-green.svg)](https://opensea.io/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**NFT collection of 1000+ mathematical formulas** (Mathematics, Physics, Statistics) — from elementary to PhD level. Each NFT is a clean formula image (name + equation on white background), with OpenSea-ready metadata. Generate images in batch and publish on OpenSea or any ERC-721 marketplace.

**Documentação em português:** [README_PT.md](README_PT.md) · [Passo a passo OpenSea (PT)](docs/DEPLOY_OPENSEA_PT.md) · [Configuração (PT)](docs/CONFIG_PT.md)

---

## About this project (Portfolio)

This repository is a **full pipeline** for creating and publishing formula NFTs:

- **Database:** 1000+ formulas in CSV (math, physics, statistics), with sources and merge scripts.
- **Image generation:** Python + matplotlib — no LaTeX required; formula name on top, equation below, white background, 3000×3000 px (OpenSea recommended).
- **Metadata:** OpenSea/ERC-721 compliant JSON (name, description, image, attributes: Category, Difficulty, Subject).
- **Deployment:** Step-by-step guides for OpenSea Studio (no-code) or custom contract + IPFS.

Suitable as a **portfolio project** for NFT tooling, Python automation, and structured data pipelines.

---

## What this project does

1. **Generates formula images** — Name on top, formula below; white background; matplotlib mathtext (no LaTeX by default).
2. **Builds OpenSea metadata** — Per-token JSON with name, description, image URL, attributes.
3. **Formula database** — 1000+ formulas in `formulas/database/formulas.csv`; merge scripts for extended and bulk data; see `formulas/database/SOURCES.md`.
4. **Batch pipeline** — One command to export CSV → JSON and generate all images + metadata.
5. **Publish on OpenSea** — Use [OpenSea Studio](https://opensea.io/studio) or your own contract + IPFS; see [docs/DEPLOY_OPENSEA.md](docs/DEPLOY_OPENSEA.md).

---

## Project structure

```
Math NFT/
├── README.md
├── README_PT.md
├── LICENSE
├── requirements.txt
├── config.json
├── formulas/
│   ├── data/                    # JSON for image gen (from csv_to_json)
│   │   ├── formulas_math.json
│   │   ├── formulas_physics.json
│   │   └── formulas_statistics.json
│   ├── database/
│   │   ├── formulas.csv         # Main DB (1000+ formulas)
│   │   ├── formulas_extended.csv
│   │   ├── formulas_famous_additions.csv
│   │   ├── formulas_bulk.csv
│   │   └── SOURCES.md
│   └── schema.md
├── scripts/
│   ├── generate_images.py
│   ├── generate_metadata.py
│   ├── batch_build.py
│   ├── csv_to_json.py
│   ├── merge_formula_csvs.py
│   └── generate_bulk_formulas.py
├── build/                       # Generated (gitignored)
│   ├── images/
│   └── metadata/
└── docs/
    ├── DEPLOY_OPENSEA.md
    ├── DEPLOY_OPENSEA_PT.md
    └── CONFIG_PT.md
```

---

## Quick start

### 1. Setup

```bash
git clone <your-repo-url>
cd "Math NFT"
python -m venv venv
# Windows:
venv\Scripts\activate
# Mac/Linux:
# source venv/bin/activate
pip install -r requirements.txt
```

### 2. Generate images and metadata

```bash
python scripts/csv_to_json.py
python scripts/batch_build.py
```

Output: `build/images/` (PNGs) and `build/metadata/` (JSON). Use these to mint on OpenSea or upload to IPFS and point your contract’s `tokenURI` at the metadata base URL.

### 3. Publish on OpenSea

- **No-code:** [OpenSea Studio](https://opensea.io/studio) → create collection → upload images and copy name/description from `build/metadata/*.json`.
- **With contract + IPFS:** Upload `build/images` and `build/metadata` to IPFS (e.g. [Pinata](https://pinata.cloud)), set `image_base_url` and `metadata_base_url` in `config.json`, re-run `generate_metadata.py`, then deploy ERC-721 and mint.

Full steps: **[docs/DEPLOY_OPENSEA.md](docs/DEPLOY_OPENSEA.md)** (EN) and **[docs/DEPLOY_OPENSEA_PT.md](docs/DEPLOY_OPENSEA_PT.md)** (PT).

### 4. Publish on GitHub (portfolio)

To push this project to GitHub as a public repo: see **[docs/PUBLISH_GITHUB.md](docs/PUBLISH_GITHUB.md)** for init, remote, first commit, and push. The repo excludes `build/` and `venv/` via `.gitignore`.

---

## Adding more formulas

- **From CSV:** Edit `formulas/database/formulas_extended.csv` or `formulas_bulk.csv`, then run `python scripts/merge_formula_csvs.py` to update `formulas.csv`.
- **Schema:** Each row: `name`, `formula` (mathtext in `$...$`), `description`, `category`, `difficulty` (1–5), `subject` (Math | Physics | Statistics). See **formulas/schema.md**.

Then run `csv_to_json.py` and `batch_build.py` again.

---

## Configuration

`config.json` controls collection name, description, image size (default 3000×3000), and base URLs for metadata/images after you host on IPFS. See **[docs/CONFIG_PT.md](docs/CONFIG_PT.md)** for a field-by-field description (PT).

---

## Tech stack

- **Python 3.8+**
- **matplotlib** — formula rendering (mathtext)
- **Pillow** — optional image handling
- Output: PNG (3000×3000), JSON (OpenSea metadata standard)

---

## Checklist: OpenSea + GitHub

- [ ] **Images & metadata:** Run `python scripts/csv_to_json.py` and `python scripts/batch_build.py` (output in `build/`).
- [ ] **OpenSea:** Follow [docs/DEPLOY_OPENSEA.md](docs/DEPLOY_OPENSEA.md) — create collection in Studio or upload to IPFS and use ERC-721 contract.
- [ ] **GitHub:** Follow [docs/PUBLISH_GITHUB.md](docs/PUBLISH_GITHUB.md) — `git add .`, `git commit`, `git remote add origin <url>`, `git push -u origin main`. Set description and topics in the repo About.

---

## License

MIT. See [LICENSE](LICENSE). When publishing on OpenSea, use only content you have rights to (e.g. standard textbook formulas; attribute sources when relevant).
