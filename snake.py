from turtle import Turtle

MOVE_DISTANCE = 20
SEGMENT_GAP = 20


class Snake:

    def __init__(self):
        self.snake_body = []  # array that comprises different snake segments
        self.initial_x_cor = 0
        self.create_snake()

    # creating individual segments of the snake body and 'merging' them
    def create_snake(self):
        for _ in range(3):
            new_turtle = Turtle(shape="square")
            new_turtle.color("white")
            new_turtle.pu()
            new_turtle.goto(self.initial_x_cor, 0)
            self.snake_body.append(new_turtle)  # adding each segment to the array to form a 'solid' body
            print(new_turtle.position())
            self.initial_x_cor -= SEGMENT_GAP

    # moving segments of snake body as single entity
    def move_snake(self):
        for segment_number in range(len(self.snake_body) - 1, 0, -1):
            # ...collect the x and y coordinates of the next segment
            new_xcor = self.snake_body[segment_number - 1].xcor()
            new_ycor = self.snake_body[segment_number - 1].ycor()

            # move the current segment to the position of the next segment
            self.snake_body[segment_number].goto(new_xcor, new_ycor)
        self.snake_body[0].forward(MOVE_DISTANCE)

    def turn_right(self):
        self.snake_body[0].setheading(0)

    def move_up(self):
        self.snake_body[0].setheading(90)

    def move_down(self):
        self.snake_body[0].setheading(270)

    def turn_left(self):
        self.snake_body[0].setheading(180)