import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

pos = turtle.Turtle()
pos.pu()
pos.ht()


class Game:
    def __init__(self, states):
        self.state_dict = {}
        for state in states:
            self.state_dict[state] = False
        self.title = None
        self.prompt = "Name a state:"
        self.update_title()

    def return_states(self, state_filter=None):
        if state_filter is None:
            return [state for state in self.state_dict]
        else:
            return [
                state
                for state in self.state_dict
                if self.state_dict[state] == state_filter
            ]

    def update_title(self):
        self.title = (
            f"{len(self.return_states(True))}/"
            f"{len(self.return_states())} States Correct"
        )


with open("50_states.csv") as file:
    data = pandas.read_csv(file)
    game = Game(data.state.tolist())

while len(game.return_states(True)) < len(game.return_states()):
    try:
        guess = turtle.textinput(title=game.title, prompt=game.prompt).title()
        if guess in game.return_states() and guess not in game.return_states(True):
            state = data.loc[data["state"] == guess]
            pos.goto(state.x.item(), state.y.item())
            pos.write(guess)
            game.state_dict[guess] = True
            game.update_title()
    except AttributeError:
        with open("states_to_learn.csv", "w") as file:
            file.write("\n".join(game.return_states(False)))
        break
