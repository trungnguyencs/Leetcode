class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = self.buildGraph(equations, values)
        return [self.answerQuery(s, e, G) for s, e in queries]
        
    def buildGraph(self, equations, values):
        G = defaultdict(list)
        for equation, ratio in zip(equations, values):
            s, e = equation
            G[s].append((e, ratio))
            G[e].append((s, 1.0/ratio))
        return G
    
    def answerQuery(self, s, e, G):
        if s not in G or e not in G: return -1
        visited = {s: 1.0}
        q = deque([s])
        while q:
            cur = q.popleft()
            if cur == e: return visited[cur]
            for nxt, multiplier in G[cur]:
                if nxt not in visited:
                    q.append(nxt)
                    visited[nxt] = visited[cur] * multiplier
        return -1