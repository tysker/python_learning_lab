import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

ball = Ball()
screen.listen()
scoreboard = Scoreboard()

# Paddle 1
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

# Paddle 2
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
x_pos = 10
y_pos = 10

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle
    if (
        ball.distance(r_paddle) < 50
        and ball.xcor() > 320
        or ball.distance(l_paddle) < 50
        and ball.xcor() < -320
    ):
        ball.bounce_x()

    # Right paddle
    if ball.xcor() > 380:
        scoreboard.increase_score(0)
        ball.reset()

    # Left paddle
    if ball.xcor() < -380:
        scoreboard.increase_score(1)
        ball.reset()

    # Game Over
    if scoreboard.scores[0] == 5 or scoreboard.scores[1] == 5:
        scoreboard.game_over()
        game_is_on = False


screen.exitonclick()
