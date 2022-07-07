import pygame.locals
from .component import *


class FloatingMovementComponent(Component):
    def __init__(self, name, actor):    
        from .engine import Engine

        super().__init__(name, actor)
        engine = Engine() # this is a singleton, don't worry too much
        engine.inputSystem.bindToKeyboard(pygame.locals.K_LEFT, self.keyPressed)
        engine.inputSystem.bindToKeyboard(pygame.locals.K_RIGHT, self.keyPressed)

        self.vx = 0
        self.vy = 0
        
    def update(self, deltaTime):
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime
        
        if self.owner.x < 75:
            self.vx = 0
        # inertia
        if self.vx > 0:
            self.vx = self.vx - 100 * deltaTime
        if self.vx < 0:
            self.vx = self.vx + 100 * deltaTime
        if self.vy > 0:
            self.vy = self.vy - 100 * deltaTime
        if self.vy < 0:
            self.vy = self.vy + 100 * deltaTime
            
    def keyPressed(self, key):
        if key == pygame.locals.K_LEFT:
            if self.owner.x < 40:
                self.owner.x = 40
            else: self.vx = -100
        if key == pygame.locals.K_RIGHT:
            if self.owner.x > 600:
                self.owner.x = 600
            else: self.vx = 100