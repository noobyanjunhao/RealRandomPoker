from action.base_action import Action

class Raise(Action):
    def execute(self, player, round_instance, raise_amount):
        if raise_amount < 2 * round_instance.current_bet:
            print(f"Raise amount is too low. It must be at least twice the current bet ({round_instance.current_bet}).")
            return
        if player.stack >= raise_amount:
            additional_bet = raise_amount - round_instance.player_bets[player]
            player.place_bet(additional_bet)
            round_instance.player_bets[player] += additional_bet
            round_instance.game.dealer.pot += additional_bet
            round_instance.current_bet = raise_amount  # Update current bet to the new raise
            print(f"{player.name} raises by {raise_amount}.")
        else:
            print(f"{player.name} does not have enough chips to raise.")

    def get_raise_amount(self, current_bet):
        try:
            raise_amount = int(input(f"Enter the raise amount (at least twice the current bet of {current_bet}): "))
            return raise_amount
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            return self.get_raise_amount(current_bet)
