from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        self.score = 0
        super(Scoreboard, self).__init__()
        self.color("white")
        self.hideturtle()
        self.goto(0,280)

    def update_score(self, score):
        self.clear()
        score = "Score: " + str(score)
        self.write(score, move=False, align="center", font="Arial, 13")
