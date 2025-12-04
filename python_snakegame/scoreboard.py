from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")
FILE = "data.txt"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.read_highscore()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT,
        )

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.write_to_file(self.score)
        self.score = 0
        self.read_highscore()
        self.update_scoreboard()

    def read_highscore(self):
        with open(FILE) as data:
            self.high_score = int(data.read())

    def write_to_file(self, score):
        with open(FILE, mode="w") as file:
            file.write(str(score))
