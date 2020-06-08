import random

f = open("matrix_meta.c", "a")

f.write("double A[N][N] = { ")

for x in range(1048575):
    f.write(str(round(random.random(), 4)) + ", ")
f.write(str(round(random.random(), 4)))
f.write("};\n")

f.write("double B[N][N] = { ")

for x in range(1048575):
    f.write(str(round(random.random(), 4)) + ", ")
f.write(str(round(random.random(), 4)))
f.write("};\n")

f.write("double C[N][N] = { ")

for x in range(1048575):
    f.write(str(0.0) + ", ")
f.write(str(0.0))
f.write("};\n")

