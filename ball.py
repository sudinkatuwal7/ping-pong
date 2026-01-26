from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.speedy_pong = 1

    def move(self):
        new_x = self.xcor() + self.x_move * self.speedy_pong
        new_y = self.ycor() + self.y_move * self.speedy_pong
        self.goto(new_x, new_y)

    def y_bounce(self):
        self.y_move *= -1
        self.speedy_pong *= 1.05

    def x_bounce(self):
        self.x_move *= -1
        self.speedy_pong *= 1.05

    def restart_ball(self):
        self.goto(0, 0)
        self.x_move *= -1
        self.y_move *= -1
        self.speedy_pong = 1
        self.move()
