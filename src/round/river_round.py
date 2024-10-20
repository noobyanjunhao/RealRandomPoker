from round.base_round import Round

class RiverRound(Round):
    def __init__(self, game):
        super().__init__(game)

    def play(self):
        """River specific logic"""
        self.game.dealer.deal_river(self.game.dealer.deck)
        print("River dealt:", [str(card) for card in self.game.dealer.community_cards])

        # Handle the betting round starting from the player next to the dealer
        self.game.dealer.pot += self.handle_betting_round(Round.STARTING_PLAYER_INDEX)  # 1 is the small blind
        print(f"Pot: {self.game.dealer.pot}")
        print("River round ends")
