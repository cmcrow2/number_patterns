# These are the first 9 numbers at cords: 
# (0,0) (1,0) (1,1) (0,1) (-1,1) (-1,0) (-1,-1) (0,-1) (1,-1)
# xcords = [0, 1, 1, 0, -1, -1, -1,  0,  1]
# ycords = [0, 0, 1, 1,  1,  0, -1, -1, -1]

import matplotlib.pyplot as plt
from global_functions.patterns import *
from global_functions.detect_primes import *
from global_functions.fib import *
from global_functions.squares import *

programs = {
    "1": ["Prime", detect_prime],
    "2": ["Fibonacci", fib],
    "3": ["Perfect Square", squares]
}

options = ""
for key in programs:
    options += "\t[" + key + "] : " + programs[key][0] + "\n"

res = input("Which pattern do you want to see?\n\n" + options + "\nEnter the number that corresponds to\nthe program you wish to run: ")

# add values to each list | always start @ 0,0
xcoords = []
ycoords = []

n = 10000

xcoords, ycoords = plotter(n, programs[res][1])
paired_coords = []
for i in range(len(xcoords)):
    paired_coords.append([xcoords[i], ycoords[i]])

print("\n\nNumber of " + programs[res][0] + " Numbers in " + str(n) + " numbers: ", len(xcoords))

plt.scatter(xcoords, ycoords, c="black")
plt.show()
