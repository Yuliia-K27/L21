class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix
        self.rows = len(matrix)
        self.cols = len(matrix[0])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.matrix])

    def __add__(self, other):
        if (self.rows != other.rows) or (self.cols != other.cols):
            raise ValueError("Matrices are not the same size.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __sub__(self, other):
        if (self.rows != other.rows) or (self.cols != other.cols):
            raise ValueError("Matrices are not the same size.")
        result = []
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                row.append(self.matrix[i][j] - other.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __mul__(self, other):
        if isinstance(other, int) or isinstance(other, float):
            result = []
            for i in range(self.rows):
                row = []
                for j in range(self.cols):
                    row.append(self.matrix[i][j] * other)
                result.append(row)
            return Matrix(result)
        elif isinstance(other, Matrix):
            if self.cols != other.rows:
                raise ValueError("Matrices are not compatible for multiplication.")
            result = []
            for i in range(self.rows):
                row = []
                for j in range(other.cols):
                    sum = 0
                    for k in range(self.cols):
                        sum += self.matrix[i][k] * other.matrix[k][j]
                    row.append(sum)
                result.append(row)
            return Matrix(result)
        else:
            raise ValueError("Invalid operand type.")

    def transpose(self):
        result = []
        for j in range(self.cols):
            row = []
            for i in range(self.rows):
                row.append(self.matrix[i][j])
            result.append(row)
        return Matrix(result)

    def __eq__(self, other):
        if (self.rows != other.rows) or (self.cols != other.cols):
            return False
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] != other.matrix[i][j]:
                    return False
        return True
