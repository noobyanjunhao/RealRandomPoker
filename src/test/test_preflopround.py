from model.game import Game
from model.player import Player


def test_pre_flop_round():
    # Create players
    players = [
        Player(player_id=1, name="Alice", stack=1000),
        Player(player_id=2, name="Bob", stack=1000),
        Player(player_id=3, name="Charlie", stack=1000)
    ]

    # Initialize the game
    game = Game(players, small_blind=10, big_blind=20, ante=5, buy_in=1000)
    game.dealer.players = players  # Set players for the dealer

    # Run the pre-flop round
    game.pre_flop_round()

    # Output the results
    print("After pre-flop round:")
    for player in players:
        print(f"{player.name} has {player.stack} chips remaining.")
    print(f"Total pot: {game.dealer.pot}")

# Execute the test
test_pre_flop_round()