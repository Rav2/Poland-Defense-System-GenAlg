import numpy as np
from regions import *
import operator
from matplotlib import pyplot as plt


def terminal_view(pop_vals):
    #results = np.sum(pop_vals, axis=1)
    regions = get_regions_names()
    to_show = {}
    for ii in range(0, len(regions)):
        to_show[regions[ii]] = pop_vals[ii]
    sorted_to_show = sorted(to_show.items(), key=operator.itemgetter(1))
    for ii in range(0, len(regions)):
        print(sorted_to_show[ii])

def draw_f_evolution(vals):
    x = np.arange(0, len(vals))
    plt.plot(x, vals)
    plt.ylim(ymin=0)
    plt.show()