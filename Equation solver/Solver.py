from crossover import crossover
from mutation import mutation
from populate import generatestring
from fitness import fitnessfunction,getFitness
from selection import selection

def geneticAlgo():
    func, ranges = fitnessfunction()
    strings = []
    k = 10
    for i in range(k):
        strings.append(generatestring(ranges))
    m = 10000000000000000
    state = strings[0]
    for _ in range(1000):
        strings = selection(strings,func)
        for i in range(0,k,2):
            strings[i],strings[i+1]  = crossover(strings[i],strings[i+1])
        for i in range(k):
            strings[i] = mutation(strings[i],ranges)
        strings.sort(key = lambda x: getFitness(func,x))
        x = getFitness(func,strings[0])
        if x<m:
            m=x
            state = strings[0]
    
    x = int(state[:len(state)//2],2)
    y = int(state[len(state)//2:],2)
    print("Minimum of the function found: {} at x = {} and y = {}".format(m,x,y))
    

geneticAlgo()