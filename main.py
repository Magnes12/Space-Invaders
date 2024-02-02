import turtle
from spaceship import SpaceShip
from enemy import Enemy


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

    enemies_inst = Enemy(-175, 275, enemy_shape)
    enemies = enemies_inst.enemies_create(enemy_shape)

    bullets = []

    screen.listen()
    screen.onkey(space_ship.move_l, "a")
    screen.onkey(space_ship.move_r, "d")
    screen.onkey(lambda: bullets.append(space_ship.shot()), "space")

    def remove_bullet():
        bullet.hideturtle()
        bullets.remove(bullet)

    while True:
        for bullet in bullets:
            bullet.sety(bullet.ycor() + 5)
            if bullet.ycor() > 275:
                remove_bullet()

            enemy_to_remove = []

            for enemy in enemies:
                if bullet.distance(enemy) < 20:
                    remove_bullet()
                    enemy.remove()
                    enemy_to_remove.append(enemy)

            for enemy in enemy_to_remove:
                enemy_to_remove.remove(enemy)

        screen.update()


if __name__ == "__main__":
    main()
