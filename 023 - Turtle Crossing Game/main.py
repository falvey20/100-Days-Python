import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# Create objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Screen listen for user keystroke
screen.listen()
screen.onkey(player.go_up, "Up")


game_over = False
while not game_over:
    # Update screen ever 0.1
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_over = True
            scoreboard.game_over()

    # Detect player reaching other side
    if player.is_at_finish_line():
        player.go_to_start()
        scoreboard.increase_score()
        car_manager.speed_up()

screen.exitonclick()
