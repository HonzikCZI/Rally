import pygame

# inicializace hry
pygame.init()

# obrazovka
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RALLY")

# hlavni cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False
            
            
    # update obrazovky
    pygame.display.update()

# ukonceni hry
pygame.quit