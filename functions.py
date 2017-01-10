import numpy as np
from regions import *
from math import log, exp
import itertools as it
import random

brigade_border_control = 30 # km
brigade_area_control = 150 # km^2

# returns population, N members
def init (N, option):
    """
    Initialize the population.
    :param N: Number of population members.
    :param option: Type of the distribution used to fill chromosomes.
    :return: 1D array containing N chromosomes.
    """
    if option == 'binomial':
        distr = np.zeros(shape=(N, 16))
        for indiv in distr:
            up_limit = 24
            for ii in range(0, 16):
                indiv[ii] = np.random.binomial(up_limit, 0.5)
                up_limit -= indiv[ii]

    # probably more suitable in this case
    elif option == 'multinomial':
        distr = np.random.multinomial(24, [1 / 16.] * 16, size=N)

    elif option == 'own':
        distr = np.zeros(shape=(N, 16))
        for indiv in distr:
            up_limit = 24

            for ii in range(0, 16):
                # works quite well for this concrete problem
                indiv[ii] = np.random.randint(0, up_limit/3)
                up_limit -= indiv[ii]
    else:
        distr = np.ones(shape=(N, 16))
        for indiv in distr:
            if np.random.rand() > 0.5: # odd/even number are 2, the rest is 1
                indiv[::2] += 1
            else:
                indiv[1::2] += 1

    # print ("distribution = ", distr)
    return distr



# do przemyslenia obie funkcje
# n - liczba brygad umieszczonych


def f_teritorial(n, eps, A, region):
    """
    Calculates the territorial defense coeff of the goal function
    :param n: Number of brigades in the region.
    :param eps: Epsilon parameter.
    :param A: Multiplication const.
    :param region: Region object.
    :return: Value of the function for a given region and n.
    """
    return A * region['weight'] * (log(eps + n * brigade_area_control / region['area'])-log(eps))# + 8.64


def f_danger(n, B, C, region):
    """
    Calculates the risk of attack coeff for the goal function.
    :param n: Number of brigades in the region.
    :param B: Multiplication const.
    :param C: Exponential constant.
    :param region:  Region object.
    :return: Value of the function for a given region and n.
    """
    eff_de = eff_cz = eff_sk = eff_ua = eff_by = eff_lt = eff_ru = 0.0
    # region [country] - length of the border
    if region['DE'] > 0.0:
        eff_de = n * threat_coef['DE']**2 / region['DE'] * brigade_border_control
    if region['CZ'] > 0.0:
        eff_cz = n * threat_coef['CZ']**2 / region['CZ'] * brigade_border_control
    if region['SK'] > 0.0:
        eff_sk = n * threat_coef['SK']**2 / region['SK'] * brigade_border_control
    if region['UA'] > 0.0:
        eff_ua = n * threat_coef['UA']**2 / region['UA'] * brigade_border_control
    if region['BY'] > 0.0:
        eff_by = n * threat_coef['BY']**2 / region['BY'] * brigade_border_control
    if region['LT'] > 0.0:
        eff_lt = n * threat_coef['LT']**2 / region['LT'] * brigade_border_control
    if region['RU'] > 0.0:
        eff_ru = n * threat_coef['RU']**2 / region['RU'] * brigade_border_control

    eff = eff_de + eff_cz + eff_sk + eff_ua + eff_by + eff_lt + eff_ru
    return B * region['weight']*(exp(C*eff)-1)


def f(n, eps, A, B, C, region):
    """
    Calculates the goal function.
    :param n: Number of brigades in the region.
    :param eps: Epsilon parameter.
    :param A: Multiplication const for teritorial part.
    :param B: Multiplication const for risk part.
    :param C: Exponential constantfor risk part.
    :param region:  Region object.
    :return: Value of the function for a given region and n.
    """
    return f_teritorial(n, eps, A, region) + f_danger(n, B, C, region)



def f_chrom(chrom, A, B, C, eps):
    """
    Calculates goal function for a given chromosome
    :param chrom:
    :param A: Multiplication const for teritorial part.
    :param B: Multiplication const for risk part.
    :param C: Exponential constant for risk part.
    :param eps: Epsilon parameter.
    :return: Value of the function for a given chromosome.
    """
    f_vec = np.vectorize(f)
    return np.sum(f_vec(chrom, eps, A, B, C, get_regions_list()))


def selection(population, A, B, C, eps):
    """
    Calculates probabilities for the roulette selection method.
    :param population:
    :param A: Teritorial constant.
    :param B: Danger constant.
    :param eps: Epsilon for teritorial part.
    :return: 1D array of probabilities, a value for every chromosome.
    """
    probabilities = []
    for em in population:
        # print ("em = ", em)
        prob = f_chrom(em, A, B, C, eps)
        # print ("probability = ", prob)
        probabilities.append(prob)
        # print ("probabilities = ", probabilities)
    probabilities = np.array(probabilities)
    # print ("interesujace = ", probabilities)
    return probabilities

def roulette_select(population, fitnesses, N):

    total_fitness = float(sum(fitnesses))
    scaled_fitness = [f/total_fitness for f in fitnesses]

    # Generate probability intervals for each individual - sums from the beginning
    # of array of probabilities
    probabilities = [sum(scaled_fitness[:i+1]) for i in range(len(scaled_fitness))]
    # print ("probabilitiess = ", probabilities)

    # Draw new population
    new_population = np.zeros(shape=(N, 16))
    index =0
    for n in range(N):
        choice = np.random.rand()
        # print("choice = ", choice)
        for (i, individual) in enumerate(population):
            if choice <= probabilities[i]:
                new_population[index]= individual
                index += 1
                break
    return new_population


def selection_mod(population, A, B, C, eps):
    """
    Calculates probabilities for the roulette selection method.
    :param population:
    :param A: Teritorial constant.
    :param B: Danger constant.
    :param eps: Epsilon for teritorial part.
    :return: 1D array of probabilities, a value for every chromosome.
    """
    probabilities = []
    for em in population:
        # print ("em = ", em)
        prob = f_chrom(em, A, B, C, eps)
        # print ("prob z celu = ", prob)

        probabilities.append(prob)
        # print ("probabilities = ", probabilities)
    probabilities = np.array(probabilities)
    return probabilities/np.sum(probabilities)

def cross(chrom1, chrom2):
    """
    Perform cross over on a given pair of chromosoms. Algorithm:
    1) find random (uniformly distr) cross over point and direction (left or right)
    2) swap chromosom parts
    3) fix the swapped part in a way that the sum before and after cross over is the same using  cross_fix function
    :param chrom1: chromosom 1
    :param chrom2: chromosom 2
    :return: nothing (arguments are altered)
    """
    point =  np.random.randint(1, len(chrom1))
    direction = np.random.rand()
    # print('cross point = ', point, 'direction=', direction)
    if direction < 0.5: # left
        change = np.sum(chrom1[:point]) - np.sum(chrom2[:point])
        # print ("change = ", change)
        temp = np.copy(chrom1[:point])
        # print ("chrom1[:point] before ", chrom1[:point])
        # print ("chrom2[:point] before", chrom2[:point])
        # print ("temp = ", temp)

        chrom1[:point], chrom2[:point] = chrom2[:point], temp
        # print ("chrom1[:point] after ", chrom1[:point])
        # print ("chrom2[:point] after", chrom2[:point])
        if change != 0:
            cross_fix(chrom1[:point], chrom2[:point], int(change))
    else:
        change = np.sum(chrom1[point:]) - np.sum(chrom2[point:])
        temp = np.copy(chrom1[point:])
        chrom1[point:], chrom2[point:] = chrom2[point:], temp
        if change != 0:
            cross_fix(chrom1[point:], chrom2[point:], int(change))

def crossover(selected_pop, N, p_c):

    new_pop = np.zeros(shape=(N,16))
    # generating probabilities for N childs
    probabilities = [np.random.rand() for i in range(N)]
    index = 0
    for p in probabilities:
        if (p <= p_c):
            pairs = random.sample(selected_pop.tolist(), 2)
            point = np.random.randint(1, len(pairs[0]))
            direction = np.random.rand()
            if (direction < 0.5):
                change = np.sum(pairs[0][:point]) + np.sum(pairs[1][point:])
                new_pop[index] = pairs[0][:point]+pairs[1][point:]
                # print("child = ", new_pop[index], " ", sum(new_pop[index]))

                if change != 24:
                    # print ("repair")
                    fix_crossover(new_pop[index])

                index += 1


            else:
                change = np.sum(pairs[0][point:]) + np.sum(pairs[1][:point])
                new_pop[index] = pairs[1][:point] + pairs[0][point:]

                if change != 24:
                    fix_crossover(new_pop[index])

                index += 1


        # else leave random parent individual
        else:
            new_pop[index] = selected_pop[np.random.randint(0,N)]
            index += 1

    # returns population after the crossover process
    return new_pop




def fix_crossover(individual):
    change = int(24 - sum(individual))
    # print("sum = ", change)

    # in case of an excess
    if (change > 0):
        for ii in range(0, change):

            individual[np.random.randint(0, len(individual))] += 1
    else:
        for ii in range(0, -change):
            rand_index = np.random.randint(0, len(individual))
            if(individual[rand_index] >0):
                individual[rand_index] -= 1

    # print("after repair = ", sum(individual))

def pmx_cross(chrom1, chrom2):
    """
    Perform PMX - partially mapped cross over on a given pair of chromosomes. Algorithm:
    1) find random 2 cross over points
    2) swap chromosome parts
    3) exchange the rest genes in chromosem according to the scheme from previous exchange crossover
    :param chrom1: chromosom 1
    :param chrom2: chromosom 2
    :return: nothing (arguments are altered)
    """

    # assuming that chromosem have the same length
    cpoint1 =  np.random.randint(1, len(chrom1))
    cpoint2 =np.random.randint(1, len(chrom1)-1)

    if (cpoint1 <= cpoint2):
        cpoint2 += 1
    else:
        cpoint1, cpoint2 = cpoint2, cpoint1

    # print('cross point 1 = ', cpoint1, 'cross point 2 = ', cpoint2)

    values_change1 = np.zeros(len(cpoint2-cpoint1))
    values_change2 = np.zeros(len(cpoint2-cpoint1))
    for i in range(cpoint1, cpoint2):
        # temp1 = chrom1[i]
        # temp2 = chrom2[i]
        values_change1.append(chrom1[i])
        values_change2.append(chrom2[i])
        chrom1[i], chrom2[i] = chrom2[i], chrom1[i]

    for j in it.chain(range(0, cpoint1), range(cpoint2, len(chrom1))):
        if chrom1[i] in values_change1:
            chrom1[i] = values_change2[values_change1.index(chrom1[i])]
        if chrom1[i] in values_change2:
            chrom1[i] = values_change1[values_change2.index(chrom1[i])]

    #not finished because not suitable here :(((((



def change_elements(chromosome, index, values_change1, values_change2):
    chromosome[index] = values_change2[values_change1.index(chromosome[index])]

def cross_fix(part1, part2, val):
    """
    Fix swapped parts of chromosoms after cross over by flattening the genome (decrease maximum and increase minimum as
    long as the sum of the whole chromosome will be 24 again)
    :param part1:
    :param part2:
    :param val:
    :return:
    """
    if val > 0: # subtract from part2, add to part1
        for ii in range(0, val):
            part2[np.argmax(part2)] -= 1
            part1[np.argmin(part1)] += 1
    else:    # subtract from part1, add to part2
        for ii in range(0, -val):
            part2[np.argmin(part2)] += 1
            part1[np.argmax(part1)] -= 1


def mutate(chrom, P):
    """
    Mutation operator. Performs mutation over all genes in a chromosome and fixes it to sum up to 24.
    :param chrom: Given chromosome
    :param P: Probability of mutation.
    :return: Chromosome after mutation.
    """
    randoms = np.random.uniform(size=(len(chrom)))
    # print ("randoms = ", randoms)
    new_integers = np.random.randint(0, 25, size=(len(chrom)))
    # print ("new integers = ", new_integers)
    # print ("chrom = ", chrom)

    chrom = np.where(randoms <= P, new_integers, chrom)
    # print ("chrom z mutate = ", chrom)

    while np.sum(chrom) > 24:
       chrom[np.argmax(chrom)] -= 1
    while np.sum(chrom) < 24:
       chrom[np.argmin(chrom)] += 1
    # print ("chrom after mutate = ", chrom)

    return chrom


def inverse(chrom):
    """
    Operator of inversion. It performs linear inversion with P=0.750, left side with P=0.125 and right side with P=0.125
    :param chrom: Given chromosome.
    :return: Inversed Chromosome.
    """
    inverse_type = np.random.rand()
    if inverse_type < 0.750:
        chrom = chrom[::-1]
    elif inverse_type < 0.875: # side inversion to the left
        point = np.random.randint(1, len(chrom))
        chrom[: point] = chrom[: point][::-1]
    else:  # side inversion to the right
        point = np.random.randint(1, len(chrom))
        chrom[point :] = chrom[point :][::-1]
    return chrom


