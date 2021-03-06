import random
import math
def generatestring(range):
    x = random.randint(range[0][0],range[0][1])
    y = random.randint(range[1][0],range[1][1])
    x = bin(x)[2:] 
    r = math.ceil(math.log(range[0][1],2))
    if len(x)!=r:
        x = "0"*(r-len(x)) + x    
    y = bin(y)[2:]
    r = math.ceil(math.log(range[1][1],2))
    if len(y)!=r:
        y = "0"*(r-len(y)) + y    
    return x+y