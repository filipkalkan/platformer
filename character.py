import pygame
from gameobject import MovableGameObject


class Character(MovableGameObject):

    def __init__(self, img, coordinates, graphics, keys_dict, speed=1):
        super().__init__(img, coordinates, graphics, keys_dict)
        self.speed = speed

    def move(self, key):
        key_action = self.keys_dict[key]
        if key_action == "up":
            pass
        elif key_action == "left":
            self.move_left()
        elif key_action == "down":
            pass
        elif key_action == "right":
            self.move_right()
        elif key_action == "action":
            pass
        elif key_action == "shoot":
            pass

    def move_right(self):
        self.x += self.speed
        self.left = self.x
        self.right = self.x + self.width

    def move_left(self):
        self.x -= self.speed
        self.left = self.x
        self.right = self.x + self.width

    def jump(self):
        pass

    def crouch(self):
        pass
