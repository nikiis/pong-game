from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.speed_x = 2
        self.speed_y = 2

    def move(self):
        new_x = self.xcor() + self.speed_x
        new_y = self.ycor() + self.speed_y
        self.goto(new_x, new_y)
        self.detect_collision()

    def detect_collision(self):
        if self.ycor() >= 280 or self.ycor() <= -280:
            self.speed_y *= -1

    def bounce_x(self):
        self.speed_x *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
