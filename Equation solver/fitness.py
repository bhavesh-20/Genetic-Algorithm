import Equation

def fitnessfunction():
    s = input("Enter the equation you want to find minimum for:")
    f = Equation.Expression(s,["x","y"])
    range = []
    s = list(map(int,input("Enter range of values [a,b] for x:").split()))
    range.append(s)
    s = list(map(int,input("Enter range of values [a,b] for y:").split()))
    range.append(s)
    return [f,range]

def getFitness(f,string: str):
    x = int(string[:len(string)//2],2)
    y = int(string[len(string)//2:],2)
    return f(x,y)


