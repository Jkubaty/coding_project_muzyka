from typing import Any, Self
from abc import ABC, abstractmethod
import json
from pathlib import Path
from operator import itemgetter

class Track(ABC):
    def __init__(self, track_id, title, artist, duration_seconds, rating):
        self.track_id = track_id
        self.title = title
        self.artist = artist
        self.duration_seconds = duration_seconds
        self.rating = rating
    @abstractmethod
    def calculate_storage_mb(self) -> float:
        pass

class StudioTrack(Track):
    def __init__(self, track_id, title, artist, duration_seconds, rating, album, fileformat, bitrate):
        super().__init__(track_id, title, artist, duration_seconds, rating)
        self.album = album
        self.fileformat = fileformat
        self.bitrate = bitrate


class PodcastEpisode(Track):
    def __init__(self, track_id, title, artist, duration_seconds, rating, nrodcinka, goscie, transkrypcja):
        super().__init__(track_id, title, artist, duration_seconds, rating)
        self.nrodcinka = nrodcinka
        self.goscie = goscie
        self.transkrypcja = transkrypcja
    def calculate_storage_mb(self) -> float:
        return 0
    def __repr__(self):
        return (f"Track(track_id = {self.track_id}, "
                f"Title = {self.title}, "
                f"Artist = {self.artist}, "
                f"Duration_seconds = {self.duration_seconds}, "
                f"Rating = {self.rating}, "
                f"Nrodcinka = {self.nrodcinka}, "
                f"Goscie = {self.goscie}, "
                f"Transkrypcja = {self.transkrypcja})")
episode = PodcastEpisode(1, "podcast1","artysta1", 100,
                         10, 2, "gosc", "transkrypcja")
print(repr(episode))



ITEM_REGISTRY: dict[str, type[Track]] = {
    "StudioTrack": StudioTrack,
    "PodcastEpisode": PodcastEpisode,
    }
def deserialize_item(payload: dict[str, Any]) -> Track:
    item_type = payload.get("type")
    target_cls = ITEM_REGISTRY.get(item_type)
    if target_cls is None:
        raise ValueError(f"Nieznany dyskryminator typu w bazie: {item_type!r}")
    return target_cls.from_dict(payload)

BITRATES_KBPS = {"mp3_128": 128, "mp3_320": 320, "flac": 900}

SORT_KEYS = {
    "title": lambda t: t["title"].casefold(),
    "author": lambda t: t["author"].casefold(),
    "duration": itemgetter("duration"),
}

class PlaylistManager:
    def __init__(self, format_name="mp3_128", filepath="data/playlists_content.json"):
        self.format_name = format_name
        self.filepath = Path(filepath)
        self.playlists = {}


    def create(self, name):
        self.playlists.setdefault(name, [])


    def add_track(self, name, track):
        self.playlists[name].append(track)

    def sort(self, name, by="title", reverse=False):
        self.playlists[name].sort(key=SORT_KEYS[by], reverse=reverse)

    def estimate_size(self, name):
        kbps = BITRATES_KBPS[self.format_name]
        return sum(t["duration"] * kbps * 125 for t in self.playlists[name])