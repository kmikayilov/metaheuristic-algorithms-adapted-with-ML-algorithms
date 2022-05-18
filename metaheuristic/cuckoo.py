from .de import DE
from ..helper.config import Config
from ..helper.vector import Vector
from ..helper.setup import bcolors
import numpy as np
import random as rn
from matplotlib import pyplot as plt

class Cuckoo():
    
    def __init__(self, _lambda, pa, step_size, trial):
        self.cur_iter = 0
        self._lambda = _lambda
        self.pa = pa
        self.step_size = step_size
        self.trial = trial

        self.launch()

    def initialization(self):
        self.p = []

        for i in range(Config.get_population_size()):
        self.p.append(Vector())

        self.p = sorted(self.p, key=lambda individual: individual.get_fitness())

        self.BestPosition = self.p[0].get_position()
        self.BestFitness = self.p[0].get_fitness()
        self.PrevBestFitness = self.BestFitness
        self.BestResults = []
        self.AverageResults = []

    def generation(self):
        for i in range(Config.get_population_size()):
            self.p[i] = self.cuckoo(self.p[i])
            self.p[i].set_fitness(Config.get_function().compute(self.p[i].get_position()))

        j = i
        
        while j == i:
            j = np.random.randint(0, Config.get_population_size())

        if(self.p[i].get_fitness() < self.p[j].get_fitness()):
            self.p[j].set_position(self.p[i].get_position())
            self.p[j].set_fitness(self.p[i].get_fitness())

    def levy_flight(self):
        sigma1 = np.power((math.gamma(1 + self._lambda) * np.sin((np.pi * self._lambda) / 2)) / math.gamma((1 + self._lambda) / 2) * np.power(2, (self._lambda - 1) / 2), 1 / self._lambda)
        sigma2 = 1

        u = np.random.normal(0, sigma1, size=Config.get_dimension())
        v = np.random.normal(0, sigma2, size=Config.get_dimension())
        step = u / np.power(np.fabs(v), 1 / self._lambda)

        return step 

    def cuckoo(self, vector):
        step_size = self.step_size * self.levy_flight()
        vector.set_position(vector.get_position() + step_size)
        vector.check_bounds()
        return vector

    def crossover(self):
        self.p = sorted(self.p, key=lambda individual: individual.get_fitness())
        
        for a in range(1, Config.get_population_size()):
            r = np.random.rand()
            if r < self.pa:
                for i in range(Config.get_dimension()):
                    p = np.random.rand()
                    if p < self.pa:
                        self.p[a].position[i] = np.random.rand() * (Config.get_domain_upper_bound() - Config.get_domain_lower_bound())  + Config.get_domain_lower_bound()
                
                self.p[a].set_fitness(Config.get_function().compute(self.p[a].get_position()))

    def evaluation(self):
        temp = sorted(self.p, key=lambda individual: individual.get_fitness())

        if temp[0].get_fitness() < self.BestFitness:
            self.BestFitness = temp[0].get_fitness()
            self.BestPosition = temp[0].get_position()

        self.BestResults.append(self.BestFitness)

    def visualize(self):
        plt.plot(self.BestResults)
        plt.plot(self.AverageResults)
        plt.legend()
        plt.xlabel('Iterations')
        plt.ylabel('Objective Function Value')
        plt.show()

    def launch(self):

        print(bcolors.OKGREEN + '-' * 25 + bcolors.ENDC)

        for trial in range(self.trial):
            np.random.seed(trial)
            self.initialization()

            for iteration in range(Config.get_iteration()):
                self.generation()
                self.crossover()
                self.evaluation()

                print('Trial: %d --> Iteration: %d --> f([%s]) = %.5f' % (trial, iteration, np.around(self.BestPosition, decimals=5), self.BestFitness))

        print(bcolors.OKGREEN + "-" * 25 + bcolors.ENDC)
        self.visualize()