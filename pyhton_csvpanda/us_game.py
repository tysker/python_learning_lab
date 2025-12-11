import turtle as tl

import pandas as pd

IMAGE = "./images/blank_states_img.gif"
STATES_DATA = "./data/50_states.csv"
STATES_TO_LEARN = "./data/states_to_learn.csv"

# Setup Screen
screen = tl.Screen()
screen.title("U.S States Game")
screen.setup(width=800, height=600)
screen.addshape(IMAGE)
tl.shape(IMAGE)

writer = tl.Turtle()
writer.hideturtle()
writer.penup()

# Load csv
df = pd.read_csv(STATES_DATA)

# List of all states
all_states = df.state.to_list()

guessed_states = set()

while len(guessed_states) < 50:
    answer_state = screen.textinput(
        title=f"{len(guessed_states)}/50 States Correct",
        prompt="Guess a state!\n",
    )

    # Normalize
    answer_state = answer_state.strip().title()
    if answer_state == "Exit":
        break

    if answer_state is None:
        break  # user pressed cancel

    # Dublicate ?
    if answer_state in guessed_states:
        print("You already guessed that state.")
        continue

    # Valid guess ?
    if answer_state in all_states:
        guessed_states.add(answer_state)

        row = df[df.state == answer_state].iloc[0]
        writer.goto(row.x, row.y)
        writer.write(answer_state, align="center", font=("Arial", 10, "normal"))
    else:
        print("Not a valid state.")

# Create csv file for the missing states
states_to_learn = [s for s in all_states if s not in guessed_states]
states_to_learn_dict = pd.DataFrame(states_to_learn)
states_to_learn_dict.columns = ["state"]
states_to_learn_dict.to_csv(STATES_TO_LEARN, index=False)

# screen.exitonclick()

# def get_mouse_click_coor(x, y):
#     print(x, y)
# tl.onscreenclick(get_mouse_click_coor)
# tl.mainloop()
