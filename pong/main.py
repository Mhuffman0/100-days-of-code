from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

LEFT = -350
RIGHT = 350

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)

left_paddle = Paddle(LEFT)
right_paddle = Paddle(RIGHT)
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")

while scoreboard.game_continue:
    time.sleep(ball.refresh_speed)
    screen.update()
    ball.forward(10)

    if ball.xcor() > 360:
        scoreboard.increment_l_score()
        ball.score()

    if ball.xcor() < -360:
        scoreboard.increment_r_score()
        ball.score()

    if abs(ball.ycor()) > 280:
        ball.bounce_y()

    if (
        abs(ball.xcor()) > 330
        and min(ball.distance(right_paddle), ball.distance(left_paddle)) < 55
    ):
        ball.bounce_x()

screen.exitonclick()
