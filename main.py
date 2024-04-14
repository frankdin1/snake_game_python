from turtle import Turtle, Screen

initial_x_cor = 0.0
for _ in range(3):
    new_turtle = Turtle(shape="square")
    new_turtle.color("white")
    new_turtle.pu()
    new_turtle.goto(initial_x_cor, 0)
    print(new_turtle.position())
    initial_x_cor += 20

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")



screen.exitonclick()