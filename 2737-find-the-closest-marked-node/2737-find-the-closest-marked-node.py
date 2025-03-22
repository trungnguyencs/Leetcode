class Solution:
    def minimumDistance(self, n: int, edges: List[List[int]], s: int, marked: List[int]) -> int:
        G = self.buildGraph(edges)
        marked = set(marked)
        distances = {s: 0}
        minDistance = float('inf')
        heap = [(s, 0)]
        while heap:
            cur, d = heappop(heap)
            if cur in marked:
                #cannot return here since there maybe a path with more sections but less total weights that hasn't been processed
                minDistance = min(minDistance, d)
            for neigh, delta in G[cur]:
                nd = d + delta
                if neigh not in distances or distances[neigh] > nd:
                    distances[neigh] = nd
                    heappush(heap, (neigh, nd))
        return -1 if minDistance == float('inf') else minDistance

    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e, w in edges:
            G[s].append((e, w))
        return G