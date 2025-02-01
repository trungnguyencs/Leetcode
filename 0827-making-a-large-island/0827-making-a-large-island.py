class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        #color each island (starting from 2) and store its area in a dict
        #for each 0, sum up all its neighbor islands of different colors
        dic = {}
        color = 2
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dic[color] = self.colorAndGetArea(grid, r, c, color)
                    color += 1
        maxArea = max(dic.values()) if dic else 0 #this is in case the grid has all 1s or all 0s
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] != 0: continue
                maxArea = max(maxArea, self.findCombinedArea(grid, r, c, dic))
        return maxArea

    def colorAndGetArea(self, grid, r, c, color):
        grid[r][c] = color
        area = 1
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                area += self.colorAndGetArea(grid, nr, nc, color)
        return area

    def findCombinedArea(self, grid, r, c, dic):
        visited = {0}
        combinedArea = 1
        neighs = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        for nr, nc in neighs:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] not in visited:
                color = grid[nr][nc]
                combinedArea += dic[color]
                visited.add(color)
        return combinedArea