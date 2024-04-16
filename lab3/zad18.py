def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

my_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed_matrix = transpose_matrix(my_matrix)
print("transponowana macierz:", transposed_matrix)