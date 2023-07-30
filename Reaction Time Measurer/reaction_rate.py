import pygame
import random
import time

pygame.init()
WIDTH = 800
HEIGHT = 600
FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Reaction Time Measurer")
clock = pygame.time.Clock()

def display_target():
    x = random.randint(50, WIDTH - 50)
    y = random.randint(50, HEIGHT - 50)
    colour = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))
    rad = random.randint(30,50)
    pygame.draw.circle(screen, colour, (x, y), rad)
    pygame.display.flip()
    return x, y

def main():
    pygame.init()
    running = True
    start_time = 0
    target_displayed = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and target_displayed:
                    reaction_time = time.time() - start_time
                    print(f"Your reaction time: {reaction_time:.3f} seconds")
                    target_displayed = False

        screen.fill((0,0,0))

        if not target_displayed:
            pygame.display.set_caption("Reaction Time Measurer: When you see a circle, press space!")
            pygame.display.flip()
            pygame.time.delay(random.randint(500,1000))  # Random delay before displaying the target
            x, y = display_target()
            start_time = time.time()
            target_displayed = True

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()

pygame.quit()