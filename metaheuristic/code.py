from .de import DE
from ..helper.config import Config
from ..helper.vector import Vector
from ..helper.setup import bcolors
import numpy as np
import random as rn
from numpy.random import uniform as rnd

class CODE(DE):
    
    def __init__(self, parameter_candidate_pool):
        super().__init__()
        self.parameter_candidate_pool = parameter_candidate_pool
        self.launch()
    
    def initialization(self):
        super().initialization()

    def rand_1_bin(self):
        [f, cr] = self.parameter_candidate_pool[0]

        vectors = super().get_random_individuals(self.cur_index, 3)

        u_i_1_g = Vector()

        dimension = Config.get_dimension()
        function = Config.get_function()

        cutPoint = rn.randint(0, dimension-1)

        for i in range(dimension):
            if i == cutPoint or rnd(0,1) < cr:
                u_i_1_g.position[i] = vectors[2].position[i] + f * ( vectors[0].position[i] - vectors[1].position[i] )
            else:
                u_i_1_g.position[i] = self.p[self.cur_index].position[i]

        u_i_1_g.check_bounds()

        u_i_1_g.set_fitness(function.compute(u_i_1_g.get_position()))

        self.trialVectors.append(u_i_1_g)

    def rand_2_bin(self):
        [f, cr] = self.parameter_candidate_pool[1]

        vectors = super().get_random_individuals(self.cur_index, 5)

        u_i_2_g = Vector()

        dimension = Config.get_dimension()
        function = Config.get_function()

        cutPoint = rn.randint(0, dimension-1)

        for i in range(dimension):
            if i == cutPoint or rnd(0,1) < cr:
                u_i_2_g.position[i] = vectors[0].position[i] + f * ( vectors[1].position[i] - vectors[2].position[i] ) + f * ( vectors[3].position[i] - vectors[4].position[i] )
            else:
                u_i_2_g.position[i] = self.p[self.cur_index].position[i]

        u_i_2_g.check_bounds()

        u_i_2_g.set_fitness(function.compute(u_i_2_g.get_position()))
        self.trialVectors.append(u_i_2_g)

    def current_to_rand_1(self):
        vectors = super().get_random_individuals(self.cur_index, 3)

        [f, cr] = self.parameter_candidate_pool[2]

        function = Config.get_function()

        u_i_3_g = Vector()
        cur_ind = self.p[self.cur_index]

        u_i_3_g.set_position( cur_ind.get_position() + rnd(0,1) * ( vectors[0].get_position() - cur_ind.get_position() ) + f * ( vectors[1].get_position() - vectors[2].get_position() ) )
        u_i_3_g.check_bounds()

        u_i_3_g.set_fitness(function.compute(u_i_3_g.get_position()))

        self.trialVectors.append(u_i_3_g)

    def generation(self):
        self.trialVectors = []
        self.rand_1_bin()
        self.rand_2_bin()
        self.current_to_rand_1()

    def evaluation(self):
        trialVectors = sorted(self.trialVectors, key=lambda individual: individual.get_fitness())

        trialPosition = trialVectors[0].get_position()
        trialFitness = trialVectors[0].get_fitness()

        targetFitness = self.p[self.cur_index].get_fitness()

        if trialFitness <= targetFitness:
            self.p[self.cur_index].set_position(trialPosition)
            self.p[self.cur_index].set_fitness(trialFitness)

    def launch(self):
        self.initialization()

        max_fes = Config.get_max_fes()
        population_size = Config.get_population_size()

        print(bcolors.OKGREEN + '-' * 25 + bcolors.ENDC)
        
        self.cur_iter = 1  

        fes = population_size
        
        while fes < max_fes:
            for i in range(population_size):
                self.cur_index = i
                self.generation()
                self.evaluation()

            fes += 3
            self.cur_iter += 1  
            
            super().total_evaluation()

            print('Iteration: %d --> f([%s]) = %.5f' % (self.cur_iter, np.around(self.BestPosition, decimals=5), self.BestFitness))
            
        super().visualize()
        print(bcolors.OKGREEN + "-" * 25 + bcolors.ENDC)