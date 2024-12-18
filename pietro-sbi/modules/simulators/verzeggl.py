'''
dX = -theta ( X - mu ) dt + X sigma dW 

To integrate this we use the following Euler-Something scheme

dx = - theta ( x - mu ) dt + x sigma sqrt(dt) eta

where eta ~ normal(0,1)

'''

import numpy as np
from scipy.stats import pearsonr

def verz_eggl(params,simulator_setup):

    # Local copies of the parameters
    # mu = np.exp(params['mu'])
    # theta = np.exp(params['theta'])
    # sigma = np.exp(params['sigma'])

    mu = 0.47
    v = 0.16
    theta = np.exp(params['theta'])
    sigma = np.sqrt(theta * (2*v) / (mu**2 + v))

    # Compute the number of steps to integrate the system in function of 
    # theta (dt * theta < 1)
    dt = 0.1 / theta

    # ensure compatibility between integration dt and readout delta_t
    if dt > simulator_setup['delta_t']: 
        # print('Provided delta_t is small enought to integrate. Using it')
        dt = simulator_setup['delta_t']

    else:
        best_folds_dt_in_delta_t = simulator_setup['delta_t'] // dt + 1
        dt = simulator_setup['delta_t'] / best_folds_dt_in_delta_t
        
    sqrt_dt = np.sqrt(dt)

    n_timesteps = int(simulator_setup['T'] / dt)
    

    # Integrator (some smart jit here?)
    # in theory this should not explode
    ts = np.array([dt*i for i in range(n_timesteps)])
    etas = np.random.randn(n_timesteps)

    x = np.empty_like(ts)
    x[0] = 0.5

    for i in range(1,n_timesteps):
        xpre = x[i-1]
        x[i] = xpre -theta*(xpre - mu) + xpre * sigma * sqrt_dt * etas[i]

    #### METRIC ####
    eval_steps = int(simulator_setup['T'] / simulator_setup['delta_t'])

    eval_ts = np.array([simulator_setup['delta_t'] * i for i in
                       range(eval_steps)])[-simulator_setup['eval_points']:]

    eval_x = x[np.isin(ts, eval_ts)]

    deltas = eval_x[1:] - eval_x[:-1]

    # return x
    return pearsonr(deltas[:-1], deltas[1:]).statistic
