class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph, prob = dict(), dict() #graph with prob
        for i, (u, v) in enumerate(edges):
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
            prob[u, v] = prob[v, u] = succProb[i]
        
        h = [(-1, start)] #Dijkstra's algo
        seen = set()
        while h: 
            p, n = heappop(h)
            if n == end: return -p
            seen.add(n)
            for nn in graph.get(n, []):
                if nn in seen: continue 
                heappush(h, (p * prob.get((n, nn), 0), nn))
        return 0