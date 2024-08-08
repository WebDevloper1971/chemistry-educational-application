import turtle
from tkinter import PhotoImage
from turtle import Turtle, Screen, Shape
import pandas as pd

screen = Screen()
screen.setup(1000, 700)

# substitute 'subsample' for 'zoom' if you want to go smaller:
smaller = PhotoImage(file="periodic_table.gif").subsample(3, 3)

screen.addshape("smaller", Shape("image", smaller))

tortoise = Turtle("smaller")
tortoise.stamp()
tortoise.hideturtle()

df = pd.read_csv("periodic_table_elements.csv")
symbol_list = df["Symbol of the Element"].to_list()
# print(symbol_list)
study_list = []
user_list = []

end_game = False

while not end_game:
    try:
        user_input = turtle.textinput(title="Periodic Elements", prompt="Enter Symbols Of Periodic Elements").title()
        # print(user_input)
        if user_input == "Exit":
            for symbol in symbol_list:
                if symbol not in user_list:
                    study_list.append(symbol)

            break
        if user_input in symbol_list:
            symbol_turtle = Turtle()
            symbol_turtle.hideturtle()
            symbol_turtle.penup()
            x_coordinate = df[df["Symbol of the Element"] == user_input].x.item()
            y_coordinate = df[df["Symbol of the Element"] == user_input].y.item()
            symbol_turtle.goto(x_coordinate, y_coordinate)
            symbol_turtle.write(user_input, align="center", font=("Courier", 12, "bold"))
            user_list.append(user_input)

    except Exception as e:
        print(e)
        break


study_df = df[~df["Symbol of the Element"].isin(user_list)]

# study_csv = study_df.to_csv("Periodic_Elements_To_Study.csv")
