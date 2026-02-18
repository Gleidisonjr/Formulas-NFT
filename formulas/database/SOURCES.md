# Formula database — sources / Fontes do banco de fórmulas

This folder holds a **large database of formulas** (math, physics, statistics) for the NFT project—**1000+ formulas** from elementary to PhD level, including **famous equations that changed the world** (Ian Stewart's 17 + Einstein field equations, Dirac, Black-Scholes, Shannon entropy, etc.). Use `formulas.csv` for image generation; run `python scripts/merge_formula_csvs.py` to merge base + extended + famous + `formulas_bulk.csv` (bulk adds 630+ formulas to reach 1000+ total).

Sources used or recommended for collecting more formulas:

---

## Math

| Source | URL | Notes |
|--------|-----|--------|
| **formulaHub** | https://github.com/lordcode-dev/formulaHub | JSON with algebra, geometry, calculus, trigonometry. |
| **equajson** | https://github.com/nbeaver/equajson | Equations as JSON; search and lookup. |
| **Integral Cheat Sheet** | https://github.com/xiyuanyang-code/Integral-CheatSheet | Integral formulas. |
| **im2latex 230k** | https://zenodo.org/records/7738969 | Large LaTeX formula dataset (ML-oriented). |

---

## Physics

| Source | URL | Notes |
|--------|-----|--------|
| **PhysicsFormulae** | https://github.com/BenjaminTMilnes/PhysicsFormulae | Web formulary; formulas in repo. |
| **PhysicsFormulae (live)** | http://www.physicsformulae.com | Browse formulas online. |
| **Fundamental Physical Constants (CSV)** | https://github.com/joanh/Physical-Constants | CSV of constants. |
| **AP Physics C Tables** | College Board PDF | Standard equations list. |

---

## Statistics

| Source | URL | Notes |
|--------|-----|--------|
| **Stat Trek formulas** | https://stattrek.com/statistics/formulas | Descriptive, probability, inference. |
| **OpenStax Intro Statistics** | https://openstax.org/books/introductory-statistics/pages/10-formula-review | Formula review chapter. |
| **AP Statistics formula sheet** | apcentral.collegeboard.org | PDF formula tables. |
| **MathIsSimple statistics** | https://www.mathisimple.com/statistics/statistics-formulas | Reference list. |

---

## Famous formulas (formulas_famous_additions.csv)

Iconic equations added from “most important formulas of all time” and Ian Stewart’s *17 Equations That Changed the World* (and related lists). Includes:

- **Math:** Imaginary unit (i² = -1), Euler’s polyhedra (V − E + F = 2), Fourier transform/series, logistic map (chaos), Black–Scholes, Riemann zeta, Cauchy–Schwarz, Bessel equation, Legendre polynomials, quadratic reciprocity, prime number theorem, golden ratio.
- **Physics:** Wave equation, heat equation, Navier–Stokes, second law (ΔS ≥ 0), Schrödinger (time-dependent), Einstein field equations, Dirac equation, Euler–Lagrange, Hamilton’s equations, Boltzmann entropy, continuity equation, Maxwell–Ampère.
- **Statistics / information:** Shannon entropy.

Run `python scripts/merge_formula_csvs.py` to include these in `formulas.csv`, then `python scripts/csv_to_json.py` and `python scripts/batch_build.py` to generate images.

---

## CSV format (formulas.csv)

Columns: `name`, `formula`, `description`, `category`, `difficulty`, `subject`

- **formula**: use mathtext with `$...$` (e.g. `$E = mc^2$`). See `../schema.md`.
- **difficulty**: 1 (easiest) to 5 (hardest).
- **subject**: Math | Physics | Statistics

To use the CSV for image generation, run: `python scripts/csv_to_json.py` (exports to `formulas/data/` or merges).
