import unittest
from model.player import Player

class TestPlayer(unittest.TestCase):
    """Test cases for the Player class"""
    
    def setUp(self):
        self.player = Player("Blue Player", "blue")
    
    def test_player_initialization(self):
        """Test that a player is initialized correctly"""
        self.assertEqual("Blue Player", self.player.get_name())
        self.assertEqual("blue", self.player.get_color())
        self.assertEqual("S", self.player.get_move_type())  # Default is 'S'
    
    def test_set_move_type(self):
        """Test that a player's move type can be changed"""
        self.player.set_move_type("O")
        self.assertEqual("O", self.player.get_move_type())
        
        # Invalid move type should be ignored
        self.player.set_move_type("X")
        self.assertEqual("O", self.player.get_move_type())  # Should remain "O"

if __name__ == '__main__':
    unittest.main()