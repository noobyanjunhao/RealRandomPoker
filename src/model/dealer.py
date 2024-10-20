from model.deck import Deck

class Dealer: #deal and collect bet
    def __init__(self, players):
        self.community_cards = [] 
        self.deck = Deck()
        self.deck.shuffle()
        self.players = players
        self.pot = 0

    def deal_hole_cards(self, num_cards = 2): #pre-flop
        for player in self.players:
            for _ in range(num_cards):
                card = self.deck.deal(1)[0]
                player.receive_card(card)
    
    def deal_flop(self, deck):
        self.community_cards.extend(deck.deal(3))
    
    def deal_turn(self, deck):
        self.community_cards.append(deck.deal(1)[0])
    
    def deal_river(self, deck):
        self.community_cards.append(deck.deal(1)[0])
        
    def collect_ante(self, ante):
        for player in self.players:
            player.place_bet(ante)
            self.pot += ante
        print (f"Pot: {self.pot}")
    
    def reset(self):
        self.pot = 0
        self.community_cards = []
        self.deck = Deck()
        self.deck.shuffle()