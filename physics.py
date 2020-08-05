import gameobject

GRAVITY = 0.07


def apply(movable_object):
    apply_top_collision(movable_object)
    apply_side_collision(movable_object)
    apply_falling(movable_object)


def apply_top_collision(movable_object):
    if colliding_top(movable_object):
        movable_object.move_down(2)
        movable_object.falling_velocity = 0


def apply_falling(movable_object):
    if on_ground(movable_object):
        movable_object.falling = False
        movable_object.falling_velocity = 0
    else:
        movable_object.falling = True
    if movable_object.falling:
        fall(movable_object)


def apply_side_collision(movable_object):
    if colliding_sides(movable_object):
        movable_object.go_back()
        movable_object.falling_velocity = 0


def fall(movable_object):
    movable_object.falling_velocity += GRAVITY
    movable_object.move_down(movable_object.falling_velocity)


def on_ground(movable_object):
    other_objects = [current_object for current_object in movable_object.all_objects if
                     current_object is not movable_object]
    for obj in other_objects:
        if movable_object.bottom >= obj.top and obj.left < movable_object.left < obj.right and movable_object.top < obj.bottom - obj.height / 2:
            movable_object.move_up(movable_object.bottom - obj.top)
            return True
    return False


def colliding_sides(movable_object):
    other_objects = [current_object for current_object in movable_object.all_objects if
                     current_object is not movable_object]
    for obj in other_objects:
        if obj.left < movable_object.right < obj.right and (obj.bottom > movable_object.top > obj.top or obj.bottom > movable_object.bottom > obj.top):
            print("Side Collision")

    return False


def colliding_top(movable_object):
    other_objects = [current_object for current_object in movable_object.all_objects if
                     current_object is not movable_object]
    for obj in other_objects:
        if (obj.top + obj.height / 2) < movable_object.top < obj.bottom and obj.left < movable_object.left < obj.right:
            print("Colliding")
            return True
    return False
