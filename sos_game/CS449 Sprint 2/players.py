from enums import Player
from abc import ABC, abstractmethod

class BasePlayer(ABC):
    def __init__(self, player_type: Player):
        self.player_type = player_type

    @abstractmethod
    def choose_letter(self, game):
        """Return 'S' or 'O' for the next move."""
        pass

    @abstractmethod
    def choose_cell(self, game):
        """Return (row, col) for the next move."""
        pass


class HumanPlayer(BasePlayer):
    def choose_letter(self, game):
        return None  # The UI picks the letter (radio buttons)

    def choose_cell(self, game):
        return None  # The UI picks the cell (mouse clicks)
