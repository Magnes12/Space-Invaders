import turtle


class Enemy(turtle.Turtle):

    def __init__(self, x, y, shape):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.goto(x, y)

    def move(self):
        new_x = self.xcor() + self.dx
        self.goto(new_x, self.ycor())

    def enemies_create(self, shape):
        enemies = []
        enemies_spacing_x = 70
        enemies_spacing_y = 50

        for row in range(6):
            for col in range(6):
                enemy = Enemy(-175 + col * enemies_spacing_x, 275 - row * enemies_spacing_y, shape)
                enemies.append(enemy)

        return enemies

    def remove(self):
        self.goto(1000, 1000)
