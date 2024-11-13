from typing import Callable
from functools import partial
from time import time
from datetime import datetime, timedelta

import torch
import numpy as np

from modules.utils import parse_config
from modules.simulators import verz_eggl



def generate_ground_truth_joint(simulator: Callable, 
                                simulator_setup: dict,
                                params_prior: dict) -> None:
    '''
    We run this method to generate the joint ground truth sampling.
    Later on we will subsample from this dataset to carry out the various
    benchmarking routines.
    '''

    # Simulator with fixed parameters
    partial_sim = partial(simulator, simulator_setup=simulator_setup)

    # Generate the parameter samples (logarythmic sampling)
    theta = np.stack([np.random.uniform(params_prior[key][0], params_prior[key][1],
                                        size=simulator_setup['num_simulations'])
                        for key in params_prior.keys()], axis=1)

    params_list = []
    for t in theta:
        params_list.append({k:v for k,v in zip(params_prior.keys(), t)})

    from p_tqdm import p_map
    x = p_map(partial_sim, params_list, num_cpus=simulator_setup['num_workers'])
    x = np.array(x)

    # import matplotlib.pyplot as plt
    # for xx in x:
    #     plt.plot(xx)
    # plt.show()

    np.save('data/x.npy', x)
    np.save('data/theta.npy', theta)
    


if __name__ == '__main__':

    # Select the problem to work on
    # simulator = simulate_single_neuron_stability
    simulator = verz_eggl

    # Parse the config file
    simulator_setup, _, params_prior, _ = parse_config('config.toml')

    # Get the input
    print('\nConfiguration file parsed corretly, ready to generate ground truth joint.')
    print(f' > Number of simulations: {simulator_setup["num_simulations"]}')
    print(f' > Number of workers: {simulator_setup["num_workers"]}')
    print(f'\n > Generation started:\t{datetime.now().strftime("%H:%M:%S")}')


    # Generating ground truth
    beg = time()
    generate_ground_truth_joint(simulator,
                                simulator_setup,
                                params_prior)
    end = time()

    print(f' > Generation complete:\t{datetime.now().strftime("%H:%M:%S")}')

    # Light formatting for the runtime
    tds = str(timedelta(seconds=end-beg)).split(':')
    print(f' > Total runtime:\t{tds[0]}h {tds[1]}min {tds[2]:.4}s')
