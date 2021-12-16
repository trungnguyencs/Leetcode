class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        G = self.buildGraph(edges)
        q = deque([node for node in G if len(G[node]) == 1])
        while n > 2: # there will be at most 2 MHT roots
            n -= len(q)
            for _ in range(len(q)):
                cur = q.popleft()
                for parent in G[cur]:
                    G[parent].remove(cur)
                    if len(G[parent]) == 1:
                        q.append(parent)
        return q
        
    def buildGraph(self, edges):
        G = defaultdict(set)
        for s, e in edges:
            G[s].add(e)
            G[e].add(s)
        return G