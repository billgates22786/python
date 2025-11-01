def matrix_multiply(A, B):
    p, q, r = len(A), len(A[0]), len(B[0])
    result = [[sum(A[i][k] * B[k][j] for k in range(q)) for j in range(r)] for i in range(p)]
    return result
A = [[1, 2, 3], [4, 5, 6]]
B = [[7, 8], [9, 10], [11, 12]]
result = matrix_multiply(A, B)
print("Result of matrix multiplication:")
for row in result:
    print(row)
