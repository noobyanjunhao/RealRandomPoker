import random
from model.card import Card #to get the shuffle() method to randomize the deck

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for rank in "23456789TJQK" for suit in "hearts diamonds clubs spades". split()]
        self.shuffle()
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def deal(self, num):
        dealt_cards = self.cards[:num] #get first num cards
        self.cards = self.cards[num:] #keeps all the cards from idex num to end of list
        return dealt_cards 