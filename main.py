from turtle import Screen
import time
from player import Player
from scoreboard import Scoreboard
from car_manager import CarManager


screen = Screen()
screen.setup(height=600, width=600)
screen.tracer(0)
screen.bgcolor("black")


player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")

game_is_on = True
game_speed = 0.1

while game_is_on:
    time.sleep(game_speed)
    screen.update()
    car_manager.move()
    car_manager.generate_car()

    if player.ycor() == 280:
        player.reset_player()
        scoreboard.increase_level()
        game_speed *= 0.9

    for car in car_manager.all_cars:
        if car.distance(player) < 30:
            scoreboard.game_over()
            game_is_on = False

screen.exitonclick()
