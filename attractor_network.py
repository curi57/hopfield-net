from typing import List
from configuration import Configuration
from plotter import Plotter
from energy_landscape import EnergyLandscape
from utils import Utils


class AttractorNetwork:
 
    def __init__(self): 
        self.utils = Utils()
        self.energy_landscape = EnergyLandscape() 
        self.plotter = Plotter()

        self.configurations : List[Configuration] = []
        self.weights : List[List[int]] = []


    def add_memory(self, memory : Configuration):
        # create a flat version of the configuration
        self.utils.flat(memory)

        # Set the current configuration and trigger recalculation of weights
        self.configurations.append(memory)
        self.calculate_weights()
    
        # Add the new configuration to the energy landscape and attempt to represent it visually        
        self.energy_landscape.add_point(memory) 
   
    def calculate_weights(self):
        
        if self.configurations is None:
            raise Exception("no configuration found")
                                                                                                    
        counter_i = 0                                                                                                                 
        counter_j = 0
        
        # Note: it must calculate the average between the differents weights for different memories
        for memory in self.configurations:
            for i in memory.flatten_data_representation:
                n_weights : List[int] = []                                                             
                for j in memory.flatten_data_representation:
                    wij = 0 if counter_i == counter_j else i*j # 1 * -1 ou 1 * 1 ou -1 * -1 ou -1 * 1
                    n_weights.append(wij)
                    counter_j += 1

                self.weights.append(n_weights)
                counter_i += 1
                counter_j = 0
                                                                                                                                            
        print(f"weights: {self.weights}")
                                                                                                                                                         
    def converge(self, input_configuration: Configuration) -> List[int]:
    

        input_energy = input_configuration.calculate_self_energy(self.weights) # is this the right moment to calculate the inner energy of the configuration? 
        for local_minima in self.energy_landscape.map:              
            if (input_energy <= local_minima):
                recovered_memory_data_representation = input_configuration.flatten_data_representation
                return recovered_memory_data_representation

        input_configuration.calculate_self_energy(self.weights, True);                
        self.converge(input_configuration)

