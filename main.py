# Pygame game template

import pygame
import sys
import config  # Import the config module

def init_game():
    pygame.init()
    screen = pygame.display.set_mode((config.WINDOW_WIDTH, config.WINDOW_HEIGHT))  # Use constants from config
    pygame.display.set_caption(config.TITLE)
    return screen

def handle_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True

def main():

    screen = init_game()
    clock = pygame.time.Clock() # Initialize the clock object
    
    running = True
    while running:
        running = handle_events()
        screen.fill(config.WHITE)  # Use color from config
        # Draw the initials on the screen
        def draw_rectangle(screen, rect, color, thickness):
            """Draws a rectangle on the Pygame window."""
            pygame.draw.rect(screen, color, rect, thickness)


        my_rect1 = [150, 250, 200, 150]
        thickness1 = 8 # Line thickness (width) in pixels

        draw_rectangle(screen, my_rect1, config.GREEN, thickness1)

        # Write this function above your main( ) function
        def draw_circle(screen, center, radius, color, thickness):
            """Draws a circle on the Pygame window."""
            pygame.draw.circle(screen, color, center, radius, thickness)

# Define circle arguments for the function call
        circle_center = (80, 200)  # A tuple containing the center point of the circle (x, y coordinate pair)
        circle_radius = 65          # Radius of the circle
        circle_color = config.GREEN   # Color of the circle
        circle_thickness = 2        # 0 pixels creates a filled in circle

# Call the function that draws the circle from your main() function
        draw_circle(screen, circle_center, circle_radius, circle_color, circle_thickness)

        # Write your draw_polygon( ) function above your main ( ) function

        def draw_polygon(screen, color, points, thickness=0):
            pygame.draw.polygon(screen, color, points, thickness)
        
        # Calling the draw_polygon ( ) function
# Points for an irregular, 5-sided shape
        points5 = [
            (60, 100),  # Top point
            (200, 300),  # Bottom right point
            (375, 200),  # Bottom left point
            (70, 400),  # Bottom left point
            (300, 700)   # Bottom left point
        ]

        # Draw an irregular, five-sided shape on the screen that's filled in with green
        thickness = 0
        draw_polygon(screen, config.GREEN, points5, thickness)


        pygame.display.flip()

        # Limit frame rate to certain number of frames per second (FPS)
        clock.tick(config.FPS)

    # Write this function above your main( ) function

    

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()

