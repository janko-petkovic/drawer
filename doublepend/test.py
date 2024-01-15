import matplotlib.pyplot as plt
plt.style.use('rdnstyle')
import numpy as np

from numba import jit

LENGTH_1 = 5
LENGTH_2 = 5


def h1(x):
        th1, th2, pth1, pth2 = x
        return pth1 * pth2 * np.sin(th1-th2) / (1 + np.sin(th1-th2)**2)

def h2(x):
        th1, th2, pth1, pth2 = x
        return (pth1**2 + 2*pth2**2 - 2 * pth1 * pth2 * np.cos(th1-th2)) \
                        / 2 * (1 + np.sin(th1-th2)**2)


def f(t, x):
        th1, th2, pth1, pth2 = x
        th1_dot = (pth1 - pth2 * np.cos(th1-th2))/(1 + np.sin(th1-th2)**2)
        th2_dot = (-pth1*np.cos(th1-th2) + 2 * pth2) \
                        / (1 + np.sin(th1 - th2)**2)
        pth1_dot = - 20 * np.sin(th1) - h1(x) + h2(x) * np.sin(2 * (th1-th2))
        pth2_dot = - 10 * np.sin(th2) + h1(x) - h2(x) * np.sin(2 * (th1-th2))
        return (th1_dot,
                th2_dot,
                pth1_dot,
                pth2_dot)


def transoform_to_plottable(x):
        x_1 = LENGTH_1 * np.sin(x[0])
        x_2 = x_1 + LENGTH_2 * np.sin(x[1])
        y_1 = LENGTH_1 * np.cos(x[0])
        y_2 = y_1 + LENGTH_2 * np.cos(x[1])

        return ((0,x_1), (0,-y_1)), ((x_1, x_2), (-y_1, -y_2))


from scipy.integrate import solve_ivp
res = solve_ivp(f, 
                (0,10), 
                [1.,1.,0,0], 
                dense_output=True,
                method='RK45',
                max_step=1e-2)

print('Finished integration\n')


import matplotlib.animation as animation

fig = plt.figure()
ax = fig.add_subplot()
ax.set_aspect('equal')


def animate(i):
        t = res.sol.ts[i]
        interpolant = res.sol.interpolants[i]
        x = interpolant(t)

        data_1, data_2 = transoform_to_plottable(x)
        ax.clear()
        ax.plot(*data_1)
        ax.plot(*data_2)
        ax.set_xlim(-10,10)
        ax.set_ylim(-10,10)
        
anim = animation.FuncAnimation(fig, animate, frames=1000, interval=60)
writevideo = animation.FFMpegWriter(fps=20)
anim.save('video.mp4', writer=writevideo)
