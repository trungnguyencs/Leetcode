class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        ans = 0
        for r in range(len(grid2)):
            for c in range(len(grid2[0])):
                if self.isSubIsland(grid1, grid2, r, c):
                    ans += 1
        return ans
        
    # dfs on grid2's islands but at the same time cross check if any cell is not land on grid1
    def isSubIsland(self, grid1, grid2, r, c):
        if grid2[r][c] != 1: return False
        ret = (grid1[r][c] == 1)
        grid2[r][c] = "#"
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(grid2) and 0 <= nc < len(grid2[0]) and grid2[nr][nc] == 1:
                newRet = self.isSubIsland(grid1, grid2, nr, nc)
                ret = ret and newRet
        return ret