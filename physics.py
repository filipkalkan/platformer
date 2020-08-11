GRAVITY = 0.07


def apply(movable_object):
    apply_falling(movable_object)
    apply_top_collision(movable_object)
    apply_side_collision(movable_object)



def apply_side_collision(movable_object):
    if colliding_sides(movable_object):
        movable_object.rect.x = movable_object.prev_x


def apply_top_collision(movable_object):
    if colliding_top(movable_object):
        movable_object.falling_velocity = 0
        movable_object.rect.y = movable_object.prev_y


def apply_falling(movable_object):
    if on_ground(movable_object):
        movable_object.falling = False
        movable_object.falling_velocity = 0
    else:
        movable_object.falling = True
        fall(movable_object)


def fall(movable_object):
    movable_object.falling_velocity += GRAVITY
    movable_object.move_down(movable_object.falling_velocity)


def on_ground(movable_object):
    other_objects = [obj for obj in movable_object.all_objects if obj is not movable_object]
    for obj in other_objects:
        if movable_object.rect.colliderect(obj.rect):
            side = determine_side_y(movable_object.rect, obj.rect)
            if side == "bottom":
                print("On ground")
                if movable_object.prev_y + movable_object.rect.h <= obj.rect.top:
                    movable_object.rect.bottom = obj.rect.top + 1
                movable_object.colliding_bottom = True
                return True
    return False


def colliding_sides(movable_object):
    other_objects = [obj for obj in movable_object.all_objects if obj is not movable_object]
    for obj in other_objects:
        copy_rect = obj.rect.copy()
        copy_rect.y += 10
        if movable_object.rect.colliderect(copy_rect):
            side = determine_side_x(movable_object.rect, obj.rect)
            if side in ("left", "right"):
                if side == "left":
                    movable_object.colliding_left = True
                elif side == "right":
                    movable_object.colliding_right = True
                print("side collison")
                return True
    return False


def colliding_top(movable_object):
    other_objects = [obj for obj in movable_object.all_objects if obj is not movable_object]
    for obj in other_objects:
        if movable_object.rect.colliderect(obj.rect):
            side = determine_side_y(movable_object.rect, obj.rect)
            if side == "top":
                print("Bump head")
                movable_object.colliding_top = True
                return True
    return False


def determine_side_x(movable_rect, obj_rect):
    if movable_rect.midleft[0] < obj_rect.midright[0]:
        return "left"
    elif movable_rect.midright[0] > obj_rect.midleft[0]:
        return "right"
    else:
        return "none"


def determine_side_y(movable_rect, obj_rect):
    if movable_rect.midbottom[1] > obj_rect.midtop[1]:
        return "bottom"
    elif movable_rect.midtop[1] < obj_rect.midbottom[1]:
        return "top"
    else:
        return "none"
