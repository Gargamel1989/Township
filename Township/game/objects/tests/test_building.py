'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from game.objects.Building import Building
from assets.db.Blueprint import Blueprint

class BuildingTest(TestCase):
    
    def setUp(self):
        self.blueprint = Blueprint(blueprint_id=1, building_type='test')
        self.building = Building(blueprint=self.blueprint, location=(0, 0))
    
    
    
    def test_init(self):
        self.assertEqual(self.building.blueprint, self.blueprint)
        self.assertEqual(self.building.location, (0, 0))

        self.assertEqual(self.building.inhabitant, None)
        
    def test_floor_rect(self):
        self.assertEqual(self.building.floor_rect.topleft, (0, 0))
        self.assertEqual(self.building.floor_rect.size, (0, 0))
        
        blueprint = Blueprint(blueprint_id=1, building_type='test', floor_plan='xx\nxx')
        building = Building(blueprint=blueprint, location=(1, 1))
        
        self.assertEqual(building.floor_rect.topleft, (1, 1))
        self.assertEqual(building.floor_rect.size, (2, 2))
        
    def test_is_inhabited(self):
        self.assertFalse(self.building.is_inhabited())
        
        self.building.inhabitant = object()
        self.assertTrue(self.building.is_inhabited())
        