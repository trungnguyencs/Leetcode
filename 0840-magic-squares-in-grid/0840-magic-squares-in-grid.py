class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        # a1,a2,a3
        # a4,a5,a6
        # a7,a8,a9
        # We have:
        # a2 + a5 + a8 = 15
        # a4 + a5 + a6 = 15
        # a1 + a5 + a9 = 15
        # a3 + a5 + a7 = 15
        # => sum(ai) + 3 * a5 = 60
        # => a5 = 5
        return sum(self.isMagicSquare(grid, r, c) for r in range(1, len(grid) - 1) for c in range(1, len(grid[0]) - 1))
        
    def isMagicSquare(self, grid, r, c):
        if grid[r][c] != 5: return False
        flatten = [grid[i][j] for i in [r-1, r, r+1] for j in [c-1, c, c+1]]
        if sorted(flatten) != [1, 2, 3, 4, 5, 6, 7, 8, 9]: return False
        return 15\
            == flatten[0] + flatten[1] + flatten[2]\
            == flatten[3] + flatten[4] + flatten[5]\
            == flatten[6] + flatten[7] + flatten[8]\
            == flatten[0] + flatten[3] + flatten[6]\
            == flatten[1] + flatten[4] + flatten[7]\
            == flatten[2] + flatten[5] + flatten[8]\
            == flatten[0] + flatten[4] + flatten[8]\
            == flatten[2] + flatten[4] + flatten[6]