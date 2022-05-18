from .de import DE
from ..helper.config import Config
from ..helper.vector import Vector
from ..helper.setup import bcolors
import numpy as np
import random as rn

class SDE(DE):
    
    def __init__(self, f, cr):
        super().__init__()
        self.f = f
        self.cr = cr

        population_size = Config.get_population_size()

        if population_size < 4:
            print('The population size must be equal or greater than 4!')  
            return

        if f < 0 or f > 2:
            print('The mutation factor must be between 0 and 2!')  
            return

        if cr < 0 or f > 1:
            print('The crossover probability must be between 0 and 1!')  
            return

        self.launch()

    def initialization(self):
     super().initialization()

    def generation(self):
        self.x_i = self.p[self.cur_index]
        self.random_vectors = super().get_random_individuals(self.cur_index, 3)

    def mutation(self):
        [a, b, c] = self.random_vectors

        self.v_i = Vector()
        self.v_i.set_position( a.get_position() + self.f * ( b.get_position() - c.get_position() ) )

    def crossover(self):
        u_i = Vector()

        dimension = Config.get_dimension()

        j_rand = rn.randrange(0, dimension)

        for j in range(dimension):
            if self.x_i.position[j] < self.cr or j == j_rand:
                u_i.position[j] = self.v_i.position[j]
            else:
                u_i.position[j] = self.x_i.position[j]

        self.u_i = u_i

    def evaluation(self):
        function = Config.get_function()

        TargetFitness = function.compute(self.x_i.get_position())
        TrialFitness = function.compute(self.u_i.get_position())

        if TrialFitness < TargetFitness:
            self.p[self.cur_index].set_position(self.u_i.get_position())
            self.p[self.cur_index].set_fitness(TrialFitness)

    def launch(self):
        self.initialization()

        print(bcolors.OKGREEN + '-' * 25 + bcolors.ENDC)

        for i in range(Config.get_iteration()):
            self.cur_iter = i 
            for j in range(Config.get_population_size()):
                self.cur_index = j
                self.generation()
                self.mutation()
                self.crossover()
                self.evaluation()

            super().total_evaluation()

            print('Iteration: %d --> f([%s]) = %.5f' % (self.cur_iter + 1, np.around(self.BestPosition, decimals=5), self.BestFitness))

        super().visualize()
        print(bcolors.OKGREEN + "-" * 25 + bcolors.ENDC)