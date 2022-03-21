class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        dic = {}
        color = 2
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    dic[color] = self.getAreaOfIsland(grid, r, c, color)
                    color += 1
        maxArea = max(dic.values()) if dic else 0 # in case of all ones -> not change any 0 to 1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    maxArea = max(maxArea, self.findCombinedArea(grid, r, c, dic))
        return maxArea
        
    def getAreaOfIsland(self, grid, r, c, color):
        grid[r][c] = color
        area = 1
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                area += self.getAreaOfIsland(grid, nr, nc, color)
        return area
            
    def findCombinedArea(self, grid, r, c, dic):
        visited = {0}
        combinedArea = 1
        for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]:
            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] not in visited:
                combinedArea += dic[grid[nr][nc]]
                visited.add(grid[nr][nc])
        return combinedArea