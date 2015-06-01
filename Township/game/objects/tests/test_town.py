'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from game.objects.Town import Town, CollisionException, ConnectionException
from game.objects.RecruitableNpc import RecruitableNpc
from assets.db.Blueprint import Blueprint
from util.constants import TOWNHALL, DWELLING
from assets.db.Database import DB, BLUEPRINT
from game.objects.Inventory import Inventory, InventoryError
from game.objects.Item import Item
import pygame
from util import constants

class TownTest(TestCase):
    
    def setUp(self):
        self.town = Town(size=(100, 100))
    
    
    
    def test_init(self):
        self.assertEqual(self.town.town_hall, None)
        
        self.assertEqual(self.town.buildings, [])
        self.assertEqual(self.town.ao_buildings(), 0)
        
        self.assertEqual(self.town.recruits, [])
        self.assertEqual(self.town.ao_recruits(), 0)
        
        self.assertEqual(self.town.inhabitants, [])
        self.assertEqual(self.town.ao_inhabitants(), 0)
        
    
    
    def test_available_buildings(self):
        self.assertEqual(self.town.available_blueprints(), [])
         
        bp = Blueprint(blueprint_id=1, building_type=DWELLING)
        DB.add(data_type=BLUEPRINT, data_object=bp, data_id=bp.blueprint_id)
         
        self.assertEqual(len(self.town.available_blueprints()), 1)
        self.assertIn(bp, self.town.available_blueprints())
         
        bp = Blueprint(blueprint_id=2, building_type=TOWNHALL)
        DB.add(data_type=BLUEPRINT, data_object=bp, data_id=bp.blueprint_id)
         
        self.assertEqual(len(self.town.available_blueprints()), 1)
        self.assertNotIn(bp, self.town.available_blueprints())
        
        bp = Blueprint(blueprint_id=3, building_type=DWELLING, unlock_condition=lambda _: False)
        DB.add(data_type=BLUEPRINT, data_object=bp, data_id=bp.blueprint_id)
          
        self.assertEqual(len(self.town.available_blueprints()), 1)
        self.assertNotIn(bp, self.town.available_blueprints())
    
    def test_stockpile(self):
        self.assertIsInstance(self.town.stockpile, Inventory)
        self.assertEqual(len(self.town.stockpile), 0)
        
        stackable_item = Item(item_id=1, name='test1', stackable=True)
        non_stackable_item = Item(item_id=1, name='test1', stackable=False)
        
        self.assertRaises(InventoryError, lambda: self.town.add_to_stockpile(non_stackable_item, amount=1))
        self.town.add_to_stockpile(stackable_item, amount=1)
        
        self.assertEqual(len(self.town.stockpile), 1)
        self.assertIn(stackable_item, self.town.stockpile)
         
#         self.assertRaises(InventoryError, lambda: self.town.remove_from_stockpile(non_stackable_item, amount=1))
#         self.assertRaises(InventoryError, lambda: self.town.remove_from_stockpile(stackable_item, amount=2))
#          
#         self.town.remove_from_stockpile(stackable_item, amount=1)
#         self.assertEqual(len(self.town.stockpile), 0)

    
    
    def test_zones(self):
        self.town.set_zone(pygame.Rect(0, 0, 10, 10), constants.ROAD)
        
        self.assertTrue(self.town.is_in_zone(pygame.Rect(0, 0, 1, 1), constants.ROAD))
        self.assertTrue(self.town.is_in_zone(pygame.Rect(1, 1, 1, 1), constants.ROAD))
        self.assertTrue(self.town.is_in_zone(pygame.Rect(0, 0, 10, 10), constants.ROAD))
        
        self.assertFalse(self.town.is_in_zone(pygame.Rect(0, 0, 11, 11), constants.ROAD))
        self.assertFalse(self.town.is_in_zone(pygame.Rect(0, 0, 1, 1), constants.HOUSING))
        
        # Zones should not overlap
        self.assertFalse(self.town.can_place_zone(pygame.Rect(1, 1, 1, 1), constants.ROAD))
        self.assertFalse(self.town.can_place_zone(pygame.Rect(1, 1, 1, 1), constants.HOUSING))
        self.assertFalse(self.town.can_place_zone(pygame.Rect(9,9, 10, 10), constants.ROAD))
        self.assertRaises(Exception, lambda: self.town.can_place_zone(pygame.Rect(1, 1, 1, 1), constants.ROAD, exc=True))
        self.assertRaises(Exception, lambda: self.town.can_place_zone(pygame.Rect(1, 1, 1, 1), constants.HOUSING, exc=True))
        self.assertRaises(Exception, lambda: self.town.can_place_zone(pygame.Rect(9,9, 10, 10), constants.ROAD, exc=True))
        
        self.assertRaises(Exception, lambda: self.town.set_zone(pygame.Rect(1, 1, 1, 1), constants.ROAD))
    
    def test_zones_road(self):
        # Road zones must touch the edge of the map
        self.assertTrue(self.town.can_place_zone(pygame.Rect(0, 1, 1, 1), constants.ROAD))
        self.assertTrue(self.town.can_place_zone(pygame.Rect(1, 0, 1, 1), constants.ROAD))
        self.assertTrue(self.town.can_place_zone(pygame.Rect(self.town.size[0] - 1, self.town.size[1] - 2, 1, 1), constants.ROAD))
        self.assertTrue(self.town.can_place_zone(pygame.Rect(self.town.size[0] - 2, self.town.size[1] - 1, 1, 1), constants.ROAD))
        
        self.assertRaises(ConnectionException, lambda: self.town.can_place_zone(pygame.Rect(1, 1, self.town.size[0] - 2, self.town.size[1] - 2), constants.ROAD, exc=True))
        
        
        # Or touch an existing piece of road (thus indirectly touching the edge of the map
        self.town.set_zone(pygame.Rect(0, 1, 3, 1), constants.ROAD)
        
        self.assertTrue(self.town.can_place_zone(pygame.Rect(3, 1, 1, 3), constants.ROAD))
    
    def test_zones_housing(self):
        # Housing zones must touch a road zone
        self.assertRaises(ConnectionException, lambda: self.town.can_place_zone(pygame.Rect(1, 1, 1, 1), constants.HOUSING, exc=True))
        
        self.town.set_zone(pygame.Rect(0, 1, 3, 1), constants.ROAD)
        
        self.assertTrue(self.town.can_place_zone(pygame.Rect(3, 1, 1, 1), constants.HOUSING))
    
    
        
    def test_recruit(self):
        recruitable_npc = RecruitableNpc(name='Mark')
        
        self.town.recruit(recruitable_npc)
        
        self.assertEqual(self.town.ao_recruits(), 1)
        self.assertTrue(recruitable_npc.has_been_recruited)
    
    def test_build(self):
        blueprint = Blueprint(blueprint_id=1, building_type=DWELLING, floor_plan='xx\nxx')
        
        self.town.build(building_blueprint=blueprint, location=(0, 0))
        self.assertEqual(len(self.town.buildings), 1)
        self.assertEqual(self.town.buildings[0].location, (0, 0))
        
        # Buildings can not collide
        self.assertRaises(CollisionException, lambda: self.town.build(building_blueprint=blueprint, location=(0, 0)))
        self.assertRaises(CollisionException, lambda: self.town.build(building_blueprint=blueprint, location=(1, 1)))
        
        self.town.build(building_blueprint=blueprint, location=(2, 2))
        self.assertEqual(len(self.town.buildings), 2)
        self.assertEqual(self.town.buildings[1].location, (2, 2))
        