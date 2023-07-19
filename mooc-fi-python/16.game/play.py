import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))
mood = pygame.image.load('robot.png')

window.fill((0,0,0))
window.blit(mood, (0, 0))
window.blit(mood, (600, 0))
window.blit(mood, (0, 400))
window.blit(mood, (600, 400))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()