#######################################################################################################################
# Genetic Algorithm project made by R. Maselek & M. Seniut at Warsaw University of Technology.
# The aim of the project is to find optimal distribution of Polish Army forces to provide the best security for Poland.
# Simple model is used, the goal function consists of two parts: territorial defense part (area must be protected) and
# possible risk part (some countries are more likely to attack than others).
# Country is divided into 16 regions ('wojewodztwa'), troops are distributed into regions. Some regions are more important
# than others, e.g. 'mazowieckie' is important, because it contains the capital -- Warsaw.
# Armed forces are not distinguished, there are 24 brigades in total.
#######################################################################################################################


import functions as func
import numpy as np
from regions import *


def main(A, B, C, eps, sim_steps = 100):
    steps = int(sim_steps) # simulation steps
    p_c = 0.7 # cross over probability
    p_m = 10**-5 # mutation probability
    p_i = 0.1  # inversion probability

    pop = func.init(100, 'uniform')
    for ii in range(0, steps):
        # 1 SELECTION
        p_sel = func.selection(pop, A, B, C, eps)
        new_pop = np.zeros(shape=pop.shape)

        index = 0
        while index < len(pop):
            y = np.random.rand()
            x = np.random.randint(0, len(pop))
            if y < p_sel[x]:
                new_pop[index] = pop[x]
                index += 1
        pop = new_pop
        # 2 cross over
        probs_cross = np.random.uniform(size=(len(pop), len(pop)))
        to_cross = probs_cross < p_c
        indices = np.ndindex(*probs_cross.shape)
        for index in indices:
            if (index[0] > index[1]) and to_cross[index[0]][index[1]]:
                func.cross(pop[index[0]], pop[index[1]])
        # 3 mutation
        for chromosome in pop:
            func.mutate(chromosome, p_m)
        # 4 inversion
        probs_inv = np.random.uniform(len(pop))
        pop = np.where(probs_inv < p_i, func.inverse(pop), pop)
    return pop

if __name__ == "__main__":
    main(0.5, 1.0, 0.1, 10**-4, 100)