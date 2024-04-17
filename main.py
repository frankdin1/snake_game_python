from turtle import Turtle, Screen
import time
from snake import Snake

snake = Snake()

screen = Screen()
screen.setup(width=300, height=300)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
game_is_on = True

# moving segments of snake body as single entity
while game_is_on:
    snake.move_snake()

screen.exitonclick()
