import csv
import json
from pathlib import Path

fields = ["id", "title", "duration", "author"]

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(parents=True, exist_ok=True)

FILE_PATH = DATA_DIR / "test.txt"

with open(FILE_PATH, mode="w", encoding="utf-8") as f:
    f.write("Inżynieria Oprogramowania PK\n")

def export_to_csv(path: Path, data: list[dict], fields: list[str]) -> None:

    with open(path, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(data)

def import_from_csv(path: Path) -> list[dict]:

    with open(path, mode="r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def save_catalog(path: Path, items: list[dict]) -> None:

    with open(path, mode="w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)

def load_catalog(path: Path) -> list[dict]:

    with open(path, mode="r", encoding="utf-8") as f:
        return json.load(f)


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


def get_menu_file() -> Path:
    data_dir = Path(__file__).resolve().parent.parent / "data"
    data_dir.mkdir(parents=True, exist_ok=True)
    return data_dir / "menu.json"

def save_menu(items: list[dict]) -> None:
    with open(get_menu_file(), mode="w", encoding="utf-8") as f:
        json.dump(items, f, indent=4, ensure_ascii=False)