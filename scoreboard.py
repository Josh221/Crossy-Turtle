from turtle import Turtle

FONT = ("Courier", 20, "bold")
ALIGNMENT = "left"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.Score = 0

    def update_scoreboard(self):
        self.clear()
        self.goto(-290, 260)
        self.write("Level: " + str(self.Score), align=ALIGNMENT, font=FONT)

    def add_point(self):
        self.Score += 1
        self.update_scoreboard()