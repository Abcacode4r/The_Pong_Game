from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.score_og()
    def score_og(self):
        self.goto(100, 200)
        self.right=self.write(self.r_score, align="center", font=("courier", 80, "normal"))
        self.goto(-100, 200)
        self.left=self.write(self.l_score, align="center", font=("courier", 80, "normal"))

    def score_up_l(self):
        self.clear()
        self.r_score+=1
        self.score_og()


    def score_up_r(self):
        self.clear()
        self.l_score+=1
        self.score_og()


