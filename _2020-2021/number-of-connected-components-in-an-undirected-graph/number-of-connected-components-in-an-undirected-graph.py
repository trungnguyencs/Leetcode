class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        G = self.buildGraph(edges)
        visited = set()
        count = 0
        for i in range(n):
            if i in visited: continue
            self.dfs(G, i, visited)
            count += 1
        return count
    
    def dfs(self, G, cur, visited):
        for neigh in G[cur]:
            if neigh in visited: continue
            visited.add(neigh)
            self.dfs(G, neigh, visited)
    
    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)
        return G