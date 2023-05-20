import random

print("Welcome to Quinn's Blackjack Table.")

# vars
player_money = 1000.00
won = 1
bet = 0.0
game_over = False
loss = False
jack = "Jack"
queen = "Queen"
king = "King"
ace = "Ace"
cards = [ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, jack, queen, king]
player_hand = [cards[random.randint(0, 12)]]
player_secret_hand = [player_hand[0]]


def reset_hand():
    global player_secret_hand
    global player_hand
    global loss
    player_hand = [cards[random.randint(0, 12)]]
    player_secret_hand = [player_hand[0]]
    loss = False


def face_check():
    faces_removed = False
    while not faces_removed:
        if jack in player_secret_hand:
            player_secret_hand.remove(jack)
            player_secret_hand.append(10)
        if queen in player_secret_hand:
            player_secret_hand.remove(queen)
            player_secret_hand.append(10)
        if king in player_secret_hand:
            player_secret_hand.remove(king)
            player_secret_hand.append(10)
        if jack not in player_secret_hand:
            if queen not in player_secret_hand:
                if king not in player_secret_hand:
                    faces_removed = True


def ace_check():
    aces_removed = False
    while not aces_removed:
        if ace in player_secret_hand:
            player_secret_hand.remove(ace)
            player_secret_hand.append(1)
        if ace not in player_secret_hand:
            aces_removed = True


def ace_higher_check():
    aces_left = True
    while aces_left:
        if 1 in player_secret_hand and sum(player_secret_hand) <= 11:
            player_secret_hand.remove(1)
            player_secret_hand.append(11)
        if 1 not in player_secret_hand or sum(player_secret_hand) >= 12:
            aces_left = False


def ace_lower_check():
    aces_left = True
    while aces_left:
        if 11 in player_secret_hand and sum(player_secret_hand) >= 22:
            player_secret_hand.remove(11)
            player_secret_hand.append(1)
        if 11 not in player_secret_hand or sum(player_secret_hand) >= 22:
            aces_left = False


def check_loss():
    if sum(player_secret_hand) >= 22:
        return True


def draw():
    player_secret_hand.append(cards[random.randint(0, 12)])
    player_hand.append(player_secret_hand[-1])
    face_check()
    ace_check()
    ace_higher_check()
    ace_lower_check()
    print(player_hand)
    print(sum(player_secret_hand))


def player_turn():
    global bet
    global game_over
    global player_money

    allowed = False
    drawn = False

    while not allowed:

        if not drawn:
            draw()
            drawn = True

        print("Hit = H")
        print("Stand = S")
        print("Double down = DD")
        print("Split = SP")
        print("Insurance = I")

        drawyn = input("What would you like to do? ")

        if drawyn == "H":
            draw()

        elif drawyn == "DD":
            player_money = player_money - bet
            bet = bet + bet

            draw()

            print("your hand was at " + str(sum(player_secret_hand)))

            allowed = True
            not_answered = True

            while not_answered:
                over = input("Would you like to stop playing? ")

                if over == "yes":
                    game_over = True
                    not_answered = False

                elif over == "no":
                    drawn = False
                    not_answered = False
                    if sum(player_secret_hand) <= 21:
                        reset_hand()
                        return True

                    elif sum(player_secret_hand) >= 22:
                        reset_hand()
                        return False

                else:
                    print("Input not accepted use yes or no")

        elif drawyn == "S":
            print("your hand was at " + str(sum(player_secret_hand)))

            allowed = True
            not_answered = True

            while not_answered:
                over = input("Would you like to stop playing? ")

                if over == "yes":
                    game_over = True
                    not_answered = False

                elif over == "no":
                    drawn = False
                    not_answered = False
                    if sum(player_secret_hand) <= 21:
                        reset_hand()
                        return True

                    elif sum(player_secret_hand) >= 22:
                        reset_hand()
                        return False

                else:
                    print("Input not accepted use yes or no")

        elif not drawyn == "H" or not drawyn == "S":
            print("Input not accepted")


while not game_over:

    print("You have " + str(player_money) + " dollars. ")

    bet_accepted = False

    while not bet_accepted:
        bet = input("How much would you like to bet? ")

        if bet.isnumeric():
            bet = float(bet)
            player_money = player_money - bet
            bet_accepted = True

        else:
            print("Use numbers for your bet")

    if player_turn():
        bet = (bet * 2)
        player_money = (player_money + bet)

    else:
        bet = (bet * 0)
