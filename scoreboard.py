from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
with open("highscore.txt") as file:
    hiscore = int(file.read())


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = hiscore
        self.pu()
        self.color("white")
        self.speed("fastest")
        self.goto(0, 270)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"SCORE: {self.score} HIGHSCORE: {self.highscore}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def save_score(self):
        with open("highscore.txt", mode="w") as file:
            highscore = str(self.highscore)
            file.write(highscore)
