import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Crossy Turtle")
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")

game_is_on = True
count = 0

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.drive()

    #Detect collision with car.
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False

    #Detect successful crossing:
    if player.is_at_finish_line():
        player.reset_position()
        scoreboard.add_point()
        car_manager.increase_speed()
        
screen.exitonclick()
    
