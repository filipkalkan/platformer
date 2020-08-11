import pygame, graphics_components
from character import Character
from graphics import Graphics

g, clock = [0] * 2
pressed_keys = set()

def game_loop():
    global pressed_keys
    g.clear()
    g.draw_map()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit
            elif event.type in (pygame.KEYDOWN, pygame.KEYUP):
                pressed_keys = update_keys()

        for obj in Character.all_movable_objects:
            obj.do_movement(pressed_keys)
            g.blit(obj)

            g.update()
            clock.tick(200)

def update_keys():
    new_pressed_keys = set()
    pressed = pygame.key.get_pressed()
    for i, key in enumerate(pressed):
        if key:
            new_pressed_keys.add(chr(i))
    return new_pressed_keys


def init_world():
    g.draw_map()
    keys_dict = {"w":"up", "a":"left", "s":"down", "d":"right"}
    player1 = Character(graphics_components.Characters.Adventurer.standing, (500, 450), g, keys_dict)
    g.blit(player1)


def run():
    global clock
    clock = pygame.time.Clock()
    pygame.init()
    init_display()
    init_world()
    game_loop()


def init_display():
    global g

    pygame.display.set_mode((1200, 800))
    logo = pygame.image.load("./images/weapon_logo.png")
    pygame.display.set_caption("Platformer")
    pygame.display.set_icon(logo)
    g = Graphics(pygame.display)


if __name__ == '__main__':
    run()
