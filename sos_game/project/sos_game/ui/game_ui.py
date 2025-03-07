import tkinter as tk
from tkinter import ttk, messagebox
from model import SOSGame, GameMode

class SOSGameUI(tk.Tk):
    """Main UI class for the SOS Game"""
    
    def __init__(self):
        super().__init__()
        
        # Initialize the game with default settings
        self.game = SOSGame(board_size=3, game_mode=GameMode.SIMPLE)
        
        # Configure the main window
        self.title("SOS Game")
        self.geometry("500x550")
        self.resizable(False, False)
        
        # Create the game options panel
        self.create_options_panel()
        
        # Create the game board panel
        self.create_game_board()
        
        # Create the player panels
        self.create_player_panels()
        
        # Create the status bar
        self.create_status_bar()
    
    def create_options_panel(self):
        """Create the panel for game options (board size and game mode)"""
        options_frame = ttk.LabelFrame(self, text="Game Options")
        options_frame.pack(fill="x", padx=10, pady=10)
        
        # Board size selection
        board_size_frame = ttk.Frame(options_frame)
        board_size_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(board_size_frame, text="Board Size:").pack(side="left", padx=5)
        
        self.board_size_var = tk.StringVar(value="3")
        self.board_size_spinbox = ttk.Spinbox(
            board_size_frame, 
            from_=3, 
            to=12, 
            textvariable=self.board_size_var, 
            width=5
        )
        self.board_size_spinbox.pack(side="left", padx=5)
        
        # Game mode selection
        game_mode_frame = ttk.Frame(options_frame)
        game_mode_frame.pack(fill="x", padx=5, pady=5)
        
        ttk.Label(game_mode_frame, text="Game Mode:").pack(side="left", padx=5)
        
        self.game_mode_var = tk.StringVar(value="simple")
        self.simple_radio = ttk.Radiobutton(
            game_mode_frame, 
            text="Simple Game", 
            variable=self.game_mode_var, 
            value="simple"
        )
        self.simple_radio.pack(side="left", padx=5)
        
        self.general_radio = ttk.Radiobutton(
            game_mode_frame, 
            text="General Game", 
            variable=self.game_mode_var, 
            value="general"
        )
        self.general_radio.pack(side="left", padx=5)
        
        # New Game button
        self.new_game_button = ttk.Button(
            options_frame, 
            text="New Game", 
            command=self.start_new_game
        )
        self.new_game_button.pack(pady=10)
    
    def create_game_board(self):
        """Create the game board canvas"""
        self.board_frame = ttk.LabelFrame(self, text="Game Board")
        self.board_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        self.canvas = tk.Canvas(
            self.board_frame, 
            width=400, 
            height=400, 
            bg="white"
        )
        self.canvas.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Bind mouse click event to the canvas
        self.canvas.bind("<Button-1>", self.on_board_click)
        
        # Set default cell size
        self.cell_size = 40
        
        # Draw the initial board
        self.draw_board()
    
    def create_player_panels(self):
        """Create panels for both players"""
        players_frame = ttk.Frame(self)
        players_frame.pack(fill="x", padx=10, pady=10)
        
        # Blue player panel
        self.blue_player_frame = ttk.LabelFrame(players_frame, text="Blue Player")
        self.blue_player_frame.pack(side="left", fill="both", expand=True, padx=5)
        
        self.blue_move_var = tk.StringVar(value="S")
        ttk.Radiobutton(
            self.blue_player_frame, 
            text="S", 
            variable=self.blue_move_var, 
            value="S",
            command=lambda: self.game.players[0].set_move_type("S")
        ).pack(anchor="w", padx=10, pady=5)
        
        ttk.Radiobutton(
            self.blue_player_frame, 
            text="O", 
            variable=self.blue_move_var, 
            value="O",
            command=lambda: self.game.players[0].set_move_type("O")
        ).pack(anchor="w", padx=10, pady=5)
        
        # Red player panel
        self.red_player_frame = ttk.LabelFrame(players_frame, text="Red Player")
        self.red_player_frame.pack(side="right", fill="both", expand=True, padx=5)
        
        self.red_move_var = tk.StringVar(value="S")
        ttk.Radiobutton(
            self.red_player_frame, 
            text="S", 
            variable=self.red_move_var, 
            value="S",
            command=lambda: self.game.players[1].set_move_type("S")
        ).pack(anchor="w", padx=10, pady=5)
        
        ttk.Radiobutton(
            self.red_player_frame, 
            text="O", 
            variable=self.red_move_var, 
            value="O",
            command=lambda: self.game.players[1].set_move_type("O")
        ).pack(anchor="w", padx=10, pady=5)
    
    def create_status_bar(self):
        """Create the status bar at the bottom of the window"""
        self.status_var = tk.StringVar(value="Current turn: Blue")
        self.status_bar = ttk.Label(
            self, 
            textvariable=self.status_var, 
            relief="sunken", 
            anchor="center"
        )
        self.status_bar.pack(fill="x", padx=10, pady=5)
    
    def start_new_game(self):
        """Start a new game with the chosen settings"""
        try:
            board_size = int(self.board_size_var.get())
            if board_size < 3 or board_size > 12:
                messagebox.showerror("Invalid Input", "Board size must be between 3 and 12")
                return
            
            game_mode = GameMode.SIMPLE if self.game_mode_var.get() == "simple" else GameMode.GENERAL
            
            self.game.start_new_game(board_size, game_mode)
            self.draw_board()
            self.update_status()
            
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number for board size")
    
    def draw_board(self):
        """Draw the game board on the canvas"""
        self.canvas.delete("all")  # Clear canvas
        
        board = self.game.get_board()
        board_size = board.get_size()
        
        # Calculate cell size based on canvas size and board size
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        
        # Use a minimum size to ensure the board is drawn even before the canvas is fully realized
        if canvas_width < 50:  # Default min size
            canvas_width = 400
        if canvas_height < 50:  # Default min size
            canvas_height = 400
        
        self.cell_size = min(canvas_width, canvas_height) // board_size
        
        # Draw the grid
        for i in range(board_size + 1):
            # Horizontal lines
            self.canvas.create_line(
                0, i * self.cell_size,
                board_size * self.cell_size, i * self.cell_size,
                fill="gray"
            )
            # Vertical lines
            self.canvas.create_line(
                i * self.cell_size, 0,
                i * self.cell_size, board_size * self.cell_size,
                fill="gray"
            )
        
        # Draw the S and O markers
        for row in range(board_size):
            for col in range(board_size):
                value = board.get_cell_value(row, col)
                if value != ' ':
                    x = col * self.cell_size + self.cell_size // 2
                    y = row * self.cell_size + self.cell_size // 2
                    
                    # Determine color based on player turn
                    # Since we switch players after a move, the color is opposite to current player
                    player_color = "blue" if self.game.current_player_index == 1 else "red"
                    
                    self.canvas.create_text(
                        x, y,
                        text=value,
                        font=("Arial", 20, "bold"),
                        fill=player_color
                    )
    
    def on_board_click(self, event):
        """Handle click events on the game board"""
        board_size = self.game.board.get_size()
        
        # Calculate row and column based on click position
        col = event.x // self.cell_size
        row = event.y // self.cell_size
        
        if 0 <= row < board_size and 0 <= col < board_size:
            if self.game.make_move(row, col):
                self.draw_board()
                self.update_status()
    
    def update_status(self):
        """Update the status bar to show current player's turn"""
        current_player = self.game.get_current_player()
        self.status_var.set(f"Current turn: {current_player.get_color().capitalize()}")
        
        # Update the player panel highlight to indicate current turn
        if current_player.get_color() == "blue":
            self.blue_player_frame.config(background="#ADD8E6")  # Light blue
            self.red_player_frame.config(background="SystemButtonFace")  # Default
        else:
            self.blue_player_frame.config(background="SystemButtonFace")  # Default
            self.red_player_frame.config(background="#FFCCCB")  # Light red