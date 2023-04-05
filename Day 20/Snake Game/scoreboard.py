from turtle import Turtle
ALIGN = "center"
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        with open("Day 20/Snake Game/data.txt") as file:
            high = file.read()
            self.high_score = int(high)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.score_board()

    def score_board(self):
        self.setposition(x=0, y=270)
        self.clear()
        self.write(
            f"Score: {self.score} High score: {self.high_score}",  align=ALIGN, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.setposition(x=0, y=270)
        self.clear()
        self.write(f"Score: {self.score} High score: {self.high_score}", align=ALIGN,
                   font=FONT)

    def reset(self):
        if self.score > self.high_score:
            with open("Day 20/Snake Game/data.txt", mode="w") as file:
                self.high_score = self.score
                file.write(f"{self.high_score}")
        self.score = 0
        self.score_board()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)
