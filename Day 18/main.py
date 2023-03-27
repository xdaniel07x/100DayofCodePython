from turtle import Turtle, Screen, colormode
import random


colormode(255)
timmy = Turtle()


# timmy.shape("turtle")
# timmy.color("red")

# #Draw Multiple Shapes

# for i in range(3, 11):
#     timmy.color(random.random(), random.random(), random.random())
#     for _ in range(i):
#         timmy.forward(100)
#         timmy.right(360/i)

timmy.speed("fastest")
timmy.shape("turtle")
timmy.pensize(2)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


for i in range(100):
    timmy.color(random_color())
    timmy.tiltangle(45)
    timmy.circle(90)
    timmy.left(10)


# def left_or_right():
#     direction = random.randint(0, 1)
#     if direction == 0:
#         return timmy.left(90)
#     else:
#         return timmy.right(90)


# timmy.pensize(10)
# timmy.speed("fastest")

# for i in range(100):
#     left_or_right()
#     timmy.color(random_color())
#     timmy.forward(50)


# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()


screen = Screen()
screen.exitonclick()
