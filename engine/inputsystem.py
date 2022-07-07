import pygame

class InputSystem:
    
    def __init__(self):
        self.control_key = {}
        
    def bindToKeyboard(self, key, function):
        if function is not None:
            self.control_key[key] = function
            
    def process(self):
        keyboardEvent = pygame.key.get_pressed()
        
        #every single key is mapped here, with a boolean set to True for those keys that were pressed
        for key, function in self.control_key.items():
            if keyboardEvent[key]:
                function(key)