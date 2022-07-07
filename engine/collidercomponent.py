from .component import Component
#from bouncingmovementcomponent import BouncingMovementComponent
import pygame

class ColliderComponent(Component):

    def __init__(self, name, actor, AABB):
        super().__init__(name, actor)
        self.vy = 100
        self.AABB = AABB
        self.actor = actor
        
    def load(self):
        from .engine import Engine
        e = Engine()
        e.collisionSystem.registerCollider(self)
        
    def update(self, deltaTime):
        self.AABB.x = self.owner.x
        self.AABB.y = self.owner.y
        
    def onCollision(self, otherCollider):
        #print(self.owner.y)
        if self.name != "collisionBase" and otherCollider.name == "collisionBall":
            self.actor.y = -300
        if self.name == "collisionBall" and otherCollider.name == "collisionBase":
            #print(f"{self.name} Colliding with {otherCollider.name}")
            self.vy = - self.vy
            self.owner.y += self.vy
            print("mario")
            #print(self.owner.y)
            #print(self.vy)"""
            
        
        
           
    def removeActor(self, otherCollider):
        pass