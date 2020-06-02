import pygame
from game_object import Movable_game_object


class Character(Movable_game_object):

    def __init__(self, img, coordinates, graphics, keys_dict, speed=0.1):
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

    def move_left(self):
        self.x -= self.speed

    def jump(self):
        pass
