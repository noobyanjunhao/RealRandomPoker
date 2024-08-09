
from deck import Deck
from player import Player
from dealer import Dealer
from evaluate import Evaluate
import time

global small_blind
global big_blind
global ante
global buy_in

"""
def game_setup():
    small_blind = int(input("Enter the small blind: "))
    big_blind = 2 * small_blind
    ante = int(input(f"Enter the ante: smaller then {small_blind}"))
    buy_in = int(input("Enter the buy in amount: "))
    print(f"Small blind: {small_blind}, Big blind: {big_blind}, Ante: {ante}, Buy in: {buy_in}")

#the following player enter method should be changed 
players = []
ids = [1, 2, 3, 4, 5, 6, 7, 8]
for id in ids:
    name = input(f"Enter player {id}'s name: ")
    player = Player(id, name, buy_in)
    players.append(player)
"""

class Game:
    def __init__(self, players, small_blind, big_blind, ante , buy_in):
        self.players = players
        self.dealer = Dealer(players)
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.ante = ante
        self.buy_in = buy_in
    
    # the order of the players is the indexing of the list of players, so when player enters the game, they can choose their positions
    #player when entering could choose which position they want to seat in the list of players

    def assign_dealer_button(self): 
        self.dealer.deck.shuffle()
        self.dealer.deal_hole_cards(1)
        #pick out who has the dealer button
        # the player with the dealer button is the player has the highest card
        highest_card_player = max(self.players, key = lambda p : p.hand[0].value())
        dealer_button = self.players.index(highest_card_player)
        self.players = self.players[dealer_button + 1:] + self.players[:dealer_button + 1]
        print(f"{self.players[0].name} get the dealer button, {self.players[1].name} is the small blind, {self.players[2].name} is the big blind")
        print(f"table order: {[player.name for player in self.players]}")
        
    def setup_table(self):
        self.dealer.community_cards = []
        self.dealer.deck = Deck()
        self.dealer.deck.shuffle()
        for player in self.players:
            player.hand = []
        print ("Table is set up")
        
    def check_player_action(self, player, current_bet, player_bets):
        #player action: fold, call, raise,check 
        while player.stack > 0:
            action = input(f"{player.name}, enter your action (fold/check/call/raise):").lower()
            if action == "fold":
                print(f"{player.name} folds")
                player.fold()
                return "fold", 0
            elif action == "check":
                if current_bet == player_bets[player] or current_bet == 0:
                    print(f"{player.name} checks")
                    return "check", 0
                else:
                    print("You can't check, you need to call, raise or fold")
            elif action == "call":
                call_amount = current_bet - player_bets[player]
                if player.stack >= call_amount:
                    player.place_bet(call_amount)
                    player_bets[player] += call_amount
                    print(f"{player.name} calls")
                    return "call", current_bet #what we return here is for person next to you to no what is the current bet
                else:
                    print("You don't have enough money to call")
            elif action == "raise":
                #rasie amount is restrcited to be at least 2 times greater then the current bet
                raise_amount = int(input("Enter the raise amount: "))
                if raise_amount < 2 * current_bet:
                    print("Raise amount is too low")
                else:
                    player_bets[player] = raise_amount
                    player.place_bet(raise_amount - player_bets[player])
                    return "raise", raise_amount #the current bet is now the raise amount
            else:
                print("Invalid action")
        all_in_amount = player.stack
        player.place_bet(all_in_amount)
        player_bets[player] += all_in_amount
        print (f"{player.name} goes all in amount:{all_in_amount}")
        return "All in", all_in_amount
                    
    def pre_flop_round(self):
        self.setup_table()
        self.assign_dealer_button()
        self.dealer.deal_hole_cards(2)
        #look at the hole cards
        for player in self.players:
            if player.active:
                player.check_hole_cards(2)
        #collect ante
        self.dealer.collect_ante(self.ante)
        #betting round
        #starting from small blind to bet
        player_bets = {player : 0 for player in self.players} #dict containing the player and their bet
        current_bet = self.big_blind
        #get the amount of bet from each player
        self.players[0].place_bet(self.small_blind)
        player_bets[self.players[0]] = self.small_blind
        self.dealer.pot += self.small_blind

        self.players[1].place_bet(self.big_blind)
        player_bets[self.players[1]] = self.big_blind
        self.dealer.pot += self.big_blind

        all_called = True #we need this boolean to make sure all called 
        for i in range(2, len(self.players)):
            if self.players[i].active:
                action, amount = self.check_player_action(self.players[i], current_bet, player_bets)
                if action == "raise":
                    current_bet = amount
                    all_called = False
                elif action == "All in":
                    current_bet = amount
                    all_called = False 
        #back to sb and bb for raise or call
        for i in range(2):
            if self.players[i].active:
                action, amount = self.check_player_action(self.players[i], current_bet, player_bets)
                if action == "raise":
                    current_bet = amount
                    all_called = False
                elif action == "All in":
                    current_bet = amount
                    all_called = False
        #back to the rest of the players
        while not all_called:
            all_called = True
            for i in range(2, len(self.players)):
                if self.players[i].active:
                    action, amount = self.check_player_action(self.players[i], current_bet, player_bets)
                    if action == "raise":
                        current_bet = amount
                        all_called = False
                    elif action == "All in":
                        current_bet = amount
                        all_called = False
            for i in range(2, len(self.players)):
                if self.players[i].active and player_bets[players[i]] < current_bet:
                    all_called = False

        pots = sum(player_bets.values())
        print(f"Pot: {self.dealer.pot}")
        print("Pre-flop round ends")
        time.sleep(1)


        