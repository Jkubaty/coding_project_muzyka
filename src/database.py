import sqlite3
from models import Track
import json
from pathlib import Path


def get_connection(db_path: str = "music.db") -> (
        sqlite3.Connection):
    conn = sqlite3.connect(db_path)
    conn.execute("PRAGMA foreign_keys = ON;")
    conn.row_factory = sqlite3.Row
    return conn

class Database_Music():
    def __init__(self):
        self.conn = get_connection()
        self.cursor = self.conn.cursor()
        self.create_tables()
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
                """INSERT INTO playlist_tracks (playlist_id, title, artist, duration_seconds, rating)
                VALUES (?, ?, ?, ?, ?);""",
                payload
            )
            return playlist_id

    def migrate_playlists(self) -> None:
        with open("src/data/playlst.json", "r", encoding="utf-8") as file:
            playlists = json.load(file)
        with self.conn:
            for playlist in playlists:
                self.conn.execute(
                    """INSERT INTO playlists (playlist_id, name) VALUES (?, ?);""",
                    (playlist["playlist_id"], playlist["name"])
                )
            for track in playlist["tracks"]:
                self.conn.execute(
                    """INSERT INTO playlist_tracks (playlist_id, track_id, title, artist, duration_seconds, rating)
                    VALUES (?, ?, ?, ?, ?, ?);""",
                    track["track_id"], track["playlist_id"], track["title"], track["artist"], track["duration_seconds"], track["rating"]

                )


conn = get_connection()
cursor = conn.execute("SELECT playlist_id, name, description FROM playlists WHERE playlist_id = 1;")
row: sqlite3.Row = cursor.fetchone()
print(row["name"], row["description"])
playlist = Track.from_dict(dict(row))





