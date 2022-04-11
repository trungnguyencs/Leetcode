class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        R, C = len(grid), len(grid[0])
        k %= R*C
        self.reverseGrid(grid, 0, R*C - 1)
        self.reverseGrid(grid, 0, k - 1)
        self.reverseGrid(grid, k, R*C - 1)
        return grid
    
    def reverseGrid(self, grid, i, j):
        while i < j:
            ir, ic = divmod(i, len(grid[0]))
            jr, jc = divmod(j, len(grid[0]))
            grid[ir][ic], grid[jr][jc] = grid[jr][jc], grid[ir][ic]
            i += 1
            j -= 1