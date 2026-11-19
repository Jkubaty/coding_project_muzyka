import sqlite3
from models import Track

class Database_Music():
    def __init__(self):
        self.conn = sqlite3.connect('music.db')
        self.cursor = self.conn.cursor()

def get_connection(db_path: str = "music.db") -> (
        sqlite3.Connection):

        conn = sqlite3.connect(db_path)
        conn.execute("PRAGMA foreign_keys = ON;")
        conn.row_factory = sqlite3.Row
        return conn

conn = get_connection()
cursor = conn.execute("SELECT playlist_id, name, description FROM playlists WHERE playlist_id = 1;")
row: sqlite3.Row = cursor.fetchone()

print(row["name"], row["description"])

playlist = Track.from_dict(dict(row))

DDL_Musics = """
CREATE TABLE IF NOT EXISTS playlists (
    playlist_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
);
"""


conn.execute(DDL_Musics)