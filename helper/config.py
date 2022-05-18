class Config:
    function = None
    populationSize = 30
    dimension = 30
    iteration = 1000
    domainLowerBound = -1
    domainUpperBound = 1
    maxFes = 3000

    #----------------------------------------------------

    @classmethod
    def get_function(cls):
        return cls.function

    @classmethod
    def set_function(cls, function):
        cls.function = function

    #-----------------------------------------------------

    @classmethod
    def get_population_size(cls):
        return cls.populationSize

    @classmethod
    def set_population_size(cls, population_size):
        cls.populationSize = population_size

    #-----------------------------------------------------
    
    @classmethod
    def get_dimension(cls):
        return cls.dimension

    @classmethod
    def set_dimension(cls, dimension):
        cls.dimension = dimension

    #-----------------------------------------------------
    
    @classmethod
    def get_iteration(cls):
        return cls.iteration

    @classmethod
    def set_iteration(cls, iteration):
        cls.iteration = iteration

    #-----------------------------------------------------
    
    @classmethod
    def get_domain_lower_bound(cls):
        return cls.domainLowerBound

    @classmethod
    def set_domain_lower_bound(cls, domain_lower_bound):
        cls.domainLowerBound = domain_lower_bound

    #-----------------------------------------------------
    
    @classmethod
    def get_domain_upper_bound(cls):
        return cls.domainUpperBound

    @classmethod
    def set_domain_upper_bound(cls, domain_upper_bound):
        cls.domainUpperBound = domain_upper_bound

    #-----------------------------------------------------

    @classmethod
    def get_max_fes(cls):
        return cls.maxFes

    @classmethod
    def set_max_fes(cls, max_fes):
        cls.maxFes = max_fes

    #-----------------------------------------------------