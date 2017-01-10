from main import *
from visualization import *
from matplotlib import pyplot as plt

################################################################################
def test():
    """
    Main testing function to run all tests.
    :return: nothing
    """
    # goal_func_test()
    # single_sim_test()
    # selection_test()
    # selection_mod_test()
    crossover_test()
    # mutation_test()
    # init_test()
    # roulette_test()

################################################################################
def init_test():
    N = 4
    pop = func.init(N, 'multinomial')

    print("pop from init = ", pop)



def goal_func_test():
    """
    Tests goal function for a given set of parameters and perfectly uniform distributions.
    :return: nothing
    """
    A = 0.5
    B = 1.0
    C = 0.1
    eps = 10**-4
    pop = [x*np.ones(16) for x in range(0, 25)]

    vals_total = []
    for chrom in pop:
        vals = []
        for ii in range(0, len(chrom)):
            # print("chrom[ii]= ", chrom[ii])
            # print ("regions = ", get_regions_list()[ii])
            vals.append(func.f(chrom[ii], eps, A, B, C, get_regions_list()[ii]))
            # print("vals = ", vals[ii])
        vals_total.append(sum(vals))#]sum(vals))
        # print("sum_vals = ", sum(vals))
    terminal_view(vals)
    print(vals_total)
    plt.plot(range(0, 25), vals_total)
    plt.show()

def selection_test():
    steps = 1 # simulation steps
    A = 0.5
    B = 1.0
    C = 0.1
    eps = 10**-4

    pop = func.init(4, 'multinomial')
    # print ("pop = ", pop)
    for ii in range(0, steps):
        # 1 SELECTION
        p_sel = func.selection(pop, A, B, C, eps)
        new_pop = np.zeros(shape=pop.shape)

        # print("p_sel ", p_sel)

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

        print("end = ", pop)

def selection_mod_test():
    steps = 1  # simulation steps
    A = 0.5
    B = 1.0
    C = 0.1
    eps = 10 ** -4

    pop_size = 4
    pop = func.init(pop_size, 'multinomial')



    for ii in range(0, steps):
        # 1 SELECTION
        p_sel = func.selection_mod(pop, A, B, C, eps)
        new_pop = np.zeros(shape=pop.shape)

        # sum of all chromosome fitnesses in population
        Sum = p_sel.sum()

        print ("Sum = ", Sum)
        # print ("p_sel = ", p_sel)
        prob_sum = 0.
        # array of probabilities for all the chromosomes in the population on the roullette
        prob_array = np.zeros(pop_size)
        for i in range(pop_size):
            probability = prob_sum + p_sel[i]
            prob_array[i] = probability
            prob_sum += probability

        print ("prob sum = ", prob_sum)

        # print ("prob_array = ", prob_array)

        # print ("pop before selection = ", pop)

        #index in new population
        index = 0
        while (index < len(pop)):
            # random choice on the roullette
            # choice = np.random.uniform(prob_array[0], prob_array[-1])
            choice = np.random.uniform(0, prob_array[-1])
            print ("choice = ", choice)
            for i in range(pop_size):
                if(prob_array[i] > choice):
                    print ("prob_array[i] = ", prob_array[i], "i = ", i)
                    # print ("choice ", choice)
                    print ("warunek spelniony!")
                    new_pop[index] = pop[i]
                    break
            index += 1

        pop = new_pop
        print("end = ", pop)
    return pop

def crossover_test():
    p_c = 0.7
    # pop = main(0.5, 1.0, 0.1, 10**-4, 1)
    # pop = selection_mod_test()
    distr = np.zeros(shape=(2, 6))
    distr[0] = [2,4,6,3,8,1]
    distr[1] = [1,7,5,6,2,3]

    # pop = distr
    pop = roulette_test()
    print("pop to cross = ", pop)
    probs_cross = np.random.uniform(size=(len(pop), len(pop)))
    to_cross = probs_cross < p_c
    # return index numbers of all elements in an array
    indices = np.ndindex(*probs_cross.shape)
    for index in indices:
        if (index[0] > index[1]) and to_cross[index[0]][index[1]]:
    # for i in range(0,2,1):
            print("i = ", index[0], index[1])
            print("crossing: ")
        # print ('index[0] = ', index[0])
        # print ('index[1] = ', index[1])
        # func.cross(pop[i], pop[i+2])
            func.cross(pop[index[0]], pop[index[1]])

    print ("pop after = ", pop)
    return pop

def mutation_test():
    p_m = 3*10**-1
    pop = crossover_test()

    for chromosome in pop:
        func.mutate(chromosome, p_m)

    print( "after mutation = ", pop)


def roulette_test():
    A = 0.5
    B = 1.0
    C = 0.1
    eps = 10 ** -4
    pop = func.init(4 ,'multinomial')
    p_sel = func.selection(pop, A, B, C, eps)
    print ("before roulette: ", pop)
    new_pop = func.roulette_select(pop, p_sel, 4)

    print ("after roulette: ", new_pop)
    return new_pop



def single_sim_test():
    pop = main(0.5, 1.0, 0.1, 10**-4, 100)
    # print ("population end = ", pop)
    # print ("population sum = ", pop.sum(axis=1))
    vals = np.zeros(16)
    for ii in range(0, 16):
        for em in pop:
            # print ("ii = ", ii, "em = ", em[ii])
            vals[ii] += em[ii]
    vals /= 100
    terminal_view(vals)
    #TODO:Wyniki sa zle, zobaczyc co jest nie tak? !!!NIE UZYWAC PYTHON 2.X.X!! TO JEST PRZESTARZALE!!! Zalecane 3.5.1




test()