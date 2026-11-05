class Track:
    def init(self, track_id, title, artist, duration_seconds, rating):
            self.track_id = track_id
            self.title = title
            self.artist = artist
            self.duration_seconds = duration_seconds
            self.rating = rating

        def repr(self):
            return f"MenuItem(track_id={self.track_id}, title={self.title!r}, artist={self.artist}, duration_seconds={self.duration_seconds}, rating={self.rating})"

        def str(self):
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
