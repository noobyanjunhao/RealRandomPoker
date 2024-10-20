from round.base_round import Round

class FlopRound(Round):
    def __init__(self, game):
        super().__init__(game)

    def play(self):
        # Deal the flop (three community cards)
        self.game.dealer.deal_flop(self.game.dealer.deck)
        print(f"Flop dealt: {[str(card) for card in self.game.dealer.community_cards]}")

        # Handle betting round starting with small blind
        self.game.dealer.pot += self.handle_betting_round(Round.STARTING_PLAYER_INDEX)  # 1 is the small blind
        
        print(f"Pot: {self.game.dealer.pot}")
        print("Flop round ends")