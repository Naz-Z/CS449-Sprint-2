from base_game import BaseGame
from enums import Player, GameMode
from players import HumanPlayer

class SimpleGame(BaseGame):
    pass

class GeneralGame(BaseGame):
    pass

class GameFactory:
    @staticmethod
    def create_game(mode, size):
        if mode == GameMode.SIMPLE:
            return SimpleGame(size)
        elif mode == GameMode.GENERAL:
            return GeneralGame(size)
        else:
            raise ValueError(f"Unknown game mode: {mode}")

    @staticmethod
    def set_player_types(game_instance):
        game_instance.blue_player_object = HumanPlayer(Player.BLUE)
        game_instance.red_player_object = HumanPlayer(Player.RED)
