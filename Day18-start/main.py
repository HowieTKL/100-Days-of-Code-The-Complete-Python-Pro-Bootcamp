import random
import turtle
from turtle import Turtle, Screen


timmy = Turtle()
timmy.shape("turtle")

# timmy.fd(100)
# timmy.right(90)
# timmy.fd(100)
# timmy.right(90)
# timmy.fd(100)
# timmy.right(90)
# timmy.fd(100)

# for _ in range(10):
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()
#     timmy.fd(10)

def calc_angle(sides):
    return 360 / sides

def draw_shape(sides):
    r = random.random()
    g = random.random()
    b = random.random()
    timmy.pencolor((r, g, b))
    angle = calc_angle(sides)
    for i in range(sides):
        timmy.fd(100)
        timmy.rt(angle)

# for i in range(3, 11):
#    draw_shape(i)


def random_color():
    turtle.colormode(255)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    timmy.pencolor((r, g, b))

def random_direction():
    choice = random.randint(0, 3)
    return choice * 90

def random_walk():
    timmy.width(10)
    timmy.speed("fastest")
    for _ in range(100):
        random_color()
        angle = random_direction()
        timmy.right(angle)
        timmy.forward(20)

def draw_circles():
    timmy.speed("fastest")
    circles = 75
    angle = 360 / circles
    for _ in range(circles):
        random_color()
        timmy.circle(100)
        timmy.setheading(timmy.heading() + angle)



screen = Screen()
screen.exitonclick()
