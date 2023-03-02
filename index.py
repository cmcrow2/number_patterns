# These are the first 9 numbers at cords: 
# (0,0) (1,0) (1,1) (0,1) (-1,1) (-1,0) (-1,-1) (0,-1) (1,-1)
# xcords = [0, 1, 1, 0, -1, -1, -1,  0,  1]
# ycords = [0, 0, 1, 1,  1,  0, -1, -1, -1]

import matplotlib.pyplot as plt
from global_functions.primes import *
from global_functions.detect_primes import *

options = ""
programs = {
    "1": "Primes"
}

for key in programs:
    options += "\t[" + key + "] : " + programs[key] + "\n"

res = input("Which pattern do you want to see?\n\n" + options + "\nEnter the number that corresponds to\nthe program you wish to run: ")

# add values to each list | always start @ 0,0
xcords = []
ycords = []

n = 25000

if programs[res] == "Primes":
    xcords, ycords = primes(n)

print("\n\nNumber of " + programs[res] + " in " + str(n) + " numbers: ", len(xcords))

plt.scatter(xcords, ycords, c="black")
plt.show()
