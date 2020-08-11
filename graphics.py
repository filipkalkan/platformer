import pygame, graphics_components
from gameobject import EnvironmentGameObject, MovableGameObject


class Graphics:

    def __init__(self, display):
        self.display = display
        self.screen = display.get_surface()
        self.dirty_rects = []
        self.new_rects = []

    def draw_ground(self):
        block = graphics_components.ground_flat
        x = 0
        y = self.screen.get_size()[1] - block.get_size()[1]
        while x < self.screen.get_size()[0]:
            ground_tile = EnvironmentGameObject(block, (x, y), self)
            self.blit(ground_tile)
            x += block.get_size()[0]

    def draw_middle_piece(self):
        block = graphics_components.ground_flat
        x = block.get_size()[0] * 6
        y = self.screen.get_size()[1] - 2 * block.get_size()[1]
        ground_tile = EnvironmentGameObject(block, (x, y), self)
        self.blit(ground_tile)

    def draw_side_pieces(self):
        block = graphics_components.ground_flat
        x = 0
        y = self.screen.get_size()[1] - 4 * block.get_size()[1]
        for i in range(4):
            ground_tile = EnvironmentGameObject(block, (x, y), self)
            self.blit(ground_tile)
            x += block.get_size()[0]
            if i == 1:
                x = self.screen.get_size()[0] - 2 * block.get_size()[0]

    def draw_map(self):
        self.screen.fill(graphics_components.Color.SKY)
        self.draw_ground()
        self.draw_side_pieces()
        self.draw_middle_piece()

    def blit(self, obj):
        if isinstance(obj, MovableGameObject):
            background_surface = pygame.Surface((obj.rect.width, obj.rect.height))
            background_surface.fill(graphics_components.Color.SKY)
            self.screen.blit(background_surface, (obj.prev_x, obj.prev_y))
            self.dirty_rects.append(background_surface.get_rect())

        self.screen.blit(obj.img, (obj.rect.x, obj.rect.y))
        self.new_rects.append(obj.rect)

    def clear(self):
        self.screen.fill(graphics_components.Color.SKY)

    def update(self):
        self.display.update(self.dirty_rects + self.new_rects)