import sys
import pygame
from scripts.utils import load_images
from scripts.tilemap import Buttonmap

RENDER_SCALE = 2.0

class Editor: 
    def __init__(self):
        pygame.init()
        pygame.display.set_caption('MENU EDITOR')
        self.screen = pygame.display.set_mode((640,480))
        self.display = pygame.Surface((320,240))
        self.clock = pygame.time.Clock()

        self.assets = {'buttons': load_images('tiles/buttons')}

        self.buttonMap = Buttonmap(self, tile_size=16)

        try:
            self.buttonMap.load('map.json')
        except FileNotFoundError:
            pass

        self.tile_list = list(self.assets)
        self.menu_scene = 0
        self.button_varient = 0

        self.clicking = False
        self.right_clicking = False
        self.shift = False
        self.ongrid = True

    def run(self):
        while True:
            self.display.fill((255,255,255))
            self.buttonMap.render(self.display, offset=(0,0))
            current_button_img = self.assets[self.tile_list[self.menu_scene]][self.button_varient]
            current_button_img.set_alpha(200)


            mpos = pygame.mouse.get_pos() # gets mouse positon
            mpos = (mpos[0] / RENDER_SCALE, mpos[1] / RENDER_SCALE) # since screen scales x2
            tile_pos = (int((mpos[0] + self.scroll[0]) // self.buttonMap.tile_size), int((mpos[1]) // self.buttonMap.tile_size)) 

            if self.ongrid:
                self.display.blit(current_button_img, (tile_pos[0] * self.tilemap.tile_size - self.scroll[0], tile_pos[1] * self.tilemap.tile_size - self.scroll[1]))

            if self.clicking and self.ongrid:
                self.buttonMap.tilemap[str(tile_pos[0]) + ';' + str(tile_pos[1])] = {'type': self.tile_list[self.tile_group], 'variant': self.tile_variant, 'pos': tile_pos}
            if self.right_clicking:
                tile_loc = str(tile_pos[0]) + ";" + str(tile_pos[1]) 
                if tile_loc in self.buttonMap.tilemap:
                    #location already exists
                    del self.buttonMap.tilemap[tile_loc]

            self.display.blit(current_button_img, (5,5))


            for event in pygame.event.get():
                if event.type == pygame.QUIT: # have to code the window closing
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1: # left click, places
                        self.clicking = True
                    if event.button == 3: # right click
                        self.right_clicking = True
                if event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1: # left click
                        self.clicking = False
                    if event.button == 3: # right click
                        self.right_clicking = False
                    
                    if self.shift:
                        # scroll between variants
                        if event.button == 4: # scroll wheel up, % so no null pointer
                            self.tile_variant = (self.menu_scene - 1) % len(self.assets[self.menu_scene[self.button_varient]])
                        if event.button == 5: # scroll wheel down, % trick so no null pointer
                            self.tile_variant = (self.menu_scene + 1) % len(self.assets[self.menu_scene[self.button_varient]]])
                    else:
                        # scroll between groups
                        if event.button == 4: # scroll wheel up, % so no null pointer, len(title_list) = how many groups
                            self.tile_group = (self.menu_scene - 1) % len(self.menu_scene)
                            self.tile_variant = 0 # no index errors
                        if event.button == 5: # scroll wheel down, % trick so no null pointer
                            self.tile_group = (self.menu_scene + 1) % len(self.menu_scene)
                            self.tile_variant = 0 

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a: # referencing WASD
                        self.movement[0] = True
                    if event.key == pygame.K_d:
                        self.movement[1] = True
                    if event.key == pygame.K_w:
                        self.movement[2] = True
                    if event.key == pygame.K_s:
                        self.movement[3] = True
                    if event.key == pygame.K_LSHIFT:
                        self.shift = True
                    if event.key == pygame.K_g: # switch drawing on/offgrid 
                        self.ongrid = not self.ongrid
                    if event.key == pygame.K_o: # same tilemap
                        self.buttonMap.save('map.json') # path we are saving it to
                if event.type == pygame.KEYUP: # when key is released
                    if event.key == pygame.K_a: 
                        self.movement[0] = False
                    if event.key == pygame.K_d: 
                        self.movement[1] = False
                    if event.key == pygame.K_w:
                        self.movement[2] = False
                    if event.key == pygame.K_s:
                        self.movement[3] = False
                    if event.key == pygame.K_LSHIFT:
                        self.shift = False
            
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0)) # render (now scaled) display image on big screen
            pygame.display.update()
            self.clock.tick(60) # run at 60 fps, like a sleep

# returns the editor then runs it
Editor().run()
            
                


