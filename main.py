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
from visualization import *

def main(A, B, C, eps, sim_steps = 100):
    """
        Genetic Algorithm simulation with a given number of steps and initial values: A, B, C, eps,
        required for the goal function calculation.
        :return: Last population after GA simulation is finished.
        """
    steps = int(sim_steps)  # simulation steps
    p_c = 0.15  # cross over probability # 0.15
    p_m = 0.0005  # mutation probability # 0.0005
    p_i = 0.0001  # inversion probability # 0.0001

    pop_size = 200  # 200
    ### INITIALIZATION ###
    pop = func.init(pop_size, 'multinomial')
    best_fs = [] # goal function of the best one in populationin each step
    fs = [] # summary goal function of the population in each step
    for ii in range(0, steps):
        ##### 1 SELECTION
        p_sel = func.selection(pop, A, B, C, eps)
        fs.append(np.sum(p_sel))
        best_fs.append(np.max(p_sel))
        new_pop = func.roulette_select(pop, p_sel, pop_size)

        ##### 2 CROSSOVER
        pop = func.crossover(new_pop, pop_size, p_c)

        ###### 3 MUTATION
        for cc in range(0, len(pop)):
            pop[cc] = func.mutate(pop[cc], p_m)

        ###### 4 INVERSION
        probs_inv = np.random.uniform(size=len(pop))
        for nn in range(0, len(probs_inv)):
            if probs_inv[nn] < p_i:
                pop[nn] = func.inverse(pop[nn])

    # after the GA steps >= simulation steps - i.e. the result of GA
    # the code below calculates results averaged over the whole population
    vals = np.zeros(16)
    get_av = False
    if get_av:
        for ii in range(0, 16):
            for em in pop:
                vals[ii] += em[ii]
        vals /= pop_size
        terminal_view(vals)

    return pop, vals, np.array(best_fs), fs


if __name__ == "__main__":
    sim_n = 1  # number of simulations to be done #20 is OK
    # PARAMETERS OF THE SIMULATION
    A = 0.35  # 0.35
    B = 0.5  # 0.5
    C = 0.1  # 0.1
    eps = 10 ** -2 # 10 ** -2
    sim_steps = 2000  # 800

    # SIMULATION LOOP
    # inside this loop many simulations are done
    best_f = []
    for ii in range(0, sim_n):
        end_pop, vals, f_evol, fs = main(A, B, C, eps, sim_steps)
        f_vals = func.selection(end_pop, A, B, C, eps)
        index = np.argmax(f_vals)
        best_f.append(end_pop[index])
        if int((ii+1) * 1000 / sim_n) % 100 == 0: # and int((ii) / sim_n * 100) > 0:
            print(int((ii+1) * 100/sim_n), '% done')

    av_result = np.zeros(16)
    for em in best_f:
        av_result += em
    av_result /= len(best_f)
    # print(av_result, sum(av_result))
    terminal_view(av_result) # prints out solution of the best one in population, averaged over all simulations

    # UNCOMMENT TO SEE GOAL FUNCTION OF THE POPULATION FROM THE LAST SIMULATION
    plt.plot(range(0, sim_steps), fs)
    plt.ylim(ymin=0)
    plt.ylabel("funkcja przystosowania populacji")
    plt.xlabel("krok symulacji")
    plt.show()

    # UNCOMMENT TO SEE GOAL FUNCTION OF THE BEST ONE IN POPULATION FROM THE LAST SIMULATION
    # draw_f_evolution(f_evol)

