# File to model and graph a system of differential equations
# modeling population change in birds who steal hair from live animals.
from math import cos
import numpy as np
import matplotlib.pyplot as plt


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


def main():
    pass


if __name__ == '__main__':
    main()