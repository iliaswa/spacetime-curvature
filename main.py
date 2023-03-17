import pygame
import numpy as np

# Set up Pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Curvature of Spacetime")

# Define the function that calculates the curvature of spacetime
def curvature(x, y):
    r = np.sqrt(x**2 + y**2)
    return 1.0 / (1.0 + r)

# Set up the animation loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the curvature of spacetime
    for x in range(-400, 400, 10):
        for y in range(-300, 300, 10):
            c = curvature(x/100.0, y/100.0)
            pygame.draw.rect(screen, (255*c, 255*c, 255*c), (x+400, y+300, 10, 10))

    # Update the screen
    pygame.display.flip()

    # Limit the frame rate
    clock.tick(60)

# Clean up Pygame
pygame.quit()
