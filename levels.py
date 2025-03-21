from objects import *
from setitngs import *

pygame.init()

level1 = [
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "                                                                      ",
    "             0            0                                           ",
    "                                                                      ",
    "          0   ~              0           0                            ",
    "         -- ---                        -----        ----              ",
    "@    0     00     0       --           00    ---          0           ",
    "--  ---    00    ---   --     --   -----           --------           ",
]

level1_width = len(level1[0]) * 100
level1_height = len(level1) * 50

level_objects = pygame.sprite.Group()

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = pygame.Rect(0, 0, width, height) # прозорий прямокутник з'являється у координата (0,0), він і відіграє роль камери

    def apply(self, target):
        return target.rect.move(self.state.topleft) # цей метод буде робити всі об'єкти гри видимими для камери

    def update(self, target):
        self.state = self.camera_func(self.state, target.rect) # оновлюємо положення камери, відносно певної рухомої цілі (гравця)


# налаштування розмірів та положення камери
def camera_config(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l + W / 2, -t + H / 2 # налаштовуємо положення камери, відносно гравця

    l = min(0, l)                    # Не виходимо за ліву межу
    l = max(-(camera.width - W), l)  # Не виходимо за праву межу
    t = max(-(camera.height - H), t) # Не виходимо за нижню межу
    t = min(0, t)                    # Не виходимо за верхню межу

    return pygame.Rect(l, t, w, h)


camera = Camera(camera_config, level1_width, level1_height)

def draw_level(level: list):
    x = y = 0
    for row in level:
        for symbol in row:
            if symbol == "-":
                platform = MapObject(x, y, 100, 50, platform_image)
                level_objects.add(platform)
                platforms.add(platform)
            elif symbol == "0":
                coin = MapObject(x, y, 60, 60, coin_image)
                level_objects.add(coin)
                coins.add(coin)
            elif symbol == "~":
                key = MapObject(x, y, 60, 60, key_image)
                level_objects.add(key)
            elif symbol == "@":
                shest = MapObject(x, y, 80, 80, chest_image)
                level_objects.add(shest)
            x += 100
        x = 0
        y += 50
        
    return level_objects, key, shest