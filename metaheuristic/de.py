from ..helper.config import Config
from ..helper.vector import Vector
from matplotlib import pyplot as plt
from numpy.random import choice

class DE:
    def __init__(self):
        self.cur_iter = 0

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

    def get_random_individuals(self, current_index, num_of_vectors):
        candidates = [cand for cand in range(Config.get_population_size()) if cand != current_index]
        idx = choice(candidates, num_of_vectors, replace=False)
        return [self.p[i] for i in idx]

    def total_evaluation(self):
        temp = sorted(self.p, key=lambda individual: individual.get_fitness())

        self.BestFitness = temp[0].get_fitness()

        if self.BestFitness < self.PrevBestFitness:
            self.BestPosition = temp[0].get_position()
            self.PrevBestFitness = self.BestFitness
            self.BestResults.append(self.BestFitness)
        
    def visualize(self):
        plt.plot(self.BestResults)
        plt.plot(self.AverageResults)
        plt.legend()
        plt.xlabel('Iterations')
        plt.ylabel('Objective Function Value')
        plt.show()