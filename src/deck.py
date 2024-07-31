import random
from src.card import Card

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in "23456789TJQK" for suits in "hearts diamonds clubs spades". split()]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, num):
        dealt_cards = self.cards 