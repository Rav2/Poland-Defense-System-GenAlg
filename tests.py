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
    selection_test()

################################################################################
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

    pop = func.init(4, 'uniform')
    print ("pop = ", pop)
    for ii in range(0, steps):
        # 1 SELECTION
        p_sel = func.selection(pop, A, B, C, eps)
        new_pop = np.zeros(shape=pop.shape)

        print("p_sel ", p_sel)

        index = 0
        while index < len(pop):
            y = np.random.rand()
            x = np.random.randint(0, len(pop))
            print("y = ", y)
            print("x = ", x)

            if y < p_sel[x]:
                new_pop[index] = pop[x]
                index += 1
        pop = new_pop

        print("end = ", pop)

def single_sim_test():
    pop = main(0.5, 1.0, 0.1, 10**-4, 1000)
    vals = np.zeros(16)
    for ii in range(0, 16):
        for em in pop:
            vals[ii] += em[ii]
    vals /= 100
    terminal_view(vals)
    #TODO:Wyniki sa zle, zobaczyc co jest nie tak? !!!NIE UZYWAC PYTHON 2.X.X!! TO JEST PRZESTARZALE!!! Zalecane 3.5.1




test()