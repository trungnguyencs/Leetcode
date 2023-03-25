class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        G = self.buildGraph(edges)
        visited = set()
        self.componentSize = 0
        for node in range(n):
            if node in visited: continue
            self.componentSize = 0
            self.dfs(node, G, visited)
            count += self.componentSize * (n - self.componentSize)
        return count//2
    
    def dfs(self, cur, G, visited):
        visited.add(cur)
        self.componentSize += 1
        for neigh in G[cur]:
            if neigh in visited: continue
            self.dfs(neigh, G, visited)
    
    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)
        return G