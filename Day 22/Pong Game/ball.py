from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_xcor = 10
        self.move_ycor = 10

    def move_ball(self):
        new_x = self.xcor() + self.move_xcor
        new_y = self.ycor() + self.move_ycor
        self.goto(new_x, new_y)

    def bounce(self):
        self.move_ycor *= -1

    def bounce2(self):
        self.move_ycor *= 1
