from turtle import Turtle

FONT = ("Courier", 32, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.l_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.r_score}", align=ALIGNMENT, font=FONT)

    def inc_left(self):
        self.l_score += 1
        self.refresh()

    def inc_right(self):
        self.r_score += 1
        self.refresh()
