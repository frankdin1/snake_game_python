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
    initial_x_cor += 20

screen = Screen()
screen.setup(width=300, height=300)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(3)
print(screen.window_width(), screen.window_height())
game_is_on = True


def move_left():
    segment.setheading(90)


# moving segments of snake body as single entity
while game_is_on:
    screen.update()
    time.sleep(1)
    for segment in snake_body:
        screen.onkey(key="s", fun=move_left)
        segment.backward(20)
        print(segment.pos())
        # affecting the snake movement once the 'head' segment of the body reaches position (200, 0)
        if segment.xcor() >= screen.window_width() / 2 or \
                segment.ycor() >= screen.window_height() / 2 or \
                segment.xcor() <= -screen.window_width() / 2 or \
                segment.ycor() <= -screen.window_height() / 2:
            #segment.setheading(90)  # changes the snakes direction
            game_is_on = False # stops the movement of the snake

screen.exitonclick()
