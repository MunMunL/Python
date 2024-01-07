import time
import turtle
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Turtle Crosser")

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.generate_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.car_group:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False


    # Detect player reaches top, reset player, level up car speed, increase score
    if player.ycor() > 300:
        player.reset()
        car_manager.reset()
        scoreboard.level_up()


screen.exitonclick()