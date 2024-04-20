class Solution:
    def findFarmland(self, grid: List[List[int]]) -> List[List[int]]:
        ans = []
        R, C = len(grid), len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0: continue 
                if (r == 0 and c == 0) or (r == 0 and grid[r][c-1] == 0) or (c == 0 and grid[r-1][c] == 0) or (grid[r-1][c] == 0 and grid[r][c-1] == 0):
                    nr, nc = r, c
                    while 0 <= nr + 1 < R and grid[nr+1][nc] == 1:
                        nr += 1
                    while 0 <= nc + 1 < C and grid[nr][nc+1] == 1:
                        nc += 1
                    ans.append((r, c, nr, nc))
        return ans                     