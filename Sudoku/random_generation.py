import numpy as np

"""Function which generates random strings for genetic algorithm, each string
 is a representation of genetic string used in the algorithm. Randomness is used in a smart way to remove
 the chance of each row having duplicates in sudoku and also trying to minimise conflicts with columns,
hence the generated random string doesn't have any duplicates row-wise and minimum duplicates column-wise"""

def random_generation():
    l = ["x8xxxxx9x","xx75x28xx","6xx8x7xx5","37xx8xx51","2xxxxxxx8","95xx4xx32","8xx1x4xx9","xx19x36xx",
        "x4xxxxx2x"]
    rand_string = []
    number_set = {1,2,3,4,5,6,7,8,9}
    columns = [] 
    for _ in range(9):
        columns.append(set())
    for i in l:
        for j in range(9):
            if i[j]!='x':
                columns[j].add(int(i[j]))
    for i in l:
        s = ''
        n = list(number_set - set([int(x) for x in i if x!='x']))
        for column in range(9):
            possible = set(n)
            if i[column]!='x':
                s+=i[column]
            else:
                a = list(possible - columns[column])
                if len(a) == 0:
                    r = np.random.randint(0, len(n))
                    r = n[r]
                    n.remove(r)
                    s+=str(r)
                else:
                    r = np.random.randint(0, len(a))
                    r = a[r]
                    n.remove(r)
                    s+=str(r)
        rand_string.append(s)
    rand_string = ''.join(x for x in rand_string)
    return rand_string


"""Function which generates random strings for genetic algorithm, each string
 is a representation of genetic string used in the algorithm. Randomness is used in a smart way to remove
 the chance of each row having duplicates in sudoku, hence the generated random string doesn't have any duplicates
 row-wise"""

def random_generation2():
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