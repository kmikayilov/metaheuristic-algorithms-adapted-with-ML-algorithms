# class to print text in different colors
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKCYAN = '\033[96m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
  
# global variables
F = 0.5 # Mutation factor
CR = 0.7 # Crossover probability

available_function_settings = [
    {
        "name": "Ackley",
        "bounds": [-32, 32]
    },
    {
        "name": "Rastrigin",
        "bounds": [-5.12, 5.12]
    },
    {
        "name": "Rosenbrock",
        "bounds": [-30,30]
    },
    {
        "name": "Schwefel",
        "bounds": [-500,500]
    }
]

parameter_candidate_pool = [[1.0,0.1], [1.0,0.9], [0.8,0.2]]

_lambda = 1.5
pa = .25
step_size = 0.01
trial = 1