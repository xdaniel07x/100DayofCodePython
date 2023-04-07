from turtle import Turtle, Screen
import pandas

TOTAL_STATES = 50
FONT = ("Courier", 6, "bold")
INCORRECT_FONT = ("Courier", 20, "bold")
ALIGN = "center"

turtle = Turtle()
screen = Screen()

screen = Screen()
screen.title("U.S. States Game")
image = "Day 25/US States Game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = Turtle()
writer.penup()
writer.hideturtle()

data = pandas.read_csv("Day 25/US States Game/50_states.csv")

state_list = data.state.to_list()
correct_guess_list = []
game_is_on = True
cont_game = True
num_correct = 0

answer_state = screen.textinput(
    title=f"{num_correct}/{TOTAL_STATES} States Correct", prompt="What's another state's name?").capitalize()

while game_is_on:

    cont_game = True

    for state in state_list:
        if answer_state == state:
            get_state = data[data.state == f"{answer_state}"]
            x_cor = int(get_state.x)
            y_cor = int(get_state.y)
            writer.setpos(x=x_cor, y=y_cor)
            correct_guess_list.append(answer_state)
            writer.write(f"{answer_state}", align=ALIGN, font=FONT)
            num_correct += 1

    while cont_game:
        cont_game = screen.textinput(
            title="Continue?", prompt="Do you want to continue? Y / N").upper()

        if cont_game == "N":
            game_is_on = False
            cont_game = False
        else:
            answer_state = screen.textinput(
                title=f"{num_correct}/{TOTAL_STATES} States Correct", prompt="What's another state's name?").capitalize()
            cont_game = False


writer.setpos(x=0, y=250)
writer.write(f"You scored: {num_correct}/{TOTAL_STATES}",
             align=ALIGN, font=INCORRECT_FONT)

answer_dict = {
    "States": [answer_state]
}

frame = pandas.DataFrame(answer_dict)
frame.to_csv("Day 25/US States Game/Guess_List.csv")


screen.exitonclick()
