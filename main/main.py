import time

from ..helper.benchmark import Function
from ..helper.config import Config
from ..metaheuristic.code import CODE
from ..metaheuristic.sde import SDE
from ..metaheuristic.jde import JDE
from ..metaheuristic.cuckoo import Cuckoo
from ..helper.setup import available_function_settings, parameter_candidate_pool, F, CR, _lambda, pa, step_size, trial

def initial_config(func_id):
    fnc = Function(fnc=available_function_settings[func_id]["name"])
    bounds = available_function_settings[func_id]["bounds"]

    Config.set_function(fnc)
    Config.set_domain_lower_bound(bounds[0])
    Config.set_domain_upper_bound(bounds[1])

def sde_launch(func_id):
    initial_config(func_id)
    
    start = time.time()
    sde = SDE(F, CR)
    end = time.time()
    
    print(f"Time taken for SDE to find the most optimal value is {end - start} seconds")
    
def code_launch(func_id):
    initial_config(func_id)
    
    start = time.time()
    code = CODE(parameter_candidate_pool)
    end = time.time()
    
    print(f"Time taken for CODE to find the most optimal value is {end - start} seconds")
    
def jde_launch(func_id):
    initial_config(func_id)
    
    start = time.time()
    jde = JDE(F, CR)
    end = time.time()
    
    print(f"Time taken for JDE to find the most optimal value is {end - start} seconds")
     
def cuckoo_launch(func_id):
    initial_config(func_id)
    
    start = time.time()
    cuckoo = Cuckoo(_lambda, pa, step_size, trial)
    end = time.time()
    
    print(f"Time taken for Cuckoo search to find the most optimal value is {end - start} seconds")
    
    
if __name__ == "__main__":
    sde_launch(0)
    
    
