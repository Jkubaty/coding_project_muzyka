import json
from pathlib import Path
from operator import itemgetter
from storage import save_catalog

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