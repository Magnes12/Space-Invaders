import turtle
import time
from spaceship import SpaceShip
from enemies import Enemies

enemy_shape = turtle.register_shape('enemy.gif')


def main():
    screen = turtle.Screen()
    screen.bgcolor('white')
    screen.setup(width=800, height=600)
    screen.title('Space Invaders')
    screen.tracer(0)

    turtle.register_shape('enemy.gif')
    turtle.register_shape('spaceship.gif')
    ship_shape = 'spaceship.gif'
    enemy_shape = 'enemy.gif'

    space_ship = SpaceShip(ship_shape)

    enemies_inst = Enemies(-175, 275, enemy_shape)
    enemies = enemies_inst.enemies_create(enemy_shape)

    screen.listen()
    screen.onkey(space_ship.move_l, "a")
    screen.onkey(space_ship.move_r, "d")

    while True:
        screen.update()


if __name__ == "__main__":
    main()
