import sys
import pygame

from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhysicsEntity, Player
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds

class Game:
    # ------------------------- Initialize the Game ---------------------------------------------------
    
    def __init__(self):
        pygame.init()

        # Set up the window and display surface
        pygame.display.set_caption('ninja game')
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        # Create a clock object to control the frame rate
        self.clock = pygame.time.Clock()

        # Movement array to track player movement (left, right)
        self.movement = [False, False]

        # Load assets (tiles, player, background, clouds, and animations)
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'player/run': Animation(load_images('entities/player/run'), img_dur=4),
            'player/jump': Animation(load_images('entities/player/jump')),
            'player/slide': Animation(load_images('entities/player/slide')),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
        }

        # Initialize clouds with a count of 16
        self.clouds = Clouds(self.assets['clouds'], count=16)

        # Create player entity at position (50, 50) with size (8, 15)
        self.player = Player(self, (50, 50), (8, 15))

        # Initialize tilemap with tile size 16 and load the map
        self.tilemap = Tilemap(self, tile_size=16)
        self.tilemap.load('map.json')

        # Set initial scroll values for camera movement
        self.scroll = [0, 0]

    # ------------------------- Main Game Loop ------------------------------------------------------

    def run(self):
        while True:
            # Fill the screen with the background image
            self.display.blit(self.assets['background'], (0, 0))

            # Update scroll to center on player smoothly
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))

            # Update and render clouds with scroll offset
            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)

            # Render the tilemap with the scroll offset
            self.tilemap.render(self.display, offset=render_scroll)

            # Update and render player with the scroll offset
            self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
            self.player.render(self.display, offset=render_scroll)

            # ------------------------- Handle Events -----------------------------------------------------
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # Quit the game if the window is closed
                    pygame.quit()
                    sys.exit()

                # Handle keydown events for movement and jumping
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True  # Move left when left arrow is pressed
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True  # Move right when right arrow is pressed
                    if event.key == pygame.K_UP:
                        self.player.velocity[1] = -3  # Jump when up arrow is pressed

                # Handle keyup events to stop movement
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False  # Stop left movement when left arrow key is released
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False  # Stop right movement when right arrow key is released

            # ------------------------- Update Display and Frame Rate -----------------------------------

            # Scale the smaller display surface to fit the main screen and update the screen
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()

            # Lock the frame rate to 60 FPS
            self.clock.tick(60)

# ------------------------- Run the Game ---------------------------------------------------------

Game().run()