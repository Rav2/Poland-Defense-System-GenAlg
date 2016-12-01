import functions as func
from regions import *
def main():
    steps = 1000
    pop = func.init(100, 'uniform')
    print "pop[0]", pop[0]
    val = func.f_chrom(pop[0], 1, 1, 0.05)
    print "przerywnik "
    value = func.f(5,0.5,1,1,zachodnio_pomorskie)
    # func.mutate(pop[0], 0.1)
    print(len(val))
    print(val)
    for step in range(0, steps):
        #do stuff
        0

main()