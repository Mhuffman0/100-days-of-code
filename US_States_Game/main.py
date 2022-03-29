import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")

turtle.shape("blank_states_img.gif")

guess = turtle.textinput(title="State Guesser 9000", prompt="Name a state!:")

class State:
    def __init__(self, name, x_cor, y_cor, visible=False):
        self.name = name
        self.x_cor = x_cor
        self.y_cor = y_cor
        self.visible = visible
        state_list.append(self)


state_list = []

with open("50_states.csv") as file:
    data = pandas.read_csv(file)
    print(data["state"])
#        State(row["state"], row.x, row.y)

# print(state_list)

# turtle.exitonclick()
