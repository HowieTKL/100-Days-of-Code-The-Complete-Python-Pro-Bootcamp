import time
from turtle import Screen
import car_manager as cm
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_up, "w")

car_manager = cm.CarManager()
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()

    car_manager.move_cars()

    if player.collision(car_manager):
        scoreboard.game_over()
        game_is_on = False

    if player.has_crossed_finish():
        car_manager.increase_level()
        scoreboard.inc()
        player.reset_position()

screen.exitonclick()
