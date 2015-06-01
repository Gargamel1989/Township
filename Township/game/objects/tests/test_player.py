'''
Created on May 19, 2015

@author: joep
'''
import unittest
from game.objects.Player import Player
from game.objects.Inventory import Inventory
from util.constants import NO_DIRECTION, UP, RIGHT, DOWN, LEFT

class PlayerTestCase(unittest.TestCase):
    
    def setUp(self):
        self.player = Player()
    
    
    
    def test_player_init(self):
        self.assertEqual(self.player.currency, 0)
        self.assertIsInstance(self.player.inventory, Inventory)
        self.assertEqual(self.player.location, [0, 0])
        
        
    
    def test_player_move(self):
        self.player.move(UP, 10)
        self.assertEqual(self.player.location, [0, -10])
        
        self.player.move(RIGHT, 8)
        self.assertEqual(self.player.location, [8, -10])
        
        self.player.move(DOWN, 4)
        self.assertEqual(self.player.location, [8, -6])
        
        self.player.move(LEFT, 3)
        self.assertEqual(self.player.location, [5, -6])
        
        
        
    def test_get_next_tile_aligned_position(self):
        self.player.location = [0, 0]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [0, 0])
        self.player.location = [0.1, 0.8]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [0, 0])
        self.player.location = [-0.1, -0.8]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [-1, -1])
        
        self.player.walking_direction = RIGHT
        self.player.location = [0, 0]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [0, 0])
        self.player.location = [0.1, 0.1]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [1, 0])
        self.player.location = [-0.1, -0.1]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [0, -1])
        
        self.player.walking_direction = LEFT
        self.player.location = [0.1, 0.1]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [0, 0])
        self.player.location = [-0.1, -0.1]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [-1, -1])
        
        self.player.walking_direction = DOWN
        self.player.location = [0.1, 0.1]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [0, 1])
        self.player.location = [-0.1, -0.1]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [-1, 0])
        
        self.player.walking_direction = UP
        self.player.location = [0.1, 0.1]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [0, 0])
        self.player.location = [-0.1, -0.1]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [-1, -1])
        self.player.location = [0, -2]
        self.assertEqual(self.player.get_next_tile_aligned_position(), [0, -2])
        
    
    def test_player_walk(self):
        self.player.movement_speed = 1
        
        self.player.update(dt=1)
        self.assertEqual(self.player.location, [0, 0])
        
        self.player.stop_walking()
        self.player.update(dt=1)
        self.assertEqual(self.player.location, [0, 0])
        
        self.player.walk(UP)
        self.player.update(1)
        self.assertEqual(self.player.location, [0, -1])
        self.player.update(1)
        self.assertEqual(self.player.location, [0, -2])
        
        self.player.stop_walking()
        self.player.update(dt=1)
        self.assertEqual(self.player.location, [0, -2])
        
        self.player.stop_walking()
        self.player.walk(RIGHT)
        self.player.update(1)
        self.assertEqual(self.player.location, [1, -2])
        
        self.player.stop_walking()
        self.player.update(1)
        self.assertEqual(self.player.location, [1, -2])
        self.player.walk(DOWN)
        self.player.update(1)
        self.assertEqual(self.player.location, [1, -1])
    
    def test_player_walk_tile_aligned(self):
        self.player.movement_speed = 0.4
         
        self.player.walk(RIGHT)
        self.player.update(1)
        self.assertEqual(self.player.location, [0.4, 0])
        self.assertEqual(self.player.walking_direction, RIGHT)
         
        self.player.stop_walking()
        self.player.update(1)
        self.assertEqual(self.player.location, [0.8, 0])
        self.assertEqual(self.player.walking_direction, RIGHT)
         
        self.player.update(1)
        self.assertEqual(self.player.location, [1, 0])
        self.assertEqual(self.player.walking_direction, NO_DIRECTION)
        self.assertEqual(self.player._stop_walking_location, None)
        
        self.player.movement_speed = 1
         
        self.player.walk(RIGHT)
        self.player.update(1)
        self.assertEqual(self.player.location, [2, 0])
        self.assertEqual(self.player.walking_direction, RIGHT)
        
        self.player.stop_walking()
        self.player.update(1)
        self.assertEqual(self.player.location, [2, 0])
        self.assertEqual(self.player.walking_direction, NO_DIRECTION)
        self.assertEqual(self.player._stop_walking_location, None)
        