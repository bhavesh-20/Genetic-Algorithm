"""
The fitness function is based on how fit the string is based on rows,columns and blocks of sudoku.
The fitness calculated is sum of the number of distinct numbers in each row, column or block.
The solution has the fitness of (9*9) + (9*9) + (9*9) = 81 * 3 = 243, which is the highest fitness possible
"""

def fitness_function(rand_string :str) -> int:
    rand_string = [rand_string[(x-1)*9:x*9] for x in range(1,10)]
    return row_fitness(rand_string) + column_fitness(rand_string) + block_fitness(rand_string)
    pass

#Part of fitness function: calculates Fitness of the rows

def row_fitness(rand_string):
    s = 0
    for i in rand_string:
        s += len(set(i))
    return s

#Part of fitness function: calculates Fitness of the columns

def column_fitness(rand_string):
    columns = ['']*9
    for i in rand_string:
        for j in range(9):
            columns[j] += i[j]
    return row_fitness(columns)            

#Part of fitness function: calculates Fitness of the Blocks

def block_fitness(rand_string):
    blocks = ['']*9
    for row in range(9):
        string = rand_string[row]
        blocks[row//3 * 3] += string[:3]
        blocks[row//3 * 3 + 1] += string[3:6]
        blocks[row//3 * 3 + 2] += string[6:9]
    return row_fitness(blocks)

