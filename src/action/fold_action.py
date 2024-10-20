from action.base_action import Action

class Fold(Action):
    def execute(self, player, round_instance, amount=None):
        player.active = False  # Mark the player as folded
        print(f"{player.name} folds.")
