from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Ariel", 25, "normal")

class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.points=0
        self.hideturtle()
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.goto(position)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(self.points, False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.points += 1
        self.update_score()