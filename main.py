from turtle import Turtle, Screen
import time
from snake import Snake
from dot import Dot

snake = Snake()
screen = Screen()
screen.setup(width=400, height=400)
dot = Dot(screen.window_width(), screen.window_height())
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

screen.listen()

screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")
screen.onkey(screen.bye, "Escape")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move_snake()
    print(f"dot position\tsnake position")
    print(f"{dot.dot.position()}\t{snake.snake_body[0].position()}")
    if snake.snake_body[0].position() == dot.dot.position():
        print("contact")


screen.exitonclick()
