from game import Game
import matplotlib.pyplot as mpt

def main():

    turns = []

    for x in range(100):
        new_game = Game()
        new_game.setup()
        new_game.play()
        print(f"Game completed in {new_game.round} rounds")
        turns.append(new_game.round)

    mpt.scatter(range(100), turns)
    mpt.title("Turns to complete for 100 games")
    mpt.xlabel("Game number")
    mpt.ylabel("Turns to complete game")
    mpt.show()

if __name__ == '__main__':
    main()