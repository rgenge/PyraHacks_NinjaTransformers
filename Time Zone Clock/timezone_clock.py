import pygame
import time
from datetime import datetime, timedelta

pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
FONT_SIZE = 20
timezones = {
    "UTC": 0,
    "EDT (Toronto)": -4,
    "NDT (St. John's)": -2.5,
    "ADT (Halifax)": -3,
    "EST (Coral Harbour)": -5,
    "CDT (Winnipeg)": -5,
    "CST (Regina)": -6,
    "MDT (Edmonton)": -6,
    "PDT (Vancouver)": -7,
    "AST (Blanc-Sablon)": -4,
}

# Colors
DARKBROWN = (92, 64, 51)
BEIGE = (211, 182, 156)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Canadian Time Zones")

# Create a font for displaying the time
font = pygame.font.SysFont("Impact", FONT_SIZE, bold=False)

def get_time_in_timezone(timezones):
    return datetime.utcnow() + timedelta(hours=timezones)

# Main game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get the current time for each time zone
    times = {
        name: get_time_in_timezone(offset).strftime("%H:%M:%S") for name, offset in timezones.items()
    }

    screen.fill(BEIGE)

    # Display the times on the screen
    y = 30
    for name, time_str in times.items():
        text = font.render(f"{name}: {time_str}", True, DARKBROWN)
        text_rect = text.get_rect(center=(WIDTH // 2, y))
        screen.blit(text, text_rect)
        y += 60

    pygame.display.flip()
    clock.tick(1)  # Update the time every 1 second

pygame.quit()