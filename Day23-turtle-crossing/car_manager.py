import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.move_speed = 0.1
        self.cars = []
        for i in range(5):
            car = Car()
            self.cars.append(car)

    def randomize_cars(self):
        for car in self.cars:
            car.new_random_position()

    def move_cars(self):
        for car in self.cars:
            car.fd(MOVE_INCREMENT)
            if car.xcor() < -300:
                car.setx(300)

    def increase_level(self):
        self.move_speed *= 0.9
        car = Car()
        self.cars.append(car)
        self.randomize_cars()

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.penup()
        self.new_random_position()
        self.setheading(180)

    def new_random_position(self):
        self.goto(random.randrange(-280, 250), random.randrange(-200, 250))
