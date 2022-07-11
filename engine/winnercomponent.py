from .component import Component
from .bouncingmovementcomponent import *
from engine.collidercomponent import *
import pygame

class WinnerComponent(Component):
    def __init__(self, assetFileName, name, actor, n_actor):
        super().__init__(name, actor)
        self.assetFileName = assetFileName
        global listBrick
        self.image = None
        self.n_actor = n_actor

    def load(self):
        self.image = pygame.image.load(self.assetFileName)
        
            
    def render(self, surface):
        #for win
        if len(listBrick)>self.n_actor and self.image != None:
            rect = self.image.get_rect()
            rect.centerx = self.owner.x
            rect.centery = self.owner.y
            surface.blit(self.image, rect)