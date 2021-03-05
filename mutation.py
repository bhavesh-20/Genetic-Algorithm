import numpy as np

"""Mutation is done in a smart way, a random row is selected and chance of not doing mutation is also taken
into interest, this random row has been mutated in such a way that it minimises both row and column wise
duplicates. """
def mutation(string: str):
    l = ["x8xxxxx9x","xx75x28xx","6xx8x7xx5","37xx8xx51","2xxxxxxx8","95xx4xx32","8xx1x4xx9","xx19x36xx",
        "x4xxxxx2x"]
    string = [string[(x-1)*9:x*9] for x in range(1,10)]
    x = np.random.randint(0,10)
    if x!=0:
        a = l[x-1]
        n = list({1,2,3,4,5,6,7,8,9} - set([int(x) for x in a if x!='x']))
        s = ''
        column = 0
        for i in l[x-1]:
            possible = set(n)
            if i!='x':
                s+=i
            else:
                for j in range(9):
                    if j!=x and int(string[j][column]) in possible:
                        possible.remove(int(string[j][column]))
                possible = list(possible)
                if len(possible) == 0:
                    r = np.random.randint(0,len(n))
                    r = n[r]
                    s+=str(r)
                    n.remove(r)
                else:
                    r = np.random.randint(0,len(possible))
                    r = possible[r]
                    s+=str(r)
                    n.remove(r)
            column+=1
        string[x-1] = s
    return ''.join(x for x in string)    