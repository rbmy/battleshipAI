import random

from knowledge import Knowledge
from reasoning import Reasoning


class Player:
    def __init__(self):
        self.knowledge = Knowledge()
        self.reasoning = Reasoning()

    def guess(self) -> tuple:
        guess_coordinates = self.random_coordinates()

        while not self.knowledge.player_shots_board[guess_coordinates[0]][guess_coordinates[1]] == "_":
            guess_coordinates = self.random_coordinates()

        print(f"Is {guess_coordinates} a hit?")
        return guess_coordinates

    def is_hit(self, coordinates: tuple) -> bool:
        hit = self.knowledge.player_board[coordinates[0]][coordinates[1]] in ["b", "r", "s", "c", "d"]

        if hit:
            self.knowledge.update_ships_status(coordinates)

        return hit

    def record_hit(self, coordinate:tuple, is_hit: bool):
        symbol = "G"

        if is_hit:
            symbol = "X"

        self.knowledge.player_shots_board[coordinate[0]][coordinate[1]] = symbol
        print("Player's Shots so far:")
        print(self.knowledge.__str__(True))

    def place_ships(self):
        for ship in self.knowledge.ship_names:
            coordinates, is_vertical = self.find_empty_space_and_orientation(ship)
            print(f"Placing ship {ship} at coordinates {coordinates}, is vertical: {bool(is_vertical)}")
            self.place_ship(ship, coordinates, is_vertical)


    def place_ship(self, ship_name: str, coordinates: tuple, is_vertical: bool):
        if is_vertical:
            for row in range(coordinates[0], self.knowledge.ship_sizes[ship_name] + coordinates[0]):
                self.knowledge.player_board[row][coordinates[1]] =  self.knowledge.ship_symbols[ship_name]
        else:
            for column in range(coordinates[1], self.knowledge.ship_sizes[ship_name] + coordinates[1]):
                self.knowledge.player_board[coordinates[0]][column] = self.knowledge.ship_symbols[ship_name]

    def find_empty_space_and_orientation(self, ship_name) -> tuple:
        coordinates = self.random_coordinates()
        is_vertical = random.randint(0, 1)

        while not self.can_fit(ship_name, coordinates, is_vertical):
            coordinates = self.random_coordinates()
            is_vertical = random.randint(0, 1)

        return coordinates, is_vertical

    def can_fit(self, ship_name, coordinates, is_vertical) -> bool:
        ## coordinate refers to starting tip of ship

        if coordinates[1] + self.knowledge.ship_sizes[ship_name] >= 10 or \
                coordinates[0] + self.knowledge.ship_sizes[ship_name] >= 10 or \
                self.knowledge.player_board[coordinates[0]][coordinates[1]] in ["b", "r", "s", "c", "d"]:
            return False

        if self.knowledge.player_board[coordinates[0]][coordinates[1]] == "_":
            if is_vertical:
                for row in range(coordinates[0], self.knowledge.ship_sizes[ship_name] + coordinates[0]):
                    if not self.knowledge.player_board[row][coordinates[1]] == "_" or \
                            self.knowledge.player_board[row][coordinates[1]] in ["b", "r", "s", "c", "d"]:
                        return False
            else:
                for column in range(coordinates[1], self.knowledge.ship_sizes[ship_name] + coordinates[1]):
                    if not self.knowledge.player_board[coordinates[0]][column] == "_" or \
                            self.knowledge.player_board[coordinates[0]][column] in ["b", "r", "s", "c", "d"]:
                        return False

        return True

    def is_defeated(self) -> bool:
        for ship in self.knowledge.ships_destroyed:
            if not self.knowledge.ships_destroyed[ship]:
                return False
        return True

    def random_coordinates(self) -> tuple:
        return random.randint(0, 9), random.randint(0, 9)