from abc import ABC, abstractmethod
from action.fold_action import Fold
from action.check_action import Check
from action.call_action import Call
from action.raise_action import Raise

class Round(ABC):
    STARTING_PLAYER_INDEX = 1  # Constant for small blind being the first to act after the flop

    def __init__(self, game):
        self.game = game
        self.current_bet = 0  # Tracks the current highest bet in this round
        self.player_bets = {player: 0 for player in self.game.players}  # Tracks bets by player

    @abstractmethod
    def play(self):
        """Abstract method to define the round-specific logic."""
        pass

    def handle_betting_round(self, starting_player_index):
        """Handles the betting for the round, ensuring players call, raise, or fold."""
        all_called = False
        last_raiser = None  # Keep track of the last player who raised

        while not all_called:
            all_called = True  # Assume all players have called or checked

            for i in range(starting_player_index, len(self.game.players) + starting_player_index):
                index = i % len(self.game.players)  # Wrap-around for circular betting
                player = self.game.players[index]

                # If coming back to the raiser, we can break out of the loop
                if player == last_raiser: 
                    break

                print(f"Current player to take action: {player.name}")  # Debugging

                if not player.active:
                    continue  # Skip inactive players

                # Decide available actions for the player based on the current bet
                if self.player_bets[player] < self.current_bet:
                    # Player must call, raise, or fold if there’s a current bet
                    action = self.get_player_action(player, can_check=False)
                else:
                    # Player can check, fold, or raise if there’s no active raise
                    action = self.get_player_action(player, can_check=True)

                # Process player action
                if isinstance(action, Fold):
                    action.execute(player, self)  # Pass the current round instance (self)
                elif isinstance(action, Call):
                    call_amount = self.current_bet - self.player_bets[player]
                    action.execute(player, self, call_amount)  # Pass round instance and call amount
                elif isinstance(action, Raise):
                    raise_amount = action.get_raise_amount(self.current_bet)
                    if raise_amount:
                        action.execute(player, self, raise_amount)  # Pass round instance and raise amount
                        all_called = False  # Since there's a raise, we loop again
                        last_raiser = player
                elif isinstance(action, Check):
                    action.execute(player, self)  # Pass the current round instance (self)

                # If any player's bet is less than the current bet, we need another round
                if self.player_bets[player] < self.current_bet:
                    all_called = False

        return sum(self.player_bets.values())  # Return the total amount of bets for the round

    def get_player_action(self, player, can_check):
        """Prompt the player for an action and return the corresponding action object."""
        if can_check:
            action_input = input(f"{player.name}, enter your action (fold/check/raise):").lower()
        else:
            action_input = input(f"{player.name}, enter your action (fold/call/raise):").lower()

        if action_input == "fold":
            return Fold()
        elif action_input == "check" and can_check:
            return Check()
        elif action_input == "call" and not can_check:
            return Call()
        elif action_input == "raise":
            return Raise()
        else:
            print("Invalid action, try again.")
            return self.get_player_action(player, can_check)
