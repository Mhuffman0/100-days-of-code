from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)

screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while True:
    try:
        screen.update()
        snake.move()
        time.sleep(0.1)
        if snake.head.distance(food) < 15:
            food.change_postion()
            scoreboard.increment_score()
            snake.extend()
        if (
            abs(snake.head.xcor()) > WIDTH / 2
            or abs(snake.head.ycor()) > HEIGHT / 2
            or not snake.check_overlap()
        ):
            scoreboard.reset()
            snake.reset()
    except:
        print("Game is over!")
        break
