import unittest
from model.game import SOSGame
from model.game_mode import GameMode

class TestSOSGame(unittest.TestCase):
    """Test cases for the SOSGame class"""
    
    def setUp(self):
        self.game = SOSGame(3, GameMode.SIMPLE)
    
    def test_game_initialization(self):
        """Test that the game is initialized correctly"""
        self.assertEqual(3, self.game.get_board().get_size())
        self.assertEqual(GameMode.SIMPLE, self.game.get_game_mode())
        self.assertEqual("Blue Player", self.game.get_current_player().get_name())
        self.assertEqual("blue", self.game.get_current_player().get_color())
    
    def test_switch_player(self):
        """Test that players can be switched"""
        self.assertEqual("Blue Player", self.game.get_current_player().get_name())
        self.game.switch_player()
        self.assertEqual("Red Player", self.game.get_current_player().get_name())
        self.game.switch_player()
        self.assertEqual("Blue Player", self.game.get_current_player().get_name())
    
    def test_make_move(self):
        """Test that a move can be made and the turn switches"""
        self.assertTrue(self.game.make_move(0, 0))
        self.assertEqual("S", self.game.get_board().get_cell_value(0, 0))  # Default move type is 'S'
        self.assertEqual("Red Player", self.game.get_current_player().get_name())  # Should switch to Red player
        
        self.game.get_current_player().set_move_type("O")
        self.assertTrue(self.game.make_move(1, 1))
        self.assertEqual("O", self.game.get_board().get_cell_value(1, 1))
        self.assertEqual("Blue Player", self.game.get_current_player().get_name())  # Should switch back to Blue player
    
    def test_start_new_game(self):
        """Test that a new game can be started with different settings"""
        # Make some moves
        self.game.make_move(0, 0)
        self.game.make_move(1, 1)
        
        # Start a new game
        self.game.start_new_game(4, GameMode.GENERAL)
        
        # Verify new game state
        self.assertEqual(4, self.game.get_board().get_size())
        self.assertEqual(GameMode.GENERAL, self.game.get_game_mode())
        self.assertEqual("Blue Player", self.game.get_current_player().get_name())
        
        # Check that board is empty
        for i in range(4):
            for j in range(4):
                self.assertEqual(' ', self.game.get_board().get_cell_value(i, j))

# ChatGPT-generated test
class TestGameOptions(unittest.TestCase):
    """Test cases for game options functionality"""
    
    def setUp(self):
        self.game = SOSGame()
    
    def test_board_size_validation(self):
        """Test that board size validation works correctly"""
        # Valid board size
        self.game.start_new_game(3, GameMode.SIMPLE)
        self.assertEqual(3, self.game.get_board().get_size())
        
        self.game.start_new_game(8, GameMode.SIMPLE)
        self.assertEqual(8, self.game.get_board().get_size())
        
        self.game.start_new_game(12, GameMode.SIMPLE)
        self.assertEqual(12, self.game.get_board().get_size())
        
        # Test boundary conditions - these should be handled by UI validation
        # but the model should still accept them if they get past validation
        self.game.start_new_game(1, GameMode.SIMPLE)
        self.assertEqual(1, self.game.get_board().get_size())
        
        self.game.start_new_game(20, GameMode.SIMPLE)
        self.assertEqual(20, self.game.get_board().get_size())
    
    def test_game_mode_selection(self):
        """Test that game mode selection works correctly"""
        # Simple game mode
        self.game.start_new_game(3, GameMode.SIMPLE)
        self.assertEqual(GameMode.SIMPLE, self.game.get_game_mode())
        
        # General game mode
        self.game.start_new_game(3, GameMode.GENERAL)
        self.assertEqual(GameMode.GENERAL, self.game.get_game_mode())

if __name__ == '__main__':
    unittest.main()