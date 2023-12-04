from turtle import Turtle
import random

CAR_COLORS = ["orange", "red", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DIST = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def generate_car(self):
        random_chance = random.randint(1, 7)
        if random_chance == 7:
            new_car = Turtle("square")
            new_car.color(random.choice(CAR_COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_len=2, stretch_wid=1)
            y_cor = random.randint(-250, 250)
            new_car.penup()
            new_car.goto(300, y_cor)
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.fd(STARTING_MOVE_DIST)
