from unittest.mock import patch
from game import Game
from player import Player


def mock_input(prompt):
    # Add actions for the flop round
    simulated_inputs = {
        "Alice, enter your action (fold/check/call/raise):": "call",
        "Bob, enter your action (fold/check/call/raise):": "raise",
        "Enter the raise amount:": "40",
        "Charlie, enter your action (fold/check/call/raise):": "call",
    }
    
    return simulated_inputs.get(prompt, "check")  # Default action is 'check'


def test_pre_flop_and_flop_round():
    # Create players
    players = [
        Player(player_id=1, name="Alice", stack=1000),
        Player(player_id=2, name="Bob", stack=1000),
        Player(player_id=3, name="Charlie", stack=1000)
    ]

    # Initialize the game
    game = Game(players, small_blind=10, big_blind=20, ante=5, buy_in=1000)
    game.dealer.players = players  # Set players for the dealer

    # Mock the input to simulate player actions
    with patch('builtins.input', side_effect=mock_input):
        # Run the pre-flop round
        game.pre_flop_round()

        # Output the results after pre-flop
        print("\nAfter pre-flop round:")
        for player in players:
            print(f"{player.name} has {player.stack} chips remaining.")
        print(f"Total pot: {game.dealer.pot}")

        # Run the flop round
        game.flop_round()

        # Output the results after flop
        print("\nAfter flop round:")
        for player in players:
            print(f"{player.name} has {player.stack} chips remaining.")
        print(f"Total pot: {game.dealer.pot}")

# Execute the test
test_pre_flop_and_flop_round()
