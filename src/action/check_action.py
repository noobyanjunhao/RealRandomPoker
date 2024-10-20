from action.base_action import Action

class Check(Action):
    def execute(self, player, round_instance, amount=None):
        # No need to update the bet or pot, just log the action
        print(f"{player.name} checks.")
