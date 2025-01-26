import numpy as np
import matplotlib as plt


def py_integrate_g_against_spikes(g0, t_end, dt, t_spikes):
    '''returns some numpy stuff'''
    
    if t_spikes[0] < 0: raise ValueError('Spikes start before t=0')
    if t_end < t_spikes[-1]: raise ValueError('Spikes continue after t_end')

    g_t = 

    for left_t_spike, right_t_spike in zip(t_spikes[:-1], t_spikes[1:]):
        n_steps = int((right_t_spike - left_t_spike)/dt) + 1
        
        for _ in n_steps:





if __name__ == '__main__':

