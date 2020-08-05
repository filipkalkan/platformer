import pygame
from gameobject import MovableGameObject


class Character(MovableGameObject):

    def __init__(self, img, coordinates, graphics, keys_dict, speed=3):
        super().__init__(img, coordinates, graphics, keys_dict)
        self.speed = speed
        self.jumping_height = -6

    def move(self, key):
        key_action = self.keys_dict[key]
        if key_action == "up":
            self.jump()
        elif key_action == "left":
            self.run_left()
        elif key_action == "down":
            pass
        elif key_action == "right":
            self.run_right()
        elif key_action == "action":
            pass
        elif key_action == "shoot":
            pass

    def run_right(self):
        self.move_right(self.speed)

    def run_left(self):
        self.move_left(self.speed)

    def jump(self):
        if not self.falling:
            self.falling_velocity = self.jumping_height
            self.falling = True
            self.move_up(1) #Gets stuck in ground if not moved up a bit.

    def crouch(self):
        pass

    def shoot(self):
        pass
