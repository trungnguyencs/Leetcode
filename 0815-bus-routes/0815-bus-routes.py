class Solution:
    def numBusesToDestination(self, routes: List[List[int]], start: int, end: int) -> int:
        # bfs on stop will time out so bfs on bus instead
        if start == end: return 0
        G = self.buildGraph(routes)
        q = deque(G[start])
        seen = set(G[start])
        d = 1
        while q:
            for _ in range(len(q)):
                curBus = q.popleft()
                for stop in routes[curBus]:
                    if stop == end: return d
                    for nextBus in G[stop]:
                        if nextBus in seen: continue
                        q.append(nextBus)
                        seen.add(nextBus)
            d += 1
        return -1
        
    def buildGraph(self, routes):
        G = defaultdict(set)
        for bus, route in enumerate(routes):
            for stop in route:
                G[stop].add(bus)
        return G