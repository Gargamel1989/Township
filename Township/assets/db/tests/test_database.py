'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from assets.db.Database import Database, DB, BLUEPRINT
from assets import AssetError
from collections import OrderedDict

class DatabaseTest(TestCase):
    
    def setUp(self):
        self.DB = Database()

    
    
    def test_init(self):
        self.assertIsInstance(DB, Database)
    
    
    
    def test_load(self):
        self.assertRaises(AssetError, lambda: self.DB.load('bad_data_type'))
        
        self.DB.load(BLUEPRINT)
        
        odict = getattr(self.DB, self.DB.attr_name_from_data_type(BLUEPRINT))
        self.assertIsInstance(odict, OrderedDict)
        
        DB.load(BLUEPRINT)
        self.assertEqual(getattr(self.DB, self.DB.attr_name_from_data_type(BLUEPRINT)), odict)
    
    def test_get(self):
        self.assertRaises(AssetError, lambda: self.DB.get('bad_data_type'))
        self.assertRaises(AssetError, lambda: self.DB.get(BLUEPRINT))
        self.assertRaises(AssetError, lambda: self.DB.get(BLUEPRINT, None))
        
        self.DB.load(BLUEPRINT)
        
        self.assertEqual(len(self.DB.get(BLUEPRINT)), 0)
        self.assertEqual(self.DB.get(BLUEPRINT, data_id=1), None)
    
    def test_add(self):
        self.assertRaises(AssetError, lambda: self.DB.add('bad_data_type', None, 1))
        self.assertRaises(AssetError, lambda: self.DB.add(BLUEPRINT, None, 1))
        
        self.DB.load(BLUEPRINT)
        self.DB.add(BLUEPRINT, object(), 1)
        
        self.assertEqual(len(self.DB.get(BLUEPRINT)), 1)
        self.assertFalse(self.DB.get(BLUEPRINT, data_id=1) is None)
        self.assertIsNone(self.DB.get(BLUEPRINT, data_id=2))
        
        # No duplicate IDs allowed 
        self.assertRaises(AssetError, lambda: self.DB.add(BLUEPRINT, object(), 1))
        