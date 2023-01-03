class Knowledge:
    def __init__(self):
        self.player_board = [["_"]*10 for x in range(10)]
        self.player_shots_board = [["_"]*10 for x in range(10)]
        self.ship_names = ["carrier", "battleship", "cruiser", "submarine", "destroyer"]
        self.ship_symbols = {"carrier": "c", "battleship": "b", "cruiser": "r", "submarine": "s", "destroyer": "d"}
        self.ship_sizes = {"carrier": 5, "battleship": 4, "cruiser": 3, "submarine": 3, "destroyer": 2}
        self.ships_destroyed = {"carrier": False, "battleship": False, "cruiser": False, "submarine": False, "destroyer": False}

    def update_ships_status(self, coordinates: tuple):
        self.player_board[coordinates[0]][coordinates[1]] = "*"

        print("--- Ship Status ---")
        for ship in self.ship_names:
            ship_hits_remaining = 0
            for row in range(0,10):
                for column in range(0,10):
                    if self.player_board[row][column] == self.ship_symbols[ship]:
                        ship_hits_remaining += 1
            if ship_hits_remaining == 0:
                print(f"\tYou sank my {ship}!")
                self.ships_destroyed[ship] = True


    def __str__(self, opponent_board:bool = False):
        board_str = ""

        if not opponent_board:
            board_str = "\t\t\t-- Player Board --\n\t0  1   2   3   4   5   6   7   8   9\n"
            for row in range(10):
                board_str += f"{row}\t"
                for column in range(10):
                    board_str += self.player_board[row][column] + "\t"
                board_str += "|\n"
            board_str += "\t-  -   -   -   -   -   -   -   -   -\n"
        else:
            board_str = "\t\t\t-- Player's Shots Board --\n\t0  1   2   3   4   5   6   7   8   9\n"
            for row in range(10):
                board_str += f"{row}\t"
                for column in range(10):
                    board_str += self.player_shots_board[row][column] + "\t"
                board_str += "|\n"
            board_str += "\t-  -   -   -   -   -   -   -   -   -\n"

        return board_str
