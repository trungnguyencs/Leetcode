class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        if len(connections) < n - 1: return -1
        G = self.buildGraph(connections)
        visited = set()
        islands = 0
        for i in range(n):
            if i not in visited:
                islands += 1
                self.dfs(i, G, visited)
        return islands - 1
        
    def dfs(self, cur, G, visited):
        for neigh in G[cur]:
            if neigh in visited: continue
            visited.add(neigh)
            self.dfs(neigh, G, visited)
    
    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)
        return G