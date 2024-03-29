class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        G = self.buildGraph(times)
        visited = {}
        heap = [(0, k)]
        while heap:
            cost, node = heappop(heap)
            if node in visited: continue
            visited[node] = cost
            for neigh, w in G[node]:
                heappush(heap, (cost + w, neigh))
        return max(visited.values()) if len(visited) == n else -1
        
    def buildGraph(self, times):
        G = defaultdict(list)
        for s, e, w in times:
            G[s].append((e, w))
        return G