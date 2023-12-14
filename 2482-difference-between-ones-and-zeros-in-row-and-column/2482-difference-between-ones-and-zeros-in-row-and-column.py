class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        rows = [0]*R
        cols = [0]*C
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    rows[r] += 1
                    cols[c] += 1
        diff = [[0]*C for _ in range(R)]
        for r in range(R):
            for c in range(C):
                diff[r][c] = 2*rows[r] - R + 2*cols[c] - C
        return diff