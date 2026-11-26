import sqlite3
from models import Track, Playlist
import json
from pathlib import Path


def get_connection(db_path: str = "music.db") -> (
        sqlite3.Connection):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn
ALLOWED_SORT_COLS = {"track_id", "title", "artist", "duration_sec", "rating"}
class Database_Music():
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        self.create_tables()
        self.migrate_playlists()
    def create_tables(self):
        DDL_Musics = """
            CREATE TABLE IF NOT EXISTS playlists (
            playlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT
        );
        """
        DDL_MUSIC_TRACK = """
            CREATE TABLE IF NOT EXISTS playlist_tracks (
            track_id INTEGER PRIMARY KEY AUTOINCREMENT,
            playlist_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            artist TEXT NOT NULL,
            duration_sec INTEGER CHECK (duration_sec > 0),
            rating INTEGER CHECK (rating BETWEEN 1 AND 5),
            FOREIGN KEY (playlist_id) REFERENCES playlists(playlist_id) ON DELETE CASCADE
            );
            """
        self.conn.execute(DDL_Musics)
        self.conn.execute(DDL_MUSIC_TRACK)

    def save_playlists(self, name: str, descrition: str, tracks: list[dict]) -> int:
        with self.conn:
            cur = self.conn.execute(
                "INSERT INTO playlists (name, description) VALUES (?, ?);",
          (name, descrition)
            )
            playlist_id: int = cur.lastrowid
            payload = [
                (playlist_id, track["title"], track["artist"], track["duration_seconds"], track["rating"])
                for track in tracks
            ]
            self.conn.executemany(
                """INSERT INTO playlist_tracks (playlist_id, title, artist, duration_sec, rating)
                VALUES (?, ?, ?, ?, ?);""",
                payload
            )
            return playlist_id

    def migrate_playlists(self) -> None:
        path = Path("src/data/playlists.json")
        count = self.conn.execute(
            "SELECT COUNT(*) FROM playlists;"
        ).fetchone()[0]
        print("Liczba playlist:", count)
        print("Czy JSON istnieje:", path.exists())
        if count == 0 and path.exists():
            with open(path, "r", encoding="utf-8") as file:
                playlists = json.load(file)
            tracks = []
            for item in playlists:
                track_data = {
                    "track_id": item["id"],
                    "title": item["title"],
                    "artist": item["author"],
                    "duration_seconds": item["duration"],
                    "rating": 5
                }
                if isinstance(track_data["duration_seconds"], str):
                    minutes, seconds = track_data["duration_seconds"].split(":")
                    track_data["duration_seconds"] = int(minutes) * 60 + int(seconds)

                tracks.append(Track.from_dict(track_data))

            playlist = Playlist(1, "Playlista", tracks)
            self.save_playlists(
                playlist.name,
                None,
                [track.to_dict() for track in playlist.tracks]
            )
            path.rename(path.with_suffix(".json.bak"))



    def search_tracks_safe(
            conn: sqlite3.Connection,
            phrase: str,
            sort_by: str = "track_id",
    ) -> list[sqlite3.Row]:
        if sort_by not in ALLOWED_SORT_COLS:
            raise ValueError(f"Niedozwolona kolumna sortowania: {sort_by}")
        sql = (
            "SELECT track_id, title, artist, duration_sec, rating "
            "FROM playlist_tracks "
            "WHERE title LIKE :pattern OR artist LIKE :pattern "
            f"ORDER BY {sort_by} ASC;"
        )
        params = {"pattern": f"%{phrase}%"}
        return conn.execute(sql, params).fetchall()