from random import choice
from BJ import deck


class Player:
    def __init__(self):
        self.hand = []
        self.win = 0

    def new_hand(self):
        self.hand.clear()
        self.hand += [choice(deck) for i in range(2)]
        return self.hand


if __name__ == "__main__":
    print("Hello World!")
