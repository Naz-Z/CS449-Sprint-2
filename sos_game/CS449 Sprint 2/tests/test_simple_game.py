import unittest
from enums import Player
from game_types import SimpleGame

class TestSimpleGame(unittest.TestCase):
    def setUp(self):
        self.game = SimpleGame(3)
    
    def test_simple_game_win(self):
        self.game.make_move(0, 0, 'S')
        self.assertFalse(self.game.game_over)
        
        self.game.make_move(1, 1, 'S')
        self.assertFalse(self.game.game_over)
        
        self.game.make_move(0, 1, 'O')
        self.assertFalse(self.game.game_over)
        
        self.game.make_move(2, 2, 'S')
        self.assertFalse(self.game.game_over)
        
        self.game.make_move(0, 2, 'S')
        self.assertTrue(self.game.game_over)
        self.assertEqual(self.game.winner, Player.BLUE)

if __name__ == '__main__':
    unittest.main()
