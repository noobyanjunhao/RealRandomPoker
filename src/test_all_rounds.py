from unittest.mock import patch
import random
from game import Game
from player import Player

def test_pre_flop_to_river_round():
    # Create players
    players = [
        Player(player_id=1, name="Alice", stack=1000),
        Player(player_id=2, name="Bob", stack=1000),
        Player(player_id=3, name="Charlie", stack=1000)
    ]

    # Initialize the game
    game = Game(players, small_blind=10, big_blind=20, ante=5, buy_in=1000)
    game.dealer.players = players  # Set players for the dealer

    def mock_input_pre_flop(prompt):
        """Handles pre-flop round actions with no raises."""
        # Pre-flop round: everyone just calls or checks, no raises
        if "Alice" in prompt:
            return "check"
        elif "Bob" in prompt:
            return "check"
        elif "Charlie" in prompt:
            return "check"
        return "check"

    def mock_input_other(prompt):
        """Handles flop, turn, and river rounds where Bob raises randomly between 20 to 50."""
        if "Bob" in prompt:
            return "raise"
        elif "Enter the raise amount:" in prompt:
            raise_amount = random.randint(20, 50)
            return str(raise_amount)
        elif "Alice" in prompt or "Charlie" in prompt:
            return "call"
        return "check"

    # Mock pre-flop round (no raises)
    with patch('builtins.input', side_effect = mock_input_pre_flop):
        # Run the pre-flop round
        game.pre_flop_round()

        # Output the results after pre-flop
        print("\nAfter pre-flop round:")
        for player in players:
            print(f"{player.name} has {player.stack} chips remaining.")
        print(f"Total pot: {game.dealer.pot}")

    # Mock flop, turn, and river rounds (Bob raises randomly between 20 and 50)
    with patch('builtins.input', side_effect = mock_input_other):
        # Run the flop round
        game.flop_round()
        # Output the results after the flop round
        print("\nAfter flop round:")
        for player in players:
            print(f"{player.name} has {player.stack} chips remaining.")
        print(f"Total pot: {game.dealer.pot}")

        # Run the turn round
        game.turn_round()
        # Output the results after the turn round
        print("\nAfter turn round:")
        for player in players:
            print(f"{player.name} has {player.stack} chips remaining.")
        print(f"Total pot: {game.dealer.pot}")

        # Run the river round
        game.river_round()
        # Output the results after the river round
        print("\nAfter river round:")
        for player in players:
            print(f"{player.name} has {player.stack} chips remaining.")
        print(f"Total pot: {game.dealer.pot}")

# Execute the test
test_pre_flop_to_river_round()
