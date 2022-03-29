from turtle import Turtle

FONT = ("Arial", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("high_score.txt", "r") as file:
                self.high_score = int(file.read())
        except FileNotFoundError:
            self.high_score = 0
        self.ht()
        self.pu()
        self.color("white")
        self.write_score()

    def write_score(self):
        self.clear()
        self.goto(0, 265)
        self.write(
            f"Score: {self.score} High-Score: {self.high_score}",
            font=FONT,
            align=ALIGNMENT,
        )

    def increment_score(self):
        self.score += 1
        self.write_score()


    def reset(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))
        self.write_score()