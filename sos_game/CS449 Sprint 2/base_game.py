from enums import Player

class BaseGame:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.current_player = Player.BLUE
        self.winner = None
        self.blue_score = 0
        self.red_score = 0
        self.game_over = False

    def make_move(self, row, col, letter):
        if self.game_over:
            return False
        
        if self.board[row][col] == ' ':
            self.board[row][col] = letter
            self.switch_player()
            return True
        return False

    def switch_player(self):
        self.current_player = self.current_player.get_opposite()
    
    def reset(self):
        self.board = [[' ' for _ in range(self.size)] for _ in range(self.size)]
        self.current_player = Player.BLUE
        self.winner = None
        self.blue_score = 0
        self.red_score = 0
        self.game_over = False
