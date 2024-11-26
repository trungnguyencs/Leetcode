class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        G, ind = self.buildGraph(edges)
        q = deque([x for x in range(n) if ind[x] == 0])
        roots = []
        while q:
            cur = q.popleft()
            if not G[cur]: #cur node has no parent
                roots.append(cur)
            for parent in G[cur]:
                ind[parent] -= 1
                if ind[parent] == 0:
                    q.append(parent)
        return roots[0] if len(roots) == 1 else -1
    
    def buildGraph(self, edges):
        G = defaultdict(list)
        ind = defaultdict(int)
        for s, e in edges:
            G[e].append(s)
            ind[s] += 1
        return G, ind