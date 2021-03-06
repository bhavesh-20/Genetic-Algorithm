from fitness import getFitness
import random

def selection(strings: list,f):
    a = []
    for i in strings:
        a.append([i,getFitness(f,i)])
    a.sort(key= lambda x:x[1])
    b = []
    for _ in range(len(strings)//2):
        x = random.randint(0,len(a)-1)    
        y = random.randint(0,len(a)-1)
        if a[x][1]<a[y][1]:
            b.append(a[x][0])
        else:
            b.append(a[y][0])
        last = b[-1]
        while last==a[x][0]:
            x = random.randint(0,len(a)-1) 
        while last == a[y][0]:
            y = random.randint(0,len(a)-1)
        if a[x][1]<a[y][1]:
            b.append(a[x][0])
        else:
            b.append(a[y][0])
    return b
