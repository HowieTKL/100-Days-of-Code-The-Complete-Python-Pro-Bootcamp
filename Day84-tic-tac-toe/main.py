LOCATIONS="""
123
456
789"""
print(LOCATIONS)
game = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
    7: "",
    8: "",
    9: ""
    }

def is_available(location):
    return game[location] == ""

def print_grid():
    print()
    for i in game.keys():
        if game[i] == "":
            print('.', end="")
        else:
            print(game[i], end="")
        if i % 3 == 0:
            print()
    print()

def game_has_winner():
    return ((game[1] == game[2] == game[3] != "") or
            (game[4] == game[5] == game[6] != "") or
            (game[7] == game[8] == game[9] != "") or
            (game[1] == game[5] == game[9] != "") or
            (game[1] == game[4] == game[7] != "") or
            (game[2] == game[5] == game[8] != "") or
            (game[3] == game[6] == game[9] != "") or
            (game[3] == game[5] == game[7] != ""))

def game_tie():
    return game[1] != "" and game[2] != "" and game[3] != "" and game[4] != "" and game[5] != "" and game[6] != "" and game[7] != "" and game[8] != "" and game[9] != ""

print_grid()
while True:
    location_o = 0
    while not(1 <= location_o <= 9 and is_available(location_o)):
        location_o = int(input("'O': "))
    game[location_o] = "O"
    print_grid()
    if game_has_winner():
        print("Winner is 'O'!")
        break
    elif game_tie():
        print("Tie!")
        break
    else:
        location_x = 0
        while not(1 <= location_x <= 9 and is_available(location_x)):
            location_x = int(input("'X': "))
        game[location_x] = "X"
        print_grid()
        if game_has_winner():
            print("Winner is 'X'!")
            break
