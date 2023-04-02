from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_board()

    def score_board(self):
        self.setposition(x=0, y=270)
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.setposition(x=0, y=270)
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGN,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
