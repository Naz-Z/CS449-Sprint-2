class Player:
    """Represents a player in the SOS game"""
    
    def __init__(self, name, color):
        """Initialize a new player with a name and color"""
        self.name = name
        self.color = color
        self.move_type = 'S'  # Default to 'S'
    
    def get_name(self):
        """Get the player's name"""
        return self.name
    
    def get_color(self):
        """Get the player's color"""
        return self.color
    
    def get_move_type(self):
        """Get the player's current move type ('S' or 'O')"""
        return self.move_type
    
    def set_move_type(self, move_type):
        """Set the player's move type ('S' or 'O')"""
        if move_type in ['S', 'O']:
            self.move_type = move_type