from turtle import Turtle, Screen
import time
initial_x_cor = 0
snake_body = []  # array that comprises different snake segments
# creating individual segments of the snake body and 'merging' them
for _ in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.pu()
    new_turtle.goto(initial_x_cor, 0)
    snake_body.append(new_turtle)  # adding each segment to the array to form a 'solid' body
    print(new_turtle.position())
    initial_x_cor -= 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(3)

game_is_on = True

# moving segments of snake body as single entity
while game_is_on:
    screen.update()
    time.sleep(1)
    for segment in snake_body:
        segment.forward(20)
        # affecting the snake movement once the 'head' segment of the body reaches position (200, 0)
        if segment.xcor() >= 200.0:
            segment.setheading(90)  # changes the snakes direction
            #game_is_on = False # stops the movement of the snake

screen.exitonclick()
