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
	

	def rotate_rows(self, number):
	    pass	  
	
	
    #def rotate_columns(self, number):
    	#pass


m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(m.get_diagonal())
print(m.get_counter_diagonal())
