import pyglet


def load_picture(name):
    picture = pyglet.image.load(name)  # Loads the picture from folder
    sprite = pyglet.sprite.Sprite(picture)  # Creates Object Sprite and puts it in left corner


if __name__ == "__main__":
    window = pyglet.window.Window()     # Calling a class Window creates an object window
    load_picture(ship, 20, 20)
    sprite.draw()
    pyglet.app.run()                    # cycle while for game
---
    import pyglet

    picture_list = []
    picture_names = ['ship', 'meteor_large']


    def load_picture():
        for picture in picture_names:
            print(picture)
            name = picture + '.png'
            print(name)
            picture_object = pyglet.image.load(name)  # Loads the picture from folder
            print(picture_object)
            picture_sprite = pyglet.sprite.Sprite(picture_object, x=0, y=0)
            # Creates Object Sprite and puts it in left corner
            picture_list.append(picture_sprite)

        print(picture_list)
        return picture_list


    def on_text(text):  # function reacts on keyboard input
        print(text)


    def draw():
        window.clear()
        ship.draw()
        meteor.draw()


    if __name__ == "__main__":
        window = pyglet.window.Window(width=500, height=500)  # Calling a class Window creates an object window
        load_picture()
        ship = picture_list[0]
        meteor = picture_list[1]

        window.push_handlers(
            on_text=on_text,
            on_draw=draw,
        )

        pyglet.app.run()  # cycle while for game
---
import pyglet
from objects import load_picture


class SpaceObject:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.speed_x = 0
        self.speed_y = 0
        self.angle = 0

        self.sprite = pyglet.sprite.Sprite(ship)

    def draw(self):
        self.sprite.x = self.x
        self.sprite.y = self.y


def draw():
    window.clear()
    asteroid.draw()


def on_text():
    pass


picture_list = load_picture()

window = pyglet.window.Window(width=500, height=500)
# Calling a class Window creates an object window
window.push_handlers(
    on_text=on_text,
    on_draw=draw,
)
load_picture()
ship = picture_list[0]
asteroid = picture_list[1]
pyglet.app.run()            # cycle while for game
print('Hotovo!')            # prints after the cycle ends
---