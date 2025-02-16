import pygame

pygame.init()

W, H = 1280, 650
FPS = 20

window = pygame.display.set_mode((W, H))
pygame.display.set_caption("Dino")
pygame.display.set_icon(pygame.image.load("assets/images/player/move_right_3.png"))

clock = pygame.time.Clock()

bg = pygame.transform.scale(pygame.image.load("assets/backround/level1.png"), (W, H))

platform_image = pygame.image.load("assets/backround/platform.png")
