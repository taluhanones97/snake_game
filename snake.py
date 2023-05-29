
from turtle import Screen,Turtle
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()

    def create_snake(self):
        snake_tail = Turtle()
        snake_middle = Turtle()
        snake_head = Turtle()

        snake_head.penup()
        snake_middle.penup()
        snake_tail.penup()
        snake_tail.shape("square")
        snake_middle.shape("square")
        snake_head.shape("square")

        snake_tail.color("white")
        snake_middle.color("white")
        snake_head.color("white")

        snake_head.setx(0)
        snake_middle.setx(-20)
        snake_tail.setx(-40)
        self.segments.append(snake_head)
        self.segments.append(snake_middle)
        self.segments.append(snake_tail)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)

        self.segments.clear()
        self.create_snake()
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(20)

    def add_segment(self,position):
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    def up(self):
        if self.segments[0].heading() != 270:
            for i in range(0,2):
                self.segments[i].setheading(90)

    def down(self):
        if self.segments[0].heading()!=90:
            for i in range(0,2):
                self.segments[i].setheading(270)

    def left(self):
        if self.segments[0].heading() != 0:
            for i in range(0,2):
                self.segments[i].setheading(180)


    def right(self):
        if self.segments[0].heading() != 180:
            for i in range(0,2):
                self.segments[i].setheading(0)