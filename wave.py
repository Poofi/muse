import numpy as np
from matplotlib import pyplot as plt
import matplotlib.animation as animation

def wavegen(p, f, d, ed=0, e=None):
    x = np.linspace(0, p, 1000)
    w = np.sin(x*f*2*np.pi - d)
    if e:
        w = np.multiply(w, np.exp(-(x-ed)*e))
        w[x < ed] = 0
        return x, w

    w = w/np.max(w)
    return x, w



def transmit_wave():
    fig, axs = plt.subplots(4, 1)
    axs[0].set_title("E-field")
    axs[0].set(ylim=(-1.1, 1.1))
    axs[1].set_title("atoms")
    axs[1].set(ylim=(-1.1, 1.1))

    axs[2].set_title("D-field")
    axs[2].set(ylim=(-3, 3))
    axs[3].set_title("sim atoms")
    axs[3].set(ylim=(-1.1, 1.1))

    p = 20
    d = 0
    f1 = 1
    f2 =1.5
    e = 2
    x, w = wavegen(p, f1, d)
    x, w_a = wavegen(p, f2, d)
    w_d = w + w_a

    w_exp = 0
    for i in range(1, p*2):
        x, w_e = wavegen(p, f1, d, ed=i/4, e=e)
        w_exp = w_exp + w_e

    e_line, = axs[0].plot(x, w)
    a_line, = axs[1].plot(x, w_a)
    d_line, = axs[2].plot(x, w_d)
    exp_line, = axs[3].plot(x, w_e)
    def animate(i):
        r = 0.1
        xi, wi = wavegen(p, f1, d + i*r)
        xa, wa = wavegen(p, f2, d + i*r)

        wd = wa - wi
        we = 0
        subs=20
        for j in range(1, p * subs):
            x, w_e = wavegen(p, f1, d+ i*r, ed=j / subs, e=e)
            we = we + w_e
        we = we/subs
       # xe, we = wavegen(p, f1, d + i*r, ed=p/5, e=e)

        e_line.set_ydata(wi)
        a_line.set_ydata(wa)
        d_line.set_ydata(wd)
        exp_line.set_ydata(we)
        return e_line
    ani = animation.FuncAnimation(fig, animate, interval=1, frames=1000)
    plt.show()


transmit_wave()