import turtle
from turtle import Turtle, Screen, write
import pandas as pd

t = Turtle()
screen = Screen()


screen.addshape("./blank_states_img.gif")
turtle.shape("./blank_states_img.gif")


d = pd.read_csv("50_states.csv")
df = pd.DataFrame(d)

correct_answer = 0
while correct_answer < len(df["state"]):
    answer_state = screen.textinput(title="Guess the State", prompt="What is another state's name? :")
    if answer_state in df["state"].tolist():
        x = int(df[df["state"] == f"{answer_state}"]["x"])
        y = int(df[df["state"] == f"{answer_state}"]["y"])
        print(f"{x},{y}")
        state = Turtle()
        state.penup()
        state.goto(x, y)
        state.write(f"{answer_state }")
        state.hideturtle()






screen.mainloop()