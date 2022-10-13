class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        colored = {}
        for node in range(len(graph)):
            if node in colored: continue
            if not self.dfs(node, 0, colored, graph): return False
        return True
            
    def dfs(self, node, color, colored, graph):
        colored[node] = color
        for neigh in graph[node]:
            if neigh in colored and colored[neigh] == color: return False
            if neigh not in colored:
                if not self.dfs(neigh, 1-color, colored, graph): return False
        return True