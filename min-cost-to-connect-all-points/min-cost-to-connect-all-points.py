class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        minCost = 0
        visited = set()
        heap = [(0, 0)]
        G = self.buildGraph(points)
        while heap:
            d, cur = heappop(heap)
            if cur in visited: continue
            visited.add(cur)
            minCost += d
            if len(visited) == len(points): return minCost
            for d, neigh in G[cur]:
                if neigh in visited: continue
                heappush(heap, (d, neigh))
                
    def buildGraph(self, points):
        G = defaultdict(list)
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                d = self.distance(points[i], points[j])
                G[i].append((d, j))
                G[j].append((d, i))
        return G
        
    def distance(self, x, y):
        return abs(x[0] - y[0]) + abs(x[1] - y[1])