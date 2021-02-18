from random import choice
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'K', 'Q', 'J', 'A']


def convert_suit(hand):
    """Takes input list, converts face cards into int values, and returns the list"""
    ace_count = True
    for i in range(len(hand)):
        if hand[i] in ('K', 'Q', 'J'):
            hand[i] = 10
        if hand[i] == 'A' and ace_count:
            hand[i] = 11
            ace_count = False
        elif hand[i] == 'A':
            hand[i] = 1
    return hand


def count_total(hand):
    """Takes input converted list, returns total value of the hand"""
    total = 0
    for cards in hand:
        total += cards
    return total


def convert_ace(hand):
    """Converts all the aces in hand to 1"""
    hand = convert_suit(hand)
    for i in range(len(hand)):
        if hand[i] == 11:
            hand[i] = 1
    return hand


def game_start(gambler, dealer):
    g_copy = gambler[:]  # Convert suits in Gambler's hand
    d_copy = dealer[:]   # Convert suits in Dealer's hand
    g_total = count_total(convert_suit(g_copy))   # Gambler's total
    d_total = count_total(convert_suit(d_copy))   # Dealer's total

    # if total is <= 21 and there's an Ace in hand, it is a soft number
    gambler_soft = True
    dealer_soft = True

    print(f"The dealer's hand is [X, {dealer[1]}]")

    while True:
        if d_total == 21 and 'A' in dealer and 'A' not in gambler:
            break
        print(f"Your cards are: {gambler} with a value of {g_total}")
        ans = input("Do you wish to Draw or Stand D/S: ")
        if ans.upper() == 'D':
            gambler.append(choice(deck))     # appends a random card to gambler's hand
            g_copy.append(gambler[-1])  # appends the last index of p2 to p2_converted
            if g_total >= 11 and g_copy[-1] == 'A':
                g_copy[-1] = 1

            if gambler[-1] == 'A' and not gambler_soft:
                g_copy[-1] = 1
                g_total = count_total(convert_suit(g_copy))
            else:
                g_total = count_total(convert_suit(g_copy))  # calculates total value of gambler's hand

            if g_total > 21 and 'A' in gambler and gambler_soft:
                g_total = count_total(convert_ace(g_copy))
                gambler_soft = False
            elif g_total > 21:
                break
        else:
            if d_total >= 17:           # dealer stands on soft 17 or greater
                break
            else:
                while d_total < 17:     # dealer continues to draw until bust or >= 17
                    dealer.append(choice(deck))
                    d_copy.append(dealer[-1])
                    if d_total >= 11 and d_copy[-1] == 'A':
                        d_copy[-1] = 1
                    if dealer[-1] == 'A' and not dealer_soft:
                        d_copy[-1] = 1
                        d_total = count_total(convert_suit(d_copy))
                    else:
                        d_total = count_total(convert_suit(d_copy))
                    if d_total > 21 and 'A' in dealer and dealer_soft:
                        d_total = count_total(convert_ace(d_copy))
                        dealer_soft = False
            break

    print(f"The dealer's hand is {dealer} with a total of {d_total}")
    print(f"The gambler's hand is {gambler} with a total of {g_total}")

    if d_total < g_total <= 21 or d_total > 21:
        print("Gambler won!")
        return 2
    elif g_total < d_total or g_total > 21:
        print("Gambler lost")
        return 1
    else:
        print("It's a push")
        return 0
