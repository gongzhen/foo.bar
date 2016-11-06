#!/usr/bin/env python

'''
Author: John D. Anderson (TigerJ)
Program: zombit_infection.py -case1 | -case1
Origin: Google "foo.bar" project - Problem 2.1
Problem Description:

    Zombit infection
    ================

    Dr. Boolean continues to perform diabolical studies on your fellow rabbit
    kin, and not all of it is taking place in the lab. Reports say the mad
    doctor has his eye on infecting a rabbit in a local village with a virus
    that transforms rabbits into zombits (zombie-rabbits)!

    Professor Boolean is confident in the virus's ability to spread,
    and he will only infect a single rabbit. Unfortunately, you and your fellow
    resistance agents have no idea which rabbit will be targeted. You've been
    asked to predict how the infection would spread if uncontained, so you
    decide to create a simulation experiment. In this simulation, the rabbit
    that Dr. Boolean will initially infect will be called "Patient Z".

    So far, the lab experts have discovered that all rabbits contain a property
    they call "Resistance", which is capable of fighting against the infection.
    The virus has a particular "Strength" which Dr. Boolean needs to make at
    least as large as the rabbits' Resistance for it to infect them.

    You will be provided with the following information:
    population = A 2D non-empty array of positive integers of the form
                 population[y][x], that is, row then column.
                 (The dimensions of the array are not necessarily equal.)
                 Each cell contains one rabbit, and the value of the cell
                 represents that rabbit's Resistance.
    x = The X-Coordinate (column) of "Patient Z" in the population array.
    y = The Y-Coordinate (row) of "Patient Z" in the population array.
    strength = A constant integer value representing the Strength of the virus.

    Here are the rules of the simulation: First, the virus will attempt to
    infect Patient Z. Patient Z will only be infected if the infection's
    Strength equals or exceeds Patient Z's Resistance. From then on, any
    infected rabbits will attempt to infect any uninfected neighbors
    (cells that are directly - not diagonally - adjacent in the array).
    They will succeed in infecting any neighbors with a Resistance lower than
    or equal to the infection's Strength. This will continue until no further
    infections are possible (i.e., every uninfected rabbit adjacent to an
    infected rabbit has a Resistance greater than the infection's Strength.)

    You will write a function answer(population, x, y, strength), which outputs
    a copy of the input array representing the state of the population at the
    end of the simulation, in which any infected cells value has been replaced
    with -1. The Strength and Resistance values will be between 0 and 10000.
    The population grid will be at least 1x1 and no larger than 25x25. The x
    and y values will be valid indices in the population arrays, with numbering
    beginning from 0.

    Languages
    =========

    To provide a Python solution, edit solution.py
    To provide a Java solution, edit solution.java

    Test cases
    ==========

    Inputs:
        (int) population = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
        (int) x = 0
        (int) y = 0
        (int) strength = 2
    Output:
        (int) [[-1, -1, 3], [-1, 3, 4], [3, 2, 1]]

    Inputs:
        (int) population = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10],
                            [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
        (int) x = 2
        (int) y = 1
        (int) strength = 5
    Output:
        (int) [[6, 7, -1, 7, 6], [6, -1, -1, -1, 7], [-1, -1, -1, -1, 10],
               [8, -1, -1, -1, 9], [8, 7, -1, 9, 9]]

    Use verify [file] to test your solution and see how it does.
    When you are finished editing your code, use submit [file] to submit
    your answer. If your solution passes the test cases, it will be removed
    from your home folder.
'''

# libs
import sys


# func
def answer(population, x, y, strength):

    # calculate rows and columns
    row = len(population)
    col = len(population[0])

    # infection function
    def infection(population, x, y, strength):

        # neighbor coords
        N = y - 1
        S = y + 1
        E = x + 1
        W = x - 1

        # check North neighbor
        if N >= 0:
            neighbor = population[N][x]
            if neighbor <= strength and neighbor != -1:
                population[N][x] = -1
                # call recursive function
                infection(population, x, N, strength)

        # check South neighbor
        if S <= row-1:
            neighbor = population[S][x]
            if neighbor <= strength and neighbor != -1:
                population[S][x] = -1
                # call recursive function
                infection(population, x, S, strength)

        # check East neighbor
        if E <= col-1:
            neighbor = population[y][E]
            if neighbor <= strength and neighbor != -1:
                population[y][E] = -1
                # call recursive function
                infection(population, E, y, strength)

        # check West neighbor
        if W >= 0:
            neighbor = population[y][W]
            if neighbor <= strength and neighbor != -1:
                population[y][W] = -1
                # call recursive function
                infection(population, W, y, strength)

        # else return
        return

    # initial infection attempt
    z = population[y][x]
    if z <= strength:
        population[y][x] = -1
    else:
        return population

    # start recursion
    infection(population, x, y, strength)

    # return final population
    return population


# executable
if __name__ == '__main__':

    # ussage message
    usage = '\nUsage: zombit_infection -case1 | -case2\n'

    # CLA check
    if len(sys.argv) == 2:

        if sys.argv[1] == '-case1':
            population = [[1, 2, 3], [2, 3, 4], [3, 2, 1]]
            x = 0
            y = 0
            strength = 2

        elif sys.argv[1] == '-case2':
            population = [[6, 7, 2, 7, 6], [6, 3, 1, 4, 7], [0, 2, 4, 1, 10],
                          [8, 1, 1, 4, 9], [8, 7, 4, 9, 9]]
            x = 2
            y = 1
            strength = 5

        # wrong arguments passed
        else:
            sys.exit(usage)

        # correct agurments passed
        print answer(population, x, y, strength)
        sys.exit()

    # no arguments passed
    sys.exit(usage)
