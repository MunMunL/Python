from turtle import Turtle

SCOREBOARD_ALIGN = "center"
SCOREBOARD_FONT = ('Arial', 16, 'bold')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("White")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.score = 0
        with open("data.txt", mode="r") as data:
            self.high_score = int(data.read())
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score}  High Score: {self.high_score}", move=False, align=SCOREBOARD_ALIGN, font=SCOREBOARD_FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="GAME OVER", move=False, align=SCOREBOARD_ALIGN, font=SCOREBOARD_FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def gain_score(self):
        self.score += 1
        self.update_scoreboard()


# score = Scoreboard()
# print(score.high_score)
# score.starting_high_score()

# game = Scoreboard()
#
# print(game.score)
# game.gain_score()
# print(game.score)