
from deck import Deck
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
    def __init__(self, players, small_blind, big_blind, ante, buy_in):
        self.players = players
        self.dealer = Dealer(players)
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.ante = ante
        self.buy_in = buy_in
    
    # the order of the players is the indexing of the list of players, so when player enters the game, they can choose their positions
    # player when entering could choose which position they want to seat in the list of players

    def assign_dealer_button(self): 
        self.dealer.deck.shuffle()
        self.dealer.deal_hole_cards(1)
        # pick out who has the dealer button
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
        # Player action: fold, check, call, raise
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
                    return "call", current_bet
                else:
                    print("You don't have enough money to call")
            
            elif action == "raise":
                # Raise amount is restricted to be at least 2 times greater than the current bet
                raise_amount = int(input("Enter the raise amount:"))
                
                # Check if the player's stack can support the raise
                if raise_amount > player.stack:
                    print(f"You don't have enough chips to raise {raise_amount}. Your stack is {player.stack}.")
                elif raise_amount < 2 * current_bet:
                    print("Raise amount is too low")
                else:
                    additional_bet = raise_amount - player_bets[player]  # Only bet the additional amount
                    player.place_bet(additional_bet)
                    player_bets[player] += additional_bet
                    print(f"{player.name} raises: {raise_amount}")
                    return "raise", raise_amount  # The current bet is now the raise amount
            
            else:
                print("Invalid action")
        
        # If the player goes all-in because they have no more chips
        all_in_amount = player.stack
        player.place_bet(all_in_amount)
        player_bets[player] += all_in_amount
        print(f"{player.name} goes all in with: {all_in_amount}")
        return "All in", all_in_amount

    
    def handle_betting_round(self, starting_player_index):
        print("handle_betting_round is running")  # Debugging

        # Initialize current_bet to 0 (or the big blind for pre-flop rounds)
        current_bet = 0

        # Initialize player bets for the current round
        player_bets = {player: 0 for player in self.players}

        print(f"Initial pot after blinds: {self.dealer.pot}")  # Debugging

        # Circular betting sequence starting from a given player index
        all_called = False
        while not all_called:
            all_called = True  # Assume all have called or checked until proven otherwise

            for i in range(starting_player_index, len(self.players) + starting_player_index):
                index = i % len(self.players)
                player = self.players[index]
                print(f"Looping through player {player.name}")  # Debugging

                if not player.active:
                    print(f"{player.name} is not active, skipping.")  # Debugging
                    continue  # Skip inactive players

                # Check if the player has not yet placed a bet or if they need to match the current bet
                if player_bets[player] == 0 and current_bet == 0:
                    # The player can check (no bet has been placed yet)
                    print(f"{player.name} can check since current_bet is {current_bet}")
                    action, amount = self.check_player_action(player, current_bet, player_bets)
                elif player_bets[player] < current_bet:
                    print(f"Running check_player_action for {player.name}")  # Debugging
                    action, amount = self.check_player_action(player, current_bet, player_bets)

                # Calculate how much more the player needs to bet based on the current bet
                additional_bet = amount - player_bets[player]

                if additional_bet > 0:
                    # Deduct the additional bet from the player's stack
                    player.place_bet(additional_bet)

                    # Update the player's total bet and add the additional amount to the pot
                    player_bets[player] = amount  # Set the player's total bet to the full amount
                    self.dealer.pot += additional_bet

                    print(f"{player.name} places an additional bet of {additional_bet}, current bet: {player_bets[player]}")
                    print(f"Pot is now {self.dealer.pot}")

                if action == "raise" or action == "All in":
                    current_bet = amount  # Update current bet to the new raise amount
                    all_called = False  # Reset the loop to allow other players to respond to the raise

        return sum(player_bets.values())  # Return the total bets for the round

    def pre_flop_round(self):
        self.setup_table()
        self.assign_dealer_button()
        self.dealer.deal_hole_cards(2)
        for player in self.players:
            if player.active:
                player.check_hole_cards(2)
        self.dealer.collect_ante(self.ante)

        # Initial small blind and big blind
        self.players[0].place_bet(self.small_blind)
        self.players[1].place_bet(self.big_blind)
        self.dealer.pot += self.small_blind + self.big_blind

        # Handle the betting round starting from the player next to the big blind
        self.dealer.pot += self.handle_betting_round(2)  # Start betting from player next to big blind

        print(f"Pot: {self.dealer.pot}")
        print("Pre-flop round ends")
        time.sleep(1)

    def flop_round(self):
        # Deal the flop (three community cards)
        self.dealer.deal_flop(self.dealer.deck)
        print("Flop dealt:", [str(card) for card in self.dealer.community_cards])  # Fixed card display

        # Start a new betting round, this time starting from the small blind (player[1])
        starting_player_index = 1  # Small blind is always the first to act after the flop
        self.dealer.pot += self.handle_betting_round(starting_player_index)  # Start betting from the small blind
        
        print(f"Pot: {self.dealer.pot}")
        print("Flop round ends")
        time.sleep(1)

    def turn_round(self):
        # Deal the turn (one community card)
        self.dealer.deal_turn(self.dealer.deck)
        print("Turn dealt:", str(self.dealer.community_cards[-1]))  # Print the last (turn) card dealt
        
        # Start a new betting round starting from the small blind (player[1])
        starting_player_index = 1  # Small blind is always first to act after the flop
        self.dealer.pot += self.handle_betting_round(starting_player_index)  # Start betting from small blind
        
        print(f"Pot: {self.dealer.pot}")
        print("Turn round ends")
        time.sleep(1)

    def river_round(self):
        # Deal the river (one community card)
        self.dealer.deal_river(self.dealer.deck)
        print("River dealt:", str(self.dealer.community_cards[-1]))  # Print the last (river) card dealt
        
        # Start a new betting round starting from the small blind (player[1])
        starting_player_index = 1  # Small blind is always first to act after the flop
        self.dealer.pot += self.handle_betting_round(starting_player_index)  # Start betting from small blind
        
        print(f"Pot: {self.dealer.pot}")
        print("River round ends")
        time.sleep(1)

    def evaluate_hands_and_print_winner(self):
        evaluator = Evaluate()
        community_cards = self.dealer.community_cards
        active_players = [player for player in self.players if player.active]

        if not active_players:
            print("No active players left in the game.")
            return

        best_hands = {}

        # Evaluate the hand of each active player
        for player in active_players:
            best_hand = evaluator.evaluate(player, community_cards)
            best_hands[player] = best_hand
            print(f"{player.name}'s best hand is: {best_hand}")

        # Determine the winner(s)
        winning_hand_rank = max(evaluator.combination[best_hand] for best_hand in best_hands.values())
        winners = [player for player, hand in best_hands.items() if evaluator.combination[hand] == winning_hand_rank]

        if len(winners) == 1:
            print(f"The winner is {winners[0].name} with a {best_hands[winners[0]]}!")
        else:
            print(f"It's a tie between: {', '.join([winner.name for winner in winners])}. They all have a {best_hands[winners[0]]}.")
            