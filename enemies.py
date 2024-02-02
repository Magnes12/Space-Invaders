import turtle
import time


class Enemies(turtle.Turtle):

    def __init__(self, x, y, shape):
        super().__init__()
        self.shape(shape)
        self.penup()
        self.turtlesize(stretch_wid=0.5, stretch_len=0.5)
        self.goto(x, y)

    def enemies_create(self, shape):
        enemies = []
        enemies_spacing_x = 70
        enemies_spacing_y = 50

        for row in range(6):
            for col in range(6):
                enemy = Enemies(-175 + col * enemies_spacing_x, 275 - row * enemies_spacing_y, shape)
                enemies.append(enemy)

        return enemies
