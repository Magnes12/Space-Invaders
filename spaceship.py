import turtle


class SpaceShip(turtle.Turtle):

    def __init__(self, shape):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.setposition(0, -250)

    def move_r(self):
        self.setx(self.xcor() + 10)

    def move_l(self):
        self.setx(self.xcor() - 10)

    def shot(self):
        bullet = turtle.Turtle()
        bullet.shape('square')
        bullet.shapesize(stretch_len=0.05, stretch_wid=0.5)
        bullet.penup()
        bullet.setposition(self.pos())

        return bullet
