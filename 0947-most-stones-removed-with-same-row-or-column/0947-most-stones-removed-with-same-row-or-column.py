class Solution:
    def removeStones(self, points: List[List[int]]) -> int:
        islandCount = 0
        visited = set()
        rows, cols = self.buildGraph(points)
        for r, c in points:
            if (r, c) in visited: continue
            self.dfs(r, c, rows, cols, visited)
            islandCount += 1
        return len(points) - islandCount
        
    def buildGraph(self, points):
        rows, cols = defaultdict(set), defaultdict(set)
        for r, c in points:
            rows[r].add(c)
            cols[c].add(r)
        return rows, cols
    
    def dfs(self, r, c, rows, cols, visited):
        if (r, c) in visited: return
        visited.add((r, c))
        for nc in rows[r]:
            self.dfs(r, nc, rows, cols, visited)
        for nr in cols[c]:
            self.dfs(nr, c, rows, cols, visited)