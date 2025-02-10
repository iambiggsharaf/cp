import random

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

flat = [elem for row in matrix for elem in row]

random.shuffle(flat)

rows = len(matrix)
cols = len(matrix[0])
for i in range(rows):
    for j in range(cols):
        matrix[i][j] = flat[i * cols + j]

