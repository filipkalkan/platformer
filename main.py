import pygame, graphics
from character import Character

g = [0] * 1


def game_loop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                raise SystemExit

        pygame.display.update()


def init_world():
    g.draw_map()
    player1 = Character()


def run():
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
    screen = pygame.display.get_surface()
    g = graphics.Graphics(screen)


if __name__ == '__main__':
    run()
