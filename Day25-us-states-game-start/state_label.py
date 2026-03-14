from turtle import Turtle

FONT = ("Arial", 12, "normal")
ALIGNMENT = "center"

class StateLabel(Turtle):
    def __init__(self, label, pos):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(pos)
        self.write(arg=label, align=ALIGNMENT, font=FONT)
