from utils import Utils


class Configuration:

    def __init__(self, pattern, name): 
        self.utils = Utils()        
        self.id = id(self) # not necessary

        print(id(self))
        print(self.id)

        self.name = name
        self.pattern = pattern # array multidimensional
        self.flatten_configuration_pattern = [] # "same" multidimensional array, but flatten

        self.energy = None


    def calculate_self_energy(self, weights):
        if len(weights) == 0:
            raise Exception("Calculate weights before is mandatory")

        self.energy = 0
        for idx_i, i in enumerate(self.pattern):
            h = 0
            for idx_j, j in enumerate(self.pattern):
                wij = weights[idx_i][idx_j] 
                h += wij*i*j
              
            self.energy += h


    def flat(self):
        self.utils.flat(self)
                                                                                                                                            
 
