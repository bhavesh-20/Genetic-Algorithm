import numpy as np
import math


"""Function which generates random strings for genetic algorithm, each string
 is a representation of genetic string used in the algorithm."""

def random_generation():
    l = ["x8xxxxx9x","xx75x28xx","6xx8x7xx5","37xx8xx51","2xxxxxxx8","95xx4xx32","8xx1x4xx9","xx19x36xx",
        "x4xxxxx2x"]
    rand_string = []
    number_set = {1,2,3,4,5,6,7,8,9}
    for i in l:
        a = set([int(x) for x in i if x!='x'])
        a = np.array(list(number_set - a))
        np.random.shuffle(a)
        a, k, string = list(a), 0, ""
        for j in i:
            if j=='x':
                string+=str(a[k])
                k+=1
            else:
                string+=j
        rand_string.append(string)
    rand_string = ''.join(x for x in rand_string)
    return rand_string


"""
The fitness function is based on how fit the string is based on rows,columns and blocks of sudoku.
The fitness calculated is sum of the number of distinct numbers in each row, column or block.
The solution has the fitness of (9*9) + (9*9) + (9*9) = 81 * 3 = 243, which is the highest fitness possible
"""

def fitness_function(rand_string :str) -> int:
    rand_string = [rand_string[(x-1)*9:x*9] for x in range(1,10)]
    return row_fitness(rand_string) + column_fitness(rand_string) + block_fitness(rand_string)
    pass

#Part of fitness function: calculates Fitness of the rows

def row_fitness(rand_string):
    s = 0
    for i in rand_string:
        s += len(set(i))
    return s

#Part of fitness function: calculates Fitness of the columns

def column_fitness(rand_string):
    columns = ['']*9
    for i in rand_string:
        for j in range(9):
            columns[j] += i[j]
    return row_fitness(columns)            

#Part of fitness function: calculates Fitness of the Blocks

def block_fitness(rand_string):
    blocks = ['']*9
    for row in range(9):
        string = rand_string[row]
        blocks[row//3 * 3] += string[:3]
        blocks[row//3 * 3 + 1] += string[3:6]
        blocks[row//3 * 3 + 2] += string[6:9]
    return row_fitness(blocks)


def selection(gs: list):
    global k
    gs1 = []
    s = 0
    for i in gs:
        fitness = fitness_function(i)
        gs1.append([i,fitness])
        s += fitness
    for i in gs1:
        i[1] = math.ceil((i[1]*100)/s)
    gs1.sort(key = lambda x:-x[1])
    g = [] 
    #since, k= 8
    for i in range(k//2):
        x = np.random.randint(0,60)
        #selecting first one in pair
        for j in gs1:
            if x-j[1]<0:
                g.append(j[0])
                break
            x-=j[1]
        #selecting second one in pair
        r = g[-1]
        while g[-1] == r:
            x = np.random.randint(0,60)
            for j in gs1:
                if x-j[1]<0:
                    r = j[0]
                    break
                x-=j[1]
        g.append(r)
    return g

#crossover for list of strings
"""here crossover takesplace with rows, that is, the random point for crossover is always 
    the ending point of a row or starting point of a row, in this case starting point of 5th row"""

def crossover_2(string1 :str, string2 :str) -> list:
    string1 = [string1[(x-1)*9:x*9] for x in range(1,10)]
    string2 = [string2[(x-1)*9:x*9] for x in range(1,10)]
    x = np.random.randint(1,8)
    string1, string2 = string1[:x] + string2[x:], string2[:x] + string1[x:]
    string1, string2 = ''.join(x for x in string1),  ''.join(x for x in string2)
    return [string1,string2]


def mutation_2(string: str):
    l = ["x8xxxxx9x","xx75x28xx","6xx8x7xx5","37xx8xx51","2xxxxxxx8","95xx4xx32","8xx1x4xx9","xx19x36xx",
        "x4xxxxx2x"]
    string = [string[(x-1)*9:x*9] for x in range(1,10)]
    x = np.random.randint(0,10)
    if x!=0:
        a = l[x-1]
        n = np.array(list({1,2,3,4,5,6,7,8,9} - set([int(x) for x in a if x!='x'])))
        np.random.shuffle(n)
        n = list(n)
        i = 0
        s = ''
        for j in a:
            if j!='x':
                s+=j
            else:
                s+=str(n[i])
                i+=1
        string[x-1] = s 
    return ''.join(x for x in string)    


k = 20

def genetic_algorithm():
    gs = []
    for i in range(k):
        gs.append(random_generation())
    for _ in range(1000):
        gs1 = selection(gs)
        for i in range(0,len(gs1),2):
            gs1[i],gs1[i+1] = crossover_2(gs1[i],gs1[i+1])
        for i in range(len(gs1)):
            gs1[i] = mutation_2(gs1[i])
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
