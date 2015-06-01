'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from assets.db.Blueprint import Blueprint
from util import constants

class BlueprintTest(TestCase):
    
    def setUp(self):
        self.blueprint = Blueprint(blueprint_id=1, building_type=constants.TOWNHALL, unlock_condition=lambda x: True)
        
    
    
    def test_init(self):
        self.assertEqual(self.blueprint.blueprint_id, 1)
        self.assertEqual(self.blueprint.building_type, constants.TOWNHALL)
        self.assertTrue(self.blueprint.is_unlocked_by(town=None))
        self.assertEqual(self.blueprint.floor_size, (0, 0))
        
    def test_floor_plan(self):
        floor_plan = 'xx\nxx'
        self.blueprint.floor_plan = floor_plan
        
        # must be converted to a list of strings
        self.assertEqual(len(self.blueprint.floor_plan), 2)
        
        # Can also assign a list
        self.blueprint.floor_plan = self.blueprint.floor_plan
        
        self.assertEqual(self.blueprint.floor_size, (2, 2))
        
        # None should be possible
        self.blueprint.floor_plan = None
        self.assertEqual(self.blueprint.floor_size, (0, 0))
        