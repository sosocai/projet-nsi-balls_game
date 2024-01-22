import pygame

pygame.init()
window = pygame.display.set_mode((700, 700))
clock = pygame.time.Clock()

pygameSurface = pygame.image.load('apple.png').convert_alpha()
pygameSurface = pygame.transform.scale(pygameSurface, (100, 100))

run = True
while run:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill((127, 127, 127))
    window.blit(pygameSurface, pygameSurface.get_rect(center = window.get_rect().center))
    rect = pygameSurface.get_rect()
    rect = rect.move((5, 5))
    pygame.display.flip()

pygame.quit()
exit()