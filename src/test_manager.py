import unittest
from manager import (
    Track,
    PodcastEpisode,
    deserialize_item,
    PlaylistManager
)

class TestManager(unittest.TestCase):

    def test_track_abstract(self):
        with self.assertRaises(TypeError):
            Track(1, "Tytul", "Artysta", 100, 10)

    def test_podcast_episode(self):
        episode = PodcastEpisode(
            1, "Podcast", "Artysta", 100, 10,
            2, "Gosc", "Transkrypcja"
        )

        self.assertEqual(episode.title, "Podcast")
        self.assertEqual(episode.calculate_storage_mb(), 0)

    def test_deserialize_unknown_type(self):
        with self.assertRaises(ValueError):
            deserialize_item({"type": "Nieznany"})

    def test_create_playlist(self):
        manager = PlaylistManager()
        manager.create("Rock")

        self.assertEqual(manager.playlists["Rock"], [])

    def test_add_track(self):
        manager = PlaylistManager()
        manager.create("Rock")

        track = {
            "title": "Tytul1",
            "author": "Autor1",
            "duration": 200
        }

        manager.add_track("Rock", track)

        self.assertEqual(len(manager.playlists["Rock"]), 1)

    def test_sort_playlist(self):
        manager = PlaylistManager()
        manager.create("Rock")

        manager.add_track("Rock", {
            "title": "Tytul2",
            "author": "Autor2",
            "duration": 200
        })

        manager.add_track("Rock", {
            "title": "Tytul3",
            "author": "Autor3",
            "duration": 100
        })

        manager.sort("Rock")

        self.assertEqual(
            manager.playlists["Rock"][0]["title"],
            "Tytul2"
        )

    def test_estimate_size(self):
        manager = PlaylistManager()
        manager.create("Rock")

        manager.add_track("Rock", {
            "title": "Piosenka1",
            "author": "wykonawca1",
            "duration": 100
        })

        self.assertEqual(manager.estimate_size("Rock"), 100*125*128)


if __name__ == "__main__":
    unittest.main()
