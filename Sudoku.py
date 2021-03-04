import numpy as np


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


def fitness_function(rand_string :str) -> int:
    rand_string = [rand_string[(x-1)*9:x*9] for x in range(1,10)]
    return row_fitness(rand_string) + column_fitness(rand_string) + block_fitness(rand_string)
    pass


def row_fitness(rand_string):
    s = 0
    for i in rand_string:
        s += len(set(i))
    return s

def column_fitness(rand_string):
    columns = ['']*9
    for i in rand_string:
        for j in range(9):
            columns[j] += i[j]
    return row_fitness(columns)            

def block_fitness(rand_string):
    blocks = ['']*9
    for row in range(9):
        string = rand_string[row]
        blocks[row//3 * 3] += string[:3]
        blocks[row//3 * 3 + 1] += string[3:6]
        blocks[row//3 * 3 + 2] += string[6:9]
    return row_fitness(blocks)

