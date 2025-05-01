from enum import Enum

class GameMode(Enum):
    SIMPLE = "Simple"
    GENERAL = "General"

class Player(Enum):
    BLUE = "Blue"
    RED = "Red"
    
    def get_opposite(self):
        return Player.RED if self == Player.BLUE else Player.BLUE
    
    def get_color(self):
        return "blue" if self == Player.BLUE else "red"
