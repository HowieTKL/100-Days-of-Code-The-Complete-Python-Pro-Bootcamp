import sys
import time
import turtle as t
import snake as s
import food as f
import scoreboard as sb

screen = t.Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = s.Snake()

def done():
    global is_game_on
    is_game_on = False

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")
screen.onkey(done, "q")


is_game_on = True
food = f.Food()
score = sb.Scoreboard()
while is_game_on:
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.inc()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset()
        snake.reset()

    segments = snake.segments[1:]
    for segment in segments:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()

    screen.update()
    time.sleep(0.1)
