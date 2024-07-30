import turtle
import pandas


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
correct_guesses = []

all_states = data["state"].to_list()
while len(correct_guesses) < 50:
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/50 Guess the stare",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in correct_guesses]
        # missing_states = []
        # for state in all_states:
        #     if state not in correct_guesses:
        #         missing_states.append(state)
        missing_state_data_frame = pandas.DataFrame(missing_states)
        missing_state_data_frame.to_csv("state_to_learn.csv")
        break
    if answer_state in all_states:
        correct_guesses.append(answer_state)

        row_data = data[data["state"] == answer_state]
        x_cor = int(row_data["x"])
        y_cor = int(row_data["y"])

        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x_cor, y_cor)
        t.write(arg=answer_state)
