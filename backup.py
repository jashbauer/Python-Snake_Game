from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

x_offset = 0
segments = []
for i in range(3):
    snake = Turtle(shape="square")
    snake.pu()
    snake.color("white", "white")
    snake.setposition(x=x_offset, y=0)
    segments.append(snake)
    x_offset -= 20


def right():
    segments[0].right(90)


def left():
    segments[0].left(90)


game_on = True
while game_on:
    screen.update()
    time.sleep(0.10)
    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num-1].xcor()
        new_y = segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x, new_y)

    screen.onkey(fun=left, key="Left")
    screen.onkey(fun=right, key="Right")
    screen.listen()
    segments[0].forward(20)

    if segments[0].xcor() <= -300 or segments[0].xcor() >= 300 or\
            segments[0].ycor() <= -300 or segments[0].ycor() >= 300:
        game_on = False


screen.exitonclick()
