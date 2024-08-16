from functools import cmp_to_key
from itertools import combinations
from collections import defaultdict

from card import Card
from player import Player

class Evaluate:
    combination = {
        'High Card': 0,
        'One Pair': 1,
        'Two Pair': 2,
        'Three of a Kind': 3,
        'Straight': 4,
        'Flush': 5,
        'Full House': 6,
        'Four of a Kind': 7,
        'Straight Flush': 8,
        'Royal Straight': 9
    }

    def __init__(self):
        pass

    @staticmethod
    def compare_card(card1, card2):
        # Compare based on card value first
        if card1.value() < card2.value():
            return -1
        elif card1.value() > card2.value():
            return 1
        else:
            return 0

    def evaluate(self, player, community_cards):
        all_combinations = list(combinations(player.hand + community_cards, 5))
        best_hand = None

        for five_cards in all_combinations:
            current_hand = self.check_pattern(five_cards)
            if best_hand is None or self.combination[current_hand] > self.combination[best_hand]:
                best_hand = current_hand
                print(f"Player: {player.name}")
                print(f"Best hand: {best_hand}")
                print(f"Current hand: {current_hand}")

        return best_hand

    def check_pattern(self, five_cards): # Return the highest hand detected as a string, e.g., 'Full House'
        key_function = cmp_to_key(self.compare_card)
        five_cards = sorted(five_cards, key=key_function)
        
        # check for "Pair", "Two Pair", "Three of a Kind", "Full House", "Four of a Kind"
        value_counts = defaultdict(int)
        for card in five_cards:
            value_counts[card.value()] += 1
        pair_count = 0
        three_of_a_kind = False
        four_of_a_kind = False

        for count in value_counts.values():
            if count == 4:
                four_of_a_kind = True
            elif count == 3:
                three_of_a_kind = True
            elif count == 2:
                pair_count += 1
                
        if four_of_a_kind:
            return "Four of a Kind"
        elif three_of_a_kind and pair_count > 0:
            return "Full House"
        elif three_of_a_kind:
            return "Three of a Kind"
        elif pair_count == 2:
            return "Two Pair"
        elif pair_count == 1:
            return "One Pair"
        
        # check for "Straight", "Flush", "Straight Flush", "Royal Straight"
        if five_cards[4].value() == five_cards[3].value() + 1 and \
            five_cards[3].value() == five_cards[2].value() + 1 and \
            five_cards[2].value() == five_cards[1].value() + 1 and \
            five_cards[1].value() == five_cards[0].value() + 1:
            if five_cards[4].rank == "A":
                return "Royal Straight"
            if five_cards[0].suit == five_cards[1].suit == five_cards[2].suit \
                == five_cards[3].suit == five_cards[4].suit:
                return "Straight Flush"
            return "Straight"
        
        return "High Card"

    def compare(self, player1, player2, community_cards):
        # player1 and player2 would have a hand property which is a list of Card objects
        # community_cards would be a list of Card objects 
        best_hand_p1 = self.evaluate(player1, community_cards)
        best_hand_p2 = self.evaluate(player2, community_cards)

        if self.combination[best_hand_p1] > self.combination[best_hand_p2]:
            return "Player 1 wins"
        elif self.combination[best_hand_p1] < self.combination[best_hand_p2]:
            return "Player 2 wins"
        else:
            return "Tie"
        

# To test the function of Evaluate class
# if __name__ == "__main__":
#     # Create an instance of Evaluate
#     evaluator = Evaluate()
    
#     # Create mock players and community cards
#     yjh = Player(0, "yjh")
#     yjh.receive_card(Card("2", "Diamonds"))
#     yjh.receive_card(Card("3", "Clubs"))
#     mom = Player(1, "mom")
#     mom.receive_card(Card("4", "Hearts"))
#     mom.receive_card(Card("5", "Spades"))
#     community_cards = [Card("4", 'Hearts'), Card("5", 'Diamonds'), Card("6", 'Spades'), Card("Q", 'Clubs'), Card("J", 'Hearts')]
    
#     # Test the evaluate method
#     best_hand = evaluator.evaluate(mom, community_cards)
#     print(f"Best hand: {best_hand}")
    
#     # Test the compare method
#     comparison_result = evaluator.compare(yjh, mom, community_cards)
#     print(f"Comparison result: {comparison_result}")

