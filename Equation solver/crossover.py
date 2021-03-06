def crossover(string1: str,string2: str):
    x = len(string1)//2
    string1, string2 = string1[:x] + string2[x:], string2[:x] + string1[x:]
    return [string1,string2]
