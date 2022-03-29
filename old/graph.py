import numpy as np
import matplotlib.pyplot as plt
from math import e


def popGrow(B, t, G, c):
    num = B * (e ** (G*t + c*B))
    den = (e ** (G*t + c*B)) - 1
    return num / den

def main():
    hist = []
    for i in range(10):
        hist.append(popGrow(1, i, 0.5, 0.2))
    # plot data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(range(10), hist, color='tab:blue')
    ax.set_title(f'Growth over 10 generations')
    plt.show()


if __name__ == '__main__':
    main()
