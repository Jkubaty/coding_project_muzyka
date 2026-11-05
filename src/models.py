from typing import Any, Self
class Track:
    def __init__(self, track_id, title, artist, duration_seconds, rating):
        self.track_id = track_id
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds
        self.rating = rating

    def __repr__(self):
        return f"MenuItem(track_id={self.track_id}, title={self.title!r}, artist={self.artist}, duration_seconds={self.duration_seconds}, rating={self.rating})"

    def __str__(self):
        return f"[{self.track_id} {self.title} {self.artist:}"

    @property
    def duration_seconds(self) -> int:
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, czas: int) -> None:
        if not isinstance(czas, int):
            raise TypeError("Czas musi być nie przecinkowy.")
        if czas <= 0:
            raise ValueError(f"Czas musi być większa od zera (podano: {int}).")
        self._duration_seconds = czas

class Playlist:

    def __init__(self, playlist_id: int, name: str,
                 tracks: list[Track] | None = None) -> None:
        self.playlist_id = playlist_id
        self.name = name
        self.tracks: list[Track] = tracks if tracks is not None else []

    def to_dict(self) -> dict[str, Any]:
        return {
            "playlist_id": self.playlist_id,
            "name": self.name,
            "tracks": [track.to_dict() for track in self.tracks],
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Self:
        restored_tracks = [Track.from_dict(raw) for raw in data.get("tracks", [])]
        return cls(int(data["playlist_id"]), data["name"], restored_tracks)