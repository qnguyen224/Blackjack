from random import choice

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A']


class Player:
    def __init__(self):
        self.hand = []
        self.win = 0

    def new_hand(self):
        self.hand.clear()
        self.hand += [choice(deck) for i in range(2)]
        return self.hand


def convert_suit(hand):
    """Takes input list, converts face cards into int values, and returns the list"""
    for i in range(len(hand)):
        if hand[i] in ('K', 'Q', 'J'):
            hand[i] = 10
        if hand[i] == 'A':
            hand[i] = 11
    return hand


def count_total(hand):
    """Takes input list, returns total value of the hand"""
    total = 0
    for cards in hand:
        total += cards
    return total


def game_start(gambler, dealer):
    g_converted = convert_suit(gambler[:])  # Player's hand converted
    d_converted = convert_suit(dealer[:])  # Dealer's hand converted
    g_total = count_total(convert_suit(g_converted))
    d_total = count_total(convert_suit(d_converted))

    print(f"The dealer's hand is [X, {dealer[1]}]")

    while True:
        print(f"Your cards are: {gambler} with a value of {count_total(g_converted)}")
        ans = input("Do you wish to Draw or Stand D/S: ")
        if ans.upper() == 'D':
            gambler.append(choice(deck))     # appends a random card to gambler's hand
            g_converted.append(gambler[-1])  # appends the last index of p2 to p2_converted
            g_total = count_total(convert_suit(g_converted))  # calculates total value of gambler's hand
            if g_total > 21:
                print(f"\nWhoops, your hand went over 21")
                break
        else:
            if d_total >= 17:           # dealer stands on 17 or greater
                break
            else:
                while d_total < 17:     # dealer continues until bust or >= 17
                    dealer.append(choice(deck))
                    d_converted.append(dealer[-1])
                    d_total = count_total(convert_suit(d_converted))
            break

    print(f"The dealer's hand is {dealer} with a total of {d_total}")
    print(f"The gambler's hand is {gambler} with a total of {g_total}")

    if d_total < g_total <= 21 or d_total > 21:
        print("Gambler won!")
        Gambler.win += 1
    elif g_total < d_total or g_total > 21:
        print("Gambler lost")
        Dealer.win += 1

    # restart the game
    play_again = input("Do you wish to play again? Y/N ")
    game_start(Gambler.new_hand(), Dealer.new_hand()) if play_again.upper() == 'Y' else print("Thanks for playing!")


Gambler = Player()
Dealer = Player()

game_start(Gambler.new_hand(), Dealer.new_hand())
print(f"Total number of Gambler's wins: {Gambler.win}")
print(f"Total number of Dealer's wins: {Dealer.win}")
