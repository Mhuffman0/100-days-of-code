from turtle import Turtle
from scoreboard import ScoreBoard
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.pu()
        self.ran_direction()
        self.forward(10)
        self.refresh_speed = .1

    def ran_direction(self):
        ne_heading = random.randint(0, 45)
        nw_heading = random.randint(135, 180)
        sw_heading = random.randint(180, 225)
        se_heading = random.randint(315, 360)
        rand_heading = [ne_heading, nw_heading, sw_heading, se_heading]
        self.setheading(random.choice(rand_heading))
        self.refresh_speed = .1

    def score(self):
        self.goto(0, 0)
        self.ran_direction()

    def bounce_y(self):
        if (180 > self.heading() > 0 and self.ycor() > 0) or (
            self.heading() > 180 and self.ycor() < 0
        ):
            self.setheading(random.randint(355, 360) - self.heading())

    def bounce_x(self):
        if (self.xcor() > 0 and (self.heading() > 270 or self.heading() < 90)) or (
            self.xcor() < 0 and 270 > self.heading() > 90
        ):
            self.setheading(random.randint(175, 180) - self.heading())
        self.refresh_speed = self.refresh_speed * .9
