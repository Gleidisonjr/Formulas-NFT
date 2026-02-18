# Formula data schema

Each formula file in `formulas/data/*.json` is a JSON array of objects with:

| Field         | Type   | Required | Description |
|---------------|--------|----------|-------------|
| `name`        | string | Yes      | Short title (e.g. "Quadratic formula") |
| `formula`     | string | Yes      | Math expression in mathtext: use `$...$` (e.g. `$E = mc^2$`). Supports fractions `\frac{a}{b}`, sums `\sum`, integrals `\int`, Greek `\alpha`, `\beta`, etc. |
| `description` | string | Yes      | One or two sentences for the NFT description |
| `category`    | string | Yes      | Subject area, e.g. "Algebra", "Calculus", "Mechanics" |
| `difficulty`  | number | Yes      | 1 (easiest) to 5 (hardest) — used as OpenSea attribute |

Example:

```json
{
  "name": "Euler's identity",
  "formula": "$e^{i\\pi} + 1 = 0$",
  "description": "Euler's identity links five fundamental constants: e, i, pi, 1, and 0.",
  "category": "Calculus",
  "difficulty": 4
}
```

Mathtext reference: https://matplotlib.org/stable/users/explain/text/mathtext.html
