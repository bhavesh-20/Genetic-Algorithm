import numpy as np
#crossover for list of strings
"""here crossover takesplace with rows, that is, the random point for crossover is always 
    the ending point of a row or starting point of a row, in this case starting point of 5th row"""

def crossover(string1 :str, string2 :str) -> list:
    string1 = [string1[(x-1)*9:x*9] for x in range(1,10)]
    string2 = [string2[(x-1)*9:x*9] for x in range(1,10)]
    # x = np.random.randint(1,8)
    x = 5
    string1, string2 = string1[:x] + string2[x:], string2[:x] + string1[x:]
    string1, string2 = ''.join(x for x in string1),  ''.join(x for x in string2)
    return [string1,string2]
