from turtle import Turtle


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
            self.initial_x_cor -= 20

    def move_snake(self):
        # screen.update()
        # time.sleep(1)
        # starting with the last segment...
        for segment_number in range(len(self.snake_body) - 1, 0, -1):
            # ...collect the x and y coordinates of the next segment
            new_xcor = self.snake_body[segment_number - 1].xcor()
            new_ycor = self.snake_body[segment_number - 1].ycor()

            # move the current segment to the position of the next segment
            self.snake_body[segment_number].goto(new_xcor, new_ycor)
        self.snake_body[0].forward(20)
