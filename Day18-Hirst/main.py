import random
import turtle as t

color_list = [(207, 160, 83), (54, 89, 131), (145, 91, 40), (139, 27, 48), (222, 206, 108), (132, 177, 203), (157, 46, 83), (46, 55, 103), (168, 159, 40), (128, 188, 143), (83, 20, 44), (37, 43, 68), (186, 93, 106), (185, 139, 172), (84, 123, 181), (59, 39, 31), (79, 153, 165), (88, 156, 91), (194, 79, 72), (45, 74, 77), (161, 201, 220), (80, 73, 44), (62, 127, 120), (219, 175, 186), (168, 206, 169), (221, 181, 167), (178, 188, 212), (47, 74, 73), (148, 37, 35), (44, 64, 63)]

t.colormode(255)
t.speed('fastest')
t.hideturtle()

t.penup()
t.lt(180)
t.fd(250)
t.lt(90)
t.fd(250)
t.lt(90)
for x in range(10):
    for y in range(10):
        t.dot(20, random.choice(color_list))
        t.penup()
        t.fd(50)
        t.pendown()
    t.penup()
    t.lt(90)
    t.fd(50)
    t.lt(90)
    t.fd(500)
    t.lt(180)
    t.pendown()

screen = t.Screen()
screen.exitonclick()