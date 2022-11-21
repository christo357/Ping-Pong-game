from turtle import Turtle
import random as rm

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.speed("slow")
        self.penup()


        self.x = 10
        self.y = 10

    def create_ball(self):
        self.color("white")
        self.shape("circle")
        self.speed("slow")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def refresh_l(self):
        self.goto(0, 0)
        self.x = 10
        self.y = 10

    def refresh_r(self):
        self.goto(0, 0)
        self.x = -10
        self.y = -10

    def hori_collide(self):
        self.y = self.y*-1

    def verti_collide(self):
        self.x = self.x*-1


        
    # def move_lu(self):
    #     new_x = self.xcor() - x
    #     new_y = self.ycor() + y
    #     self.goto(new_x, new_y)
    #
    # def move_rd(self):
    #     new_x = self.xcor() + x
    #     new_y = self.ycor() - y
    #     self.goto(new_x, new_y)
    #
    # def move_ld(self):
    #     new_x = self.xcor() - x
    #     new_y = self.ycor() - y
    #     self.goto(new_x, new_y)

    # def clock_angle(self):
    #     if self.tiltangle() < 90:
    #         angle = 180 - self.tiltangle()
    #     elif self.tiltangle() < 180:
    #         angle = 360 - self.tiltangle()
    #     elif self.tiltangle() < 270:
    #         angle = 540 - self.tiltangle()
    #     else:
    #         angle = 360 - self.tiltangle()
    #     self.settiltangle(angle)
    #
    # def aclock_angle(self):
    #     if self.tiltangle() < 90:
    #         angle = 360 - self.tiltangle()
    #     elif self.tiltangle() < 180:
    #         angle = 180 - self.tiltangle()
    #     elif self.tiltangle() < 270:
    #         angle = 360 - self.tiltangle()
    #     else:
    #         angle =