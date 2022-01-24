class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                upleft = 0 if r == 0 or c == 0 else matrix[r-1][c-1]
                upright = 0 if r == 0 else matrix[r-1][c]
                downleft = 0 if c == 0 else matrix[r][c-1]
                matrix[r][c] += downleft + upright - upleft
        self.matrix = matrix

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        upleft = 0 if r1 == 0 or c1 == 0 else self.matrix[r1-1][c1-1]
        upright = 0 if r1 == 0 else self.matrix[r1-1][c2]
        downleft = 0 if c1 == 0 else self.matrix[r2][c1-1]
        return self.matrix[r2][c2] - downleft - upright + upleft


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)