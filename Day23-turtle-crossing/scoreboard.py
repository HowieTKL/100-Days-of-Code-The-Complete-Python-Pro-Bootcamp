from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"Level {self.level}", align=ALIGNMENT, font=FONT)

    def inc(self):
        self.level += 1
        self.refresh()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
