from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.tilt(90)
        self.penup()
        self.reset_position()
        self.y_move = MOVE_DISTANCE
        self.x_move = MOVE_DISTANCE

    def reset_position(self):
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
        
    def move_up(self):
        x_cor = self.xcor()
        new_y = self.ycor() + self.y_move
        self.tiltangle(90)
        self.goto(x_cor, new_y)

    def move_down(self):
        x_cor = self.xcor()
        new_y = self.ycor() - self.y_move
        self.tiltangle(270)
        self.goto(x_cor, new_y)

    def move_left(self):
        x_cor = self.xcor() - self.x_move
        new_y = self.ycor() 
        self.tiltangle(180)
        self.goto(x_cor, new_y)

    def move_right(self):
        x_cor = self.xcor() + self.x_move
        new_y = self.ycor() 
        self.tiltangle(0)
        self.goto(x_cor, new_y)