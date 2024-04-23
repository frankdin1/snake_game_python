from turtle import Turtle
import random


class Dot:
    def __init__(self, screen_width, screen_height):
        self.dot = None
        self.x_pos = range(round(-screen_width / 2), round(screen_width / 2), 20)
        self.y_pos = range(round(-screen_height / 2), round(screen_height / 2), 20)
        self.create_dot()

    def create_dot(self):
        self.dot = Turtle()
        self.dot.shape("square")
        self.dot.color("blue")
        self.dot.pu()
        self.dot.goto(random.choice(self.x_pos), random.choice(self.y_pos))
