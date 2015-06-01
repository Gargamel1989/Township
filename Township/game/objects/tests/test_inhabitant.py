'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from game.objects.Inhabitant import Inhabitant
from game.objects.Building import Building
from game.objects.Item import Item

class InhabitantTest(TestCase):
    
    def setUp(self):
        self.building = Building(blueprint=None, location=None)
        self.inhabitant = Inhabitant(dwelling=self.building)
    
    
    
    def test_init(self):
        self.assertEqual(self.inhabitant.dwelling, self.building)
        self.assertEqual(self.inhabitant.produced_items, {})
        self.assertEqual(self.inhabitant.dwelling.inhabitant, self.inhabitant)
        self.assertTrue(self.building.is_inhabited())
        
    
    
    def test_produce(self):
        invalid_produced_item = Item(item_id=1, name='wood')
        produced_item = Item(item_id=1, name='wood', stackable=True)
        
        self.assertRaises(AttributeError, lambda: self.inhabitant.produce(item_to_produce=invalid_produced_item, amount=10))
        self.inhabitant.produce(item_to_produce=produced_item, amount = 10)
        
        self.assertEqual(self.inhabitant.produced_items[produced_item], 10)