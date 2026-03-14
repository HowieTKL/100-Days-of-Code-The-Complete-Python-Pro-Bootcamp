import random
import art

print(art.logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def score(the_cards):
    result = 0
    aces = 0
    for card in the_cards:
        if card == 11:
            aces += 1
        else:
            result += card
    if aces > 0:
        if result < 11 - aces:
            result += 10 + aces
        else:
            result += aces
    return result

def play_blackjack():
    continue_playing = True
    while continue_playing:
        my_cards = []
        computer_cards = [random.choice(cards)]

        my_cards.append(random.choice(cards))
        my_cards.append(random.choice(cards))

        print(f"Computer cards: {computer_cards}")
        print(f"My cards: {my_cards}")

        still_playing = True
        my_score = 0
        while still_playing:
            get_card = input("Hit me (y/n) ")
            if get_card == "y":
                my_cards.append(random.choice(cards))
            else:
                still_playing = False
            print(f"My cards {my_cards} == {score(my_cards)}")
            my_score = score(my_cards)
            if my_score > 21:
                still_playing = False

        while score(computer_cards) < 16:
            computer_cards.append(random.choice(cards))

        print(f"Computer cards {computer_cards} == {score(computer_cards)}")
        computer_score = score(computer_cards)
        if my_score <= 21:
            if my_score > computer_score:
                print("You win!")
            elif score(my_cards) == computer_score:
                print("Draw!")
            elif computer_score > 21:
                print("You win!")
            else:
                print("You lose!")
        else:
            print("You lose!")

        cont = input("Continue playing? y/n ")
        if cont != "y":
            continue_playing = False

play_blackjack()