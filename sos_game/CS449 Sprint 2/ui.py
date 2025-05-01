import tkinter as tk
from tkinter import messagebox, ttk
from enums import GameMode, Player
from game_types import GameFactory
from players import HumanPlayer

class SOSGameUI:
    def __init__(self, root):
        self.root = root
        self.root.title("SOS Game")
        self.root.geometry("800x600")
        
        self.size_var = tk.IntVar(value=3)
        self.mode_var = tk.StringVar(value=GameMode.SIMPLE.value)
        self.blue_letter = tk.StringVar(value='S')
        self.red_letter = tk.StringVar(value='S')

        # Player type is always human
        self.blue_player_type = "Human"
        self.red_player_type = "Human"

        self.game = None
        self.cell_size = 50
        self.canvas = None
        self.cells = []

        self.initialize_ui()
    
    def initialize_ui(self):
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Options panel
        options_frame = ttk.LabelFrame(main_frame, text="Game Options", padding="10")
        options_frame.pack(side=tk.TOP, fill=tk.X, pady=10)
        
        # Board size
        size_frame = ttk.Frame(options_frame)
        size_frame.pack(side=tk.LEFT, padx=10)
        ttk.Label(size_frame, text="Board Size:").pack(side=tk.LEFT)
        size_spinner = ttk.Spinbox(size_frame, from_=3, to=10, width=5, textvariable=self.size_var)
        size_spinner.pack(side=tk.LEFT, padx=5)
        
        # Game mode
        mode_frame = ttk.Frame(options_frame)
        mode_frame.pack(side=tk.LEFT, padx=20)
        ttk.Label(mode_frame, text="Game Mode:").pack(side=tk.LEFT)
        ttk.Radiobutton(mode_frame, text=GameMode.SIMPLE.value, variable=self.mode_var, 
                        value=GameMode.SIMPLE.value).pack(side=tk.LEFT)
        ttk.Radiobutton(mode_frame, text=GameMode.GENERAL.value, variable=self.mode_var, 
                        value=GameMode.GENERAL.value).pack(side=tk.LEFT)
        
        # New Game button
        ttk.Button(options_frame, text="New Game", command=self.start_new_game).pack(side=tk.RIGHT, padx=10)

        # Main game frame
        game_frame = ttk.Frame(main_frame)
        game_frame.pack(fill=tk.BOTH, expand=True, pady=10)
        
        # Blue player panel
        blue_frame = ttk.LabelFrame(game_frame, text="Blue Player", padding="10")
        blue_frame.pack(side=tk.LEFT, fill=tk.Y, padx=10)
        
        ttk.Radiobutton(blue_frame, text="S", variable=self.blue_letter, value='S').pack(anchor=tk.W)
        ttk.Radiobutton(blue_frame, text="O", variable=self.blue_letter, value='O').pack(anchor=tk.W)
        
        self.blue_score_label = ttk.Label(blue_frame, text="Score: 0")
        self.blue_score_label.pack(pady=10)
        
        # Board frame
        self.board_frame = ttk.Frame(game_frame)
        self.board_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Red player panel
        red_frame = ttk.LabelFrame(game_frame, text="Red Player", padding="10")
        red_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10)
        
        ttk.Radiobutton(red_frame, text="S", variable=self.red_letter, value='S').pack(anchor=tk.W)
        ttk.Radiobutton(red_frame, text="O", variable=self.red_letter, value='O').pack(anchor=tk.W)
        
        self.red_score_label = ttk.Label(red_frame, text="Score: 0")
        self.red_score_label.pack(pady=10)
        
        # Status bar
        self.status_var = tk.StringVar(value="Start a new game")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, relief=tk.SUNKEN, anchor=tk.W)
        status_bar.pack(side=tk.BOTTOM, fill=tk.X)
    
    def start_new_game(self):
        size = self.size_var.get()
        mode = GameMode(self.mode_var.get())
        
        # Create game
        self.game = GameFactory.create_game(mode, size)

        # Set player types (both are Human)
        GameFactory.set_player_types(self.game)

        self.create_board()
        self.update_status(f"{self.game.current_player.value} player's turn")
        self.update_scores()
    
    def create_board(self):
        if self.canvas:
            self.canvas.destroy()
        
        board_size = self.size_var.get()
        canvas_size = board_size * self.cell_size
        
        self.canvas = tk.Canvas(self.board_frame, width=canvas_size, height=canvas_size,
                                background='white', highlightthickness=1, highlightbackground='black')
        self.canvas.pack(expand=True)
        
        self.cells = []
        for row in range(board_size):
            row_cells = []
            for col in range(board_size):
                x1 = col * self.cell_size
                y1 = row * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                rect_id = self.canvas.create_rectangle(x1, y1, x2, y2, fill='white', outline='black')
                text_id = self.canvas.create_text(
                    x1 + self.cell_size / 2,
                    y1 + self.cell_size / 2,
                    text='',
                    font=('Arial', 14, 'bold')
                )
                row_cells.append((rect_id, text_id))

                # Only clickable if it's a human turn
                self.canvas.tag_bind(rect_id, '<Button-1>',
                                     lambda event, r=row, c=col: self.on_board_click(r, c))
            self.cells.append(row_cells)
    
    def on_board_click(self, row, col):
        if not self.game or self.game.game_over:
            return
        
        # If the cell is occupied, ignore
        if self.game.board[row][col] != ' ':
            return

        # Human letter
        letter = self.blue_letter.get() if self.game.current_player == Player.BLUE else self.red_letter.get()
        success = self.game.make_move(row, col, letter)
        if success:
            self.update_board()
            self.update_scores()

            if self.game.game_over:
                self.handle_game_over()
            else:
                self.update_status(f"{self.game.current_player.value} player's turn")

    def update_board(self):
        for r in range(self.game.size):
            for c in range(self.game.size):
                _, text_id = self.cells[r][c]
                letter = self.game.board[r][c]
                self.canvas.itemconfig(text_id, text=letter)
        
    def update_status(self, message):
        self.status_var.set(message)
    
    def update_scores(self):
        if self.game:
            self.blue_score_label.config(text=f"Score: {self.game.blue_score}")
            self.red_score_label.config(text=f"Score: {self.game.red_score}")

    def handle_game_over(self):
        if self.game.winner:
            self.update_status(f"Game over! {self.game.winner.value} player wins!")
            messagebox.showinfo("Game Over", f"{self.game.winner.value} player wins!")
        else:
            self.update_status("Game over! It's a draw!")
            messagebox.showinfo("Game Over", "It's a draw!")
