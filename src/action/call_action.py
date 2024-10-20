from action.base_action import Action

class Call(Action):
    def execute(self, player, round_instance, call_amount):
        additional_bet = call_amount - round_instance.player_bets[player]
        if additional_bet > 0:
            player.place_bet(additional_bet)  # Deduct chips from the player's stack
            round_instance.player_bets[player] += additional_bet  # Update player's total bet
            round_instance.game.dealer.pot += additional_bet  # Update the pot
        print(f"{player.name} calls with {call_amount}.")
