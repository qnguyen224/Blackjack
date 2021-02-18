from random import choice
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A']


def convert_suit(hand):
    """Takes input list, converts face cards into int values, and returns the list"""
    ace_count = 0
    for i in range(len(hand)):
        if hand[i] in ('K', 'Q', 'J'):
            hand[i] = 10
        if hand[i] == 'A' and not ace_count:
            hand[i] = 11
            ace_count += 1
        elif ace_count and hand[i] == 'A':
            hand[i] = 1
    return hand


def count_total(hand):
    """Takes input converted list, returns total value of the hand"""
    total = 0
    for cards in hand:
        total += cards
    return total


def game_start(gambler, dealer):
    g_converted = convert_suit(gambler[:])  # Convert suits in Gambler's hand
    d_converted = convert_suit(dealer[:])   # Convert suits in Dealer's hand
    g_total = count_total(g_converted)    # Gambler's total
    d_total = count_total(d_converted)    # Dealer's total

    print(f"The dealer's hand is [X, {dealer[1]}]")

    while True:
        if d_total == 21 and 'A' in dealer and 'A' not in gambler:
            break
        print(f"Your cards are: {gambler} with a value of {g_total}")
        ans = input("Do you wish to Draw or Stand D/S: ")
        if ans.upper() == 'D':
            gambler.append(choice(deck))     # appends a random card to gambler's hand
            g_converted.append(gambler[-1])  # appends the last index of p2 to p2_converted
            g_total = count_total(convert_suit(g_converted))  # calculates total value of gambler's hand
            if g_total > 21:
                break
        else:
            if d_total >= 17:           # dealer stands on 17 or greater
                break
            else:
                while d_total < 17:     # dealer continues to draw until bust or >= 17
                    dealer.append(choice(deck))
                    d_converted.append(dealer[-1])
                    d_total = count_total(convert_suit(d_converted))
            break

    print(f"The dealer's hand is {dealer} with a total of {d_total}")
    print(f"The gambler's hand is {gambler} with a total of {g_total}")

    if d_total < g_total <= 21 or d_total > 21:
        print("Gambler won!")
        return 1
    elif g_total < d_total or g_total > 21:
        print("Gambler lost")
        return 0
    else:
        print("It's a push")
