class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_over = 0
        mm = self.matrix[row1:row2+1]
        for i, row in enumerate(mm):
            sum_over += sum(row[col1:col2+1])
        return sum_over 



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)