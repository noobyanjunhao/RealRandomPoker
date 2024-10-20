from round.pre_flop_round import PreFlopRound
from round.flop_round import FlopRound
from round.turn_round import TurnRound
from round.river_round import RiverRound
from model.dealer import Dealer
from model.deck import Deck
from model.evaluator import Evaluator

class Game:
    def __init__(self, players, small_blind, big_blind, ante, buy_in):
        self.players = players
        self.dealer = Dealer(players)
        self.small_blind = small_blind
        self.big_blind = big_blind
        self.ante = ante
        self.buy_in = buy_in
        self.current_bet = 0

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
    
    def play_game(self):
        # Play each round using Round objects
        pre_flop = PreFlopRound(self)
        pre_flop.play()

        flop = FlopRound(self)
        flop.play()
        self.inspect_players("flop")

        turn = TurnRound(self)
        turn.play()
        self.inspect_players("turn")

        river = RiverRound(self)
        river.play()
        self.inspect_players("river")

        # Evaluate hands and determine the winner
        self.evaluate_hands_and_print_winner()
    
    def inspect_players(self, round):
        print(f"Inspecting players at the end of the {round} round")
        for player in self.players:
            print(f"{player.name} has {player.stack} chips")

    def evaluate_hands_and_print_winner(self):
        evaluator = Evaluator()
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
