from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.title("--Pong Game--")
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.game_speed)
    screen.update()
    ball.move()

    #Ball hits wall and bounce
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Ball hits paddle and bounce
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()


    # R Paddle miss ball
    if ball.xcor() > 380 :
        ball.reset()
        r_paddle.reset()
        l_paddle.reset()
        scoreboard.l_point()


    # L Paddle miss ball
    if ball.xcor() < -380:
        ball.reset()
        r_paddle.reset()
        l_paddle.reset()
        scoreboard.r_point()















screen. exitonclick()
