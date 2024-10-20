from enum import Enum

class PlayerAction(Enum):
    FOLD = 1
    CHECK = 2
    CALL = 3
    RAISE = 4
    ALL_IN = 5
