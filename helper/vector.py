from .config import Config


class Vector:
    
    def __init__(self):
        self.generate_vector()

    #-----------------------------------------------------

    def generate_vector(self):
        function = Config.get_function()
        dimension = Config.get_dimension()
        domain_lower_bound = Config.get_domain_lower_bound()
        domain_upper_bound = Config.get_domain_upper_bound()

        self.position = np.random.uniform(domain_lower_bound, domain_upper_bound, (dimension,))
        self.fitness = function.compute(self.position)

    #-----------------------------------------------------

    def get_position(self):
        return self.position

    def set_position(self, position):
        self.position = position

    #-----------------------------------------------------

    def get_fitness(self):
        return self.fitness

    def set_fitness(self, fitness):
        self.fitness = fitness  

    #-----------------------------------------------------

    def check_bounds(self):
        dimension = Config.get_dimension()
        domain_lower_bound = Config.get_domain_lower_bound()
        domain_upper_bound = Config.get_domain_upper_bound()

        for i in range(dimension):
            if self.position[i] < domain_lower_bound:
                self.position[i] = domain_lower_bound
            
            if self.position[i] > domain_upper_bound:
                self.position[i] = domain_upper_bound