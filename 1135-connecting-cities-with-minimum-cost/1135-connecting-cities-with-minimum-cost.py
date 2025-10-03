class Solution:
    def minimumCost(self, n: int, connections: List[List[int]]) -> int:
        #Prim's Algorithm for mininum spanning tree (MST)
        G = self.buildGraph(connections)
        visited = set()
        heap = [(0, 1)]
        cost = 0
        while heap:
            w, node = heappop(heap)
            if node in visited:
                continue
            visited.add(node)
            cost += w
            for w, neigh in G[node]:
                if neigh not in visited:
                    heappush(heap, (w, neigh))
            if len(visited) == n: return cost
        return -1

    def buildGraph(self, connections):
        G = defaultdict(list)
        for s, e, w in connections:
            G[s].append((w, e))
            G[e].append((w, s))
        return G