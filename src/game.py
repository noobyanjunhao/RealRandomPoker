
from deck import Deck
from player import Player
from table import Table
from dealer import Dealer
from evaluate import Evaluate
import time

small_blind = int(input("Enter the small blind: "))
big_blind = 2 * small_blind
ante = int(input(f"Enter the ante: smaller then {small_blind}"))
buy_in = int(input("Enter the buy in amount: "))

#the following player enter method should be changed 
players = []
ids = [1, 2, 3, 4, 5, 6, 7, 8]
for id in ids:
    name = input(f"Enter player {id}'s name: ")
    player = Player(id, name, buy_in)
    players.append(player)

class Game:
    def __init__(self, players, small_blind, big_blind, ante , buy_in):
        self.deck = Deck()
        self.players = players
        self.table = Table(players)
        self.dealer = Dealer()
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.ante = ante
        self.buy_in = buy_in
    player_positions = players # the order of the players is the indexing of the list of players, so when player enters the game, they can choose their positions
    #player when entering could choose which position they want to seat in the list of players

    def assign_dealer(self): 
        self.deck.shuffle()
        for i in range(len(self.players)):
            card = self.deck.deal(1)
            self.players[i].hand.append(card)
        #pick out who has the dealer button
        # the player with the dealer button is the player has the highest card
        for i in range(len(self.players)):
            if self.players[i].hand[0] == max(self.players[i].hand):
                self.players = self.players[i:] + self.players[:i] # the player with the dealer button is the first player in the list of players
                break
        print(f"{self.players[0].name} get the dealer button, {self.players[1].name} is the small blind, {self.players[2].name} is the big blind")
        

    

                