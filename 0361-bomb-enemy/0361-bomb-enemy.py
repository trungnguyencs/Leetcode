class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        numRow, numCol = len(grid), len(grid[0])
        L = [[0]*numCol for _ in range(numRow)]
        R = [[0]*numCol for _ in range(numRow)]
        T = [[0]*numCol for _ in range(numRow)]
        B = [[0]*numCol for _ in range(numRow)]
        ans = 0
        for r in range(numRow):
            for c in range(numCol):
                if c != 0:
                    if grid[r][c] == 'W':
                        L[r][c] = 0
                    else:
                        L[r][c] = L[r][c-1] + (grid[r][c-1] == 'E')
                if r != 0:
                    if grid[r][c] == 'W':
                        T[r][c] = 0
                    else:
                        T[r][c] = T[r-1][c] + (grid[r-1][c] == 'E')
        for r in range(numRow - 1, -1, -1):
            for c in range(numCol - 1, -1, -1):
                if c != numCol - 1:
                    if grid[r][c] == 'W':
                        R[r][c] = 0
                    else:
                        R[r][c] = R[r][c+1] + (grid[r][c+1] == 'E')
                if r != numRow - 1:
                    if grid[r][c] == 'W':
                        B[r][c] = 0
                    else:
                        B[r][c] = B[r+1][c] + (grid[r+1][c] == 'E')
        for r in range(numRow):
            for c in range(numCol):
                if grid[r][c] == '0':
                    ans = max(ans, L[r][c] + R[r][c] + T[r][c] + B[r][c])
        return ans