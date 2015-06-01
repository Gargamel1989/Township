'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from game.objects.RecruitableNpc import RecruitableNpc

class RecruitableNpcTest(TestCase):
    
    def setUp(self):
        self.recruitable_npc = RecruitableNpc(name='Mark')
        
    
    
    def test_init(self):
        self.assertEqual(self.recruitable_npc.has_been_recruited, False)
        self.assertEqual(self.recruitable_npc.level, 0)