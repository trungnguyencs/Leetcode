class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        minR, maxR = R - 1, 0
        minC, maxC = C - 1, 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    minR = min(minR, r)
                    maxR = max(maxR, r)
                    minC = min(minC, c)
                    maxC = max(maxC, c)
        return (maxR - minR + 1) * (maxC - minC + 1)