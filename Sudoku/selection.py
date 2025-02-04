import numpy as np
from fitness import fitness_function

"""First the fitness values are calculated for each genetic string passed in the list, and sorted 
based on them in descending order, then the selection percentage is calculated and pairs are found
based on the selection strategy randomly and returned to whom crossover is applied to."""

def selection(gs: list,k: int):
    gs1 = []
    s = 0
    for i in gs:
        fitness = fitness_function(i)
        gs1.append([i,fitness])
        s += fitness
    gs1.sort(key = lambda x:-x[1])
    for i in gs1:
        i[1] = (i[1]*100)/s   
    g = [] 
    #since, k= 8
    for i in range(k//2):
        x = np.random.randint(0,50)
        #selecting first one in pair
        for j in gs1:
            if x-j[1]<0:
                g.append(j[0])
                break
            x-=j[1]
        #selecting second one in pair
        r = g[-1]
        while g[-1] == r:
            x = np.random.randint(0,50)
            for j in gs1:
                if x-j[1]<0:
                    r = j[0]
                    break
                x-=j[1]
        g.append(r)
    return g

