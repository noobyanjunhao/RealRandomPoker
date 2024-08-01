class Player:
    def __init__ (self, player_id, name, stack = 1000):
        self.id = player_id
        self.name = name
        self.hand = []
        self.stack = stack
        self.emoji = None
    
    def receive_card(self, card):
        self.hand.append(card)
    
    def send_emoji(self, emoji): #need front end 
        self.emoji = emoji