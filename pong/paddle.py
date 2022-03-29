from turtle import Turtle

PADDLE_HEIGHT = 100
UP = 20
DOWN = -20


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_HEIGHT / 20, stretch_len=1)
        self.pu()
        self.goto(side, 0)

    def move(self, direction):
        new_y = self.ycor() + direction
        self.goto(self.xcor(), y=new_y)

    def go_up(self):
        if self.ycor() < 240:
            self.move(UP)

    def go_down(self):
        if self.ycor() > -240:
            self.move(DOWN)
