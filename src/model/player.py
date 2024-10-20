class Player:
    def __init__ (self, player_id, name, stack = 1000):
        self.id = player_id
        self.name = name
        self.hand = []
        self.stack = stack
        self.emoji = None
        self.active = True #if the player is still in the game
    
    def receive_card(self, card):
        self.hand.append(card)
    
    def check_hole_cards(self, num_card):
        #print the first num_card cards in the hand in string format
        print(f"{self.name}'s hole cards: {[str(card) for card in self.hand[:num_card]]}")
    
    def send_emoji(self, emoji): #need front end 
        pass
    
    def place_bet(self, amount):
        self.stack -= amount
        return amount
    
    def fold(self):
        self.active = False
        self.hand = []

    def __eq__(self, other):
        if isinstance(other, Player):
            return (self.id == other.id and
                    self.name == other.name and
                    self.stack == other.stack)
        return False
    
    def __hash__(self):
        return hash(self.id)
    
    def __str__(self):
        return self.name + " with stack " + str(self.stack) + " with hand" + str(self.hand)
    