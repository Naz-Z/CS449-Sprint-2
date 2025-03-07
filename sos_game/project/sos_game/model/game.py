from model.board import Board
from model.game_mode import GameMode
from model.player import Player

class SOSGame:
    """Main game class that manages the state of an SOS game"""
    
    def __init__(self, board_size=3, game_mode=GameMode.SIMPLE):
        """Initialize a new game with the given board size and game mode"""
        self.board = Board(board_size)
        self.game_mode = game_mode
        
        # Initialize players
        self.players = [
            Player("Blue Player", "blue"),
            Player("Red Player", "red")
        ]
        
        self.current_player_index = 0  # Blue player starts
    
    def get_board(self):
        """Get the game board"""
        return self.board
    
    def get_game_mode(self):
        """Get the current game mode"""
        return self.game_mode
    
    def get_current_player(self):
        """Get the current player"""
        return self.players[self.current_player_index]
    
    def switch_player(self):
        """Switch to the next player's turn"""
        self.current_player_index = (self.current_player_index + 1) % 2
    
    def make_move(self, row, col):
        """Make a move at the specified position using current player's move type"""
        current_player = self.get_current_player()
        move_type = current_player.get_move_type()
        
        if self.board.make_move(row, col, move_type):
            self.switch_player()
            return True
        return False
    
    def start_new_game(self, board_size, game_mode):
        """Start a new game with the specified board size and game mode"""
        self.board = Board(board_size)
        self.game_mode = game_mode
        self.current_player_index = 0  # Blue player starts