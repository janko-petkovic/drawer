import numpy as np
import matplotlib.pyplot as plt
from ctypes import cdll
from ctypes import c_float, POINTER


def e1_integrator_lorenzo(dt, T, alpha, tau, spike_times):
    
    times = np.arange(0,T,dt)
    t_next_spike = spike_times.pop(0) if spike_times else np.inf

    x_t = [0.]
    x = 0.
    
    for t in times:
        if t >= t_next_spike:
            t_next_spike = spike_times.pop(0) if spike_times else np.inf
            x += alpha * (1 - x_t[-1])
        else:
            x += dt * (-x/tau)

        x_t.append(x)
    
    return np.array(x_t)


if __name__ == '__main__':
    
    lib = cdll.LoadLibrary('./integrator_lorenzo_cpp.so')
    lib.e1_integrator_lorenzo_cpp.argtypes = [
        c_float,
        c_float,
        c_float,
        c_float,
        POINTER(c_float)
    ]
    
    rng = np.random.default_rng(2025)

    dt = 0.001
    T = 10
    alpha = 0.1
    tau = 0.1

    n_spikes = 100
    spike_times = list(np.sort(rng.uniform(0, T, size=(n_spikes))))
    
    g_t = e1_integrator_lorenzo(dt, T, alpha, tau, spike_times)
    g_t = lib.e1_integrator_lorenzo_cpp(dt, T, alpha, tau, spike_times)
    

    # plt.plot(g_t)
    # plt.show()
    


