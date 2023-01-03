from player import Player


class Game:

    def __init__(self):
        self.player_1 = Player()
        self.player_2 = Player()
        self.round = 0
        self.whose_turn = 1

    def setup(self):
        print("Placing ships for Player 1...")
        self.player_1.place_ships()
        print(self.player_1.knowledge)

        print("Placing ships for Player 2...")
        self.player_2.place_ships()
        print(self.player_2.knowledge)

    def play(self):
        while not self.player_1.is_defeated() and not self.player_2.is_defeated():
            print(f"\t\t\t||| TURN {self.round} |||")
            if self.whose_turn == 1:
                self.whose_turn = 2
                print("Player 1 guessing...")

                guess = self.player_1.guess()

                if self.player_2.is_hit(guess):
                    self.player_1.record_hit(guess, True)
                else:
                    self.player_1.record_hit(guess, False)
            else:
                self.whose_turn = 1
                print("Player 2 guessing...")
                guess = self.player_2.guess()
                if self.player_1.is_hit(guess):
                    self.player_2.record_hit(guess, True)
                else:
                    self.player_2.record_hit(guess, False)
            self.round += 1

            print("Status of Player 1...")
            print(self.player_1.knowledge)
            print("Status of Player 2...")
            print(self.player_2.knowledge)

        return self.whose_turn