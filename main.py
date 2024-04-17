from turtle import Turtle, Screen
import time
from snake import Snake
initial_x_cor = 0
snake_body = []  # array that comprises different snake segments
# creating individual segments of the snake body and 'merging' them

snake = Snake(Screen, Turtle, time)
# for _ in range(3):
#     new_turtle = Turtle(shape="square")
#     new_turtle.color("white")
#     new_turtle.pu()
#     new_turtle.goto(initial_x_cor, 0)
#     snake_body.append(new_turtle)  # adding each segment to the array to form a 'solid' body
#     print(new_turtle.position())
#     initial_x_cor -= 20

screen = Screen()
screen.setup(width=300, height=300)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
print(screen.window_width(), screen.window_height())
game_is_on = True


# def move_up():
#     segment.setheading(90)

# def move_snake():
#     screen.update()
#     time.sleep(1)
#     for segment_number in range(len(snake_body) - 1, 0, -1):
#         new_xcor = snake_body[segment_number - 1].xcor()
#         new_ycor = snake_body[segment_number - 1].ycor()
#         snake_body[segment_number].goto(new_xcor, new_ycor)
#     snake_body[0].forward(20)


# moving segments of snake body as single entity
while game_is_on:
    snake.move_snake()

screen.exitonclick()
