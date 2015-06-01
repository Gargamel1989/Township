'''
Created on May 25, 2015

@author: joep
'''
from game.objects.Inhabitant import Inhabitant

class Recruit(object):
    
    def __init__(self, recruitable_npc):
        self.npc = recruitable_npc
        self.npc.has_been_recruited = True
    
    
    def move_into(self, dwelling):
        return Inhabitant(dwelling=dwelling)