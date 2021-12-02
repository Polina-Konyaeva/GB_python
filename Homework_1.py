import numpy as np

class Matrix:

    def __init__(self, matrix_value):
        self.matrix_value = matrix_value

    def __str__(self):
        return '\n'.join('\t'.join(map(str, j)) for j in self.matrix_value)

    def __add__(self, other):
        new_matrix = np.zeros((3, 3))
        for i in range(len(self.matrix_value)):
            for j in range(len(other.matrix_value[i])):
                new_matrix[i][j] = self.matrix_value[i][j] + other.matrix_value[i][j]
        return Matrix(new_matrix)

my_matrix1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
my_matrix2 = Matrix([[10, 8, 5], [13, 7, 11], [12, 9, 4]])
result = my_matrix1 + my_matrix2
print(result)

