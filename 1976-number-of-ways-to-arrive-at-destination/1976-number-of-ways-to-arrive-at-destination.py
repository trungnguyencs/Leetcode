class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        G = self.buildGraph(roads)
        distances = [float('inf')] * n
        ways = [0] * n #ways[i] keeps the number of shortest path from src = 0 to dst = i
        distances[0], ways[0] = 0, 1
        heap = [(0, 0)]
        while heap:
            d, cur = heappop(heap)
            if d > distances[cur]: continue
            for neigh, delta in G[cur]:
                nd = d + delta
                if nd < distances[neigh]:
                    distances[neigh] = nd
                    ways[neigh] = ways[cur]
                    heappush(heap, (nd, neigh))
                elif nd == distances[neigh]:
                    ways[neigh] += ways[cur]
        return ways[-1] % (10**9 + 7)

    def buildGraph(self, roads):
        G = defaultdict(list)
        for s, e, w in roads:
            G[s].append((e, w))
            G[e].append((s, w))
        return G