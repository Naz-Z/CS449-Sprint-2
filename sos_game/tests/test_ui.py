import unittest
import tkinter as tk
from unittest.mock import MagicMock
from model.board import Board
from model.player import Player

class TestGameUI(unittest.TestCase):
    """Test cases for the UI components"""
    
    def setUp(self):
        # Create a root window for testing
        self.root = tk.Tk()
        self