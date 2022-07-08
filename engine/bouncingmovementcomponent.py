from .component import *
from engine.collidercomponent import *
import pygame.locals


counter = [1, 2, 3]
class BouncingMovementComponent(Component):
    # Owner could be empty at first
    def __init__(self, name, actor, boundingRect, vx, vy):
        from .engine import Engine
        
        engine = Engine() # this is a singleton, don't worry too much
        engine.inputSystem.bindToKeyboard(pygame.locals.K_SPACE, self.keyPressed)
        super().__init__(name, actor)
        self.vx = vx
        self.vy = vy
        global counter 
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
         
        #remove life  
        if self.owner.y > 615:
            if len(counter)>0:
                counter.pop()
                self.owner.x = 320
                self.owner.y = 580
                self.vx= 0
                self.vy= 0
        
        if len(listCollider)==2:
            base = listCollider[0]
            #bouncing with base
            if ColliderComponent.onCollision(listCollider[0], listCollider[1]) == True and self.vy > 0:
                self.vy = - self.vy
                
            #bouncing with brick
            if listCollider[1].name != "collisionStart":
                if ColliderComponent.onCollision(listCollider[0], listCollider[1]) == False and self.vy < 0:
                    self.vy = - self.vy
                
            #clean the list after bouncing    
            listCollider.clear()
            listCollider.append(base)
            
            
    #to start press space
    def keyPressed(self, key):
        if key == pygame.locals.K_SPACE:
            self.owner.x = 320
            self.owner.y = 580
            self.vx = 150
            self.vy = -150
            
            