# These are the first 9 numbers at cords (0,0)()
# xcords = [0, 0, 1, 1, 1, 0, -1, -1, -1]
# ycords = [0, 1, 1, 0, -1, -1, -1, 0, 1]


# plt.show()

from numpy import random
import matplotlib.pyplot as plt
from python_primes.detect_primes import *

print(detect_prime(1))
print(detect_prime(2))
print(detect_prime(3))
print(detect_prime(4))
print(detect_prime(5))
print(detect_prime(6))
print(detect_prime(7))
print(detect_prime(8))
print(detect_prime(9))
print(detect_prime(10))
print(detect_prime(11))
print(detect_prime(12))

# plt.plot(xcords, ycords, 'o')
# plt.axis([0, 6, 0, 20])

# data = random.random((5,5))
# img = plt.imshow(data, interpolation='nearest')
# img.set_cmap('hot')
# plt.axis('off')
# plt.savefig("test.png", bbox_inches='tight')

# plt.show()
