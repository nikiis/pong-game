from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

WIDTH = 800
HEIGHT = 600

screen = Screen()

screen.setup(WIDTH + 4, HEIGHT + 8)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True

while game_is_on:
    # time.sleep(0.07)
    screen.update()
    ball.move()

    #Detect collision with r_paddle
    if ball.distance(r_paddle) < 70 and ball.xcor() > 340:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 70 and ball.xcor() < -340:
        ball.bounce_x()

    #if ball goes out of bounds (paddle misses it)
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_l_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_r_score()

screen.exitonclick()