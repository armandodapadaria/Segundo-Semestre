A = [[1, 2], [3, 4]]
B = [[5, 6], [7, 8]]
soma = [[0, 0], [0, 0]]

for i in range(len(A)):
    for j in range(len(A[0])):
        soma[i][j] = A[i][j] + B[i][j]

print(soma)