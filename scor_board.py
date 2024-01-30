from turtle import Turtle
FONT = ('courier', 14, 'normal')



class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as high:
            content = int(high.read())
            self.highscore = content
        self.color("red")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"score:{self.score} highscore:{self.highscore}", move=False, align='center', font=('courier', 14, 'normal'))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as j:
                j.write(f"{self.highscore}")

        self.score = 0
        self.update_score()


    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", move=False, align='center', font=FONT)

    def update(self):
        self.score += 1
        self.update_score()



