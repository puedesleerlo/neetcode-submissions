class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        sum_over = 0
        for i, row in enumerate(self.matrix):
            for j, cell in enumerate(row):
                mult_row = 1 if i >= row1 and i <= row2 else 0
                mult_col = 1 if j >= col1 and j <= col2 else 0
                sum_over += mult_row*mult_col*cell
        return sum_over 



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)