from src.ecoplotlib import plot
import matplotlib.pyplot as plt
plt.style.use('./src/ecoplotlib/eplstyle.mplstyle')
import numpy as np

def f(X):
    return np.sin(X) + np.random.randn(X.shape[0])

X = np.linspace(1,10,100)
Y = f(X)

fig, axs = plt.subplots(2,2, figsize=(8,6))

ax = axs[0,0]
ax.plot(X,Y)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title(r'\Huge{Some title}'+'\n'+r'\tiny{Subtitle}')

plt.show()

