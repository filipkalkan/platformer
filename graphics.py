import pygame, graphics_components


class Graphics:

    def __init__(self, screen):
        self.screen = screen

    def draw_ground(self):
        block = graphics_components.ground_flat
        x = 0
        y = self.screen.get_size()[1] - block.get_size()[1]
        while x < self.screen.get_size()[0]:
            self.screen.blit(block, (x, y))
            x += block.get_size()[0]

    def draw_map(self):
        self.screen.fill(graphics_components.Color.SKY)
        self.draw_ground()

    def blit(self, obj):
        self.screen.blit(obj.img, (obj.x, obj.y))
