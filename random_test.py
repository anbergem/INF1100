import random
import numpy as np

a = 1
b = 6
N = 10

# Et random tall
print [random.random() for i in range(N)]

# Et random tall, men kan lage en liste med random tall
print np.random.random(N)

# Mellom og TIL OG MED b
# Bare to argumenter, sa ma lage liste
print [random.randint(a, b) for i in range(N)]

# Mellom og MEN IKKE MED b
# Tar tre argumenter
print np.random.randint(a, b, N)
