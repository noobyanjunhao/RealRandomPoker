from abc import ABC, abstractmethod

class Action(ABC):
    @abstractmethod
    def execute(self, player, round_instance, amount=None):
        """Execute the action. Needs to be implemented by all subclasses."""
        pass
