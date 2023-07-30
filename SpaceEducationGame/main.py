
import pygame
import random
import time

pygame.init()
start_time = time.time()
quizz_list = ['Did you know, there is no atmosphere in space, which means that sound has no medium or way to travel to be heard.', 'Did you know ,Venus is the hottest planet in the solar system and has an average surface temperature of around 450° C. ', 'Did you know, While the entire suit costs a cool $12m, 70percent of that cost is for the backpack and control module.', 'Did you know , The Sun accounts for 99.86 percent of the mass in our solar system with a mass of around 330,000 times that of Earth. ', 'Did you know ,Just as colors are made more dramatic in sunsets on Earth, sunsets on Mars, according to NASA,  would appear bluish to human observers watching from the red planet.', 'Did you know, The universe extends far beyond our own galaxy, scientists estimate the universe contains approximately 1,000,000,000,000,000,000,000,000 stars, or a septillion.', 'Did you know, there is a planet made of diamonds twice the size of earth The "super earth,"is made of graphite and diamond. ', ' Did you know, The Moon has no atmosphere, which means there is no wind to erode the surface .This means the footprint will be there for millions of years.', 'Did you know, The largest known asteroid is 965 km (600 mi) wide.', 'Did you know, The Moon was once a piece of the Earth.']
# Create the screen.
screen = pygame.display.set_mode((1600, 800))
# Load images.
player_image = pygame.image.load("player.png")
background_image = pygame.image.load("background.png")
obstacle_image = pygame.image.load("rocks.png")
energy_image = pygame.image.load("energy.png")
#Create rects with positions and sizes
player = pygame.Rect(700, 400, 100,100)
background = pygame.Rect(0, 0, 1500, 800)
obstacle1 = pygame.Rect(random.randint(0, 120),random.randint(100, 600), 100, 100)
obstacle2 = pygame.Rect(random.randint(0, 120), random.randint(110, 500), 100, 100)
obstacle3 = pygame.Rect(random.randint(0, 120), random.randint(130, 450), 100, 100)
energy = pygame.Rect(random.randint(0, 1100), random.randint(0,750), 100, 100)
counter = 0
index = 1
elapsed_time = 0
bonus_points = 0
while True:
    # Handle events.
    if obstacle1.x > 1599:
        obstacle1.x = 0
        counter +=1
        obstacle1 = pygame.Rect(200,random.randint(0, 1000), 50, 50)
    if obstacle2.x > 1599:
        obstacle2.x = 0
        obstacle2 = pygame.Rect(200,random.randint(0, 1000), 50, 50)
    if obstacle3.x > 1599:
        obstacle3.x = 0
        obstacle3 = pygame.Rect(200,random.randint(0, 1000), 50, 50)
    if elapsed_time%3 == 0:
        energy = pygame.Rect(random.randint(0, 1100), random.randint(0,700), 100, 100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    # Update the player.
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        player.x -= 10
    elif pygame.key.get_pressed()[pygame.K_RIGHT]:
        player.x += 10
    if pygame.key.get_pressed()[pygame.K_UP]:
        player.y -= 10
    elif pygame.key.get_pressed()[pygame.K_DOWN]:
        player.y += 10
    player.clamp_ip(background)
    end_time = time.time()
    elapsed_time = round(end_time - start_time + bonus_points*3, 2)
    if (elapsed_time % 4 == 0 & (elapsed_time < float(25))):
        index +=1
    # Update the obstacles speed.
    obstacle1.x += (index * 4)
    obstacle2.x += (index * 4)
    obstacle3.x += (index * 4)
    # Check for collision.

    if player.colliderect(obstacle1):
        quiz = random.choice(quizz_list)
        font = pygame.font.SysFont("Arial", 15)
        game_over_text = font.render(quiz, True, (255, 255, 255))
        text_rect = game_over_text.get_rect()
        text_rect.centerx = 800
        text_rect.centery = 300
        screen.blit(game_over_text, text_rect)
        pygame.display.update()
        print("You lost!")
        time.sleep(5)
        break
    if player.colliderect(obstacle2):
        quiz = random.choice(quizz_list)
        font = pygame.font.SysFont("Arial", 15)
        game_over_text = font.render(quiz, True, (255, 255, 255))
        text_rect = game_over_text.get_rect()
        text_rect.centerx = 800
        text_rect.centery = 300
        screen.blit(game_over_text, text_rect)
        pygame.display.update()
        print("You lost!")
        time.sleep(5)
        break
    if player.colliderect(obstacle3):
        quiz = random.choice(quizz_list)
        font = pygame.font.SysFont("Arial", 15)
        game_over_text = font.render(quiz, True, (255, 255, 255))
        text_rect = game_over_text.get_rect()
        text_rect.centerx = 800
        text_rect.centery = 300
        screen.blit(game_over_text, text_rect)
        pygame.display.update()
        print("You lost!")
        time.sleep(5)
        break
    if player.colliderect(energy):
        bonus_points +=1
        energy = pygame.Rect(random.randint(0, 1100), random.randint(0,700), 100, 100)
    score_font = pygame.font.SysFont("Arial", 50)
    stringtime = str(elapsed_time)
    score = score_font.render(stringtime, 1, (200,150, 40))
    # Draw9
    screen.blit(score, (700,350))
    screen.blit(background_image, background)
    screen.blit(obstacle_image, obstacle1)
    screen.blit(obstacle_image, obstacle2)

    screen.blit(obstacle_image, obstacle3)
    screen.blit(energy_image, energy)
    screen.blit(player_image, player)
    screen.blit(score, (1400,10))
    pygame.display.update()
