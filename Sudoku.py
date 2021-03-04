import numpy as np


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


#crossover for strings
""" Here crossover takes place between two strings, and crossover point is the midpoint of both strings """

def crossover_1(string1 :str, string2 :str) -> list:
    string1, string2 = string1[:40] + string2[40:], string2[:40] + string1[40:]
    return [string1,string2]


#crossover for list of strings
"""here crossover takesplace with rows, that is, the random point for crossover is always 
    the ending point of a row or starting point of a row, in this case starting point of 5th row"""

def crossover_2(string1 :str, string2 :str) -> list:
    string1 = [string1[(x-1)*9:x*9] for x in range(1,10)]
    string2 = [string2[(x-1)*9:x*9] for x in range(1,10)]
    string1, string2 = string1[:4] + string2[4:], string2[:4] + string1[4:]
    string1, string2 = ''.join(x for x in string1),  ''.join(x for x in string2)
    return [string1,string2]

