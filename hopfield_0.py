def flat(pattern):    
    flatten = []               
    for i in pattern:
        for j in i:
            flatten.append(j);
    return flatten


def calculate_configuration_energy(configuration, weights, update = False):
    configuration_energy = 0
    for idx_i, i in enumerate(configuration):
        h = 0
        for idx_j, j in enumerate(configuration):
            wij = weights[idx_i][idx_j] # index out of range
            h += wij*i*j
        
        if update:
            configuration[idx_i] = update_rule(h, i)

        configuration_energy += h

    return configuration_energy


def update_rule(h, i):
    #print(f"h: {h}")
    if (h > 0):
        i *= 1
    elif (h <= 0):
        i *= -1

    return i;


# 1. Create the pattern to memorize
pattern = [[1, -1, -1],
           [-1, 1, -1],
           [-1, -1, 1]]
flatten = flat(pattern)
print(f"pattern: {flatten}")

# 2. Calculate the weights between each of the possible neurons interactions (or the outer product with the vector itself)
weights = []

counter_i = 0
counter_j = 0
for i in flatten:
    n_weights = [] # what happens here if i do not copy the value?
    for j in flatten:
        wij = 0 if counter_i == counter_j else i*j
        n_weights.append(wij)
        counter_j += 1

    weights.append(n_weights.copy())
    counter_i += 1
    counter_j = 0

print(f"weights: {weights}")

stable_configuration_energy_value = -(calculate_configuration_energy(flatten, weights)) 
print(f"stable_configuration_energy_value: {stable_configuration_energy_value}")

random_input = [[-1, -1, 1],
                [-1, 1, 1],
                [1, -1, -1]]
flatten_input = flat(random_input)
print(f"input {flatten_input}")
current_configuration_energy_value = -(calculate_configuration_energy(flatten_input, weights))
print(f"current energy: {current_configuration_energy_value}")

stable_state = False
energy = float('inf')
while not stable_state:
    if (energy > stable_configuration_energy_value): 
        energy = -(calculate_configuration_energy(flatten_input, weights, True)) # calculates de energy of the system and apply the neurons update rule
        print(f"flatten_input: {flatten_input}")
        print(f"updated energy: {energy}")
    else:
        print(f"stable state [end]: {flatten_input}")
        stable_state = True

    
    
    
    
    

    
    





















         






















