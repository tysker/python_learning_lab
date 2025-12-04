import random
from turtle import Screen, Turtle

# Setup
is_race_on = False
colors = ["red", "orange", "green", "blue", "purple"]
all_turtles = []
y_pos = 50
x_pos = -230

# Screen
screen = Screen()
screen.setup(width=500, height=400)

# User
user_bet = screen.textinput(
    title="Make your bet", prompt="Which turtle will win the race? Enter a color: "
)

if user_bet:
    is_race_on = True

for val in colors:
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(val)
    new_turtle.penup()
    new_turtle.goto(x=x_pos, y=y_pos)
    y_pos -= 30
    all_turtles.append(new_turtle)

# Game

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 220:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
# def move_forwards():
#     tim.forward(10)
#
#
# def move_backwards():
#     tim.backward(10)
#
#
# def move_left():
#     new_heading = tim.heading() + 10
#     tim.setheading(new_heading)
#
#
# def move_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     # tim.setpos(0, 0)
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(key="w", fun=move_forwards)
# screen.onkey(key="s", fun=move_backwards)
# screen.onkey(key="a", fun=move_left)
# screen.onkey(key="d", fun=move_right)
# screen.onkey(key="c", fun=clear)
# screen.exitonclick()
