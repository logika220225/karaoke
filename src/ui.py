import pygame

WIDTH = 1280
HEIGHT = 600


BLACK = (0, 0, 0)

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("<Your game>")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()

running = True
while running:

    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

all_sprites.draw(screen)

screen.fill(BLACK)

pygame.display.flip()

pygame.quit()
