from turtle import Turtle, Screen

MOVEMENT_DISTANCE = 20
UP_ANGLE = 90
DOWN_ANGLE = 270
LEFT_ANGLE = 180
RIGHT_ANGLE = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x_offset = 0
        for i in range(3):
            snake = Turtle(shape="square")
            snake.pu()
            snake.color("white", "white")
            snake.setposition(x=x_offset, y=0)
            self.segments.append(snake)
            x_offset -= 20

    def move(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVEMENT_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN_ANGLE:
            self.head.setheading(UP_ANGLE)

    def down(self):
        if self.head.heading() != UP_ANGLE:
            self.head.setheading(DOWN_ANGLE)

    def right(self):
        if self.head.heading() != LEFT_ANGLE:
            self.head.setheading(RIGHT_ANGLE)

    def left(self):
        if self.head.heading() != RIGHT_ANGLE:
            self.head.setheading(LEFT_ANGLE)


    def turn_snake(self):
        screen = Screen()
        screen.onkey(fun=self.up, key="Up")
        screen.onkey(fun=self.down, key="Down")
        screen.onkey(fun=self.left, key="Left")
        screen.onkey(fun=self.right, key="Right")
        screen.listen()

    def food_collision(self, food):
        if self.head.distance(food) <= 15:
            return True
        else:
            return False

    def body_collision(self):
        for segment in self.segments[1:]:
            if self.head.distance(segment) <= 15:
                return True

    def increase_segment(self):
        snake = Turtle(shape="square")
        snake.pu()
        snake.color("white", "white")
        tail = self.segments[len(self.segments)-1]
        to_x = tail.xcor()
        to_y = tail.ycor()
        snake.goto(x=(to_x-20), y=to_y)
        self.segments.append(snake)

    def game_over_checker(self):
        if self.head.xcor() < -295 or\
           self.head.xcor() > 295 or\
           self.head.ycor() < -295 or\
           self.head.ycor() > 295:
            return True
        elif self.body_collision():
            return True

    def reset_snake(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]