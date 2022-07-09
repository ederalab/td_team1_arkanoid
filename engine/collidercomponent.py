from .component import Component
import pygame


listCollider = []
listBrick = []
class ColliderComponent(Component):
    
    
    def __init__(self, name, actor, AABB):
        super().__init__(name, actor)
        self.AABB = AABB
        self.actor = actor
        global listCollider
        global listBrick
        
    def load(self):
        from .engine import Engine
        e = Engine()
        e.collisionSystem.registerCollider(self)
        
    def update(self, deltaTime):
        self.AABB.x = self.owner.x
        self.AABB.y = self.owner.y
        
    def onCollision(self, otherCollider):
        
        if self.name != "collisionBase" and otherCollider.name == "collisionBall":
            self.owner.y= -100
            listBrick.append(1)
            #to start
            if len(listCollider) == 0:
                listCollider.append(otherCollider)
        #collision with base
        if self.name == "collisionBall" and otherCollider.name == "collisionBase":
            if len(listCollider)==1:
                listCollider.append(otherCollider)
            return True
        #collision with brick
        if self.name == "collisionBall" and otherCollider.name != "collisionBase":
            if len(listCollider)==1:
                listCollider.append(otherCollider)
            return False
           
    def removeActor(self, otherCollider):
        pass
            
          
