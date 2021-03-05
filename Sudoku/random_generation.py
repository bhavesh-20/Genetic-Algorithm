import numpy as np

"""Function which generates random strings for genetic algorithm, each string
 is a representation of genetic string used in the algorithm. Randomness is used in a smart way to remove
 the chance of each row having duplicates in sudoku, hence the generated random string doesn't have any duplicates
 row-wise"""

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
