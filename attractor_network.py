from plotter import Plotter


class AttractorNetwork:

    
    def __init__(self, configuration):  
        self.memorized_patterns = configuration
        self.plotter = Plotter()


    def hebbian_learning(self, h, i):
        if (h > 0):
            i *= 1
        elif (h <= 0):
            #i *= -1
            i = 0
                                      
        return i


    def converge(self, input_configuration):

        stable_state = False
        #energy = float('inf')
        local_minima = self.memorized_pattern.energy 
        while not stable_state:
            if (input_configuration.energy > local_minima):
                #input_configuration.
                #energy = -(calculate_configuration_energy(flatten_input, weights, True)) # calculates de energy of the system and apply the neurons update rule
            else:
                stable_state = True

