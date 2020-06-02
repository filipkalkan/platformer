import pygame

tiles_path = "./images/PNG/Tiles"
adventurer_path = "./images/PNG/Characters/Adventurer/Poses"

ground_flat = pygame.image.load("./images/PNG/Tiles/platformPack_tile001.png")


class Color:
    SKY = (135, 206, 235)


class Tiles:
    ground_flat = pygame.image.load(tiles_path + "/platformPack_tile001.png")


class Characters:
    class Adventurer:
        standing = pygame.image.load(adventurer_path + "/adventurer_stand.png")
