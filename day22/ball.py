from turtle import Turtle

X_MOVEMENT = 45
Y_MOVEMENT = 45

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.game_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.game_speed *= 0.8

    def reset(self):
        if self.xcor() > 380 or self.xcor() < -380:
            self.x_move *= -1
        self.home()
        self.game_speed = 0.1




