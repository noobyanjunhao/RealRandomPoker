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

    def decide_bet_amount(self):
        #front end part should be responsible for handling or excluding value error
        amount = int(input(f"{self.name}, enter your bet amount (1 - {self.stack}): "))
    def place_bet(self, amount):
        if amount > self.stack:
            raise ValueError("Bet amount exceeds player's stack")
        self.stack -= amount
        return amount
    