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
from visualization import *
from regions import *

def mainR(A, B, C, eps, sim_steps = 100):
    steps = int(sim_steps) # simulation steps
    p_c = 0.7 # cross over probability
    p_m = 10**-5 # mutation probability
    p_i = 0.1  # inversion probability

    pop_size = 100
    pop = func.init(pop_size, 'uniform')



    for ii in range(0, steps):
        # 1 SELECTION
        p_sel = func.selection_mod(pop, A, B, C, eps)
        new_pop = np.zeros(shape=pop.shape)

        index = 0
        while index < len(pop):
            y = np.random.rand()
            x = np.random.randint(0, len(pop))
            # print("y = ", y)
            # print("x = ", x)

            if y < p_sel[x]:
                new_pop[index] = pop[x]
                index += 1

        pop = new_pop
        # print ("population to cross = ", pop)
        # 2 CROSS OVER
        probs_cross = np.random.uniform(size=(len(pop), len(pop)))
        to_cross = probs_cross < p_c
        indices = np.ndindex(*probs_cross.shape)
        for index in indices:
            if (index[0] > index[1]) and to_cross[index[0]][index[1]]:
                func.cross(pop[index[0]], pop[index[1]])
        # 3 MUTATION
        for chromosome in pop:
            func.mutate(chromosome, p_m)
        # 4 INVERSION
        probs_inv = np.random.uniform(len(pop))
        pop = np.where(probs_inv < p_i, func.inverse(pop), pop)
        if int(ii*1000/steps) % 10 == 0 and int(ii/steps*100)>0:
            print(int(ii/steps*100), '% done')
    return pop

def main(A, B, C, eps, sim_steps = 100):
    steps = int(sim_steps) # simulation steps
    p_c = 0.7 # cross over probability
    p_m = 10**-5 # mutation probability
    p_i = 0.1  # inversion probability

    pop_size = 10
    pop = func.init(pop_size, 'uniform')



    for ii in range(0, steps):
        # 1 SELECTION
        p_sel = func.selection_mod(pop, A, B, C, eps)
        new_pop = np.zeros(shape=pop.shape)

        # sum of all chromosome fitnesses in population
        Sum = p_sel.sum()

        # print ("p_sel = ", p_sel)
        prob_sum = 0.
        # array of probabilities for all the chromosomes in the population on the roullette
        prob_array = np.zeros(pop_size)
        for i in range(pop_size):
            probability = prob_sum + p_sel[i]
            prob_array[i] = probability
            prob_sum += probability

        # print ("prob_array = ", prob_array)

        # print ("pop before selection = ", pop)

        #index in new population
        index = 0
        while (index < len(pop)):
            # random choice on the roullette
            choice = np.random.uniform(prob_array[0], prob_array[-1])
            # print ("choice = ", choice)
            for i in range(pop_size):
                if(prob_array[i] < choice):
                    new_pop[index] = pop[i]
                    break
            index += 1


            # index in new population
        # index = 0
        # print ("p_sel = ", p_sel)
        # while index < len(pop):
        #     for j in range(2):
        #         y = np.random.rand()
        #         x = np.random.randint(0, len(pop))
        #     # looping through old population
        #     # print ("Y = ", y)
        #         for i in range(len(pop)):
        #         # print ("p_sel[i] = ", p_sel[i])
        #         #     if(( y < p_sel[i]) and (i!=0) and (y>p_sel[i-1])):
        #             if(( y < prob_array[i]) and (i!=0) and (y>prob_array[i-1])):
        #                 new_pop[index] = pop[i]
        #             else:
        #                 if(y<prob_array[i]):
        #
        #                 # if(y<p_sel[i]):
        #                     new_pop[index] = pop[i]
        #     index +=1

                        # if y < p_sel[x]:
                # new_pop[index] = pop[x]
                # index += 1

        pop = new_pop
        # print ("population to cross = ", pop)
        # 2 CROSS OVER
        probs_cross = np.random.uniform(size=(len(pop), len(pop)))
        to_cross = probs_cross < p_c
        indices = np.ndindex(*probs_cross.shape)
        for index in indices:
            if (index[0] > index[1]) and to_cross[index[0]][index[1]]:
                func.cross(pop[index[0]], pop[index[1]])
        # 3 MUTATION
        for chromosome in pop:
            func.mutate(chromosome, p_m)
        # 4 INVERSION
        probs_inv = np.random.uniform(len(pop))
        pop = np.where(probs_inv < p_i, func.inverse(pop), pop)
        if int(ii*1000/steps) % 10 == 0 and int(ii/steps*100)>0:
            print(int(ii/steps*100), '% done')
    return pop

if __name__ == "__main__":
    main(0.5, 1.0, 0.1, 10**-4, 100)


# main()