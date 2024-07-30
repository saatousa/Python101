import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from  scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = ScoreBoard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with cars
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

    # Detect successful crossing
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        score_board.increase_level()

screen.exitonclick()
