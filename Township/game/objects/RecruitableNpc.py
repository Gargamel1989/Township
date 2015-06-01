'''
Created on May 25, 2015

@author: joep
'''
from game.objects.Npc import Npc

class RecruitableNpc(Npc):
    
    def __init__(self, name):
        super(RecruitableNpc, self).__init__(name=name)
        
        self.has_been_recruited = False
        self.profession = None 
        self.level = 0