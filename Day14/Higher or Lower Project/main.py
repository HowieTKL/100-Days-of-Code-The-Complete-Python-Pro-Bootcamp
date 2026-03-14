import random
from os import name

import art
import game_data

print(art.logo)

def check_guess(guess, entry_a, entry_b):
    if guess == "a":
        if entry_a["follower_count"] >= entry_b["follower_count"]:
            return True
    elif guess == "b":
        if entry_b["follower_count"] >= entry_a["follower_count"]:
            return True
    return False


entry_a = random.choice(game_data.data)
is_playing = True
score = 0
while is_playing:
    entry_b = random.choice(game_data.data)
    print(f"Score: {score}")
    print(f"A. {entry_a['name']} {entry_a['follower_count']}")
    print(art.vs)
    print(f"B. {entry_b['name']} {entry_b['follower_count']}")
    guess = input("A or B ").lower()
    if (check_guess(guess, entry_a, entry_b)):
        print("Correct")
        entry_a = entry_b
        score += 1
    else:
        print("Incorrect")
        is_playing = False
