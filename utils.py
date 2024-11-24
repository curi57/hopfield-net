


class Utils:

    def flat(self, pattern):    
        flatten = []               
        for i in pattern:
            for j in i:
                flatten.append(j);
        return flatten

    def create_pattern(self):
        
        pattern = [[1, -1, -1],
                   [-1, 1, -1],
                   [-1, -1, 1]]
        
        flatten = self.flat(pattern)
        return flatten
