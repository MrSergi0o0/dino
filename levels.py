from objects import *
from setitngs import *

pygame.init()

level1 = [
    "                                                                      ",
    "                               ---                                    ",
    "                                                                      ",
    "                                                                      ",
    "    --              --------                  ---------               ",
    "        ---                                                           ",
    "----                      -------                                     ",
    "                                                 --------             ",
    "       ---          ------------                                      ",
    "---                            --------                               ",
    "    --       -             ----                                       ",
    "       ---         --------               ----          ---           ",
    "----           ----                                                   ",
]

level1_width = len(level1[0])
level1_height = len(level1)

level_objects = pygame.sprite.Group()

def draw_level(level: list):
    x = 0
    y = 0
    for row in level:
        for symbol in row:
            if symbol == "-":
                platform = MapObject(x, y, 100, 50, platform_image)
                level_objects.add(platform)
            x += 100
        x = 0
        y += 50



    return level_objects