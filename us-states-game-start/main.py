
import pandas as pd
import turtle

with open("50_states.csv") as data_file:
    df = pd.read_csv(data_file)

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.addshape(image)
background = turtle.Turtle(shape=image)
df["guess"] = 0
pen = turtle.Turtle()
pen.pu()

while True:
    guess_summ = sum(list(df["guess"]))
    answer_state = screen.textinput(title=f"{guess_summ}/50 Guess the state", prompt="What is the next state?")
    if answer_state is None:
        break

    if answer_state.title() in list(df.state):
        current_row = df[df.state == answer_state.title()].index[0]
        current_x = df.at[current_row, "x"]
        current_y = df.at[current_row, "y"]
        df.at[current_row, "guess"] = 1
        pen.goto(current_x, current_y)
        pen.write(answer_state.title(), align="center")
        pen.goto(0, 0)

df[df.guess == 0].to_csv("missed_states.csv")
