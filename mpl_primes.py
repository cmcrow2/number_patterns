# These are the first 9 numbers at cords: 
# (0,0) (1,0) (1,1) (0,1) (-1,1) (-1,0) (-1,-1) (0,-1) (1,-1)
# xcords = [0, 1, 1, 0, -1, -1, -1,  0,  1]
# ycords = [0, 0, 1, 1,  1,  0, -1, -1, -1]

import matplotlib.pyplot as plt
from global_functions.order_nums import *
from global_functions.detect_primes import *

# add values to each list | always start @ 0,0
xcords = []
ycords = []

xcords, ycords = order_nums(25000)
print(len(xcords))

plt.scatter(xcords, ycords, c="black")
plt.show()
