import unittest
from model.board import Board

class TestBoard(unittest.TestCase):
    """Test cases for the Board class"""
    
    def setUp(self):
        self.board = Board(3)
    
    def test_board_initialization(self):
        """Test that the board is initialized correctly"""
        self.assertEqual(3, self.board.get_size())
        
        # Check that all cells are empty
        for i in range(3):
            for j in range(3):
                self.assertEqual(' ', self.board.get_cell_value(i, j))
    
    def test_make_move_valid_position(self):
        """Test that a move can be made on a valid position"""
        self.assertTrue(self.board.make_move(0, 0, 'S'))
        self.assertEqual('S', self.board.get_cell_value(0, 0))
        
        self.assertTrue(self.board.make_move(1, 1, 'O'))
        self.assertEqual('O', self.board.get_cell_value(1, 1))
    
    def test_make_move_invalid_position(self):
        """Test that a move cannot be made on an invalid position"""
        self.assertFalse(self.board.make_move(-1, 0, 'S'))
        self.assertFalse(self.board.make_move(0, -1, 'S'))
        self.assertFalse(self.board.make_move(3, 0, 'S'))
        self.assertFalse(self.board.make_move(0, 3, 'S'))
    
    def test_make_move_occupied_cell(self):
        """Test that a move cannot be made on an already occupied cell"""
        self.assertTrue(self.board.make_move(0, 0, 'S'))
        self.assertFalse(self.board.make_move(0, 0, 'O'))
        self.assertEqual('S', self.board.get_cell_value(0, 0))
    
    def test_reset_board(self):
        """Test that the board can be reset"""
        self.board.make_move(0, 0, 'S')
        self.board.make_move(1, 1, 'O')
        
        self.board.reset_board()
        
        # Check that all cells are empty after reset
        for i in range(3):
            for j in range(3):
                self.assertEqual(' ', self.board.get_cell_value(i, j))

if __name__ == '__main__':
    unittest.main()