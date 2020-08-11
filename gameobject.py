from abc import ABC, abstractmethod
import physics
from pygame import Rect

top_line_height = 20


class GameObject(ABC):
    all_objects = []

    def __init__(self, img, coordinates, graphics):
        self.img = img.convert_alpha()
        self.graphics = graphics
        self.all_objects.append(self)
        self.rect = Rect(coordinates, img.get_size())


class MovableGameObject(GameObject):
    all_movable_objects = []

    # keys_dict contains eg. {"w":"up", "s":"down" ...}
    def __init__(self, img, coordinates, graphics, keys_dict):
        super().__init__(img, coordinates, graphics)
        self.keys_dict = keys_dict
        self.all_movable_objects.append(self)
        self.falling = True
        self.falling_velocity = 0
        self.prev_x, self.prev_y = coordinates
        self.came_from_above = True

    def do_movement(self, pressed_keys):
        relevant_keys = [key for key in pressed_keys if key in self.keys_dict.keys()]
        physics.apply(self)
        for key_entry in relevant_keys:
            self.move(key_entry)

    # Implement specification of movement in concrete subclass
    @abstractmethod
    def move(self, key):
        pass

    def move_right(self, distance):
        self.prev_x, self.prev_y = self.rect.x, self.rect.y
        self.rect.x += distance

    def move_left(self, distance):
        self.prev_x, self.prev_y = self.rect.x, self.rect.y
        self.rect.x -= distance

    def move_up(self, distance):
        self.prev_x, self.prev_y = self.rect.x, self.rect.y
        self.rect.y -= distance

    def move_down(self, distance):
        self.prev_x, self.prev_y = self.rect.x, self.rect.y
        self.rect.y += distance

    def go_back(self):
        self.rect.x, self.rect.y = self.prev_x, self.prev_y


class EnvironmentGameObject(GameObject):

    def __init__(self, img, coordinates, graphics):
        super().__init__(img, coordinates, graphics)
