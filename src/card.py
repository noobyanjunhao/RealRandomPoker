class Card:
    rank_values = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
                   'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def value (self):
        return self.rank_values[self.rank]
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    