'''
Created on May 19, 2015

@author: joep
'''
import unittest
from game.Game import Game
from game.objects.Player import Player
from game.World import World
from test._mock_backport import MagicMock

class GameTestCase(unittest.TestCase):


    def test_game_init(self):
        game = Game()
        
        self.assertFalse(game.is_running)
        self.assertIsInstance(game.world, World)
        self.assertIsInstance(game.player, Player)
    
    def test_game_update(self):
        game = Game()
        
        game.world.update = MagicMock()
        game.player.update = MagicMock()
        
        game.update(dt=1)
        
        game.world.update.assert_called_once_with(dt=1)
        game.player.update.assert_called_once_with(dt=1)
    
