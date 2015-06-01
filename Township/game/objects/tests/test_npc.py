'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from game.objects.Npc import Npc

class NpcTest(TestCase):
    
    def setUp(self):
        self.npc_name = 'Mark'
        self.npc = Npc(name=self.npc_name)
        
    
    
    def test_init(self):
        self.assertEqual(self.npc.name, self.npc_name)