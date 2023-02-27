# These are the first 9 numbers at cords (0,0)()
# xcords = [0, 0, 1, 1, 1, 0, -1, -1, -1]
# ycords = [0, 1, 1, 0, -1, -1, -1, 0, 1]


# plt.show()

from numpy import random
import matplotlib.pyplot as plt
from detect_primes import *

detect_prime(1)
detect_prime(2)
detect_prime(3)
detect_prime(4)
detect_prime(5)
detect_prime(6)
detect_prime(7)
detect_prime(8)
detect_prime(9)
detect_prime(10)
detect_prime(11)
detect_prime(12)

# plt.plot(xcords, ycords, 'o')
# plt.axis([0, 6, 0, 20])

# data = random.random((5,5))
# img = plt.imshow(data, interpolation='nearest')
# img.set_cmap('hot')
# plt.axis('off')
# plt.savefig("test.png", bbox_inches='tight')

# plt.show()
