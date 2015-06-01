'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from game.objects.Item import Item

class ItemTest(TestCase):
    
    def setUp(self):
        self.item_id = 1
        self.item_name = 'Test Item'
        self.item = Item(item_id=self.item_id, name=self.item_name)
        
    
    
    def test_init(self):
        self.assertEqual(self.item.item_id, self.item_id)
        self.assertEqual(self.item.name, self.item_name)
        self.assertEqual(self.item.is_stackable, False)
    
    def test_equal(self):
        same_item = Item(item_id=self.item_id, name=self.item_name)
        
        self.assertFalse(self.item is same_item)
        self.assertEqual(self.item, same_item)
    
        test_dict = {}
        test_dict[self.item] = 1
        
        self.assertIn(same_item, test_dict)