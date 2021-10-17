import random   #randomly sorts through cards
import os
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

# Show Instructions
# Show My Playboard
# Ask for guess 1
# Ask for guess 2
# Reveal tiles
# Check if they match and they haven't been guessed correctly
#   and it 's not the same card
#   - if match, then show the matches on the gameboard
#   - if no match, then I'll add one to my wrong answer
# Check for win or lose conditions
# Continue until all the matches have been found or the user
#   runs out of turns

class GameBoard():

    LETTERS = ["A","B","C","D","E","F","G","H"] * 2
    MAX_GUESSES = 7

    def __init__(self):
        random.shuffle(GameBoard.LETTERS)
        self.letters = GameBoard.LETTERS
        self.correct_indices = []
        self.board = []
        self.number_of_guesses = 0

    def make_game_board(self):
        game_board = []
        for index, letter in enumerate(self.letters, start=1):
            if index in self.correct_indices:
                if index % 4 == 0:
                    game_board.append(f"[ {letter}]\n")
                else:
                    game_board.append(f"[  {letter}]")
            else:
                if index % 4 == 0:
                    game_board.append(f"[{str(index).zfill(2)}]\n")
                else:
                    game_board.append(f"[{str(index).zfill(2)}]")
        return game_board

    def show_game_board(self):
        self.board = self.make_gameboard()
        for letter in self.board:
            print(letter, end = "")

    def is_valid_guess(self, guess):
        if 0 < guess < len(self.letters) + 1 and guess not in self.correct_indices:
            return True
        return False

    def show_card(self, index):
        return self.letters[index-1]

    def make_guess(self, index1, index2):
        if self.letters[index1-1] == self.letters[index2-1]:
            self.correct_indices.append(index1)
            self.correct_indices.append(index2)
            return True

    def is_game_over(self):
        if self.number_of_guesses == GameBoard.MAX_GUESSES:
            # player lost
            return 2
        elif len(self.correct_indices) == len(self.board):
            return 1 # player won
        else:
            return 0

class UI():
    game = GameBoard()

    @classmethod
    def play_game(cls):
        print("""
        Welcome to the Memory Game!
        Pick a tile to reveal what is underneath.
        Pick a second tile that matches the first tile.
        You win if you match all the tiles.
        You only get 7 wrong matches.
        """)
        input("Press ENTER to continue...")
        while True:
            clear_screen()
            print("""
            ======================
            |     Memory Game    |
            ======================
            """)
            cls.game.show_game_board()
            print()
            guess1 = 99999
            guess2 = 99999
            while not cls.game.is_valid_guess(guess1):
                guess1 = int(input("What is your first choice? "))
                if cls.game.is_valid_guess(guess1):
                    print("You found " + cls.game.show_card(guess1))
                else:
                    print("Invalid Guess, Try Again!")
            while not cls.game.is_valid_guess(guess2) or guess1 == guess2:
                guess2 = int(input("What is your first choice? "))
                if cls.game.is_valid_guess(guess2):
                    print("You found " + cls.game.show_card(guess2))
                else:
                    print("Invalid Guess, Try Again!")
            if cls.game.make_guess(guess1, guess2):
                print("You made a match! ")
            else:
                print("You did not make a match! ")
            if cls.is_game_over() == 1:
                print("Congrats, you win! ")
            elif cls.is_game_over() == 2:
                print("You ran out of guesses. ")
            else:
                input("Press ENTER to continue... ")

    @classmethod
    def main(cls): #cls for class method, like self
        cls.play_game()

if __name__ == "__main__": # if i am accessing this file by this name and that name is equal to name
    UI.main()