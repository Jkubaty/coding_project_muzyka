from database import Database_Music, get_connection
import sqlite3

db = Database_Music()

conn = db.conn
cursor = conn.execute("SELECT playlist_id, name, description FROM playlists WHERE playlist_id = 1;")
row: sqlite3.Row = cursor.fetchone()

if row is not None:
    print(row["name"], row["description"])

try:
    conn.execute(
        """INSERT INTO playlist_tracks
        (playlist_id, title, artist, duration_sec, rating)
        VALUES (?, ?, ?, ?, ?);""",
        (9999, "Test", "Test", 120, 5)
    )
    conn.commit()
except sqlite3.IntegrityError:
    print("Klucze obce działają")

playlist_id = db.save_playlists("Testowa playlista","Opis testowy",[
        {
            "title": "Testowy utwor",
            "artist": "Testowy wykonawca",
            "duration_seconds": 180,
            "rating": 5
        }
    ]
)
cursor = conn.execute(
    "SELECT * FROM playlists WHERE playlist_id = ?;",
    (playlist_id,)
)

row = cursor.fetchone()
print(row["name"])

cursor = conn.execute(
    "SELECT * FROM playlist_tracks WHERE playlist_id = ?;",
    (playlist_id,)
)

row = cursor.fetchone()
print(row["title"], row["artist"])

conn.execute(
    "DELETE FROM playlists WHERE playlist_id = ?;",
    (playlist_id,)
)

count = conn.execute(
    "SELECT COUNT(*) FROM playlist_tracks WHERE playlist_id = ?;",
    (playlist_id,)
).fetchone()[0]

print(count)

cursor = conn.execute(
    "SELECT COUNT(*) FROM playlist_tracks;"
)

count = cursor.fetchone()[0]

print("Liczba utworów w bazie:", count)