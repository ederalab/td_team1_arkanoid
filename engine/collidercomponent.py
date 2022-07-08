from .component import Component
import pygame


listCollider = []
class ColliderComponent(Component):
    
    
    def __init__(self, name, actor, AABB):
        super().__init__(name, actor)
        self.AABB = AABB
        self.actor = actor
        global listCollider
        
    def load(self):
        from .engine import Engine
        e = Engine()
        e.collisionSystem.registerCollider(self)
        
    def update(self, deltaTime):
        self.AABB.x = self.owner.x
        self.AABB.y = self.owner.y
        
    def onCollision(self, otherCollider):
        if self.name != "collisionBase" and otherCollider.name == "collisionBall":
            self.actor.y = -300
            if len(listCollider) == 0:
                listCollider.append(otherCollider)
                print(listCollider, "1")
        if self.name == "collisionBall" and otherCollider.name == "collisionBase":
            if len(listCollider)==1:
                listCollider.append(otherCollider)
                print(listCollider, "2")
            return True
    print(listCollider)
            #print(f"{self.name} Colliding with {otherCollider.name}")       
           
    def removeActor(self, otherCollider):
        pass
            
          
