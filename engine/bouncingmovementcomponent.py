from .component import *
from engine.collidercomponent import *
import pygame.locals

class BouncingMovementComponent(Component):
    # Owner could be empty at first
    def __init__(self, name, actor, boundingRect, vx, vy):
        from .engine import Engine
        
        engine = Engine() # this is a singleton, don't worry too much
        engine.inputSystem.bindToKeyboard(pygame.locals.K_SPACE, self.keyPressed)
        super().__init__(name, actor)
        self.vx = vx
        self.vy = vy
        global listCollider
        self.boundingRect = boundingRect

    # I could implement some debugging rendering here
    def render(self, surface):
        pass

    # There will be timing involved
    def update(self, deltaTime): 
        
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime


        # bounce on the x axis
        if self.owner.x < 0 or self.owner.x > self.boundingRect.width:
            self.vx = - self.vx
        
        # bounce on the y axis
        if self.owner.y < 0:
            self.vy = - self.vy
        
        if len(listCollider)>=2:
            print(listCollider[0].name, listCollider[1].name)
            if ColliderComponent.onCollision(listCollider[0], listCollider[1]) == True:
                self.vy = - self.vy
                listCollider.clear()
        
        """
        if self.owner.y > 618:
            self.owner.y = -1000"""
            
    #to start
    def keyPressed(self, key):
        if key == pygame.locals.K_SPACE:
            self.owner.x = 320
            self.owner.y = 580