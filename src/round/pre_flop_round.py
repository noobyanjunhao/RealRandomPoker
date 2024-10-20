from round.base_round import Round

class PreFlopRound(Round):
    def __init__(self, game):
        super().__init__(game)

    def play(self):
        """Pre-flop specific logic"""
        self.game.setup_table()
        self.game.assign_dealer_button()
        self.game.dealer.deal_hole_cards(2)

        for player in self.game.players:
            if player.active:
                player.check_hole_cards(2)
        self.game.dealer.collect_ante(self.game.ante)

        # Initial small blind and big blind
        self.game.players[0].place_bet(self.game.small_blind)
        self.game.players[1].place_bet(self.game.big_blind)
        self.game.dealer.pot += self.game.small_blind + self.game.big_blind

        # Handle the betting round starting from the player next to the big blind
        self.game.dealer.pot += self.handle_betting_round(2)

        print(f"Pot: {self.game.dealer.pot}")
        print("Pre-flop round ends")
