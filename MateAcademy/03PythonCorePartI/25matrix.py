class Matrix:
    def __init__(self, matrix: list) -> None:
        self.matrix = matrix

    def get_diagonal(self) -> list:
        diagonal = []
        for i in range(len(self.matrix)):
            diagonal.append(self.matrix[i][i])
        return diagonal

    def get_counter_diagonal(self) -> list:
        diagonal = []
        for i in range(len(self.matrix)):
            diagonal.append(self.matrix[i][len(self.matrix) - 1 - i])
        return diagonal

    def rotate_rows(self, number: int) -> list:

        if not self.matrix:
            return self.matrix
            
        number = number % len(self.matrix)
        for i in range(number):
            self.matrix = self.matrix[1:] + self.matrix[:1]
        return self.matrix

    def rotate_columns(self, number: int) -> list:
        
        if not self.matrix:
            return self.matrix
        
        rotate = []
        for linha in self.matrix:
            nova_linha = linha
            for i in range(number):
                nova_linha = nova_linha[1:] + nova_linha[:1]

            rotate.append(nova_linha)

        self.matrix = rotate
        return self.matrix


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m.get_diagonal())
print(m.get_counter_diagonal())
print(m.rotate_rows(1))
print(m.rotate_columns(1))
