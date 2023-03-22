class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        G = self.buildGraph(roads)
        q = deque([1])
        visited = {1}
        ans = float('inf')
        while q:
            cur = q.popleft()
            for neigh, w in G[cur].items():
                ans = min(ans, w)
                if neigh not in visited:
                    visited.add(neigh)
                    q.append(neigh)
        return ans
        
    def buildGraph(self, edges):
        G = defaultdict(dict)
        for s, e, w in edges:
            G[s][e] = w
            G[e][s] = w
        return G