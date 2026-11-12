from models import Playlist, Track

track1 = Track(1, "Piosenka 1", "Wykonawca 1", 230, "10")
track2 = Track(2, "Piosenka 2", "Wykonawca 2", 100, "9")

playlist = Playlist(1, "Dowolne", [track1, track2])


assert playlist.name == "Dowolne"
assert playlist.tracks == [track1, track2]
assert len(playlist.tracks) == 2


try:
    assert track1.duration_seconds == 10
except ValueError:
    print("Oczekiwany blad")



tracks = [track1, track2]
tracks.sort()
assert tracks == [track1, track2]


original = Playlist(1, "Dowolne", [track1, track2])
data = original.to_dict()
odtworzony = Playlist.from_dict(data)

assert original == odtworzony
