import time
import turtle as t
import scoreboard as sb
import paddle as p
import ball as b

screen = t.Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("My Pong Game")
screen.tracer(0)

left_paddle = p.Paddle((-350, 0))
right_paddle = p.Paddle((350, 0))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

ball = b.Ball()
scoreboard = sb.Scoreboard()

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed())
    screen.update()

    ball.move()
    ball.check_paddle_collision(left_paddle)
    ball.check_paddle_collision(right_paddle)
    ball.check_goal(scoreboard)


screen.exitonclick()