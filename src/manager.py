from abc import ABC, abstractmethod
from typing import Any

class Track(ABC):

    def __init__(self, track_id: int,title: str, artist: str, duration: float) -> None:
        self.track_id: int = track_id
        self.title: str = title
        self.artist: str = artist
        self.duration: float = duration
    @abstractmethod
    def calculate_storage_mb(self) -> float:
        pass
    def to_dict(self) -> dict[str, Any]:
        return {
            "track_id": self.track_id,
            "title": self.title,
            "artist": self.artist,
            "duration": self.duration,
        }