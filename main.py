from turtle import Turtle, Screen
import pandas as pd

data = pd.read_csv("Bangladesh_Div.csv")

tim = Turtle()
screen = Screen()
screen.setup(height=744,width=536)
screen.title("Welcome")
image = "question.gif"
screen.addshape(image)
tim.shape(image)

w = Turtle()
w.hideturtle()
i=0
write_title = "Welcome"

while True:
    user_input = screen.textinput(title=write_title,prompt="Write a District name").title()
    if user_input in data["state"].unique():
        i += 1
        write_title = f"{i}/8 is correct"
        name = data[data["state"] == user_input]
        print(name.x)
        index = name.index[0]
        w.teleport(name["x"][index], name["y"][index])
        w.write(user_input,font=("Arial", 14, "normal"))
    elif user_input == "Exit":
        image1 = "ans.gif"
        screen.addshape(image1)
        w.clear()
        tim.clear()
        tim.shape(image1)
        break

screen.mainloop()