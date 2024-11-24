from utils import Utils


class Configuration:

    def __init__(self, pattern):
        self.pattern = pattern # how this pattern comes as an argument
        self.energy = 0
        
        utils = Utils()
        flatten_pattern = utils.flat(pattern)
        self.weights = self.calculate_weights(flatten_pattern) # what is the pattern type?


    def calculate_energy(self, weights):
        for idx_i, i in enumerate(self.pattern):
            h = 0
            for idx_j, j in enumerate(self.pattern):
                wij = weights[idx_i][idx_j] 
                h += wij*i*j
            
            #if update:
            #    self.pattern[idx_i] = self.hebbian_learning(h, i)
            self.energy += h
                                                                                                                                            

    # 2. Calculate the weights between each of the possible neurons interactions (or the outer product with the vector itself)
    def calculate_weights(self, flatten):
        self.weights = []                                                                                                                  
                                                                                                                                      
        counter_i = 0                                                                                                                 
        counter_j = 0                                                                                                                 
        for i in flatten:                                                                                                             
            n_weights = []                                                             
            for j in flatten:
                wij = 0 if counter_i == counter_j else i*j                                                                            
                n_weights.append(wij)
                counter_j += 1
                                                                                                                                            
            self.weights.append(n_weights.copy())
            counter_i += 1
            counter_j = 0
                                                                                                                                            
        print(f"weights: {self.weights}")
