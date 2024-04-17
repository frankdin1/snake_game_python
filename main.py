from turtle import Turtle, Screen
import time
from snake import Snake

snake = Snake()

screen = Screen()
screen.setup(width=300, height=300)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()


def turn_right():
    snake.snake_body[0].setheading(0)

def move_up():
    snake.snake_body[0].setheading(90)

def move_down():
    snake.snake_body[0].setheading(270)
def turn_left():
    snake.snake_body[0].setheading(180)


screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    snake.move_snake()

screen.exitonclick()
