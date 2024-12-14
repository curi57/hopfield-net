


from energy_landscape import Configuration


class Utils:

    def flat(self, configuration : Configuration):    
        for i in configuration.pattern:
            for j in i:
                configuration.flatten_pattern.append(j)
    
    
    
  
