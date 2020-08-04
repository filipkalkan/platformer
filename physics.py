import gameobject

gravity = 0.5


def apply(movable_object):
    if on_ground(movable_object):
        movable_object.falling = False
    else:
        movable_object.falling = True

    if movable_object.falling:
        fall(movable_object)


def fall(movable_object):
    movable_object.y += gravity
    movable_object.top += gravity
    movable_object.bottom += gravity


def on_ground(movable_object):
    other_objects = [current_object for current_object in movable_object.all_objects if
                     current_object is not movable_object]
    for obj in other_objects:
        if movable_object.bottom >= obj.top and obj.left < movable_object.left < obj.right:
            return True
    return False
