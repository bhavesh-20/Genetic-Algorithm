import numpy as np
from fitness import fitness_function
from random_generation import random_generation
from selection import selection
from crossover import crossover
from mutation import mutation

def genetic_algorithm():
    gs = []
    k=20
    for i in range(k):
        gs.append(random_generation())
    for _ in range(1000):
        gs1 = selection(gs,k)
        for i in range(0,len(gs1),2):
            gs1[i],gs1[i+1] = crossover(gs1[i],gs1[i+1])
        for i in range(len(gs1)):
            gs1[i] = mutation(gs1[i])
        gs = gs1[:]
        gs.sort(key = lambda x:-fitness_function(x))
        m = fitness_function(gs[0])
        s = gs[0]
        if m==243:
            print(s)
            break
    else:
        for i in range(5):
            print(gs[i],fitness_function(gs[i]))

genetic_algorithm()
