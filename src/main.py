import pygame
import random

# inicializace hry
pygame.init()

# obrazovka
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("RALLY")

# nastaveni hry
fps = 60
clock = pygame.time.Clock()
player_start_lives = 5
car_start_speed = 2
car_speed_acceleration = 0.5
speed = 0

player_lives = player_start_lives
car_speed = car_start_speed

car_x = random.choice([-1, 1])
car_y = random.choice([-1, 1])

# hlavni cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False        
            
            
    # update obrazovky
    pygame.display.update()
    
    # zpomaleni cyklu
    clock.tick(fps)

# ukonceni hry
pygame.quit