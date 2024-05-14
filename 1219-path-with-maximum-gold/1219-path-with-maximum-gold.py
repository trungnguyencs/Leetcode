class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                ans = max(ans, self.backtrack(grid, r, c))
        return ans
        
    def backtrack(self, grid, r, c):
        if not 0 <= r < len(grid) or not 0 <= c < len(grid[0]) or grid[r][c] == 0:
            return 0
        neighs = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
        ans = tmp = grid[r][c]
        grid[r][c] = 0
        ans += max(self.backtrack(grid, nr, nc) for nr, nc in neighs)
        grid[r][c] = tmp
        return ans