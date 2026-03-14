import random
import art

print(art.logo)

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def number_guessing_game():
    the_random_number = random.randint(1, 100)
    difficulty = input("Choose a difficulty: (E)asy or (H)ard ").lower()
    attempts = EASY_ATTEMPTS
    if difficulty == "h":
        attempts = HARD_ATTEMPTS
    while attempts > 0:
        print(f"You have {attempts} attempts")
        guess = int(input("Guess number "))
        if guess < the_random_number:
            print("Too low")
        elif guess > the_random_number:
            print("Too high")
        else:
            print("You guessed correctly")
            return
        attempts -= 1

    print(f"You lose - the number is {the_random_number}")

number_guessing_game()