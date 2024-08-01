class Dealer: #deal and collect bet
    def __init__(self, table):
        self.table = table

    def deal_cards(self, num_cards): #pre-flop
        for player in self.table.players:
            for _ in range(num_cards):
                card = self.table.deck.deal(1)[0]
                player.recieve_card(card)
    
    def deal_flop(self, deck):
        self.community_cards.extend(deck.deal(3))
    
    def deal_turn(self, deck):
        self.community_cards.append(deck.deal(1)[0])
    
    def deal_river(self, deck):
        self.community_cards.append(deck.deal(1)[0])
    
    def collect_bet(self):
        total_bet = 0
        for player in self.table.players:
            if player.stack > 0:
                bet_amount = player.decide_bet_amount()
                try:
                    bet = player.place_bet(bet_amount)
                    total_bet += bet
                    # the bet amount is user dependent
                except ValueError as e:
                    print(f"{player.name}:{e}")
        self.table.pot += total_bet
    
    def distribute_pot(self, winner):
        

    