import pygame
import sys
from scripts.UI import Button, TextUI

def buttonSelect():
    for event in pygame.event.get():
        if event.type == pygame.QUIT: # have to code the window closing
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                return 'a'
            if event.key == pygame.K_b:
                return 'b'
            if event.key == pygame.K_c:
                return 'c'
            if event.key == pygame.K_d:
                return 'd'
            if event.key == pygame.K_e:
                return 'e'
            if event.key == pygame.K_f:
                return 'f'
            if event.key == pygame.K_g:
                return 'g'
            if event.key == pygame.K_h:
                return 'h'
            if event.key == pygame.K_i:
                return 'i'
            if event.key == pygame.K_j:
                return 'j'
            if event.key == pygame.K_l:
                return 'l'
            if event.key == pygame.K_m:
                return 'm'
            if event.key == pygame.K_n:
                return 'n'
            if event.key == pygame.K_o:
                return 'o'
            if event.key == pygame.K_p:
                return 'p'
            if event.key == pygame.K_q:
                return 'q'
            if event.key == pygame.K_r:
                return 'r'
            if event.key == pygame.K_s:
                return 's'
            if event.key == pygame.K_t:
                return 't'
            if event.key == pygame.K_u:
                return 'u'
            if event.key == pygame.K_v:
                return 'v'
            if event.key == pygame.K_w:
                return 'w'
            if event.key == pygame.K_x:
                return 'x'
            if event.key == pygame.K_y:
                return 'y'
            if event.key == pygame.K_z:
                return 'z'
            if event.key == pygame.K_UP:
                return 'up'
            if event.key == pygame.K_DOWN:
                return 'down'
            if event.key == pygame.K_LEFT:
                return 'left'
            if event.key == pygame.K_RIGHT:
                return 'right'
    
    
class MenuPages():
    def __init__(self, game, screens):
        self.sceneIndex = 0
        self.game = game
        self.screens = screens # list [move/forward button, random button, text, etc]



    def back(self):
        self.sceneIndex = max(0, self.sceneIndex-1)

    def update(self):
        if self.screens[self.sceneIndex][0].isClicked():
            self.sceneIndex = min(self.sceneIndex+1, len(self.screens))


    def renderScreen(self, display):
        for ui in self.screens[self.sceneIndex]:
            ui.render(display) # render all elements of that scene
        
    def getScene(self):
        pass
