import numpy as np
from regions import *
from math import log, exp

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
    else:
        distr = np.ones(shape=(N, 16))
        for indiv in distr:
            if np.random.rand() > 0.5: # odd/even number are 2, the rest is 1
                indiv[::2] += 1
            else:
                indiv[1::2] += 1
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
    return probabilities/np.sum(probabilities)




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
    first_time = True
    for em in population:
        # print ("em = ", em)
        prob = f_chrom(em, A, B, C, eps)
        # print ("probability = ", prob)
        # for checking the boundaries in roulette
        # if (first_time):
        #     probabilities.append(prob)
        #     first_time = False
        # else:
            # print ("prob = ", prob)
            # print ("probabilities[-1] = ", probabilities[-1])
            # probabilities.append(prob+probabilities[-1])
        probabilities.append(prob)
        # print ("probabilities = ", probabilities)
    probabilities = np.array(probabilities)
    return probabilities

def cross(chrom1, chrom2):
    """
    Perform cross over on a given pair of chromosoms. Algorithm:
    1) find random (uniformly ditr) cross over point and direction (left or right)
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
        temp = np.copy(chrom1[:point])
        chrom1[:point], chrom2[:point] = chrom2[:point], temp
        if change != 0:
            cross_fix(chrom1[:point], chrom2[:point], int(change))
    else:
        change = np.sum(chrom1[point:]) - np.sum(chrom2[point:])
        temp = np.copy(chrom1[point:])
        chrom1[point:], chrom2[point:] = chrom2[point:], temp
        if change != 0:
            cross_fix(chrom1[point:], chrom2[point:], int(change))


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
    new_integers = np.random.randint(0, 25, size=(len(chrom)))
    chrom = np.where(randoms <= P, new_integers, chrom)
    while np.sum(chrom) > 24:
       chrom[np.argmax(chrom)] -= 1
    while np.sum(chrom) < 24:
       chrom[np.argmin(chrom)] += 1
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


