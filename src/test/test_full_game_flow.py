import sys
import os

# Add the src/ directory to sys.path so Python can find the model package
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from model.game import Game
from model.player import Player
from test_util import mock_input_for_all
from unittest.mock import patch

def test_full_game_flow():
    # Create players
    players = [
        Player(player_id=1, name="Alice", stack=1000),
        Player(player_id=2, name="Bob", stack=1000),
        Player(player_id=3, name="Charlie", stack=1000)
    ]

    # Initialize the game
    game = Game(players, small_blind=10, big_blind=20, ante=5, buy_in=1000)
    game.dealer.players = players  # Set players for the dealer

    # Mock
    with patch('builtins.input', side_effect=mock_input_for_all):
        game.play_game()  # Call play_game instead of pre_flop_round

# Execute the test
test_full_game_flow()
