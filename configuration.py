from typing import List
#from utils import Utils


class Configuration:

    def __init__(self, pattern, name): 
        self.id = id(self) 
        self.name = name
        self.pixels : List[List[int]] = pattern 
        self.flatten_data : List[int] = [] 
        self.energy : int = 0


    def calculate_self_energy(self, flat_weights: List[int], apply_hebbian_learning: bool) -> int:  
        enum_data = enumerate(self.flatten_data)
        for idx_i, i in enum_data: # idx_i is an anchor and it also goes from 0 to 1023 (after j completes its iteration)
            h = 0
            for idx_j, j in enum_data: # idx_j always goes from 0 to 1023 (32x32 image)
                pixels = len(self.flatten_data)
                wij = flat_weights[idx_j + (pixels * idx_i)]
                h += wij*i*j
            
                if apply_hebbian_learning:  
                    if (h <= 0):
                        self.pixels[idx_j * idx_i] 
                        #i *= -1 -> realizar a alteração antes de calcular a energia? (think so)
                        #i = 0

                self.energy += wij*i*j

        print(f"total energy: {self.energy}")

        return self.energy


    #def apply_hebbian_learning(self, weights: List[List[int]]):
    #    
    #    for idx_i, i_state in enumerate(self.pattern):
    #        h = 0
    #        for idx_j, j_state in enumerate(self.pattern):
    #            wij = weights[idx_i][idx_j] 
    #            h += wij* self.pattern[idx_i][idx_j] * self.pattern[idx_i][idx_j]
    #        
    #        
    #        
    #        
    #        
    #        
        
        
                                      



T

    
    
                                                                                                                                            
 
