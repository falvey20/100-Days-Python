import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
map_image = "blank_states_img.gif"
screen.addshape(map_image)

turtle.shape(map_image)

states_data = pandas.read_csv("50_states.csv")
state_names = states_data.state.to_list()
guessed_states = []

correct_answers = 0
while correct_answers < 50:
    answer_state = screen.textinput(title=f"Score: {correct_answers}/50", prompt="Next State").title()
    if answer_state == "Exit":
        missing_states = []
        for state in state_names:
            if state not in guessed_states:
                missing_states.append(state)
        states_not_guessed = pandas.DataFrame(missing_states)
        states_not_guessed.to_csv("states_to_learn.csv")
        break
    if answer_state in state_names:
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        correct_state = states_data[states_data.state == answer_state]
        x_cor = int(correct_state.x)
        y_cor = int(correct_state.y)
        t.goto(x_cor, y_cor)
        t.write(answer_state)
        correct_answers += 1
        guessed_states.append(answer_state)

screen.exitonclick()
