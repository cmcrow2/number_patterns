# this function determines where each dot is plotted on the graph
# takes in parameter "n" which dictates how many numbers we're looking at
#   i.e. "n=100" -> [1, 2, 3, ...100]

from global_functions.detect_primes import *

def order_nums(n):
    curr_num = 1
    positive = True
    x = 0
    y = 0
    max_step = 1
    curr_x_step = 0
    curr_y_step = 0
    
    # Return the coordinates in a way that matplot can understand them
    x_cords = []
    y_cords = []

    # iterate through every number from 1 to n
    while curr_num <= n:
        if detect_prime(curr_num):
            x_cords.append(x)
            y_cords.append(y)

        if curr_x_step < max_step:
            if positive:
                x += 1
            else:
                x -= 1
            curr_x_step += 1
        elif curr_y_step < max_step:
            if positive:
                y += 1
            else:
                y -= 1
            curr_y_step += 1
        curr_num += 1
        
        if curr_x_step == max_step and curr_y_step == max_step:
            positive = not positive
            max_step += 1
            curr_x_step = 0
            curr_y_step = 0

    return x_cords, y_cords
