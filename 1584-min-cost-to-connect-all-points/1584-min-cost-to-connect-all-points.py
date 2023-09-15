class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ans = 0
        G = self.buildGraph(points)
        visited = set()
        heap = [(0, 0)]
        while len(visited) < len(points):
            d, cur = heappop(heap)
            if cur in visited: continue
            ans += d
            visited.add(cur)
            if len(visited) == len(points): return ans
            for neigh, d in G[cur]:
                if neigh not in visited:
                    heappush(heap, (d, neigh))
        
    def buildGraph(self, points):
        G = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                G[i].append((j, d))
                G[j].append((i, d))
        return G