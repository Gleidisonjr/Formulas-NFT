"""
Merge formulas.csv, formulas_extended.csv, formulas_famous_additions.csv, and formulas_bulk.csv into a single formulas.csv.
Run from project root: python scripts/merge_formula_csvs.py
"""

import csv
import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(ROOT, "formulas", "database")
MAIN_CSV = os.path.join(DB_DIR, "formulas.csv")
EXTENDED_CSV = os.path.join(DB_DIR, "formulas_extended.csv")
FAMOUS_CSV = os.path.join(DB_DIR, "formulas_famous_additions.csv")
BULK_CSV = os.path.join(DB_DIR, "formulas_bulk.csv")
OUT_CSV = os.path.join(DB_DIR, "formulas.csv")


def read_rows(path):
    with open(path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return list(reader)


def main():
    # Start from base formulas (if you have a formulas_base.csv use it; else use current formulas.csv and skip extended to avoid dupes)
    # We merge: formulas.csv (current content) + formulas_extended.csv + formulas_famous_additions.csv
    # To avoid duplicating extended when formulas.csv was already merged: only add files that are "additions"
    rows = []
    if os.path.isfile(MAIN_CSV):
        rows = read_rows(MAIN_CSV)
    seen_names = {r.get("name", "").strip().lower() for r in rows if r.get("name")}
    added = 0
    if os.path.isfile(EXTENDED_CSV):
        extra = read_rows(EXTENDED_CSV)
        for r in extra:
            if r.get("name", "").strip().lower() not in seen_names:
                rows.append(r)
                seen_names.add(r.get("name", "").strip().lower())
                added += 1
    if os.path.isfile(FAMOUS_CSV):
        famous = read_rows(FAMOUS_CSV)
        for r in famous:
            if r.get("name", "").strip().lower() not in seen_names:
                rows.append(r)
                seen_names.add(r.get("name", "").strip().lower())
                added += 1
    if os.path.isfile(BULK_CSV):
        bulk = read_rows(BULK_CSV)
        for r in bulk:
            n = r.get("name", "").strip().lower()
            if n and n not in seen_names:
                rows.append(r)
                seen_names.add(n)
                added += 1
    fieldnames = ["name", "formula", "description", "category", "difficulty", "subject"]
    with open(OUT_CSV, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        w.writerows(rows)
    print(f"Merged {len(rows)} formulas into {OUT_CSV}" + (f" (+{added} new from extended/famous)" if added else ""))


if __name__ == "__main__":
    main()
