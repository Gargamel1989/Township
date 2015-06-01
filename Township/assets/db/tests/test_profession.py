'''
Created on May 25, 2015

@author: joep
'''
from unittest import TestCase
from assets.db.Profession import Profession

class ProfessionTest(TestCase):
    
    def setUp(self):
        self.profession_name = 'Test'
        self.profession = Profession(name=self.profession_name)
        
    
    
    def test_init(self):
        self.profession.name = self.profession_name