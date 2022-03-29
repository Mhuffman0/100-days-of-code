from turtle import Turtle

STARTING_SEGMENTS = 3
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.head = None
        self.create_snake()

    def create_snake(self):
        for segment in range(STARTING_SEGMENTS):
            init_position = (0, (-20 * len(self.segments)))
            self.add_segment(init_position)
        self.head = self.segments[0]

    def reset(self):
        for segment in self.segments:
            segment.reset()
        self.segments = []
        self.create_snake()

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.pu()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def check_overlap(self):
        is_not_overlapped = True
        for segment in self.segments[1:]:
            if is_not_overlapped:
                is_not_overlapped = segment.distance(self.head) > 5
        return is_not_overlapped

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_position = self.segments[i - 1].position()
            self.segments[i].setposition(new_position)
        self.head.forward(MOVE_DISTANCE)

    def set_direction(self, direction, opposite_direction):
        if self.head.heading() != opposite_direction:
            self.head.setheading(direction)

    def up(self):
        self.set_direction(UP, DOWN)

    def down(self):
        self.set_direction(DOWN, UP)

    def left(self):
        self.set_direction(LEFT, RIGHT)

    def right(self):
        self.set_direction(RIGHT, LEFT)
