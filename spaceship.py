import turtle


class SpaceShip(turtle.Turtle):

    def __init__(self, shape):
        super().__init__()
        self.shape(shape)
        self.color('black')
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.setposition(0, -250)

    def move_r(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())

    def move_l(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
