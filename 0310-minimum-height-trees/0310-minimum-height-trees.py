class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]
        G = self.buildGraph(edges)
        q = deque([x for x in range(n) if len(G[x]) == 1])
        while n > 2: # there will be at most 2 MHT roots
            for _ in range(len(q)):
                child = q.popleft()
                n -= 1
                parent = G[child].pop() # the single parent in the set 
                G[parent].remove(child)
                if len(G[parent]) == 1:
                    q.append(parent)
        return q
             
    def buildGraph(self, edges):
        G = defaultdict(set)
        for a, b in edges:
            G[a].add(b)
            G[b].add(a)
        return G