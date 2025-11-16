from math import sqrt, log
import numpy as np
rng = np.random.default_rng(seed=2025)

import matplotlib.pyplot as plt


NORM = 1/sqrt(2*3.14)

def p(x): # I guess this is the prior?
    return NORM * np.exp(-(x-10)**2/2)

def conditional_g(old, candidate):
    return NORM * np.exp(-(old**2-candidate)**2/2)

def generate_candidate(old):
    return rng.standard_normal() + old

def metropolis_ar(old, candidate):
    return min(
        1, 
        p(candidate)/p(old)
        * conditional_g(old, candidate)
        / conditional_g(candidate, old)
    )

if __name__ == '__main__':

    n_steps = 100000
    samples = [0.,]

    for _ in range(n_steps):
        old = samples[-1]
        candidate = generate_candidate(old)
        acceptance_probability = metropolis_ar(old, candidate)

        # Accept or reject
        if rng.random() < acceptance_probability: samples.append(candidate)
        else: samples.append(old)

    fig, axs = plt.subplots(2,1,figsize=(4,4))
    axs[0].plot(samples)
    axs[1].hist(samples)
    plt.show()



