from objects import *
from levels import *

pygame.init()

level1_objects, key, shest = draw_level(level1)

player = Player(50, H - 90, 40, 50, 11, player_images)
portal1 = MapObject(2100, 450, 90, 90, portal1_image)


level1_objects.add(player)
level1_objects.add(portal1)

game = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False

    window.blit(bg, (0, 0))
    key_pressed = pygame.key.get_pressed()
    for obj in level1_objects:
        window.blit(obj.image, camera.apply(obj))
    camera.update(player)
    player.update(platforms)

    window.blit(pygame.transform.scale(coin_image, (100, 100)), (0, 0))
    coin_txt = font1.render(f":{coins_count}", True, (0, 0, 0))
    window.blit(coin_txt, (75, 27))

    if pygame.sprite.spritecollide(player, coins, True):
        coins_count += 1

    if pygame.sprite.collide_rect(player, key):
        window.blit(get_key_txt, (W // 2, 50))
        if key_pressed[pygame.K_e]:
            is_key = True
            key.rect.x = -300

    if pygame.sprite.collide_rect(player, shest):
        if is_key == True:
            window.blit(get_key_txt, (W // 2, 50))
            if key_pressed[pygame.K_e]:
                coins_count += 10
                is_key == False
                key.rect.x = -300

    if pygame.sprite.collide_rect(player, shest) and not is_key:
        window.blit(find_key_txt, (W // 2, 50))

    pygame.display.update()
    clock.tick(FPS)