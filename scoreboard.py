from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.speed(0)
        self.penup()
        self.color('black')
        self.hideturtle()
        self.clear()

    def write_score(self,point):
        self.score += point
        self.clear()
        self.write("Score: {}".format(self.score), align="center", font=FONT)

    def lose(self):
        self.clear()
        self.write("GAME OVER", align="center", font=FONT)

    # def lose(self,level):
    #     self.clear()
    #     self.write("Level: {}".format(lelvel), align="center", font=FONT)
