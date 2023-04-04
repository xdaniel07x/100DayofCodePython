import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(car.car_speed)
    screen.update()

    car.create_car()
    car.move_car()

    for player_model in car.all_cars[0:]:
        if player.distance(player_model) < 25:
            scoreboard.game_over()
            game_is_on = False

    # Detect if player has reached the end
    if player.ycor() >= 280:
        player.reset_position()
        scoreboard.update_level()
        car.increase_spead()

screen.exitonclick()
