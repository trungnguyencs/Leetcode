class NumMatrix:
​
    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.matrix = None
            return
        for r in range(1, len(matrix)):
            matrix[r][0] += matrix[r-1][0]
        for c in range(1, len(matrix[0])):
            matrix[0][c] += matrix[0][c-1]
        for r in range(1, len(matrix)):
            for c in range(1, len(matrix[0])):
                matrix[r][c] += matrix[r-1][c] + matrix[r][c-1] - matrix[r-1][c-1]
        self.matrix = matrix
        
    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        if not self.matrix: return 0
        upper = self.matrix[r1-1][c2] if r1 > 0 else 0
        left = self.matrix[r2][c1-1] if c1 > 0 else 0
        upperleft = self.matrix[r1-1][c1-1] if r1 > 0 and c1 > 0 else 0
        return self.matrix[r2][c2] - upper - left + upperleft
​
​
# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
