class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        ans = 0
        counter = Counter([tuple(row) for row in grid])
        for c in range(len(grid[0])):
            col = tuple(grid[r][c] for r in range(len(grid)))
            ans += counter[col]
        return ans