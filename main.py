from turtle import Turtle, Screen

initial_x_cor = 0.0
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
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

game_is_on = True
# moving segments of snake body as single entity
while game_is_on:
    moves = 0
    for segment in snake_body:
        segment.speed("slow")
        segment.forward(20)
        print(segment.xcor())
        # stopping the snake movement once the 'head' segment of the body reaches position (200, 0)
        if segment.xcor() >= 200.0:
            #segment.setheading(90)
            game_is_on = False

screen.exitonclick()
