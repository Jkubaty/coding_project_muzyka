import csv
import json
from pathlib import Path

fields = ["id", "title", "duration", "author"]

def export_to_csv(path: Path, data: list[dict], fields: list[str]) -> None:
    """Eksportuje listę słowników do pliku CSV z nagłówkiem."""
    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)

def import_from_csv(path: Path) -> list[dict]:
    """Wczytuje rekordy CSV jako słowniki (wszystkie pola to napisy!)."""
    with open(path, mode="r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))

def safe_load_catalog(path: Path, seed_data: list[dict]) -> list[dict]:
    try:
        with open(path, mode="r", newline="", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        with open(path, mode="w", newline="", encoding="utf-8") as f:
            json.dump(seed_data, f, indent=4, ensure_ascii=False)
        return [dict(item) for item in seed_data]
    except json.JSONDecodeError:
        print(f"UWAGA Baza {path.name} jest uszkodzona. Aktywowano dane awaryjne.")
        return [dict(item) for item in seed_data]
