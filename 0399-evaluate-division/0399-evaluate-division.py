class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = self.buildGraph(equations, values)
        return [self.answerQuery(s, e, G) for s, e in queries]

    def buildGraph(self, equations, values):
        G = defaultdict(list)
        for (s, e), val in zip(equations, values):
            G[s].append((e, val))
            G[e].append((s, 1/val))
        return G

    def answerQuery(self, s, e, G):
        if s not in G: return -1
        q = deque([(s, 1)])
        visited = set([s])
        while q:
            cur, curRate = q.popleft()
            if cur == e: return curRate
            for nxt, val in G[cur]:
                if nxt not in visited:
                    visited.add(nxt)
                    q.append((nxt, curRate * val))
        return -1