'''
Created on May 19, 2015

@author: joep
'''
import unittest
from game.World import World

class WorldTestCase(unittest.TestCase):
    
    def test_world_init(self):
        world = World()
        
        self.assertEqual(world.time_expired, 0)