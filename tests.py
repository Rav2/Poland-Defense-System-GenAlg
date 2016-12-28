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
    single_sim_test()

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
            vals.append(func.f(chrom[ii], eps, A, B, C, get_regions_list()[ii]))
        vals_total.append(sum(vals))#]sum(vals))
    terminal_view(vals)
    print(vals_total)
    plt.plot(range(0, 25), vals_total)
    plt.show()


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