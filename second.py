# File to model and graph a system of differential equations
# modeling population change in birds who steal hair from live animals.
from math import cos
from math import pi as p
import numpy as np
import matplotlib.pyplot as plt


# globals true for every population
pi = 0.05 # proportion of normal pop increase
pd = 0.75 # proportion of normal pop decrease
pop_max = 20000 # population maximum
single_pop_max = 10000
generations = 100
single_pop_generations = 50

# computational functions (building system)
def temp(theta, beta):
    ''' Temperature function for the system of differential equations. '''
    return abs(beta * cos(theta))


def risk(att, att_max, infect, infect_max) -> float:
    num = att + infect
    den = att_max + infect_max
    return num / den


def reward(rho, rho_max, eta, eta_max, beta, theta) -> float:
    ''' Reward function for the system of differential equations. '''
    num = rho + eta + temp(theta, beta)
    den = rho_max + eta_max + beta
    return num / den


def growth(ri, re, pi, pd, type=None):
    ''' Piecewise function dictating the change in bird population over a given
        year, with respect to risk and reward. '''
    if type:
        if type == 'live':
            return pi + re - pd - (ri * (1 - pd))
        elif type == 'dead':
            return pi + re - pd - (ri * (1 - pd))
        elif type == 'nohair':
            return pi - pd
        else:
            # whoops? just in case
            condition = re >= (ri * (1 - pd)) # Piecewise condition
            if condition:
                # piecewise part 1
                return pi + re - pd - (ri * (1 - pd))
            else:
                # piecewise part 2
                return pi - pd
    else:
        condition = re >= (ri * (1 - pd)) # Piecewise condition
        if condition:
            # piecewise part 1
            return pi + re - pd - (ri * (1 - pd))
        else:
            # piecewise part 2
            return pi - pd
    

# Data functions
def load_live_data():
    '''Holds data for birds who steal live hairs'''
    # maximums
    beta = 0.15
    att_max = 0.5
    infect_max = 0.5
    rho_max = 0.5 # predator constant
    eta_max = 0.5 # parasite constant

    # actives (max be moved)
    theta = pi / 6 # range 0 - pi, min at pi/2
    att = 0.1
    infect = 0.05
    rho = 0.15
    eta = 0.075

    return [beta, att_max, infect_max, rho_max, eta_max], [theta, att, infect, rho, eta]


def load_dead_data():
    '''Holds data for birds who steal dead hairs'''
    # maximums
    beta = 0.12
    att_max = 0.5
    infect_max = 0.5
    rho_max = 0.5 # predator constant
    eta_max = 0.5 # parasite constant

    # actives (max be moved)
    theta = pi / 3 # range 0 - pi, min at pi/2
    att = 0.05
    infect = 0.2
    rho = 0.05
    eta = 0.01

    return [beta, att_max, infect_max, rho_max, eta_max], [theta, att, infect, rho, eta]


def load_nohair_data():
    '''Holds data for birds who steal no hairs'''
    # maximums
    beta = 0.12
    att_max = 0.5
    infect_max = 0.5
    rho_max = 0.5 # predator constant
    eta_max = 0.5 # parasite constant

    # actives (max be moved)
    theta = 0 # range 0 - pi, max at pi/2
    att = 0.001
    infect = 0.05
    rho = 0.2
    eta = 0.4

    return [beta, att_max, infect_max, rho_max, eta_max], [theta, att, infect, rho, eta]


def main():
    # initialize populations
    pop_live = 9000
    pop_dead = 5000
    pop_nohair = 5000

    # initialize history lists
    live_history = [pop_live]
    dead_history = [pop_dead]
    nohair_history = [pop_nohair]

    # run years, saving history, live only
    single_pop_history = [pop_live]
    for _ in range(single_pop_generations):
        beta, att_max, infect_max, rho_max, eta_max = load_live_data()[0]
        theta, att, infect, rho, eta = load_live_data()[1]
        pop_growth = growth(risk(att, att_max, infect, infect_max), reward(rho, rho_max, eta, eta_max, beta, theta), pi, pd)
        pop_live += pop_growth * pop_live * (1-pop_live/single_pop_max)
        single_pop_history.append(pop_live)

    # plot single pop history
    plt.plot(single_pop_history, label='live')
    plt.legend()
    plt.title('Single Population History')
    plt.xlabel('Generations')
    plt.ylabel('Population')
    plt.show()

    pop_live = 5000
    # run years, saving history
    for _ in range(1, generations): # 100 years
        # load data
        [beta, att_max, infect_max, rho_max, eta_max], [theta, att, infect, rho, eta] = load_live_data()
        # calculate risk and reward
        risk_live = risk(att, att_max, infect, infect_max)
        reward_live = reward(rho, rho_max, eta, eta_max, beta, theta)
        # calculate growth
        growth_live = growth(risk_live, reward_live, pi, pd, type='live')
        # update population
        pop_live_change = growth_live * pop_live * (1 - ((pop_live + pop_dead + pop_nohair) / pop_max))

        # load data dead hairs
        [beta, att_max, infect_max, rho_max, eta_max], [theta, att, infect, rho, eta] = load_dead_data()
        # calculate risk and reward
        risk_dead = risk(att, att_max, infect, infect_max)
        reward_dead = reward(rho, rho_max, eta, eta_max, beta, theta)
        # calculate growth
        growth_dead = growth(risk_dead, reward_dead, pi, pd, type='dead')
        # update population
        pop_dead_change = growth_dead * pop_dead * (1 - ((pop_live + pop_dead + pop_nohair) / pop_max))

        # load data no hairs
        [beta, att_max, infect_max, rho_max, eta_max], [theta, att, infect, rho, eta] = load_nohair_data()
        # calculate risk and reward
        risk_nohair = risk(att, att_max, infect, infect_max)
        reward_nohair = reward(rho, rho_max, eta, eta_max, beta, theta)
        # calculate growth
        growth_nohair = growth(risk_nohair, reward_nohair, pi, pd, type='nohair')
        # update population
        pop_nohair_change = growth_nohair * pop_nohair * (1 - ((pop_live + pop_dead + pop_nohair) / pop_max))

        # update populations
        pop_live += pop_live_change
        pop_dead += pop_dead_change
        pop_nohair += pop_nohair_change

        # save history
        live_history.append(pop_live)
        dead_history.append(pop_dead)
        nohair_history.append(pop_nohair)

    # graph history
    plt.plot(live_history, label='live')
    plt.plot(dead_history, label='dead')
    plt.plot(nohair_history, label='nohair')
    plt.legend()
    plt.show()

    # import pdb; pdb.set_trace()

if __name__ == '__main__':
    main()