import sys, random
from time import *

start = time()

n = 1024


A = [[random.random() for row in range(n)]for col in range(n)]
B = [[random.random() for row in range(n)]for col in range(n)]
C = [[0 for row in range(n)]for col in range(n)]

# Record time of our experiment
for i in range(n):
    for j in range(n):
        for k in range(n):
            C[i][j] += A[i][k] * B[k][j]

# Stop time of our experiment
end = time()
print("%0.5f" % (end-start))
