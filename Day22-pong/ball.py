from turtle import Turtle

MOVE_DISTANCE = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed("fastest")
        self.x_move = MOVE_DISTANCE
        self.y_move = MOVE_DISTANCE
        self.speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        if new_y > 280 or new_y < -280:
            self.bounce_off_wall()
        self.goto(new_x, new_y)

    def bounce_off_wall(self):
        self.y_move *= -1

    def bounce_off_paddle(self):
        self.x_move *= -1
        self.speed *= 0.9

    def check_paddle_collision(self, paddle):
        if paddle.distance(self) < 20 or (paddle.distance(self) < 50 and
                                          (self.xcor() > 320 or self.xcor() < -320)):
            self.bounce_off_paddle()

    def check_goal(self, scoreboard):
        if self.xcor() > 380:
            scoreboard.inc_left()
            self.reset_ball()
        elif self.xcor() < -380:
            scoreboard.inc_right()
            self.reset_ball()

    def reset_ball(self):
        self.goto(0, 0)
        self.x_move *= -1

    def move_speed(self):
        return self.speed
