def flat(pattern):    
    flatten = []               
    for i in pattern:
        for j in i:
            flatten.append(j);
    return flatten

def calculate_configuration_energy(configuration, weights):
    configuration_energy = 0
    for i, idx_i in enumerate(configuration):
        h = 0
        for j, idx_j in enumerate(configuration):
            wij = weights[idx_i][idx_j]
            h += wij*i*j
                                           
        if (h > 0):
            i *= 1
        elif (h < 0):
            i *= -1
                                       
        configuration_energy += h

    return configuration_energy


# 1. Create the pattern to memorize
pattern = [[1, -1, -1],
           [-1, 1, -1],
           [-1, -1, 1]]
flatten = flat(pattern)
print(f"pattern: {flatten}")

# 2. Calculate the weights between each of the possible neurons interactions (or the outer product with the vector itself)
weights = []
enum_flatten = enumerate(flatten)
for i,idx_i in enum_flatten:
    weights.append([i*j if idx_i != idx_j else 0 for j,idx_j in enum_flatten])
print(f"weights: {weights}")

stable_configuration_energy_value = calculate_configuration_energy(flatten, weights)
print(f"stable_configuration_energy_value: {stable_configuration_energy_value}")

random_input = [[-1, -1, 1],
                [-1, 1, 1],
                [1, -1, -1]]
flatten_input = flat(random_input)
print(f"input {flatten_input}")

is_stable_state = False
while is_stable_state:
    energy = calculate_configuration_energy(flatten_input, weights)
    if (energy == stable_configuration_energy_value): 
        print(f"stable state [end]: {flatten_input}")
        is_stable_state = True

    
    
    
    
    

    
    





















         






















