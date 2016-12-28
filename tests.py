from main import *
from visualization import *
from matplotlib import pyplot as plt

################################################################################
def test():
    """
    Main testing function to run all tests.
    :return: nothing
    """
    goal_func_test()


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

test()