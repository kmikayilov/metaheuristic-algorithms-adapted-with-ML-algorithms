from .config import Config
import numpy as np

class Function:
    def __init__(self, fnc=None):
        self.d = Config.get_dimension()

        benchmarks = {
        'Ackley': self.Ackley,
        'Rastrigin': self.Rastrigin,
        'Rosenbrock': self.Rosenbrock,
        'Schwefel': self.Schwefel,
        'Default': self.def_fnc
        }

        if fnc is None or fnc not in benchmarks:
            self.func_name = 'Default'
            self.f = benchmarks[self.func_name]
        else:
            self.func_name = fnc
            self.f = benchmarks[self.func_name]
        
        print('*' * 25 + ' ' + self.func_name + ' function is set to optimize ' + '*' * 25)

    def compute(self, vector):
        return self.f(vector)

    def Ackley(self, vector):
        a = 20
        b = 0.2
        c = 2 * np.pi

        term_1 = sum(vector ** 2)
        term_2 = sum(np.cos(c * vector))

        f = -a * np.exp(-b * np.sqrt(term_1)) - np.exp(term_2) + a + np.exp(1)

        return f

    def Rastrigin(self, vector):
        c = 2 * np.pi

        term = sum(vector ** 2 - 10 * np.cos(c * vector))

        f = 10 * self.d + term
        
        return f

    def Rosenbrock(self, vector):
        sum = 0

        for i in range(1, self.d-1):
            sum += 100 * (vector[i+1] - vector[i] ** 2) ** 2 + (vector[i] - 1) ** 2   

        return sum

    def Schwefel(self, vector):
        
        term = sum(vector * np.sin(np.sqrt(np.absolute(vector))))
        
        f = 418.9829 * self.d - term

        return f

    def def_fnc(self, vector):
        return vector[0]**2.0 + vector[1]**2.0