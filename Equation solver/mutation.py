import random
def mutation(string: str):
    x = random.randint(0,len(string))
    if x!=len(string):
        c = '1' if string[x] == '0' else '0'
        string = string[:x] + c + string[x+1:]
    return string
