import pyglet
from objects import create_sprites
from math import sin, cos, degrees
from random import randrange

# Picture names from Objects: 'ship' 'laser' 'satellite' 'star' 'planet' 'asteroid_large'
# Window dimensions:
height = 500
width = 500
# Constant
ROTATION_SPEED = 3
ACCELERATION = 10
# Calling a class Window creates an object window
window = pyglet.window.Window(width=width, height=height)


class SpaceObject:
    def __init__(self, sprite_name):
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.angle = 0

        self.sprite = picture_dict[sprite_name]

    def draw(self):
        self.sprite.x = self.x
        self.sprite.y = self.y
        self.sprite.rotation = 90 - degrees(self.angle)        # transfers Rad to Deg
        self.sprite.draw()

    def tick(self, dt):
        # Object flies
        self.x = self.x + self.speed_x * dt
        self.y = self.y + self.speed_y * dt
        # puts object back at the other side
        self.x = self.x % window.width
        self.y = self.y % window.height


class Ship(SpaceObject):
    def __init__(self):
        super().__init__('ship')
        self.x = width // 2
        self.y = height // 2

    def tick(self, dt):
        super().tick(dt)
        if pyglet.window.key.LEFT in pressed_keys:
            ship.angle = ship.angle + ROTATION_SPEED * dt
        if pyglet.window.key.RIGHT in pressed_keys:
            ship.angle = ship.angle - ROTATION_SPEED * dt
        if pyglet.window.key.UP in pressed_keys:
            ship.speed_x = ship.speed_x + cos(ship.angle) * ACCELERATION
            ship.speed_y = ship.speed_y + sin(ship.angle) * ACCELERATION
        if pyglet.window.key.DOWN in pressed_keys:
            ship.speed_x = ship.speed_x - cos(ship.angle) * ACCELERATION
            ship.speed_y = ship.speed_y - sin(ship.angle) * ACCELERATION


class Asteroid(SpaceObject):
    def __init__(self):
        super().__init__('asteroid_large')
        self.x = width // 4
        self.y = height // 4
        self.speed_x = randrange(-100, 100)
        self.speed_y = randrange(-100, 100)

    def tick(self, dt):
        super().tick(dt)
        # Object rotates
        self.angle = self.angle + ROTATION_SPEED * dt


pressed_keys = set()


@window.event                           # Decorator can change function or marks function
def on_key_press(key, mod):
    pressed_keys.add(key)
    print(key)


@window.event                           # Decorator can change function or marks function
def on_key_release(key, mod):
    pressed_keys.discard(key)
    print(key)


@window.event                           # Decorator can change function or marks function
def draw():
    window.clear()
    ship.draw()
    asteroid.draw()


@window.event                           # Decorator can change function or marks function
def tick(dt):
    pass


@window.event                           # Decorator can change function or marks function
def on_text():
    pass


picture_dict = create_sprites()
asteroid = Asteroid()
ship = Ship()

pyglet.clock.schedule_interval(tick, 1/30)          # Function tick is called in this interval
pyglet.clock.schedule_interval(ship.tick, 1/30)
pyglet.clock.schedule_interval(asteroid.tick, 1/30)

window.push_handlers(
    on_text=on_text,
    on_draw=draw,
)
pyglet.app.run()            # cycle while for game
print('Hotovo!')            # prints after the cycle ends