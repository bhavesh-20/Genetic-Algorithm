import numpy as np
def mutation(string: str):
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