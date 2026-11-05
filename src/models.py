class Track:

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