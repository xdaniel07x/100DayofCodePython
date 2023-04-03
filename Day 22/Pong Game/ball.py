from turtle import Turtle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_xcor = 10
        self.move_ycor = 10
        self.ball_speed = 0.05

    def move(self):
        new_x = self.xcor() + self.move_xcor
        new_y = self.ycor() + self.move_ycor
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.move_ycor *= -1

    def bounce_x(self):
        self.move_xcor *= -1
        self.ball_speed -= 0.005

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
