class Board:
    """Represents the game board for SOS game"""
    
    def __init__(self, size):
        """Initialize a new board with the given size"""
        self.size = size
        self.grid = [[' ' for _ in range(size)] for _ in range(size)]
    
    def get_size(self):
        """Get the size of the board"""
        return self.size
    
    def get_cell_value(self, row, col):
        """Get the value of a cell at the given position"""
        if self.is_valid_position(row, col):
            return self.grid[row][col]
        return ' '
    
    def make_move(self, row, col, value):
        """Place an 'S' or 'O' on the board"""
        if self.is_valid_position(row, col) and self.grid[row][col] == ' ' and value in ['S', 'O']:
            self.grid[row][col] = value
            return True
        return False
    
    def is_valid_position(self, row, col):
        """Check if position is within the board boundaries"""
        return 0 <= row < self.size and 0 <= col < self.size
    
    def is_cell_empty(self, row, col):
        """Check if the cell is empty"""
        return self.is_valid_position(row, col) and self.grid[row][col] == ' '
    
    def reset_board(self):
        """Reset the board to empty"""
        self.grid = [[' ' for _ in range(self.size)] for _ in range(self.size)]