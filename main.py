import pandas
import turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
turtle.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
data_states = data.state.to_list()

points = 0
while points < 50:
    answer_state = screen.textinput(f"States correct: {points}/50", "What's another state's name?").title()
    for states in data_states:
        if answer_state == "exit":
            break
        if answer_state == states:
            points += 1
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            coor = data[data.state == answer_state]
            t.goto(int(coor.x), int(coor.y))
            t.write(states)







turtle.mainloop()
