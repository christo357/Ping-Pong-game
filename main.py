from turtle import Turtle,Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time

TIME = .05

ball = Ball()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
l_score = Score((-100, 230))
r_score = Score((100, 230))
screen.update()

screen.listen()

screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")

game_is_on = True
while game_is_on:
    ball.move()
    time.sleep(TIME)

    # collide at top and bottom wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.hori_collide()

    # collide the paddle
    if ball.xcor() > 350 and ball.distance(r_paddle) < 50 or ball.xcor() < -350 and ball.distance(l_paddle) < 50:
        ball.verti_collide()
        TIME *= .9

    #right paddle misses
    if ball.xcor()>380:
        ball.verti_collide()
        l_score.add_score()
        ball.refresh_r()
        TIME =.05

    #left paddle misses
    if ball.xcor()<-380:
        ball.verti_collide()
        r_score.add_score()
        ball.refresh_l()
        TIME =.05

    screen.update()




































screen.exitonclick()