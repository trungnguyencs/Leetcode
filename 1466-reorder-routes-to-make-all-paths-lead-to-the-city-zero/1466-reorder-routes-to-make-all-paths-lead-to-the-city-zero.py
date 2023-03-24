class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        G = self.buildGraph(connections)
        q = deque([0])
        visited = {0}
        ans = 0
        while q:
            cur = q.popleft()
            for neigh, rightDirection in G[cur].items():
                if neigh in visited: continue
                if not rightDirection: ans += 1
                q.append(neigh)
                visited.add(neigh)
        return ans
        
    def buildGraph(self, edges):
        G = defaultdict(dict)
        for s, e in edges:
            G[s][e] = False
            G[e][s] = True
        return G