class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        visited = defaultdict(int)
        G = self.buildGraph(prereqs)
        for i in range(numCourses):
            if not self.dfs(i, G, visited): return False
        return True
        
    def dfs(self, cur, G, visited):
        if visited[cur] == -1: return False
        if visited[cur] == 1: return True
        visited[cur] = -1
        for neigh in G[cur]:
            if not self.dfs(neigh, G, visited): return False
        visited[cur] = 1
        return True
        
    def buildGraph(self, prereqs):
        G = defaultdict(list)
        for s, e in prereqs:
            G[s].append(e)
        return G