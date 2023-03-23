class Matrix:
    def __init__(self, matrix_list):
        self.matrix = matrix_list

    def __str__(self):
        matrix_str = ""
        for row in self.matrix:
            matrix_str += " ".join(str(num) for num in row) + "\n"
        return matrix_str

    def __add__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices are not the same size")
        result_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result_matrix.append(row)
        return Matrix(result_matrix)

    def __sub__(self, other):
        if len(self.matrix) != len(other.matrix) or len(self.matrix[0]) != len(other.matrix[0]):
            raise ValueError("Matrices are not the same size")
        result_matrix = []
        for i in range(len(self.matrix)):
            row = []
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result_matrix.append(row)
        return Matrix(result_matrix)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            result_matrix = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(self.matrix[0])):
                    row.append(self.matrix[i][j] * other)
                result_matrix.append(row)
            return Matrix(result_matrix)
        elif isinstance(other, Matrix):
            if len(self.matrix[0]) != len(other.matrix):
                raise ValueError("The number of columns in the first matrix must equal the number of rows in the second matrix")
            result_matrix = []
            for i in range(len(self.matrix)):
                row = []
                for j in range(len(other.matrix[0])):
                    col = [other.matrix[k][j] for k in range(len(other.matrix))]
                    dot_product = sum([self.matrix[i][k] * col[k] for k in range(len(col))])
                    row.append(dot_product)
                result_matrix.append(row)
            return Matrix(result_matrix)

    def transpose(self):
        transposed_matrix = []
        for j in range(len(self.matrix[0])):
            row = []
            for i in range(len(self.matrix)):
                row.append(self.matrix[i][j])
            transposed_matrix.append(row)
        return Matrix(transposed_matrix)

    def to_list(self):
        return self.matrix
