from app.players.elves.elf import Elf


class Druid(Elf):
    def __init__(
            self,
            nickname: str,
            musical_instrument: str = None,
            favourite_spell: str = None
    ) -> None:
        super().__init__(nickname, musical_instrument)
        self._favourite_spell = favourite_spell

    def get_rating(self) -> None:
        return len(self._favourite_spell)

    def player_info(self) -> None:
        return (f"Druid {self.nickname}. {self.nickname} "
                f"has a favourite spell: {self._favourite_spell}")
