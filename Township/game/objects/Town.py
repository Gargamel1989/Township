'''
Created on May 25, 2015

@author: joep
'''
from game.objects.Recruit import Recruit
from assets.db.Database import DB, BLUEPRINT
from util.constants import TOWNHALL
from game.objects.Building import Building
from game.objects.Inventory import Inventory, InventoryError
from util import constants
from util.rect import are_touching

class Town(object):
    
    def __init__(self, size):
        self.size = size
        
        self.town_hall = None
        self.stockpile = Inventory()
        
        self.zones = []
        self.zone_types = {}
        self.buildings = []
        self.recruits = []
        self.inhabitants = []
        
    
    
    def ao_buildings(self):
        return len(self.buildings)
    
    def ao_recruits(self):
        return len(self.recruits)
    
    def ao_inhabitants(self):
        return len(self.inhabitants)
    
    
    
    def available_blueprints(self):
        available_blueprints = []
        
        for blueprint in DB.get_all(BLUEPRINT):
            if blueprint.building_type is TOWNHALL:
                continue
            
            if blueprint.is_unlocked_by(town=self):
                available_blueprints.append(blueprint)
        
        return available_blueprints
    
    
    
    def can_place_zone(self, zone_rect, zone_type, exc=False):
        if zone_rect.collidelist(self.zones) > -1:
            if exc:
                raise CollisionException('Zone would collide with an existing zone')
            return False
        
        if zone_type is constants.ROAD:
            if zone_rect.top == 0 or zone_rect.right == self.size[0] or \
               zone_rect.bottom == self.size[1] or zone_rect.left == 0:
                return True
            
            for road_zone in filter(lambda zone: self.zone_types[id(zone)] is constants.ROAD, self.zones):
                if are_touching(zone_rect, road_zone):
                    return True
            
            if exc:
                raise ConnectionException()
            return False
        
        elif zone_type is constants.HOUSING:
            for road_zone in filter(lambda zone: self.zone_types[id(zone)] is constants.ROAD, self.zones):
                if are_touching(zone_rect, road_zone):
                    return True
            
            if exc:
                raise ConnectionException()
            return False
        
        return True
            
    
    def set_zone(self, zone_rect, zone_type):
        self.can_place_zone(zone_rect, zone_type, exc=True)
            
        self.zones.append(zone_rect)
        self.zone_types[id(zone_rect)] = zone_type
    
    def is_in_zone(self, rect, zone_type):
        colliding_zones = rect.collidelistall(self.zones)
        for zone_i in colliding_zones:
            zone = self.zones[zone_i]
            if zone.contains(rect):
                if self.zone_types[id(zone)] == zone_type:
                    return True
        
        return False
        
    def recruit(self, recruitable_npc):
        if not recruitable_npc.has_been_recruited:
            self.recruits.append(Recruit(recruitable_npc))
    
    def build(self, building_blueprint, location):
        building = Building(blueprint=building_blueprint, location=location)
        
        if building.floor_rect.collidelist([other_building.floor_rect for other_building in self.buildings]) >= 0:
            raise CollisionException()
        
        self.buildings.append(building)
    
    def add_to_stockpile(self, item, amount):
        if not item.is_stackable:
            raise InventoryError('Only stackable items can be stored in the town stockpile')
        
        self.stockpile.add(item, amount=1)


class CollisionException(Exception):
    pass

class ConnectionException(Exception):
    pass
