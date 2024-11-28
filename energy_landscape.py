


class EnergyLandscape():

    def __init__(self):
        print("Initializing the energy landscape")
        self.energy_map = {}
    
    # um dicionário que mapeia valores energéticos para o id da configuração
    def add_point(self, configuration):
        configuration.calculate_self_energy()

        self.energy_map[configuration.energy] = configuration.id

    def find_point(self):
        print("Finding point")



    

    
