'''
Created on May 17, 2015

@author: joep
'''
import unittest
from game.objects.Inventory import Inventory, InventoryError
from game.objects.Item import Item

class InventoryTestCase(unittest.TestCase):
    
    def setUp(self):
        self.items = [Item(item_id=x, name=x) for x in xrange(5)]
        self.stackable_items = [Item(item_id=6, name=x, stackable=True) for x in xrange(5)]
        
    def test_inventory_add(self):
        # Add single item
        inv = Inventory()
        inv.add(self.items[0], amount=1)
        inv.add(self.items[1], amount=3)
        
        self.assertIn(self.items[0], inv)
        self.assertEqual(inv.ao_item(self.items[1]), 3)
    
        # Add list of items
        inv = Inventory()
        inv.add_all(self.items)
        
        self.assertEqual(inv.ao_item_stacks(), len(self.items))
        for item in self.items:
            self.assertIn(item, inv)
        
        # Add multiple of an unstackable item
        inv.add(self.items[0])
        
        self.assertEqual(inv.ao_item(self.items[0]), 2)
        self.assertEqual(inv.ao_item_stacks(), len(self.items) + 1)
    
    def test_inventory_remove(self):
        inv = Inventory()
        inv.add_all(self.items)
        
        inv.remove(self.items[4])
        
        self.assertNotIn(self.items[4], inv)
        self.assertEqual(inv.ao_item_stacks(), len(self.items) - 1)
        
        # Can't remove anymore
        self.assertRaises(InventoryError, lambda: inv.remove(self.items[4]))
        
        # Add multiple of an unstackable item
        inv = Inventory()
        inv.add_all(self.items)
        inv.add(self.items[0])
        inv.remove(self.items[0])
        
        self.assertEqual(inv.ao_item(self.items[0]), 1)
        self.assertEqual(inv.ao_item_stacks(), len(self.items))
    
    def test_inventory_stackable(self):
        inv = Inventory()
        inv.add_all(self.items)
        inv.add_all(self.stackable_items)
        
        # Stackable items should take only 1 extra stack in the inventory 
        self.assertEqual(inv.ao_item_stacks(), len(self.items) + 1)
        self.assertEqual(inv.ao_item(self.stackable_items[0]), len(self.stackable_items))
        
        # Remove one of the stackables
        inv.remove(item=self.stackable_items[0])
        
        self.assertIn(self.stackable_items[0], inv)
        self.assertEqual(inv.ao_item_stacks(), len(self.items) + 1)
        self.assertEqual(inv.ao_item(self.stackable_items[0]), len(self.stackable_items) - 1)
        
        # Remove all of the stackables
        for _ in xrange(len(self.stackable_items) - 1):
            inv.remove(self.stackable_items[0])
            
        self.assertNotIn(self.stackable_items[0], inv)
        self.assertEqual(inv.ao_item_stacks(), len(self.items))
        self.assertEqual(inv.ao_item(self.stackable_items[0]), 0)
                         
        # Can't remove anymore of the stackables
        self.assertRaises(InventoryError, lambda: inv.remove(self.stackable_items[0]))
    
    def test_remove_amount(self):
        # Remove amount
        inv = Inventory()
        inv.add_all(self.stackable_items)
        
        inv.remove(self.stackable_items[0], amount=(len(self.stackable_items) - 2))
        
        self.assertIn(self.stackable_items[0], inv)
        self.assertEqual(inv.ao_item(self.stackable_items[0]), 2)
        self.assertEqual(inv.ao_item_stacks(), 1)
        
        # Remove more amount than is left
        self.assertRaises(InventoryError, lambda: inv.remove(self.stackable_items[0], amount=3))
        self.assertEqual(inv.ao_item(self.stackable_items[0]), 2)
        
        # Remove exact amount left
        inv.remove(self.stackable_items[0], amount=2)
        
        self.assertNotIn(self.stackable_items[0], inv)
        self.assertEqual(inv.ao_item(self.stackable_items[0]), 0)
        self.assertEqual(inv.ao_item_stacks(), 0)
        
        # Remove all
        inv = Inventory()
        inv.add_all(self.stackable_items)
        
        inv.remove(self.stackable_items[0], amount=-1)
        
        self.assertNotIn(self.stackable_items[0], inv)
        self.assertEqual(inv.ao_item(self.stackable_items[0]), 0)
        self.assertEqual(inv.ao_item_stacks(), 0)
                          
        # Remove amount of unstackable item not possible
        inv = Inventory()
        inv.add(self.items[0], amount=3)
        
        self.assertRaises(InventoryError, lambda: inv.remove(self.items[0], amount=2))
    