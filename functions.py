import numpy as np
from regions import *
from math import log, exp

brigade_border_control = 30 # km
brigade_area_control = 150 # km^2

# returns population, N members
def init (N, option):
    if option == 'binomial':
        return np.random.binomial(24, 0.5, size=(N, 16)) # p=0.5 probability of success, 24 - upper bound
    else:
        return np.random.randint(0, 24, size=(N, 16))

# do przemyslenia obie funkcje
# n - liczba brygad umieszczonych
def f_teritorial(n, eps, A, region):
    return A * region['weight'] * log(eps + n/brigade_area_control*region['area'])

def f_danger(n, B, region):
    eff_de = eff_cz = eff_sk = eff_ua = eff_by = eff_lt = eff_ru = 1.0
    # region [country] - length of the border
    if region['DE'] > 0.0:
        eff_de = n * threat_coef['DE'] * (region['DE'] / brigade_border_control)
    if region['CZ'] > 0.0:
        eff_cz = n * threat_coef['CZ'] * (region['CZ'] ) / brigade_border_control
    if region['SK'] > 0.0:
        eff_sk = n * threat_coef['SK'] * (region['SK'] ) / brigade_border_control
    if region['UA'] > 0.0:
        eff_ua = n * threat_coef['UA'] * (region['UA'] ) / brigade_border_control
    if region['BY'] > 0.0:
        eff_by = n * threat_coef['BY']* (region['BY'] ) / brigade_border_control
    if region['LT'] > 0.0:
        eff_lt = n * threat_coef['LT'] * (region['LT'] ) / brigade_border_control
    if region['RU'] > 0.0:
        eff_ru = n * threat_coef['RU'] * (region['LT'] ) / brigade_border_control

    eff = eff_de + eff_cz + eff_sk + eff_ua + eff_by + eff_lt + eff_ru
    # print "region ", region['name']
    # print "eff_de= ", eff_de
    # print "eff_cz= ", eff_cz
    # print "eff_sk= ", eff_sk
    # print "eff_ua= ", eff_ua
    # print "eff_by= ", eff_by
    # print "eff_lt= ", eff_lt
    # print "eff_ru= ", eff_ru
    print "eff = ", eff
    # before: exp(eff)-1, new: log(eff) + const - TODO: find the proper additive const to make func>0
    #powinien byc chyba exp, ale z jakims wspolczynnikiem
    return B * region['weight']*exp(0.01*eff) +10


def f(n, eps, A, B, region):
    #TODO: check why zachodnio-pomorskie is listed twice!
    print(region['name'])
    return f_teritorial(n, eps, A, region) + f_danger(n, B, region)


# calculates goal function for a given chromosome
def f_chrom(chrom, A, B, eps):
    f_vec = np.vectorize(f)
    print(len(chrom), len(get_regions_list()))
    return f_vec(chrom, eps, A, B, get_regions_list())

# P - prawdopodobienstwo krzyzowania. Losujemy punkt przeciecia i kierunek
def cross(chrom1, chrom2, P):
    0


def mutate(chrom, P):
    randoms = np.random.uniform(size=(len(chrom)))
    # return np.where(randoms < P, np.random.randint(0, 24), chrom)

