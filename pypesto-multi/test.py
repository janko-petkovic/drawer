# import torch
import os
os.environ["OMP_NUM_THREADS"] = "1" 
import numpy as np
from functools import partial

from pypesto import optimize, Problem, Objective
import pypesto.engine

from fides import BFGS

def main():
    # Number of parameters that the routine minimizes 
    n_pars = 65 

    # Generate the data
    X = np.ones(n_pars)
    P = np.random.randn(n_pars) # true parameter vector
    Y = X*P


    # Pypesto boilerplate
    def loss_fn(X, Y, p):
        loss = -((p*X - Y)**2).sum()
        return loss

    def grad_fn(X, Y, p):
        return -2*X*(p*X - Y) 

    p_names = [f'[{i}]' for i in range(n_pars)]
    p_scales = ['log10']*n_pars
    lb_full = list(-1*np.ones(n_pars))
    ub_full = list(1*np.ones(n_pars))

    obj_part = partial(loss_fn, X, Y)
    obj_grad = partial(grad_fn, X, Y)

    # create pypesto objective function
    objective = Objective(fun=obj_part, 
                          grad=obj_grad)

    # create pypesto problem object
    problem = Problem(objective=objective,  # objective function
                      lb=lb_full,  # lower bounds
                      ub=ub_full,  # upper bounds
                      x_names=p_names,  # parameter names
                      x_scales=p_scales)  # parameter scale

    # High number of starts so there is time to look at htop
    n_starts=20000


    # Scipy behaves correctly always
    # optimizer = optimize.ScipyOptimizer()

    # Cmaes seems to always use multiple processes
    # optimizer = optimize.CmaesOptimizer()

    # BFGS switches to multiple processes when the number of parameters to be
    # optimized is >64
    optimizer = optimize.FidesOptimizer(hessian_update=BFGS(), verbose=False)

    # engine = pypesto.engine.SingleCoreEngine()
    engine = pypesto.engine.MultiProcessEngine()

    # do the optimization
    result = optimize.minimize(problem=problem, 
                               optimizer=optimizer, 
                               n_starts=n_starts,
                               progress_bar=True,
                               engine=engine
                               )

if __name__ == '__main__':
    main()
