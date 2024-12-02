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
car_speed_acceleration = 0.1
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
midle_font = pygame.font.Font("fonts/Emulogic.ttf", 30)

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
score_text = midle_font.render(f"score:{score}",True, black)
score_text_rect = score_text.get_rect()
score_text_rect.topright = (screen_width - 30, 10)

lives_text = midle_font.render(f"zivoty:{player_start_lives}", True, black)
lives_text_rect = lives_text.get_rect()
lives_text_rect.center = (screen_width - 1100, 30)

game_over_text = big_font.render("Hra skoncila", True, black)
game_over_text_rect = game_over_text.get_rect()
game_over_text_rect.center = (screen_width//2, screen_height//2)

continue_text = midle_font.render("Klikni pro pokracovani", True, black)
continue_text_rect = continue_text.get_rect()
continue_text_rect.center = (screen_width//2, screen_height//2 + 50)

# zvuky
success_click = pygame.mixer.Sound("music/wruum.mp3")
miss_click = pygame.mixer.Sound("music/horn.mp3")
pygame.mixer.music.load("music/background.mp3")
pygame.mixer.music.set_volume(1.0)
success_click.set_volume(0.4)
miss_click.set_volume(0.4)

# hlavni cyklus
lets_continue = True
pygame.mixer.music.play(-1, 0.0)
while lets_continue:   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            lets_continue = False  

        if event.type == pygame.MOUSEBUTTONDOWN:
            click_x = event.pos[0]
            click_y = event.pos[1] 

            # Bylo kliknuto na auto 
            if car_image_rect.collidepoint(click_x, click_y):
                success_click.play()
                score += 1
                car_speed += car_speed_acceleration
                previous_x = car_x
                previous_y = car_y

                while previous_x == car_x and previous_y == car_y:
                    car_x = random.choice([-1, 1])
                    car_y = random.choice([-1, 1])    
            else:
                miss_click.play() 
                player_lives -= 1   

    # odraz auta
    if car_image_rect.left < 0 or car_image_rect.right >= screen_width:
        car_x = -1 * car_x    
    if car_image_rect.top < 0 or car_image_rect.bottom >= screen_height:    
        car_y = -1 * car_y


    # Pohyb auta
    car_image_rect.x += car_x * car_speed
    car_image_rect.y += car_y * car_speed
    
    # obrazky
    screen.blit(background_image, background_image_rect)
    screen.blit(car_image, car_image_rect)
    
    # Texty 
    screen.blit(score_text, score_text_rect)
    screen.blit(lives_text, lives_text_rect)

    # update životy a skóre
    score_text = midle_font.render(f"score:{score}",True, black)
    lives_text = midle_font.render(f"zivoty:{player_lives}", True, black)

            
    # update obrazovky
    pygame.display.update()
    
    # zpomaleni cyklu
    clock.tick(fps)

    # kontrola konce hry
    if player_lives == 0:
        screen.blit(game_over_text, game_over_text_rect)
        screen.blit(continue_text, continue_text_rect)
        pygame.display.update()

    # pozastavi hru
        pygame.mixer.music.stop() 
        pause = True
        while pause:
            # chce hrát znova
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    score = 0
                    player_lives = player_start_lives
                    car_speed = car_start_speed
                    car_image_rect.center = (screen_width//2, screen_height//2)
                    pause = False
                    car_x = random.choice([-1, 1])
                    car_y = random.choice([-1, 1])
                    pygame.mixer.music.play(-1, 0.0)
                elif event.type == pygame.QUIT:
                    pause = False
                    lets_continue = False

# ukonceni hry
pygame.quit