class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        G = self.buildGraph(dislikes)
        colors = {}
        for i in range(1, n + 1):
            if i in colors: continue
            q = deque([i])
            colors[i] = 0
            while q:
                cur = q.popleft()
                for neigh in G[cur]:
                    if neigh in colors:
                        if colors[cur] == colors[neigh]: return False
                    else:
                        colors[neigh] = 1 - colors[cur]
                        q.append(neigh)
        return True
        
    def buildGraph(self, edges):
        G = defaultdict(list)
        for s, e in edges:
            G[s].append(e)
            G[e].append(s)
        return G