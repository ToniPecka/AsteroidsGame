import pyglet

# Picture names and space for sprite
picture_dict = {
    'ship': 0,
    'laser': 0,
    'satellite': 0, 'star': 0,
    'planet': 0,
    'asteroid_large': 0
}


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


if __name__ == "__main__":
    # for testing runs only when Run as a main file
    print(create_sprites())
