import functions as func

def main():
    steps = 1000
    pop = func.init(100, 'uniform')
    val = func.f_chrom(pop[0], 1, 1, 0.05)
    # func.mutate(pop[0], 0.1)
    print(len(val))
    print(val)
    for step in range(0, steps):
        #do stuff
        0

main()