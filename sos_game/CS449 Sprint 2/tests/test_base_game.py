import unittest
from base_game import BaseGame
from enums import Player

class TestBaseGame(unittest.TestCase):
    def setUp(self):
        self.game = BaseGame(3)
    
    def test_initialization(self):
        self.assertEqual(self.game.size, 3)
        self.assertEqual(self.game.current_player, Player.BLUE)
        self.assertIsNone(self.game.winner)
        self.assertEqual(self.game.blue_score, 0)
        self.assertEqual(self.game.red_score, 0)
        self.assertFalse(self.game.game_over)
    
    def test_make_move(self):
        result = self.game.make_move(0, 0, 'S')
        self.assertTrue(result)
        self.assertEqual(self.game.board[0][0], 'S')
        self.assertEqual(self.game.current_player, Player.RED)
    
    def test_reset(self):
        self.game.make_move(0, 0, 'S')
        self.game.blue_score = 2
        self.game.red_score = 1
        self.game.reset()
        
        self.assertEqual(self.game.current_player, Player.BLUE)
        self.assertIsNone(self.game.winner)
        self.assertEqual(self.game.blue_score, 0)
        self.assertEqual(self.game.red_score, 0)
        self.assertFalse(self.game.game_over)

if __name__ == '__main__':
    unittest.main()
