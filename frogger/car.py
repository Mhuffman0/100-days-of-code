import random
from turtle import Turtle

MOVE_INCREMENT = 10


class Car(Turtle):
    def __init__(self, color=None):
        super(Car, self).__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.pu()
        if color:
            self.color(color)
        self.setheading(180)
        self.movement_speed = 1
        self.starting_position()

    def starting_position(self, x_pos=300):
        self.goto(x_pos, random.randint(-250, 250))
        self.movement_speed = self.movement_speed * random.choice([0.75, 1, 1.25])

    def move(self) -> None:
        self.forward(MOVE_INCREMENT * self.movement_speed)
        if self.xcor() < -320:
            self.starting_position(600)
