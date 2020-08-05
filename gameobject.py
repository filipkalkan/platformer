from abc import ABC, abstractmethod
import physics


class GameObject(ABC):
    all_objects = []

    def __init__(self, img, coordinates, graphics):
        self.img = img.convert_alpha()
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
        self.falling_velocity = 0
        self.prev_x, self.prev_y = coordinates

    def do_movement(self, pressed_keys):
        relevant_keys = [key for key in pressed_keys if key in self.keys_dict.keys()]
        for key_entry in relevant_keys:
            self.move(key_entry)
        physics.apply(self)

    # Implement specification of movement in concrete subclass
    @abstractmethod
    def move(self, key):
        pass

    def update_borders(self):
        self.left = self.x
        self.right = self.x + self.width
        self.top = self.y
        self.bottom = self.y + self.height

    def move_right(self, distance):
        self.prev_x, self.prev_y = self.x, self.y
        self.x += distance
        self.update_borders()

    def move_left(self, distance):
        self.prev_x, self.prev_y = self.x, self.y
        self.x -= distance
        self.update_borders()

    def move_up(self, distance):
        self.prev_x, self.prev_y = self.x, self.y
        self.y -= distance
        self.update_borders()

    def move_down(self, distance):
        self.prev_x, self.prev_y = self.x, self.y
        self.y += distance
        self.update_borders()

    def go_back(self):
        self.x, self.y = self.prev_x, self.prev_y
        self.update_borders()


class EnvironmentGameObject(GameObject):

    def __init__(self, img, coordinates, graphics):
        super().__init__(img, coordinates, graphics)
