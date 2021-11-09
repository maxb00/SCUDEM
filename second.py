# File to model and graph a system of differential equations
# modeling population change in birds who steal hair from live animals.
from math import cos
from math import pi as p
import numpy as np
import matplotlib.pyplot as plt


# globals true for every population
pi = 0.3 # proportion of normal pop increase
pd = 0.11 # proportion of normal pop decrease


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


# Data functions
def load_live_data():
    '''Holds data for birds who steal live hairs'''
    # maximums
    beta = 0.12
    att_max = 0.5
    infect_max = 0.5
    rho_max = 0.5 # predator constant
    eta_max = 0.5 # parasite constant

    # actives (max be moved)
    theta = 0 # range 0 - pi, max at pi/2
    att = 0.2
    infect = 0.1
    rho = 0.07
    eta = 0.23

    return [beta, att_max, infect_max, rho_max, eta_max], [theta, att, infect, rho, eta]


def load_dead_data():
    '''Holds data for birds who steal live hairs'''
    # maximums
    beta = 0.12
    att_max = 0.5
    infect_max = 0.5
    rho_max = 0.5 # predator constant
    eta_max = 0.5 # parasite constant

    # actives (max be moved)
    theta = 0 # range 0 - pi, max at pi/2
    att = 0.1
    infect = 0.4
    rho = 0.07
    eta = 0.16

    return [beta, att_max, infect_max, rho_max, eta_max], [theta, att, infect, rho, eta]


def load_nohair_data():
    '''Holds data for birds who steal live hairs'''
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

    # run years, saving history

    # graph history

    print('This is a placeholder.')


if __name__ == '__main__':
    main()