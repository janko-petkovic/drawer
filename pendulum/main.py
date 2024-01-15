import matplotlib.pyplot as plt
import matplotlib.animation as animation
from IPython import display
import numpy as np
from scipy.integrate import solve_ivp



OMEGA = 1

def f(t,x):
    return x[1], -OMEGA**2 * x[0], 




def main():
    res = solve_ivp(f, (0.,10.), [2., 0], dense_output=True, max_step=1e-1)

    fig = plt.Figure()
    ax = fig.add_subplot()

    def animation_function(frame_idx):
        t = res.sol.ts[frame_idx]
        interpolant = res.sol.interpolants[frame_idx]
        x = interpolant(t)
        ax.clear()
        ax.scatter(x[0], 0)
        ax.set_xlim(-2,2)

    anim_created = animation.FuncAnimation(fig, animation_function, frames=50,
                                 interval=25)

    writevideo = animation.FFMpegWriter(fps=60)
    anim_created.save('video.mp4', writer=writevideo)
    # video = anim_created.to_html5_video()
    # html = display.HTML(video)
    # display.display(html)

    plt.close()


if __name__ == '__main__':
    main()
