class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        G = self.buildGraph(edges)
        visited = set([source])
        q = deque([source])
        while q:
            cur = q.popleft()
            if cur == destination: return True
            for neigh in G[cur]:
                if neigh in visited: continue
                q.append(neigh)
                visited.add(neigh)
        return False
        
    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)
        return G