from Player import Player
from BJ import game_start

Gambler = Player()
Dealer = Player()

if __name__ == "__main__":
    while True:
        result = game_start(Gambler.new_hand(), Dealer.new_hand())
        if result:
            Gambler.win += 1
        else:
            Dealer.win += 1

        ans = input("Enter any key to play again or enter to quit: ")
        if ans:
            continue
        else:
            break

    print(f"Gambler's wins: {Gambler.win}")
    print(f"Dealer's wins: {Dealer.win}")
