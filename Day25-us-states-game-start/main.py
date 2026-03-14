import turtle as t
import pandas
import state_label as sl

screen = t.Screen()
screen.title("US States Game")
img = "blank_states_img.gif"
screen.addshape(img)
t.shape(img)

# def mouse_click_coord(x, y):
#     print(x, y)
# t.onscreenclick(mouse_click_coord)

states = pandas.read_csv("50_states.csv")
guessed = []
while len(guessed) < len(states):
    answer_state = screen.textinput(f"{len(guessed)}/{len(states)} states",
                                    "Guess a state").title()
    if (answer_state == "Exit"):
        break
    location = states[states.state == answer_state]
    if not location.empty:
        state_name = location.state.item()
        if not state_name in guessed:
            guessed.append(state_name)
            sl.StateLabel(state_name, (location.x.item(), location.y.item()))

# states to learn
states_to_learn = [s for s in states.state.tolist() if s not in guessed]
print(states_to_learn)
states_to_learn_data = pandas.DataFrame(states_to_learn)
states_to_learn_data.to_csv("states_to_learn.csv")

if len(guessed) == len(states):
    print("You guessed them all!!")
