class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        X = x + k - 1
        while x < X:
            for c in range(y, y + k):
                grid[x][c], grid[X][c] = grid[X][c], grid[x][c]
            x += 1
            X -= 1
        return grid