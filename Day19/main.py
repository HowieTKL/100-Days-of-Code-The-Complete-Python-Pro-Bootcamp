import random
import turtle as t

colors = ["red", "orange", "yellow", "green", "blue", "purple"]
screen = t.Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make a bet", prompt="Color to win")
y_positions = [-70, -40, -10, 20, 50, 80]
is_race_on = False
turtles = []
t.speed("fastest")

for i in range(6):
    new_turtle = t.Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230, y=y_positions[i])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        rand_distance = random.randint(1, 10)
        turtle.forward(rand_distance)
        if turtle.xcor() > 230:
            is_race_on = False
            if user_bet == turtle.pencolor():
                print("You win!")
            else:
                print(f"You lose - {turtle.pencolor()} won.")

screen.exitonclick()