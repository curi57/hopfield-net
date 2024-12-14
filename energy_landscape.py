from typing import Dict

from configuration import Configuration


class EnergyLandscape():

    def __init__(self):
        self.map : Dict[int, int] = {}
    
    def add_point(self, configuration : Configuration):
        self.map[configuration.energy] = configuration.id

    #def find_point(self):
    #    print("Finding point")



    

    
