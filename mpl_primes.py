# import matplotlib.pyplot as plt

# These are the first 9 numbers at cords (0,0)()
# xcords = [0, 0, 1, 1, 1, 0, -1, -1, -1]
# ycords = [0, 1, 1, 0, -1, -1, -1, 0, 1]

# plt.plot(xcords, ycords, 'o')
# plt.axis([0, 6, 0, 20])

# plt.show()

from numpy import random
import matplotlib.pyplot as plt

data = random.random((5,5))
img = plt.imshow(data, interpolation='nearest')
img.set_cmap('hot')
plt.axis('off')
# plt.savefig("test.png", bbox_inches='tight')

plt.show()
