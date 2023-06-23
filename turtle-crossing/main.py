import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()


screen.listen()
screen.onkey(player.move, "Up")

cars_list = []

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car = CarManager()
    cars_list.append(car)
    for car in cars_list:
        car.increase_distance()


