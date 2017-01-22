import numpy as np
from regions import *
import operator
from matplotlib import pyplot as plt


def terminal_view(pop_vals):
    """
    Nice way to present results in terminal console
    :param pop_vals: Simulation results.
    :return: nothing
    """
    #results = np.sum(pop_vals, axis=1)
    regions = get_regions_names()
    to_show = {}
    for ii in range(0, len(regions)):
        to_show[regions[ii]] = pop_vals[ii]
    sorted_to_show = sorted(to_show.items(), key=operator.itemgetter(1))
    for ii in range(0, len(regions)):
        print(sorted_to_show[ii])

def draw_f_evolution(vals):
    """
    Draw a plot showing the goal function of the best one in population as a function of seimualtion's step
    :param vals: Values of the goal function of the best one in population.
    :return: nothing
    """
    x = np.arange(0, len(vals))
    plt.plot(x, vals)
    plt.ylim(ymin=0)
    plt.xlabel('krok symulacji')
    plt.ylabel('funkcja przystosowania najlepszego osobnika')
    plt.show()