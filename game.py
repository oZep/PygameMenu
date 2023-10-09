import sys
import os
import math
import random
import pygame

from scripts.utils import load_image, load_images, Animation
from scripts.UI import TextUI

class Game:
    def __init__(self):
        '''
        initializes Game
        '''
        pygame.init()

        # change the window caption
        pygame.display.set_caption("Menu")
        # create window
        self.screen = pygame.display.set_mode((640, 480)) # (640, 480), (960, 720), (768, 576)

        self.display_white = pygame.Surface((320, 240), pygame.SRCALPHA) # render on smaller resolution then scale it up to bigger screen

        self.display_2 = pygame.Surface((320, 240))

        # creating 'camera' 
        self.scroll = [0, 0]


        self.clock = pygame.time.Clock()
        self.escaped = 0
        
        self.movement = [False, False, False, False] 

        self.assets = {
            'tile_a': load_image('entities/UI/tile_a'),
            'tile_b': load_image('entities/UI/tile_b'),
            'tile_c': load_image('entities/UI/tile_c'),
            'tile_d': load_image('entities/UI/tile_d'),
            'tile_e': load_image('entities/UI/tile_e'),
            'tile_f': load_image('entities/UI/tile_f'),
            'tile_g': load_image('entities/UI/tile_g'),
            'tile_h': load_image('entities/UI/tile_h'),
            'tile_i': load_image('entities/UI/tile_i'),
            'tile_j': load_image('entities/UI/tile_j'),
            'tile_k': load_image('entities/UI/tile_k'),
            'tile_l': load_image('entities/UI/tile_l'),
            'tile_m': load_image('entities/UI/tile_m'),
            'tile_n': load_image('entities/UI/tile_n'),
            'tile_o': load_image('entities/UI/tile_o'),
            'tile_p': load_image('entities/UI/tile_p'),
            'tile_q': load_image('entities/UI/tile_q'),
            'tile_r': load_image('entities/UI/tile_r'),
            'tile_s': load_image('entities/UI/tile_s'),
            'tile_t': load_image('entities/UI/tile_t'),
            'tile_u': load_image('entities/UI/tile_u'),
            'tile_v': load_image('entities/UI/tile_v'),
            'tile_w': load_image('entities/UI/tile_w'),
            'tile_x': load_image('entities/UI/tile_x'),
            'tile_y': load_image('entities/UI/tile_y'),
            'tile_z': load_image('entities/UI/tile_z'),
            'tile_up': load_image('entities/UI/tile_up'),
            'tile_down': load_image('entities/UI/tile_down'),
            'tile_left': load_image('entities/UI/tile_left'),
            'tile_right': load_image('entities/UI/tile_right'),
            'background': load_image('background.png'),
        }



    def run(self):
        '''
        runs the Game
        '''

        # creating an infinite game loop
        while True:

            self.display_white.fill((255, 255, 255, 0))    # black outlines
            # clear the screen for new image generation in loopd
            self.display_2.blit(self.assets['background'], (0,0)) # no outline


            # move 'camera' to focus on player, make him the center of the screen
            self.scroll[0] += (- self.scroll[0])  / 30  # x axis
            self.scroll[1] += (- self.scroll[1]) / 30

            # fix the jitter
            render_scroll = (int(self.scroll[0]), int(self.scroll[1]))



            for event in pygame.event.get():
                if event.type == pygame.QUIT: # have to code the window closing
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a: # referencing WASD
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                    if event.key == pygame.K_ESCAPE:
                        self.menu.enter()
                if event.type == pygame.KEYUP: # when key is released
                    if event.key == pygame.K_a: 
                        self.movement[0] = False
                    if event.key == pygame.K_d: 
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
            
            self.display_2.blit(self.display_white, (0, 0)) # white 
            self.screen.blit(pygame.transform.scale(self.display_2, self.screen.get_size()), (0,0)) # render (now scaled) display image on big screen
            pygame.display.update()
            self.clock.tick(60) # run at 60 fps, like a sleep

# returns the game then runs it
Game().run()