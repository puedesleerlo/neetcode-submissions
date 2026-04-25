class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        rows, cols = len(matrix) + 1, len(matrix[0]) + 1
        self.p = [[0] * cols for _ in range(rows)] 
        for i in range(1, rows):
            for j in range(1, cols):
                    self.p[i][j] = (matrix[i-1][j-1] 
                                        + self.p[i][j - 1] 
                                        + self.p[i - 1][j] 
                                        - self.p[i-1][j-1])

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        whole_reg = self.p[row2 + 1][col2 + 1]
        small_reg = self.p[row1][col1]
        top_reg = self.p[row1][col2 + 1]
        left_reg = self.p[row2+1][col1]
        area = whole_reg - left_reg - top_reg + small_reg
        
        
        return area 



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)