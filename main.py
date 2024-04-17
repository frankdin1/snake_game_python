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

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)
    snake.move_snake()

screen.exitonclick()
