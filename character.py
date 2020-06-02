import pygame
from game_object import Game_object


class Character(Game_object):

    def __init__(self, img, coordinates, speed=0.1):
        super().__init__(img, coordinates)
        self.speed = speed

    def move_right(self):
        self.x += self.speed

    def move_left(self):
        self.x -= self.speed

    def jump(self):
        pass
