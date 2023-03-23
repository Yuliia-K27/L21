matrix_1 = [[1, 2], [3, 4], [5, 6]]
print('Matrix 1. Current matrix:')
for row in matrix_1:
    print(row)

matrix_2 = [[matrix_1[j][i] for j in range(len(matrix_1))] for i in
            range(len(matrix_1[0]))]
print('Matrix 2. Transpose matrix:')
for row in matrix_2:
    print(row)

matrix_3 = [[matrix_1[j][i] + 1 for j in range(len(matrix_1))] for i in
            range(len(matrix_2[0]))]
print('Matrix 3. Addition 1 to each number in matrix 2:')
for row in matrix_3:
    print(row)

matrix_4 = [[0, 0, 0],
            [0, 0, 0]]

for i in range(len(matrix_2)):
    for j in range(len(matrix_3[0])):
      for k in range(len(matrix_3)):
        matrix_4[i][j] += matrix_2[i][k] * matrix_3[k][j]
print('Matrix 4. Multiplication (matrix 2 * matrix 3) using LOOP:')
for r in matrix_4:
    print(r)

matrix_5 = 3 * np.matrix(matrix_4)
print('Matrix 5. Multiplication by 3 (matrix 4) using NUMPY:\n', matrix_5)
