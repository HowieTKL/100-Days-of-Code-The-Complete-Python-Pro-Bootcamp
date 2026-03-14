from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        self.fd(MOVE_DISTANCE)

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def has_crossed_finish(self):
        return self.ycor() > FINISH_LINE_Y

    def collision(self, car_manager):
        for car in car_manager.cars:
            if car.distance(self) < 20:
                return True
        return False
