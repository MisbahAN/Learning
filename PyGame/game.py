import sys
import pygame

class Game:

    # -----------------------------Initializing Game Class-----------------------------------------------------    

    def __init__(self):
        # Initialize pygame
        pygame.init()

        # Sets caption/title for game screen
        pygame.display.set_caption("Ninja Game")

        # Creates a window with resolution 640 by 480
        self.screen = pygame.display.set_mode((640, 480)) # Screen is black by default

        # Create an instance of a clock object
        self.clock = pygame.time.Clock()

        # Load a cloud_1 image. NEED TO BLIT/PACK it
        self.img = pygame.image.load('data/images/clouds/cloud_1.png')
        self.img.set_colorkey((0, 0, 0)) # set colourkey for self.img to black

        self.img_pos = [160, 260]
        self.movement = [False, False] # position 0 represents up movement, position 1 represents down movement

        self.collision_area = pygame.Rect(50, 50, 300, 50) # (left, top, width, height)

    # -----------------------------Creating Run Function-----------------------------------------------------   

    def run(self):
        while True:
            # Filling screen colour with RGB values
            self.screen.fill((14, 219, 248))

            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height()) # matches exactly to the size of image to be renderred
            if img_r.colliderect(self.collision_area): # if colliding
                pygame.draw.rect(self.screen, (0, 100, 255), self.collision_area)
            else: # if not colliding
                pygame.draw.rect(self.screen, (0, 50, 155), self.collision_area)

            # Adjusting self.img_pos after each click and release of key
            self.img_pos[1] += (self.movement[1] - self.movement[0]) * 5 # The '* 5' makes the object move 5 times faster

            # Packing/Bliting self.img onto game screen at coordinates [160, 260], i.e self.img_pos. Note: Top left of game screen is [0, 0]
            self.screen.blit(self.img, self.img_pos)

            # So the screen doesnt freeze
            for event in pygame.event.get(): 

                # Quit Game if user closes the application 
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # -----------------------------Up and Down key movements---------------------------------------             
   
                # Check for up or down movements when up/down arrow-key pressed
                if event.type == pygame.KEYDOWN: # if any key pressed
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[0] = True # if up arrow-key or w key pressed, move up
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1] = True # if down arrow-keyor s pressed, move down

                if event.type == pygame.KEYUP: # if any key released
                    if event.key == pygame.K_UP or event.key == pygame.K_w:
                        self.movement[0] = False # if up arrow-key or w key released, stay still
                    if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                        self.movement[1] = False # if down arrow-key or s key released, stay still
            
            # -----------------------------Update Display and Lock FPS---------------------------------------  

            pygame.display.update()
            self.clock.tick(60) # Fixes to 60 FPS

# -----------------------------------------------Run Game----------------------------------------------------
Game().run()