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
    for _ in range(1000):
        strings = selection(strings,func)
        for i in range(0,k,2):
            strings[i],strings[i+1]  = crossover(strings[i],strings[i+1])
        for i in range(k):
            strings[i] = mutation(strings[i])
        strings.sort(key = lambda x: getFitness(func,x))
        m = min(m,getFitness(func,strings[0]))
    
    print("Global Minimum found: {}".format(m))
    for i in range(5):
        print(strings[i],getFitness(func,strings[i]))

geneticAlgo()