import sys
import math
import random

import pygame

from scripts.utils import load_image, load_images, Animation
from scripts.entities import PhysicsEntity, Player, Enemy
from scripts.tilemap import Tilemap
from scripts.clouds import Clouds
from scripts.particle import Particle
from scripts.spark import Spark

class Game:

    # -----------------------------Initializing Game Class-----------------------------------------------------

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Set title for game screen
        pygame.display.set_caption("Ninja Game")
        self.screen = pygame.display.set_mode((640, 480))
        self.display = pygame.Surface((320, 240))

        # Create clock object
        self.clock = pygame.time.Clock()
        
        # Track movement (left and right)
        self.movement = [False, False]
        
        # Load assets
        self.assets = {
            'decor': load_images('tiles/decor'),
            'grass': load_images('tiles/grass'),
            'large_decor': load_images('tiles/large_decor'),
            'stone': load_images('tiles/stone'),
            'player': load_image('entities/player.png'),
            'background': load_image('background.png'),
            'clouds': load_images('clouds'),
            'enemy/idle': Animation(load_images('entities/enemy/idle'), img_dur=6),
            'enemy/run': Animation(load_images('entities/enemy/run'), img_dur=4),
            'player/idle': Animation(load_images('entities/player/idle'), img_dur=6),
            'player/run': Animation(load_images('entities/player/run'), img_dur=4),
            'player/jump': Animation(load_images('entities/player/jump')),
            'player/slide': Animation(load_images('entities/player/slide')),
            'player/wall_slide': Animation(load_images('entities/player/wall_slide')),
            'particle/leaf': Animation(load_images('particles/leaf'), img_dur=20, loop=False),
            'particle/particle': Animation(load_images('particles/particle'), img_dur=6, loop=False),
            'gun': load_image('gun.png'),
            'projectile': load_image('projectile.png'),
        }
        
        # Initialize game elements
        self.clouds = Clouds(self.assets['clouds'], count=16)
        self.player = Player(self, (50, 50), (8, 15))
        self.tilemap = Tilemap(self, tile_size=16)
        self.load_level(0)

    # -----------------------------Loading Level-----------------------------------------------------

    def load_level(self, map_id):
        self.tilemap.load(f'data/maps/{map_id}.json')
        
        # Set up leaf spawners based on level layout
        self.leaf_spawners = [
            pygame.Rect(4 + tree['pos'][0], 4 + tree['pos'][1], 23, 13)
            for tree in self.tilemap.extract([('large_decor', 2)], keep=True)
        ]
        
        # Populate enemies and player spawn points
        self.enemies = []
        for spawner in self.tilemap.extract([('spawners', 0), ('spawners', 1)]):
            if spawner['variant'] == 0:
                self.player.pos = spawner['pos']
            else:
                self.enemies.append(Enemy(self, spawner['pos'], (8, 15)))
            
        # Initialize lists for projectiles, particles, and sparks
        self.projectiles, self.particles, self.sparks = [], [], []
        
        # Initial scroll and death status
        self.scroll = [0, 0]
        self.dead = 0

    # -----------------------------Game Loop-----------------------------------------------------

    def run(self):
        while True:
            self.display.blit(self.assets['background'], (0, 0))
            
            # Check if player is dead and reload level if necessary
            if self.dead:
                self.dead += 1
                if self.dead > 40:
                    self.load_level(0)
            
            # Update camera scroll to follow player
            self.scroll[0] += (self.player.rect().centerx - self.display.get_width() / 2 - self.scroll[0]) / 30
            self.scroll[1] += (self.player.rect().centery - self.display.get_height() / 2 - self.scroll[1]) / 30
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))
            
            # Spawn leaf particles at trees
            for rect in self.leaf_spawners:
                if random.random() * 49999 < rect.width * rect.height:
                    pos = (rect.x + random.random() * rect.width, rect.y + random.random() * rect.height)
                    self.particles.append(Particle(self, 'leaf', pos, velocity=[-0.1, 0.3], frame=random.randint(0, 20)))
            
            # Update and render clouds, tilemap, enemies, and player
            self.clouds.update()
            self.clouds.render(self.display, offset=render_scroll)
            self.tilemap.render(self.display, offset=render_scroll)
            
            for enemy in self.enemies.copy():
                if enemy.update(self.tilemap, (0, 0)):
                    self.enemies.remove(enemy)
                enemy.render(self.display, offset=render_scroll)
            
            if not self.dead:
                self.player.update(self.tilemap, (self.movement[1] - self.movement[0], 0))
                self.player.render(self.display, offset=render_scroll)
            
            # Update and render projectiles
            for projectile in self.projectiles.copy():
                # Moving projectile and checking for collision
                projectile[0][0] += projectile[1]
                projectile[2] += 1
                img = self.assets['projectile']
                self.display.blit(img, (projectile[0][0] - img.get_width() / 2 - render_scroll[0], projectile[0][1] - img.get_height() / 2 - render_scroll[1]))
                
                if self.tilemap.solid_check(projectile[0]) or projectile[2] > 360:
                    self.projectiles.remove(projectile)
                    for _ in range(4):
                        self.sparks.append(Spark(projectile[0], random.random() - 0.5 + (math.pi if projectile[1] > 0 else 0), 2 + random.random()))
                
                elif abs(self.player.dashing) < 50 and self.player.rect().collidepoint(projectile[0]):
                    self.projectiles.remove(projectile)
                    self.dead += 1
                    for _ in range(30):
                        angle = random.random() * math.pi * 2
                        speed = random.random() * 5
                        self.sparks.append(Spark(self.player.rect().center, angle, 2 + random.random()))
                        self.particles.append(Particle(self, 'particle', self.player.rect().center, velocity=[math.cos(angle + math.pi) * speed * 0.5, math.sin(angle + math.pi) * speed * 0.5], frame=random.randint(0, 7)))
            
            # Update and render sparks and particles
            for spark in self.sparks.copy():
                if spark.update():
                    self.sparks.remove(spark)
                spark.render(self.display, offset=render_scroll)
            
            for particle in self.particles.copy():
                if particle.update():
                    self.particles.remove(particle)
                particle.render(self.display, offset=render_scroll)
                if particle.type == 'leaf':
                    particle.pos[0] += math.sin(particle.animation.frame * 0.035) * 0.3
            
            # Handle events for player movement
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                    if event.key == pygame.K_UP:
                        self.player.jump()
                    if event.key == pygame.K_x:
                        self.player.dash()
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
            
            # Update screen display and lock FPS
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

# -----------------------------------------------Run Game----------------------------------------------------
Game().run()