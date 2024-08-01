class Table: 
    """
    to start a game, you have to have a table where there is dealer, players.
    Also, the table keeps tack of the community card and the pot
    """
    def __init__(self):
        self.player = []
        self.dealer = Dealer(self)
        self.community_cards = []
        self.pot = 0
        self.current_bet = 0
        
    
    def add_player(self, player):
        self.players.append(player)
    
    def remove_player(self, player):
        self.players.remove(player)

    def reset_table(self):
        self.community_cards = []
        self.current_bet = 0
        for player in self.players:
            player.hand = []


    
