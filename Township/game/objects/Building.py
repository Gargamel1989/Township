'''
Created on May 25, 2015

@author: joep
'''
import pygame

class Building(object):
    
    def __init__(self, blueprint, location):
        self.blueprint = blueprint
        self.location = location
        
        self.inhabitant = None
        
        self.floor_rect = pygame.Rect(self.location, self.blueprint.floor_size) if self.blueprint else None
        
    
    
    def is_inhabited(self):
        return self.inhabitant is not None