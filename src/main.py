import pygame
import random

# inicializace hry
pygame.init()

# obrazovka
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("RALLY")

# nastaveni hry
fps = 60
clock = pygame.time.Clock()
player_start_lives = 5
car_start_speed = 2
car_speed_acceleration = 0.5
speed = 0
score = 0

player_lives = player_start_lives
car_speed = car_start_speed

car_x = random.choice([-1, 1])
car_y = random.choice([-1, 1])

# barvy
black = (0, 0, 0)

# fonty
big_font = pygame.font.Font("fonts/Emulogic.ttf", 50)
#middle_font = pygame.font.Font("font/Emulogic.ttf", 30)

# obrazky
background_image = pygame.image.load("img/silnice.png")
background_image = pygame.transform.scale(background_image, (screen_width, screen_height))
background_image_rect = background_image.get_rect()
background_image_rect.topleft = (0, 0)

car_image = pygame.image.load("img/wrc.png")
car_image = pygame.transform.scale(car_image, (300,100))
car_image_rect = car_image.get_rect()
car_image_rect.center = (screen_width//2, screen_height//2)

# texty
#score_text = middle_font.render(f"score: {score}",True, black)
#score_text_rect = score_text.get_rect()


# hlavni cyklus
lets_continue = True
while lets_continue:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False        
    
    # obrazky
    screen.blit(background_image, background_image_rect)
    screen.blit(car_image, car_image_rect)
            
    # update obrazovky
    pygame.display.update()
    
    # zpomaleni cyklu
    clock.tick(fps)

# ukonceni hry
pygame.quit