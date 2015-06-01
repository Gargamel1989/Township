'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from game.objects.TownHall import TownHall

class TownHallTestCase(TestCase):
    
    def setUp(self):
        self.town_hall = TownHall()
        
    
    
    def test_init(self):
        self.assertEqual(self.town_hall.level, 1)
        self.assertEqual(self.town_hall.max_recruits, 3)