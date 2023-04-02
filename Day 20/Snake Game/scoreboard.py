from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_board()

    def score_board(self):
        self.setposition(x=0, y=275)
        self.clear()
        self.write(f"Score: {self.score}", True, align="center",
                   font=("Arial", 20, "normal"))

    def refresh_score(self):
        self.score += 1
        self.setposition(x=0, y=275)
        self.clear()
        self.write(f"Score: {self.score}", True, align="center",
                   font=("Arial", 20, "normal"))
