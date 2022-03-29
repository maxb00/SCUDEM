import argparse
import numpy as np
import matplotlib.pyplot as plt
import pdb

parser = argparse.ArgumentParser(description='Control simulation variables')
parser.add_argument('-g', '--generations', metavar='generations', type=int, nargs=1, help='Number of generations', default=[10])
parser.add_argument('-p', '--population', metavar='population', type=int, nargs=1, help='Starting population size', default=[1])
args = parser.parse_args()
GENERATIONS = args.generations[0]
initialPopulation = args.population[0]


def risk() -> float:
    ''' Function to define risk taken by stealing live hairs
        Returns some number between 0 and 1.'''
    return np.random.random_sample()


def reward() -> float:
    ''' Fucntion to define rewqrd gained by stealing live hairs
        Returns some number between 0 and 1.'''
    return np.random.random_sample()


def growth(ri, re, pi, pd):
    ''' Piecewise function dictating the change in bird population over a given
        year, with respect to risk and reward. '''
    condition = re >= (ri * (1 - pd)) # Piecewise condition
    if condition:
        # piecewise part 1
        return pi + re - pd - (ri * (1 - pd))
    else:
        # piecewise part 2
        return pi - pd

def main():
    B = initialPopulation
    ri = risk()
    re = reward()
    dbdt = growth(re, ri, 0.2, 0.1)
    B += dbdt
    history_b = [B]
    history_dbdt = [dbdt]
    for i in range(GENERATIONS):
        # dbdt = Growth * Pop Control
        ri = risk()
        re = reward()
        dbdt = growth(ri, re, 0.2, 0.1) * (1 - (B / initialPopulation))
        B += dbdt
        history_b.append(B)
        history_dbdt.append(dbdt)
    pdb.set_trace()

    # plot data
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(range(GENERATIONS + 1), history_b, color='tab:blue')
    # ax.plot(range(GENERATIONS + 1), history_dbdt, color='tab:orange')
    ax.set_title(f'Growth over {GENERATIONS} generations')
    plt.show()


if __name__ == '__main__':
    main()
