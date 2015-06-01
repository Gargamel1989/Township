'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from game.objects.Recruit import Recruit
from game.objects.Building import Building
from game.objects.Inhabitant import Inhabitant
from game.objects.RecruitableNpc import RecruitableNpc

class RecruitTest(TestCase):
    
    def setUp(self):
        self.recruitable_npc = RecruitableNpc(name='Mark')
        self.recruit = Recruit(recruitable_npc=self.recruitable_npc)
    
    
    
    def test_init(self):
        self.assertEqual(self.recruit.npc, self.recruitable_npc)
        
        
        
    def test_move_into(self):
        building = Building(blueprint=None, location=None)
        
        inhabitant = self.recruit.move_into(dwelling=building)
        self.assertIsInstance(inhabitant, Inhabitant)
        self.assertEqual(inhabitant.dwelling, building)