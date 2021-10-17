# Memory Game

# [01] [02] [03] [04]
# [05] [06] [07] [08]
# [09] [10] [11] [12]
# [13] [14] [15] [16]

# 1 - is the user out of guesses?
#   - if guesses are not = 0
#       - pick a card
#           - if card has been picked, print "card has already been chosen, pick another card"
#           - else: continue
# 2 - pick another card
#   - if card has been picked, print "card has already been chosen, pick another card"
#   - else: continue
#   - does card #1 match card #2
#       - if cards match 
#           - print "cards match" and reveal cards by changing strings on board
#       - if cards don't match
#           - print "cards don't match"
#           - subtract number of guesses left


# dictionary of key = card #, value = letter
#   - print dictionary as strings that change on board
# number of guesses
# class of events
# class of interactions

import os
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

class Card():

    def __init__(self, name):
        self.name = name

class CardEvents():

    def __init__(self, cards_hidden_numbers, cards_revealed_letters, guesses):
        self.cards_hidden_numbers = ["[01]"]
        self.cards_revealed_letters = ["[_A]"]
        self.guesses = 10

    def guess_card_1(self, cards):
        # reveal card #1
        pass

    def guess_card_2(self, cards):
        # reveal card #2 and compare to card #1
        pass

    def guess_wrong(self, guesses):
        # subtract guess
        pass

    def no_more_guesses(self, guesses):
        # end game
        pass

    def replay(self):
        # restart game
        pass

    def print_current_board(self, cards_hidden_numbers):
        # print board
        print(self.cards_hidden_numbers)
        pass




class CardInteractions():
    pass
    