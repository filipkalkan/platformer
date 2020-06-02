from abc import ABC, abstractmethod


class Game_object(ABC):

    def __init__(self, img, coordinates, screen):
        self.img = img
        self.x, self.y = coordinates
        self.screen = screen

    def blit(self, screen):
        self.screen.blit(self.img, (self.x, self.y))
