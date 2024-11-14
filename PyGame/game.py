import sys
import pygame

from scripts.utils import load_image, load_images
from scripts.entities import PhysicsEntity
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds

class Game:
    # ------------------------- Initializing Game -----------------------------------------------------
    
    def __init__(self):
        pygame.init()

        # Set up the game window and display surface
        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        # Create a clock object to control the frame rate
        self.clock = pygame.time.Clock()

        # Movement array for handling left and right movement
        self.movement = [False, False]

        # Loading game assets (tiles, player, background, clouds)
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
        }

        # Initialize clouds with count of 16
        self.clouds = Clouds(self.assets['clouds'], count=16)

        # Create player entity with initial position (50, 50) and size (8, 15)
        self.player = PhysicsEntity(self, 'player', (50, 50), (8, 15))

        # Set up the tilemap with a tile size of 16
        self.tilemap = Tilemap(self, tile_size=16)

        # Initialize scroll values to keep track of camera movement
        self.scroll = [0, 0]

    # ------------------------- Main Game Loop -----------------------------------------------------

    def run(self):
        while True:
            # Fill the display with the background image
            self.display.blit(self.assets['background'], (0, 0))

            # Update scroll based on player's position to follow them on screen
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            # Update and render clouds with the calculated scroll offset
            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)

            # Render the tilemap with the scroll offset
            self.tilemap.render(self.display, offset=render_scroll)

            # Update player and render with the scroll offset
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            # ------------------------- Handling Events -----------------------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Quit the game if the window is closed
                    pygame.quit()
                    sys.exit()

                # Handle key down events for movement and jumping
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True  # Move left when left arrow key is pressed
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True  # Move right when right arrow key is pressed
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3  # Jump when up arrow key is pressed

                # Handle key up events to stop movement
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False  # Stop left movement when left arrow key is released
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False  # Stop right movement when right arrow key is released

            # ------------------------- Updating the Display and Locking FPS -----------------------------

            # Scale the smaller display surface to fit the main screen and update the screen
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()

            # Lock the frame rate to 60 FPS
            self.clock.tick(60)

# ------------------------- Running the Game ---------------------------------------------------------

Game().run()