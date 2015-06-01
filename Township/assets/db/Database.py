'''
Created on May 25, 2015

@author: joep
'''
from assets import AssetError
from collections import OrderedDict

# Data Types
BLUEPRINT, PROFESSION = 'blueprint', 'profession'
DATA_TYPES = [BLUEPRINT, PROFESSION]

class Database(object):
    
    @classmethod
    def attr_name_from_data_type(cls, data_type):
        return '_{}s'.format(data_type)
    
    def __init__(self):
        for data_type in DATA_TYPES:
            setattr(self, self.attr_name_from_data_type(data_type), None)
    
    
    def get(self, data_type, data_id=None):
        if data_type not in DATA_TYPES:
            raise AssetError('Data type not recognized: {}'.format(data_type))
        
        data = getattr(self, self.attr_name_from_data_type(data_type))
        if data is None:
            raise AssetError('{} data has not been loaded yet!'.format(data_type.capitalize()))
        
        if data_id is None:
            return data.values()
        
        return data.get(data_id, None)
    
    def get_all(self, data_type):
        return self.get(data_type=data_type)
    
    def add(self, data_type, data_object, data_id):
        if data_type not in DATA_TYPES:
            raise AssetError('Data type not recognized: {}'.format(data_type))
        
        data = getattr(self, self.attr_name_from_data_type(data_type))
        if data is None:
            raise AssetError('{} data has not been loaded yet!'.format(data_type.capitalize()))
        
        if data_id in data:
            raise AssetError('Duplicate id: `{}`'.format(data_id))
        data[data_id] = data_object
    
    def load(self, data_type):
        if data_type not in DATA_TYPES:
            raise AssetError('Data type not recognized: {}'.format(data_type))
        
        data = getattr(self, self.attr_name_from_data_type(data_type))
        if data is None:
            setattr(self, self.attr_name_from_data_type(data_type), OrderedDict())

DB = Database()