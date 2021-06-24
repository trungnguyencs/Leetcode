class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # graph is a tree both 1 and 2 are true:
        # 1. #nodes == #edges + 1
        # 2. it has only 1 connected component
        if n != len(edges) + 1: return False
        G = self.buildGraph(edges)
        visited = {0}
        self.dfs(G, 0, visited)
        return n == len(visited)
    
    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)
        return G
            
    def dfs(self, G, cur, visited):
        for neigh in G[cur]:
            if neigh not in visited:
                visited.add(neigh)
                self.dfs(G, neigh, visited)