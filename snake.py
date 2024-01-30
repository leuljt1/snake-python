from turtle import Turtle
# -10,-20
MOVE_FORWARD = 10      # 10
STARTING = [(0, 0), (-10, 0), (-20, 0)]


class Snake:
    def __init__(self):
        self.all_turtle = []
        self.create_snake()
        self.head = self.all_turtle[0]

    def create_snake(self):
        for index in STARTING:
            self.add_segment(index)

    def add_segment(self, position):
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.shapesize(stretch_len=0.5, stretch_wid=0.5)
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtle.append(new_turtle)

    def extend(self):
        self.add_segment(self.all_turtle[-1].position())

    def move(self):
        for seg_num in range(len(self.all_turtle) - 1, 0, -1):
            new_xcor = self.all_turtle[seg_num - 1].xcor()
            new_ycor = self.all_turtle[seg_num - 1].ycor()
            self.all_turtle[seg_num].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_FORWARD)

    def reset(self):
        for i in self.all_turtle:
            i.goto(1000, 1000)
        self.all_turtle.clear()
        self.create_snake()
        self.head = self.all_turtle[0]

    def up(self):
        a = self.head.heading()
        if a == 0 or a == 180:
            self.head.setheading(90)

    def down(self):
        b = self.head.heading()
        if b == 0 or b == 180:
            self.head.setheading(270)

    def right(self):
        a = self.head.heading()
        if a == 90 or a == 270:
            self.head.setheading(0)

    def left(self):
        a = self.head.heading()
        if a == 90 or a == 270:
            self.head.setheading(180)
