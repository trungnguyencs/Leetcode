class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        r, c = R - 1, 0
        count = 0
        while r >= 0 and c < C:
            while c < C and grid[r][c] >= 0:
                c += 1
            count += C - c
            r -= 1
        return count