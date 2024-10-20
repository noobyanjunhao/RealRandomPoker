from action.base_action import Action

class AllIn(Action):
    def execute(self, player, round_instance, amount=None):
        all_in_amount = player.stack
        round_instance.player_bets[player] += all_in_amount
        round_instance.game.dealer.pot += all_in_amount
        player.place_bet(all_in_amount)
        print(f"{player.name} goes all in with {all_in_amount}.")
