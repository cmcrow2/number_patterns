# this function determines where the fibonacci numbers are plotted on the graph

import math

def fib(num):
    if num == 1:
        return True
    
    pos_square = math.sqrt((5 * num * num) + 4)
    neg_square = math.sqrt((5 * num * num) - 4)

    if int(pos_square + 0.5) ** 2 == (5 * num * num) + 4:
        return True
    elif int(neg_square + 0.5) ** 2 == (5 * num * num) - 4:
        return True
    else:
        return False