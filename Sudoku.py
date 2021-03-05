import numpy as np
from fitness import fitness_function
from random_generation import random_generation
from selection import selection
from crossover import crossover
from mutation import mutation

def printSudoku(string: str):
    l = [string[(x-1)*9:x*9] for x in range(1,10)]
    for i in l:
        for j in i:
            print(int(j),end=' ')
        print('')

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
            print("Solution Found!!")
            printSudoku(s)
            break
    else:
        print("5 Best solution along with their fitnesses of the final population")
        for i in range(5):
            printSudoku(gs[i])
            print("Fitness Value: {}".format(fitness_function(gs[i])))
            print('')

genetic_algorithm()
