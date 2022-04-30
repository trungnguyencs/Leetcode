class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = self.buildGraph(equations, values)
        return [self.answerQuery(s, e, G) for s, e in queries]
        
    def buildGraph(self, equations, values):
        G = defaultdict(list)
        for (s, e), ratio in zip(equations, values):
            G[s].append((e, ratio))
            G[e].append((s, 1.0/ratio))
        return G
    
    def answerQuery(self, s, e, G):
        if s not in G or e not in G: return -1
        q = deque([(s, 1.0)])
        visited = set([s])
        while q:
            cur, rate = q.popleft()
            if cur == e: return rate
            for neigh, multiplier in G[cur]:
                if neigh not in visited:
                    q.append([neigh, rate * multiplier])
                    visited.add(neigh)
        return -1