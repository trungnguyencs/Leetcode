class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # 1. 1st column should be all 1s => flip rows starting with 0
        # 2. from 2nd column onwards, if column has more 0s than 1s, then flip column
        R, C = len(grid), len(grid[0])
        ans = R * (1 << (C - 1)) #1st column should be all 1s
        for c in range(1, C):
            ones = sum(grid[r][c] == grid[r][0] for r in range(R)) #after step 1, A[i][j] becomes 1 if A[i][j] == A[i][0]
            ans += max(ones, R - ones) * (1 << (C - 1 - c))
        return ans