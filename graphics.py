import pygame, graphics_components
from gameobject import EnvironmentGameObject


class Graphics:

    def __init__(self, screen):
        self.screen = screen

    def draw_ground(self):
        block = graphics_components.ground_flat
        x = 0
        y = self.screen.get_size()[1] - block.get_size()[1]
        while x < self.screen.get_size()[0]:
            ground_tile = EnvironmentGameObject(block, (x, y), self)
            self.blit(ground_tile)
            x += block.get_size()[0]

    def draw_map(self):
        self.screen.fill(graphics_components.Color.SKY)
        self.draw_ground()

    def blit(self, obj):
        self.screen.blit(obj.img, (obj.x, obj.y))

    def clear(self):
        self.screen.fill(graphics_components.Color.SKY)
