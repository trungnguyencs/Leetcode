class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        G = defaultdict(list)
        for i in range(len(equations)):
            s, e = equations[i]
            G[s].append((e, values[i]))
            G[e].append((s, 1/values[i]))
        return [self.answerQuery(G, s, e) for s, e in queries]
        
    def answerQuery(self, G, s, e):
        if s not in G or e not in G: return -1
        q = deque([s])
        visited = {s: 1.0}
        while q:
            cur = q.popleft()
            if cur == e:
                return visited[cur]
            for neigh, multiplier in G[cur]:
                if neigh not in visited:
                    visited[neigh] = visited[cur] * multiplier
                    q.append((neigh))
        return -1
