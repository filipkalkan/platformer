from abc import ABC, abstractmethod


class Game_object(ABC):

    def __init__(self, img, coordinates, graphics):
        self.img = img
        self.x, self.y = coordinates
        self.graphics = graphics

class Movable_game_object(Game_object):
    all_movable_objects = []
    #keys_dict contains eg. {"w":"up", "s":"down" ...}
    def __init__(self, img, coordinates, graphics, keys_dict):
        super().__init__(img, coordinates, graphics)
        self.keys_dict = keys_dict
        self.all_movable_objects.append(self)

    def do_movement(self, pressed_keys):
        relevant_keys = [key for key in pressed_keys if key in self.keys_dict.keys()]
        for key_entry in relevant_keys:
            self.move(relevant_keys[key_entry.key])

    #Implement specification of movement in concrete subclass
    @abstractmethod
    def move(self, key):
        pass
