import turtle
from turtle import Turtle, Screen
import pandas


FONT = ('Arial', 8, 'normal')

screen = Screen()
screen.title("U.S. States Game")
screen.addshape("blank_states_img.gif")
screen.setup(width=725, height=491)
turtle.shape("blank_states_img.gif")


def take_cor(state_answered):
    state_data = data[data.state == state_answered]
    x_cor = int(state_data.x)
    y_cor = int(state_data.y)
    return x_cor, y_cor


def write_name(state_answered, cors):
    t = Turtle()
    t.hideturtle()
    t.penup()
    t.goto(cors)
    t.write(state_answered)


data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_num = 0
guessed_states = []
while guess_num != 50:
    answer_state = turtle.textinput(f"{guess_num}/50 State Correct", "What's another state name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        # missing_states = []
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_states.append(state)

        df = pandas.DataFrame(missing_states)
        df.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states and answer_state not in guessed_states:
        coordinates = take_cor(answer_state)
        write_name(answer_state, coordinates)
        guessed_states.append(answer_state)
        guess_num += 1


screen.exitonclick()
