import pygame.locals
from .component import *
from .bouncingmovementcomponent import *
from engine.collidercomponent import *


class FloatingMovementComponent(Component):
    def __init__(self, name, actor):    
        from .engine import Engine

        super().__init__(name, actor)
        engine = Engine() # this is a singleton, don't worry too much
        engine.inputSystem.bindToKeyboard(pygame.locals.K_LEFT, self.keyPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_RIGHT, self.keyPressed)
        
        global counter_center
        global listBrick
        global counter
        self.vx = 0
        self.vy = 0
        
    def update(self, deltaTime):
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime
        
        if self.owner.x < 75:
            self.vx = 0
        
        #center base when press space or lose or win
        if len(counter_center)==1 or len(counter)<1 or len(listBrick)>30:
            self.owner.x = 320
            self.vx = 0
            counter_center.clear()
            
        # inertia
        if self.vx > 0:
            self.vx = self.vx - 250 * deltaTime
        if self.vx < 0:
            self.vx = self.vx + 250 * deltaTime
            
    def keyPressed(self, key):
        if key == pygame.locals.K_LEFT:
            if self.owner.x < 40:
                self.owner.x = 40
            else: self.vx = -160
        if key == pygame.locals.K_RIGHT:
            if self.owner.x > 600:
                self.owner.x = 600
            else: self.vx = 160
        