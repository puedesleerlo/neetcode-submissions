class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix), len(matrix[0])
        self.prefix_matrix = [[0] * cols for _ in range(rows)] 
        self.prefix_matrix[0][0] = matrix[0][0]
        for j in range(1, len(matrix[0])):
            self.prefix_matrix[0][j] = matrix[0][j] + self.prefix_matrix[0][j-1]
        for i in range(1, len(matrix)):
            self.prefix_matrix[i][0] = matrix[i][0] + self.prefix_matrix[i - 1][0]
            for j in range(1, len(matrix[0])):
                    self.prefix_matrix[i][j] = (matrix[i][j] 
                                        + self.prefix_matrix[i][j - 1] 
                                        + self.prefix_matrix[i - 1][j] 
                                        - self.prefix_matrix[i-1][j-1])
        print(self.prefix_matrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        whole_reg = self.prefix_matrix[row2][col2]
        if row1 > 0 and col1> 0:
            small_reg = self.prefix_matrix[row1-1][col1-1]
        else:
            small_reg = 0
        if row1 > 0:
            top_reg = self.prefix_matrix[row1-1][col2]
        else:
            top_reg = 0
        if col1 > 0:
            left_reg = self.prefix_matrix[row2][col1-1]
        else:
            left_reg = 0
        area = whole_reg - left_reg - top_reg + small_reg
        return area 



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)