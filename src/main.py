from model.dealer import Dealer
from model.card import Card
from model.deck import Deck
from model.player import Player

def main():
    #test for the function check hole cards
    player1 = Player(1, "Alice")
    player2 = Player(2, "Bob")
    players = [player1, player2]
    dealer = Dealer(players)
    dealer.deal_hole_cards(2)
    player1.check_hole_cards(2)
    player2.check_hole_cards(2)
    print(player1.hand)
    print(player2.hand)

    dealer.reset()
    print(dealer.community_cards)

    dealer.deal_hole_cards(2)
    player1.check_hole_cards(2)
    player2.check_hole_cards(2)
    
#run
if __name__ == "__main__":
    main()
