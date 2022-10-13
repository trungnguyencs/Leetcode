class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r > 0: matrix[r][c] += matrix[r-1][c]
                if c > 0: matrix[r][c] += matrix[r][c-1]
                if r > 0 and c > 0: matrix[r][c] -= matrix[r-1][c-1]
        self.dp = matrix

    def sumRegion(self, r1: int, c1: int, r2: int, c2: int) -> int:
        ans = self.dp[r2][c2]
        if r1 > 0: ans -= self.dp[r1-1][c2]
        if c1 > 0: ans -= self.dp[r2][c1-1]
        if r1 > 0 and c1 > 0: ans += self.dp[r1-1][c1-1]
        return ans


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)