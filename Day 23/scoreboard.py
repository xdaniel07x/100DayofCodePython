from turtle import Turtle
LEVEL_FONT = ("Courier", 20, "bold")
LEVEL_ALIGN = "left"
GAME_OVER_FONT = ("Courier", 24, "normal")
GAME_OVER_ALIGN = "center"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.score_board()

    def score_board(self):
        self.setposition(x=-295, y=265)
        self.clear()
        self.write(f"Level: {self.level}", align=LEVEL_ALIGN, font=LEVEL_FONT)

    def update_level(self):
        self.level += 1
        self.score_board()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=GAME_OVER_ALIGN, font=GAME_OVER_FONT)
