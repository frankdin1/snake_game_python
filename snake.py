from turtle import Turtle, Screen
import time

screen = Screen()


class Snake:

    def __init__(self):
        self.screen = screen
        self.time = time
        self.snake_body = []
        self.initial_x_cor = 0
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.pu()
            new_turtle.goto(self.initial_x_cor, 0)
            self.snake_body.append(new_turtle)  # adding each segment to the array to form a 'solid' body
            print(new_turtle.position())
            self.initial_x_cor -= 20

    @staticmethod
    def move_snake(self):
        screen.update()
        time.sleep(1)
        for segment_number in range(len(self.snake_body) - 1, 0, -1):
            new_xcor = self.snake_body[segment_number - 1].xcor()
            new_ycor = self.snake_body[segment_number - 1].ycor()
            self.snake_body[segment_number].goto(new_xcor, new_ycor)
        self.snake_body[0].forward(20)
