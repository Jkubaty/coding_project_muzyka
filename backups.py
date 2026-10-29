import shutil
from datetime import datetime
from pathlib import Path


def createbackup(source_file: Path, backup_dir: Path, max_backups: int = 3) -> Path | None:
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

