class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count = 0
        G = self.buildGraph(edges)
        visited = set()
        for node in range(n):
            if node in visited: continue
            count += 1
            self.dfs(node, G, visited)
        return count
    
    def dfs(self, cur, G, visited):
        visited.add(cur)
        for neigh in G[cur]:
            if neigh in visited: continue
            self.dfs(neigh, G, visited)
    
    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)
        return G