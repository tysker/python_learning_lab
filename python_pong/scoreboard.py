from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = [0, 0]
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(
            f"Left: {self.scores[0]} | Right: {self.scores[1]}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self, player):
        self.scores[player] += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        if self.scores[0] > self.scores[1]:
            self.write("Left Won", align=ALIGNMENT, font=FONT)
        else:
            self.write("Right Won", align=ALIGNMENT, font=FONT)
