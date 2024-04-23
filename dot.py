from turtle import Turtle
import random


class Dot(Turtle):
    def __init__(self, screen_width, screen_height):
        super().__init__()
        self.x_pos = range(round(-screen_width / 2)+40, round(screen_width / 2)-40, 20)
        self.y_pos = range(round(-screen_height / 2)+40, round(screen_height / 2)-40, 20)
        self.create_dot()

    def create_dot(self):
        self.shape("square")
        self.color("blue")
        self.pu()
        self.goto(random.choice(self.x_pos), random.choice(self.y_pos))
        self.showturtle()
