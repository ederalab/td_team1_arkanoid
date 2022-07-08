import json
from engine.scene import *
from engine.component import *
from engine.actor import *
from engine.staticspritecomponent import *
from engine.gameovercomponent import *
from engine.winnercomponent import *
from engine.bouncingmovementcomponent import *
from .floatingmovementcomponent import *
from .pathmovementcomponent import *
from .collidercomponent import *
from pygame import rect

class SceneFactory:

    def loadSceneFromFile(fileName):
        with open(fileName, "r") as f:
            try:
                # this is a dictionary
                sceneDescriptor = json.load(f)

                scene = Scene()
                windowDescriptor = sceneDescriptor["window"]
                scene.windowRect.height = windowDescriptor["height"]
                scene.windowRect.width = windowDescriptor["width"]
                scene.title = windowDescriptor["title"]
                
                for actorDescriptor in sceneDescriptor["actors"]:
                    actor = Actor(scene)
                    actor.name = actorDescriptor["name"]
                    actor.x = actorDescriptor["x"]
                    actor.y = actorDescriptor["y"]
                    
                    for componentDescriptor in actorDescriptor["components"]:
                        component = None
                        if componentDescriptor["type"] == StaticSpriteComponent.__name__:
                            component = StaticSpriteComponent(componentDescriptor["fileName"], componentDescriptor["name"], actor)
                        elif componentDescriptor["type"] == GameOverComponent.__name__:
                            component = GameOverComponent(componentDescriptor["fileName"], componentDescriptor["name"], actor)
                        elif componentDescriptor["type"] == WinnerComponent.__name__:
                            component = WinnerComponent(componentDescriptor["fileName"], componentDescriptor["name"], actor)
                        elif componentDescriptor["type"] == BouncingMovementComponent.__name__:
                            rectDescriptor = componentDescriptor["boundingRect"]
                            r = rect.Rect(rectDescriptor["x"], rectDescriptor["y"],
                                rectDescriptor["width"], rectDescriptor["height"])
                            component = BouncingMovementComponent(componentDescriptor["name"], actor, r, componentDescriptor["vx"], componentDescriptor["vy"])
                        elif componentDescriptor["type"] == FloatingMovementComponent.__name__:
                            component = FloatingMovementComponent(componentDescriptor["name"], actor)
                        elif componentDescriptor["type"] == PathMovementComponent.__name__:
                            component = PathMovementComponent(componentDescriptor["name"], actor, componentDescriptor["path"])
                        elif componentDescriptor["type"] == ColliderComponent.__name__:
                            rectDescriptor = componentDescriptor["AABB"]
                            AABB = rect.Rect(rectDescriptor["x"], rectDescriptor["y"],
                                rectDescriptor["width"], rectDescriptor["height"])
                            component = ColliderComponent(componentDescriptor["name"], actor, AABB)
                        else:
                            raise Exception(f"Wrong component type: {componentDescriptor['type']}")
                        
                        actor.addComponent(component)
                    
                    scene.actors.append(actor)
                return scene
                
            except Exception as e:
                print(f"Error on filename : {fileName}")
                print(str(e))
                
    
    def saveSceneFromFile(fileName):
        with open(fileName, "r+") as f:
            try:
                # this is a dictionary
                k = json.load(f)
                
            except Exception as e:
                print(f"Error on filename : {fileName}")
                print(str(e))
        
        window = k['window']
        actors=k["actors"]
        
        
        def set_component_in_actor(n_actor):
            components_actor=actors[n_actor]["components"]
            
            return components_actor
            
        
        def edit_window(height, width, dict=dict()):
            window["width"] = width
            window["height"] = height
            window.update(dict)
            
            
        def new_actor():
            new_actor= k["actors"]
            actor= {
            "name": "",
            "x": 0,
            "y": 0,
            "components": [{
                    "name": "",
                    "type": "",
                    }
            
                ]
            }
            new_actor.append(actor)
        
        
        def edit_actor(name, x, y, n_actor):
            actors[n_actor]["name"]=name
            actors[n_actor]["x"]=x
            actors[n_actor]["y"]=y
           
            
        def new_component(n_actor):
            components_actor= set_component_in_actor(n_actor)
            component= {
                "name": "",
                "type": "",
            }
            components_actor.append(component)
        
        
        
        def edit_component(name, type, n_actor, n_component, dict=dict()):
            components_actor= set_component_in_actor(n_actor)
            components_actor[n_component]["name"]=name
            components_actor[n_component]["type"]=type
            components_actor[n_component].update(dict)
            
            
            
        def add_to_component(n_actor, n_component, dict=dict()):
            components_actor= set_component_in_actor(n_actor)
            components_actor[n_component].update(dict)
            
            
            
        
        
        with open("test1.json", "w") as g:   
            
            #write in windows dict
            edit_window(550, 700, {"title": "Titolo Bellissimo"})
            
            #write first actor
            edit_actor("Faccina", 0, 0, 0)
            
            #write first component
            edit_component("sprite", "StaticSpriteComponent", 0, 0, {'fileName':'assets/ghost1.png'})

            #add second component
            new_component(0)
            
            #write second component
            edit_component("bouncing", "BouncingMovementComponent", 0, 1, {"boundingRect": {"x": 100, "y": 100, "width": 400, "height": 500}})
            add_to_component(0, 1, {"vx": 0.10})
            add_to_component(0, 1, {"vy": 0.10})
            
            #add second actor
            new_actor()
            
            #write second actor
            edit_actor("Faccina", 0, 0, 1)
            
            #write first component in second actor
            edit_component("sprite", "StaticSpriteComponent", 1, 0, {'fileName':'assets/ghost2.png'})
            
            #add second component in second actor
            new_component(1)
            
            #write second component in second actor
            edit_component("bouncing", "BouncingMovementComponent", 1, 1, {"boundingRect": {"x": 0, "y": 0, "width": 200, "height": 300}})
            add_to_component(0, 1, {"vx": 0.10})
            add_to_component(0, 1, {"vy": 0.10})
            

            k=json.dump(k, g)
            
                
            
                
        