from .aux import *

def plot(ax, X,Y, **kwargs):
    out = ax.plot(X,Y, **kwargs)
    set_all(ax, **kwargs)
    return out
