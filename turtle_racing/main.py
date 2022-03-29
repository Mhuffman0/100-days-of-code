import turtle
import random

is_race_on = False
screen = turtle.Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="Place your bets!", prompt="Which turtle will win the race?"
)
if user_bet:
    is_race_on = True
color_list = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "violet",
]


turtle_list = []
i = 0
for turtle_index in range(6):
    turtle_racer = turtle.Turtle(shape="turtle")
    turtle_racer.color(color_list[i])
    turtle_racer.pu()
    turtle_racer.goto(-230, -100 + (i * 30))
    turtle_list.append(turtle_racer)
    i += 1

while is_race_on:
    for turtle in turtle_list:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 230:
            winning_color = turtle.pencolor()
            is_race_on = False

print(f"{winning_color.capitalize()} wins!")
if winning_color == user_bet.lower():
    print("You won!")
screen.exitonclick()
