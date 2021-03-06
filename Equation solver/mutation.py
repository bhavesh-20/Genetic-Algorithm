import random
def mutation(string: str,ranges: list):
    x = random.randint(0,len(string))
    if x!=len(string):
        c = '1' if string[x] == '0' else '0'
        s = string[:x] + c + string[x+1:]
        s = [s[:len(s)//2],s[len(s)//2:]]
        s = [int(s[0],2),int(s[1],2)]
        if ranges[0][0]<= s[0] <=ranges[0][1] and ranges[1][0]<=s[1]<=ranges[1][1]:
            string = string[:x] + c +string[x+1:]
    return string
