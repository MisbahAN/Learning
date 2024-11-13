import sys
import pygame

class Game:
    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Sets caption/title for game screen
        pygame.display.set_caption("Ninja Game")

        # Creates a window with resolution 640 by 480
        self.screen = pygame.display.set_mode((640, 480)) # Screen is black by default

        # Create an instance of a clock object
        self.clock = pygame.time.Clock()
    
    def run(self):
        while True:
            # So the screen doesnt freeze
            for event in pygame.event.get(): 
                if event.type == pygame.QUIT: # if user closes the application 
                    pygame.quit()
                    sys.exit()

            pygame.display.update()
            self.clock.tick(60) # Fixes to 60 FPS

# Run game
Game().run()