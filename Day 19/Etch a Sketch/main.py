from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(20)


def move_backwards():
    tim.back(20)


def counter_clockwise():
    tim.left(10)


def clockwise():
    tim.right(10)


def clear():
    tim.reset()


screen.listen()
screen.onkeypress(key="w", fun=move_forwards)
screen.onkeypress(key="s", fun=move_backwards)
screen.onkeypress(key="a", fun=counter_clockwise)
screen.onkeypress(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
