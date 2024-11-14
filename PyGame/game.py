import sys
import pygame

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds

class Game:
    
    # -----------------------------Initializing Game Class-----------------------------------------------------    

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Sets caption/title for game screen
        pygame.display.set_caption('ninja game')

        # Creates a window with resolution 640 by 480
        self.screen = pygame.display.set_mode((640, 480))

        # Creates a surface for rendering the game at a smaller resolution (320 by 240)
        self.display = pygame.Surface((320, 240))

        # Create an instance of a clock object to control frame rate
        self.clock = pygame.time.Clock()

        # Movement array for left and right keys (0 for left, 1 for right)
        self.movement = [False, False]

        # Loading game assets: decor, grass, large decor, stone, player, background, and clouds images
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
        }

        # Initializing clouds with a count of 16
        self.clouds = Clouds(self.assets['clouds'], count=16)

        # Initializing player entity with position (50, 50) and size (8, 15)
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        # Initializing tilemap with a tile size of 16
        self.tilemap = Tilemap(self, tile_size=16)

        # Scroll variables for camera following player
        self.scroll = [0, 0]

    # -----------------------------Run Game Function-----------------------------------------------------    

    def run(self):
        while True:
            # Filling the display with background image
            self.display.blit(self.assets['background'], (0, 0))

            # Calculate scroll to center the player on screen
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30

            # Convert scroll to integer for rendering offset
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            # Update and render clouds with scroll offset
            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)

            # Render the tilemap with scroll offset
            self.tilemap.render(self.display, offset=render_scroll)

            # Update and render the player with scroll offset
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            # -----------------------------Handling Events-----------------------------------------------------    

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Quit game if user closes the window
                    pygame.quit()
                    sys.exit()

                # Handle key presses for movement and player jump
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True  # Move left when left arrow key pressed
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True  # Move right when right arrow key pressed
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3  # Jump when up arrow key pressed

                # Handle key releases to stop movement
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False  # Stop left movement when left arrow key released
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False  # Stop right movement when right arrow key released

            # -----------------------------Update Display and Lock FPS---------------------------------------  

            # Scaling the display surface to fit the main screen and updating the screen
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()

            # Lock the frame rate to 60 FPS
            self.clock.tick(60)

# -----------------------------------------------Run Game----------------------------------------------------
Game().run()