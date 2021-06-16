import pygame
from game import Game
pygame.init()

pygame.display.set_caption("Game to be constructed")
screen = pygame.display.set_mode((1080, 720))
background = pygame.image.load('assets/bg.jpg')

# load game
game = Game()


running = True
while running:

    screen.blit(background, (0, -200))

    screen.blit(game.player.image, game.player.rect)

    game.player.all_projectiles.draw(screen)

    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x + game.player.rect.width < screen.get_width():
        game.player.move_right()
    elif game.pressed.get(pygame.K_LEFT) and game.player.rect.x > 0:
        game.player.move_left()

    print(game.player.rect.x)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("Game closed")
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

