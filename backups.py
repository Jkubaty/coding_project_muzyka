import shutil
from datetime import datetime
from pathlib import Path


def get_data_dir() -> Path:
    return Path(__file__).resolve().parent / "data"


def create_backup(source_file: Path, backup_dir: Path, max_backups: int = 3) -> Path | None:
    if not source_file.exists():
        return None

    backup_dir.mkdir(parents=True, exist_ok=True)
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = backup_dir / f"{source_file.stem}_{stamp}.bak"
    shutil.copy2(source_file, backup_path)

    existing = sorted(backup_dir.glob(f"{source_file.stem}_*.bak"))
    while len(existing) > max_backups:
        oldest = existing.pop(0)
        oldest.unlink(missing_ok=True)

    return backup_path


def backup_menu(keep: int = 3) -> Path | None:
    return create_backup(get_data_dir() / "playlists.json", get_data_dir() / "backups", keep)


def backup_playlists(names: list, keep: int = 3) -> None:
    backup_dir = get_data_dir() / "backups"
    create_backup(get_data_dir() / "playlist_names.json", backup_dir, keep)
    for name in names:
        create_backup(get_data_dir() / f"{name}.json", backup_dir, keep)