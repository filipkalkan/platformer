from pygame import Rect
from gameobject import MovableGameObject

foot_line_height = 5


class Character(MovableGameObject):

    def __init__(self, img, coordinates, graphics, keys_dict, speed=3):
        super().__init__(img, coordinates, graphics, keys_dict)
        self.speed = speed
        self.dx, self.dy = 0, 0
        self.jumping_height = -6
        self.colliding_left = False
        self.colliding_right = False
        self.colliding_top = False
        self.colliding_bottom = False

    def reset_collisions(self):
        self.colliding_left = False
        self.colliding_right = False
        self.colliding_top = False
        self.colliding_bottom = False

    def update_came_from_above(self):
        if self.prev_y > self.rect.y:
            self.came_from_above = False
        elif self.prev_y >= self.rect.y and (self.colliding_right or self.colliding_left):
            self.came_from_above = False
        else:
            self.came_from_above = True

    def move(self, key):
        self.update_came_from_above()

        key_action = self.keys_dict[key]
        if key_action == "up":
            if (not self.colliding_top) and self.came_from_above:
                self.jump()
        elif key_action == "left":
            if not self.colliding_left:
                self.run_left()
        elif key_action == "down":
            pass
        elif key_action == "right":
            if not self.colliding_right:
                self.run_right()
        elif key_action == "action":
            pass
        elif key_action == "shoot":
            pass

        self.reset_collisions()

    def run_right(self):
        self.move_right(self.speed)

    def run_left(self):
        self.move_left(self.speed)

    def jump(self):
        if not self.falling:
            self.falling_velocity = self.jumping_height
            self.falling = True
            self.move_up(1)  # Gets stuck in ground if not moved up a bit.

    def crouch(self):
        pass

    def shoot(self):
        pass
