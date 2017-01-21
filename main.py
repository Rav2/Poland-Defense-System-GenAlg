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
    steps = int(sim_steps) # simulation steps
    p_c = 0.7 # cross over probability
    p_m = 10**-1 # mutation probability
    p_i = 0.1  # inversion probability

    pop_size = 100
    pop = func.init(pop_size, 'multinomial')
    best_fs = []
    for ii in range(0, steps):
        # 1 SELECTION
        p_sel = func.selection(pop, A, B, C, eps)
        #print(p_sel)
        best_fs.append(np.max(p_sel))
        new_pop = func.roulette_select(pop, p_sel, pop_size)
        #TODO: BUG!
        print(np.sum(new_pop)/100)
        # 2 CROSSOVER
        pop = func.crossover(new_pop, pop_size, p_c)
        # 3 MUTATION
        for chromosome in pop:
            func.mutate(chromosome, p_m)
        # 4 INVERSION
        probs_inv = np.random.uniform(len(pop))
        pop = np.where(probs_inv < p_i, func.inverse(pop), pop)

    # after the GA steps >= simulation steps - i.e. the result of GA
    # the code below calculates results averaged over the whole population
    vals = np.zeros(16)
    get_av = False
    if get_av:
        for ii in range(0, 16):
            for em in pop:
                vals[ii] += em[ii]
        vals /= 100
        terminal_view(vals)

    return pop, vals, np.array(best_fs)


if __name__ == "__main__":
    sim_n = 1  # number of simulations to be done
    a = 0.5
    b = 1.0
    c = 0.1
    sim_steps = 400
    epsilon = 10 ** -3
    results = np.zeros(100*16).reshape((100, 16))
    best_f =[]
    # inside this loop many simulations are done
    for ii in range(0, sim_n):
        end_pop, vals, f_evol = main(a, b, c, epsilon, sim_steps)
        f_vals = func.selection(end_pop, a, b, c, epsilon)
        index = np.argmax(f_vals)
        # print(((f_vals[index])))
        best_f.append(end_pop[index])

        if int((ii+1) * 1000 / sim_n) % 10 == 0 and int((ii+1) / sim_n * 100) > 0:
            print(int((ii+1) / sim_n * 100), '% done')

    av_result = np.zeros(16)
    for em in best_f:
        av_result += em
    av_result /= len(best_f)
    print(av_result, sum(av_result))
    terminal_view(av_result)
    draw_f_evolution(f_evol)

