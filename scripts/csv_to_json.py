"""
Convert formulas/database/formulas.csv to JSON files in formulas/data/
so you can use the full database for image generation.
Run: python scripts/csv_to_json.py

Options:
  --merge   Merge CSV formulas into existing math.json, physics.json, statistics.json (by subject)
  (default) Replace: write formulas_math.json, formulas_physics.json, formulas_statistics.json
"""

import csv
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CSV_PATH = os.path.join(ROOT, "formulas", "database", "formulas.csv")
DATA_DIR = os.path.join(ROOT, "formulas", "data")


def load_csv_formulas():
    formulas = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            name = (row.get("name") or "").strip()
            formula = (row.get("formula") or "").strip()
            description = (row.get("description") or "").strip()
            category = (row.get("category") or "General").strip()
            try:
                difficulty = int(row.get("difficulty", 1))
            except ValueError:
                difficulty = 1
            subject = (row.get("subject") or "Math").strip()
            if formula:
                formulas.append({
                    "name": name,
                    "formula": formula,
                    "description": description,
                    "category": category,
                    "difficulty": max(1, min(5, difficulty)),
                    "subject": subject,
                })
    return formulas


def main():
    if not os.path.isfile(CSV_PATH):
        print(f"CSV not found: {CSV_PATH}", file=sys.stderr)
        sys.exit(1)
    formulas = load_csv_formulas()
    if not formulas:
        print("No formulas in CSV.", file=sys.stderr)
        sys.exit(1)

    merge = "--merge" in sys.argv
    os.makedirs(DATA_DIR, exist_ok=True)

    by_subject = {"Math": [], "Physics": [], "Statistics": []}
    for f in formulas:
        sub = f.get("subject", "Math")
        if sub not in by_subject:
            by_subject[sub] = []
        by_subject[sub].append({k: v for k, v in f.items() if k != "subject"})

    if merge:
        for subject, filename in [("Math", "math.json"), ("Physics", "physics.json"), ("Statistics", "statistics.json")]:
            path = os.path.join(DATA_DIR, filename)
            existing = []
            if os.path.isfile(path):
                with open(path, "r", encoding="utf-8") as f:
                    existing = json.load(f)
            combined = existing + by_subject.get(subject, [])
            with open(path, "w", encoding="utf-8") as f:
                json.dump(combined, f, indent=2, ensure_ascii=False)
            print(f"  {filename}: {len(existing)} existing + {len(by_subject.get(subject, []))} from CSV = {len(combined)}")
    else:
        for subject, filename in [("Math", "formulas_math.json"), ("Physics", "formulas_physics.json"), ("Statistics", "formulas_statistics.json")]:
            data = by_subject.get(subject, [])
            path = os.path.join(DATA_DIR, filename)
            with open(path, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"  {filename}: {len(data)} formulas")
    print(f"\nDone. Total from CSV: {len(formulas)}")
    print("To use for images: copy/merge these JSON into math.json, physics.json, statistics.json, or run generate_images with updated load_all_formulas().")


if __name__ == "__main__":
    main()
