from .component import *
from engine.collidercomponent import *
import pygame.locals

counter_center = []
counter = [1, 2, 3]
class BouncingMovementComponent(Component):
    # Owner could be empty at first
    def __init__(self, name, actor, boundingRect, vx, vy, n_actor):
        from .engine import Engine
        
        engine = Engine() # this is a singleton, don't worry too much
        engine.inputSystem.bindToKeyboard(pygame.locals.K_SPACE, self.keyPressed)
        super().__init__(name, actor)
        self.real_vx = vx
        self.real_vy = vy
        global counter_center
        global counter 
        global listCollider
        self.n_actor = n_actor
        self.boundingRect = boundingRect
        self.vx = 0
        self.vy = 0

    # I could implement some debugging rendering here
    def render(self, surface):
        pass

    # There will be timing involved
    def update(self, deltaTime): 
        
        self.owner.x += self.vx * deltaTime
        self.owner.y += self.vy * deltaTime
        #to start game
        if len(listBrick)<1:
            self.owner.x = 320
            self.owner.y = 580
            self.vx= 0
            self.vy= 0
        
        #if gameover or winner
        if len(counter)<1 or len(listBrick)>self.n_actor:
            self.owner.x = 320
            self.owner.y = 580
            self.vx = 0
            self.vy = 0

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
                counter_center.append(1)
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
            self.vx = self.real_vx
            self.vy = self.real_vy
            if len(counter_center)<1 and len(listBrick)<1:
                counter_center.append(1)
                listBrick.append(1)