from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle(-350, 0)
r_paddle = Paddle(350, 0)

# screen.tracer(True)
ball = Ball()


screen.listen()
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")
screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move_ball()

    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce()

    if ball.distance(r_paddle) < 10:
        ball.bounce_2()

screen.exitonclick()
