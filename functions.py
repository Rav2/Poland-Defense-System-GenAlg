import numpy as np


#returns population, N members
def init (N, option):
    if option == 'gauss':
        return [[]]
    elif option == 'poisson':
        return [[]]
    else:
        return [[]]


#calculates goal function for a given chromosome
def f(chrom):
    return 0.0

#P - prawdopodobienstwo krzyzowania. Losujemy punkt przeciecia i kierunek
def cross(chrom1, chrom2, P):
    0


def mutate(chrom, P):
    0