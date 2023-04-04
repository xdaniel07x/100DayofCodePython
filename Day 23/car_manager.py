from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
X_COR = 320


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = 0.08

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_turtle = Turtle(shape="square")
            new_turtle.penup()
            new_turtle.color(COLORS[random.randint(0, 5)])
            new_turtle.shapesize(stretch_wid=1, stretch_len=2)
            new_turtle.setheading(180)
            y_cor = random.randint(-250, 250)
            new_turtle.goto(X_COR, y_cor)
            self.all_cars.append(new_turtle)

    def move_car(self):
        for car_num in self.all_cars:
            car_num.forward(STARTING_MOVE_DISTANCE)

    def increase_spead(self):
        self.car_speed -= 0.02
