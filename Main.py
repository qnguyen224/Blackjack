from Player import Player
from BJ import game_start

Gambler = Player()
Dealer = Player()
ties = 0

if __name__ == "__main__":
    while True:
        result = game_start(Gambler.new_hand(), Dealer.new_hand())
        if result == 2:
            Gambler.win += 1
        elif result == 1:
            Dealer.win += 1
        else:
            ties += 1

        ans = input("Enter any key to play again or enter to quit: ")
        if ans:
            continue
        else:
            break

    print(f"\nDealer's wins: {Dealer.win}\nGambler's wins: {Gambler.win}\nTies : {ties}")