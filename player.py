from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def move_up(self):
        if self.ycor() < 280:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -280:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)

    def move_left(self):
        if self.xcor() > -280:
            new_x = (self.xcor() - 20)
            self.goto(new_x, self.ycor())

    def move_right(self):
        if self.xcor() < 280:
            new_x = self.xcor() + 20
            self.goto(new_x, self.ycor())

    def reset_player(self):
        self.goto(0, -280)
