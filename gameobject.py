from abc import ABC, abstractmethod
import physics


class GameObject(ABC):
    all_objects = []

    def __init__(self, img, coordinates, graphics):
        self.img = img
        self.x, self.y = coordinates
        self.graphics = graphics
        self.all_objects.append(self)
        self.width, self.height = img.get_size()
        self.left = self.x
        self.right = self.x + self.width
        self.top = self.y
        self.bottom = self.y + self.height


class MovableGameObject(GameObject):
    all_movable_objects = []

    # keys_dict contains eg. {"w":"up", "s":"down" ...}
    def __init__(self, img, coordinates, graphics, keys_dict):
        super().__init__(img, coordinates, graphics)
        self.keys_dict = keys_dict
        self.all_movable_objects.append(self)
        self.falling = True

    def do_movement(self, pressed_keys):
        relevant_keys = [key for key in pressed_keys if key in self.keys_dict.keys()]
        for key_entry in relevant_keys:
            self.move(key_entry)
        physics.apply(self)

    # Implement specification of movement in concrete subclass
    @abstractmethod
    def move(self, key):
        pass


class EnvironmentGameObject(GameObject):

    def __init__(self, img, coordinates, graphics):
        super().__init__(img, coordinates, graphics)
