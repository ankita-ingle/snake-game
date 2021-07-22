from turtle import Turtle

X_COORDINATES = (0, -20, -40)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
COLOR = "#89C9B8"


class Snake:

    def __init__(self):
        self.body = []

        for x in X_COORDINATES:  # set initial position of snake
            self.add_segment((x, 0))

        self.head = self.body[0]

    def add_segment(self, position):
        segment = Turtle(shape="square")  # create segments for snake body
        segment.color(COLOR)
        segment.penup()  # prevent the segments from drawing
        segment.goto(position)
        self.body.append(segment)

    def extend(self):
        self.add_segment(self.body[1].position())

    def move(self):
        for index in range(len(self.body) - 1, 0, -1):
            new_x = self.body[index - 1].xcor()  # get x-coor of prev segment
            new_y = self.body[index - 1].ycor()  # get y-coor of prev segment
            self.body[index].goto(x=new_x, y=new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:  # prevent snake from going in opposite direction
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:   # prevent snake from going in opposite direction
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:   # prevent snake from going in opposite direction
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:   # prevent snake from going in opposite direction
            self.head.setheading(0)
