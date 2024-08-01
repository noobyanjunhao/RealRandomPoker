class Table:
    def __init__(self):
        self.player = []
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        self.dealer = Dealer(self)
    
    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)
    
    
    
