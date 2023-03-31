from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()

        self.refresh_score()

    def refresh_score(self):

        self.setposition(x=0, y=275)
        self.clear()
        self.write("Score: ", True, align="center",
                   font=("Arial", 20, "normal"))
