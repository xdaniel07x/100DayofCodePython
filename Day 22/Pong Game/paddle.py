from turtle import Turtle
UP = 90
DOWN = 270


class Paddle(Turtle):

    def __init__(self, x_cor, y_cor):
        super().__init__()
        self.create_paddle(x_cor, y_cor)

    def create_paddle(self, x_cor, y_cor):
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(x_cor, y_cor)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
