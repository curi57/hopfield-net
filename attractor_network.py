from plotter import Plotter
from energy_landscape import EnergyLandscape
from utils import Utils


class AttractorNetwork:
 
    def __init__(self): 
        self.utils = Utils()
        self.energy_landscape = EnergyLandscape()
        self.configurations = None 
        self.weights = []
        self.plotter = Plotter()


    # The Hopfield network handles the weights calculation when a new configuration is added
    def add_configuration(self, configuration):

        # Set the current configuration and trigger recalculation of weights
        self.configurations = configuration # Adding a new configuration requires recalculating the calculate_weights

        # Recalculate weights based on the updated configurations
        self.weights = self.calculate_weights()
    
        # Add the new configuration to the energy landscape and attempt to represent it visually
        self.energy_landscape.add_point(configuration) # Plot the updated energy landscape representation
   

    def hebbian_learning(self, h, i):
        if (h > 0):
            i *= 1
        elif (h <= 0):
            #i *= -1
            i = 0
                                      
        return i


    # 2. Calculate the weights between each of the possible neurons interactions (or the outer product with the vector itself)
    def calculate_weights(self):
        
        if self.configurations is None:
            raise Exception("A configuration must be added first")
                                                                                                    
        counter_i = 0                                                                                                                 
        counter_j = 0

        # outer product (following the hebbian learning)
        for i in self.configurations.flatten:                                                                                                    
            n_weights = []                                                             
            for j in self.configurations.flatten:
                wij = 0 if counter_i == counter_j else i*j                                                                            
                n_weights.append(wij)
                counter_j += 1
            
            self.weights.append(n_weights)
            counter_i += 1
            counter_j = 0
                                                                                                                                            
        print(f"weights: {self.weights}")
                                                                                                                                                         
    def converge(self, input_configuration):

        stable_state = False

        input_configuration.calculate_energy(self.weights)

        # aqui precisamos descobrir iterar e verificar se a energia corresponde a algum 'local_minima' na 'paisagem de energia'
        local_minima = self.memorized_patterns[0].energy 
        while not stable_state:
            if (input_configuration.energy > local_minima):
                #input_configuration.
                #energy = -(calculate_configuration_energy(flatten_input, weights, True)) # calculates de energy of the system and apply the neurons update rule
            else:
                stable_state = True

