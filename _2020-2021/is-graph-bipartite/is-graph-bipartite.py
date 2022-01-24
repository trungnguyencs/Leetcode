class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        self.ans = True
        for node in range(len(graph)):
            if node in visited: continue
            self.dfs(node, graph, visited, 1)
            if not self.ans: break
        return self.ans
    
    def dfs(self, node, graph, visited, color):
        visited[node] = color
        for neigh in graph[node]:
            if neigh not in visited:
                self.dfs(neigh, graph, visited, -color)
            elif visited[neigh] == color:
                self.ans = False
                return