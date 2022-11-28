import pyglet
from math import sin, cos, degrees, pi
from random import randrange


# Window dimensions:
height = 500
width = 500

# Constant
ROTATION_SPEED = 3
ACCELERATION = 10
LASER_SPEED = 20

# Picture names: 'ship' 'laser' 'satellite' 'star' 'planet' 'asteroid_large' 'asteroid' and space for sprite
picture_dict = {
    'ship': 0,
    'laser': 0,
    'satellite': 0, 'star': 0,
    'planet': 0,
    'asteroid_large': 0,
    'asteroid': 0,
}

# Calling a class Window creates an object window
window = pyglet.window.Window(width=width, height=height)


class SpaceObject:
    def __init__(self, sprite_name):
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.angle = 0
        self.radius = 30
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
    
    def delete(self):
        try:
            object.remove(self)
        except ValueError:
            pass
    
    def hit_by_spaceship(self, ship):
        pass

    def hit_by_laser(self, laser):
        pass


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
        if pyglet.window.key.SPACE in pressed_keys:
            laser = Laser()
            objects.append (laser)
        # Colisions
        for obj in list(objects):
            if overlap(self, obj) and self != obj:
                obj.hit_by_spaceship(self)


class Laser(SpaceObject):
    def __init__(self, ship):
        super().__init__('laser')
        self.x = ship.x
        self.y = ship.y
        self.angle = ship.angle
        self.speed_x = ship.speed_x + cos(self.angle) * LASER_SPEED
        self.speed_y = ship.speed_y + sin(self.angle) * LASER_SPEED
        self.radius = 15
    
    def tick(self, dt):
        pass


class Asteroid_Large(SpaceObject):
    def __init__(self):
        super().__init__('asteroid_large')
        self.x = width // 4
        self.y = height // 4
        self.speed_x = randrange(-100, 100)
        self.speed_y = randrange(-100, 100)
        self.radius = 60

    def tick(self, dt):
        super().tick(dt)
        # Object rotates
        self.angle = self.angle + randrange(1, 5) * dt
    
    def hit_by_spaceship(self, ship):
        ship.delete()
    
    def hit_by_laser(self, laser):
        self.delete()
        laser.delete()
        for i in range (2):
            asteroid = Asteroid()
            objects.append(asteroid)
        pyglet.clock.schedule_interval(asteroid.tick, 1/30)


class Asteroid(Asteroid_Large):
    def __init__(self):
        super().__init__('asteroid')
        self.x = width // 4
        self.y = height // 4
        self.speed_x = randrange(-100, 100)
        self.speed_y = randrange(-100, 100)
        self.radius = 60

    def tick(self, dt):
        super().tick(dt)
        # Object rotates
        self.angle = self.angle + randrange(1, 5) * dt
    
    def hit_by_spaceship(self, ship):
        ship.delete()
    
    def hit_by_laser(self, laser):
        pass


class Satellite(SpaceObject):
    def __init__(self):
        super().__init__('satellite')
        self.x = (width // 3) * 2
        self.y = (height // 3) * 2
        self.speed_x = randrange(-100, 100)
        self.speed_y = randrange(-100, 100)

    def tick(self, dt):
        super().tick(dt)
        # Object rotates
        self.angle = self.angle + randrange(-5, -1) * dt


class Planet(SpaceObject):
    def __init__(self):
        super().__init__('planet')
        self.x = (width // 3) * 2
        self.y = height // 3
        self.speed_x = randrange(-100, 100)
        self.speed_y = randrange(-100, 100)
        self.radius = 60

    def tick(self, dt):
        super().tick(dt)
        # Object rotates
        self.angle = self.angle + randrange(-5, -1) * dt


# All pressed keys
pressed_keys = set()
# All onjects in universe
objects = list


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
    for object in objects:
        object.draw()


@window.event                           # Decorator can change function or marks function
def tick(dt):
    pass


@window.event                           # Decorator can change function or marks function
def on_text():
    pass


# Copied from Web circle, distance and overlap
def draw_circle(x, y, radius):
    iterations = 20
    s = sin(2 * pi / iterations)
    c = cos(2 * pi / iterations)

    dx, dy = radius, 0

    pyglet.gl.glBegin(pyglet.gl.GL_LINE_STRIP)
    for i in range(iterations+1):
        pyglet.gl.glVertex2f(x + dx, y + dy)
        dx, dy = (dx*c - dy*s), (dy*c + dx*s)
    pyglet.gl.glEnd()


def distance(a, b, wrap_size):
    """Distance in one direction (x or y)"""
    result = abs(a - b)
    if result > wrap_size / 2:
        result = wrap_size - result
    return result


def overlap(a, b):
    """Returns true iff two space objects overlap"""
    distance_squared = (distance(a.x, b.x, window.width) ** 2 +
                        distance(a.y, b.y, window.height) ** 2)
    max_distance_squared = (a.radius + b.radius) ** 2
    return distance_squared < max_distance_squared
# Copied END


def create_sprites():
    # Put pictures for game in to the dictionary
    for picture in picture_dict:
        name = picture + '.png'
        # makes picture name
        picture_object = pyglet.image.load(name)
        picture_object.anchor_x = picture_object.width // 2
        picture_object.anchor_y = picture_object.height // 2
        # Loads the picture from folder and sets anchor point to middle
        picture_sprite = pyglet.sprite.Sprite(picture_object)
        # Creates Object Sprite and puts it in left corner
        picture_dict[picture] = picture_sprite

    return picture_dict


print("Fun, Begins!")
create_sprites()


# Create objects in game
ship = Ship()
objects.append(ship)

satellite = Satellite()
objects.append(satellite)

planet = Planet()
objects.append(planet)

asteroid_large = Asteroid_Large()
objects.append(asteroid_large)


pyglet.clock.schedule_interval(tick, 1/30)          # Function tick is called in this interval
pyglet.clock.schedule_interval(ship.tick, 1/30)
pyglet.clock.schedule_interval(asteroid_large.tick, 1/30)
pyglet.clock.schedule_interval(satellite.tick, 1/30)
pyglet.clock.schedule_interval(planet.tick, 1/30)


window.push_handlers(
    on_text=on_text,
    on_draw=draw,
)


pyglet.app.run()            # cycle while for game
print("No! Don't Go! ;-(")            # prints after the cycle ends
