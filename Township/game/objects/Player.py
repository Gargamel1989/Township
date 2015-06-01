'''
Created on May 19, 2015

@author: joep
'''
from game.objects.Inventory import Inventory
from util.constants import NO_DIRECTION, UP, RIGHT, DOWN, LEFT
from math import ceil, floor

class Player(object):
    
    def __init__(self):
        self.currency = 0
        self.inventory = Inventory()
        self.location = [0, 0]
        self.movement_speed = 0
        
        self.walking_direction = NO_DIRECTION
        self._stop_walking_location = None
        
    
    
    def move(self, direction, distance):
        if direction is RIGHT:
            self.location[0] += distance
        elif direction is LEFT:
            self.location[0] -= distance
            
        elif direction is DOWN:
            self.location[1] += distance
        elif direction is UP:
            self.location[1] -= distance
    
    
    
    def walk(self, direction):
        if self.walking_direction is NO_DIRECTION:
            self.walking_direction = direction
    
    def get_next_tile_aligned_position(self):
        if self.walking_direction is NO_DIRECTION:
            return [int(floor(self.location[0])), int(floor(self.location[1]))] 
        
        elif self.walking_direction is RIGHT:
            return [int(ceil(self.location[0])), int(floor(self.location[1]))]
        elif self.walking_direction is LEFT:
            return [int(floor(self.location[0])), int(floor(self.location[1]))]
            
        elif self.walking_direction is DOWN:
            return [int(floor(self.location[0])), int(ceil(self.location[1]))]
        elif self.walking_direction is UP:
            return [int(floor(self.location[0])), int(floor(self.location[1]))]
        
    
    def stop_walking(self):
        if self.walking_direction is not NO_DIRECTION:
            self._stop_walking_location = self.get_next_tile_aligned_position()
        
            
            
        
    def update(self, dt):
        if self.walking_direction is not NO_DIRECTION:
            cur_x, cur_y = self.location
            
            distance = self.movement_speed * dt
            self.move(self.walking_direction, distance)
            
            if self._stop_walking_location is not None:
                new_x, new_y = self.location
                stop_x, stop_y = self._stop_walking_location
                
                if new_x < stop_x <= cur_x or cur_x <= stop_x < new_x:
                    self.location[0] = stop_x
                    
                if new_y < stop_y <= cur_y or cur_y <= stop_y < new_y:
                    self.location[1] = stop_y
                    
                if self.location == self._stop_walking_location:
                    self.walking_direction = NO_DIRECTION
                    self._stop_walking_location = None
        
        